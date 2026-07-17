import subprocess
import os
from pathlib import Path

def run_cmd(args: list, cwd: str) -> str:
    """
    Runs a shell command and returns the stdout. Raises subprocess.CalledProcessError on failure.
    """
    result = subprocess.run(
        args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    return result.stdout.strip()

class GitManager:
    def __init__(self, repo_path: str = None):
        self.repo_path = os.path.abspath(repo_path or os.getcwd())
        
    def is_git_repo(self) -> bool:
        """
        Checks if the repository path is a Git workspace.
        """
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            return False
        try:
            run_cmd(["git", "rev-parse", "--is-inside-work-tree"], cwd=self.repo_path)
            return True
        except subprocess.CalledProcessError:
            return False
            
    def init_repo(self):
        """
        Initializes a Git repository in the target path.
        """
        print(f"Initializing Git repository in {self.repo_path}...")
        run_cmd(["git", "init"], cwd=self.repo_path)
        # Ensure default branch is set to main if not configured
        try:
            run_cmd(["git", "checkout", "-b", "main"], cwd=self.repo_path)
        except subprocess.CalledProcessError:
            pass # Already on main or default branch
            
    def has_changes(self) -> bool:
        """
        Checks if there are unstaged or staged changes.
        """
        status = run_cmd(["git", "status", "--porcelain"], cwd=self.repo_path)
        return len(status) > 0

    def add_file(self, filepath: str):
        """
        Stages a specific file.
        """
        # Convert path to relative or absolute path compatible with git
        rel_path = os.path.relpath(filepath, self.repo_path)
        run_cmd(["git", "add", rel_path], cwd=self.repo_path)

    def commit(self, message: str) -> bool:
        """
        Commits staged changes. Returns True if committed, False if no changes to commit.
        """
        if not self.has_changes():
            print("No changes to commit.")
            return False
        
        try:
            run_cmd(["git", "commit", "-m", message], cwd=self.repo_path)
            print(f"Committed changes with message: '{message}'")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to commit: {e.stderr}")
            return False

    def push(self, branch: str = "main") -> bool:
        """
        Pushes commits to the remote repository.
        """
        try:
            # Check if remote exists
            remotes = run_cmd(["git", "remote"], cwd=self.repo_path)
            if not remotes:
                print("Warning: No git remotes found. Skipping push.")
                return False
                
            print(f"Pushing to origin {branch}...")
            # We use git push -u origin <branch> for the first push, otherwise regular push
            run_cmd(["git", "push", "origin", branch], cwd=self.repo_path)
            print("Successfully pushed to GitHub!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to push: {e.stderr}")
            return False

    def push_via_api(self, filepaths: list, message: str, repo_owner_and_name: str, token: str, branch: str = "main") -> bool:
        """
        Commits and pushes files using the GitHub REST API instead of local git command.
        """
        import base64
        import requests
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        success = True
        for filepath in filepaths:
            rel_path = os.path.relpath(filepath, self.repo_path)
            # GitHub API uses forward slashes regardless of OS
            github_path = rel_path.replace(os.sep, "/")
            
            # 1. Read file content
            with open(filepath, "rb") as f:
                content_bytes = f.read()
            encoded_content = base64.b64encode(content_bytes).decode("utf-8")
            
            # 2. Get file SHA if it already exists
            sha = None
            url = f"https://api.github.com/repos/{repo_owner_and_name}/contents/{github_path}"
            params = {"ref": branch}
            
            try:
                get_resp = requests.get(url, headers=headers, params=params, timeout=10)
                if get_resp.status_code == 200:
                    sha = get_resp.json().get("sha")
                elif get_resp.status_code != 404:
                    print(f"Warning: Unexpected response checking remote file {github_path}: {get_resp.status_code}")
            except Exception as e:
                print(f"Error checking remote file {github_path}: {e}")
                
            # 3. Create or update file content
            payload = {
                "message": message,
                "content": encoded_content,
                "branch": branch
            }
            if sha:
                payload["sha"] = sha
                
            try:
                put_resp = requests.put(url, json=payload, headers=headers, timeout=10)
                if put_resp.status_code in [200, 201]:
                    print(f"Successfully committed and pushed {github_path} via GitHub API.")
                else:
                    print(f"Failed to push {github_path} via GitHub API. Status: {put_resp.status_code}, Response: {put_resp.text}")
                    success = False
            except Exception as e:
                print(f"Error pushing {github_path} via API: {e}")
                success = False
                
        return success

