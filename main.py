import os
import argparse
import sys
from pathlib import Path

import config
import leetcode_client as leetcode
import solver
from git_manager import GitManager

def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch a LeetCode problem, solve it using Gemini, and commit/push to GitHub."
    )
    parser.add_argument(
        "--url", "-u",
        required=True,
        help="LeetCode problem URL (e.g., https://leetcode.com/problems/two-sum/)"
    )
    parser.add_argument(
        "--lang", "-l",
        default=config.DEFAULT_LANGUAGE,
        help=f"Target programming language (default: {config.DEFAULT_LANGUAGE})"
    )
    parser.add_argument(
        "--push", "-p",
        action="store_true",
        default=True,
        help="Stage, commit, and push solution to GitHub (default: True)"
    )
    parser.add_argument(
        "--no-push",
        action="store_false",
        dest="push",
        help="Do not push changes to GitHub"
    )
    parser.add_argument(
        "--repo", "-r",
        default=config.TARGET_REPO_PATH,
        help=f"Target Git repository path (default: {config.TARGET_REPO_PATH})"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    
    # 1. Parse URL & Fetch Problem
    slug = leetcode.parse_slug(args.url)
    print(f"Fetching problem details for '{slug}'...")
    try:
        problem = leetcode.fetch_leetcode_problem(slug)
    except Exception as e:
        print(f"Error fetching problem: {e}")
        sys.exit(1)
        
    print(f"Fetched problem: {problem['title']} [{problem['difficulty']}]")
    
    # 2. Extract starter code snippet for the requested language
    target_lang = args.lang.lower()
    snippet_data = solver.get_snippet_for_lang(problem["codeSnippets"], target_lang)
    lang_slug = snippet_data["langSlug"]
    starter_code = snippet_data["code"]
    
    # Check if target language is mapped in solver
    lang_info = solver.LANG_MAP.get(lang_slug, {"ext": "txt", "name": lang_slug.capitalize()})
    file_ext = lang_info["ext"]
    lang_name = lang_info["name"]
    
    print(f"Using template for language: {lang_name} (extension: .{file_ext})")
    if not starter_code:
        print("Warning: Starter code snippet template was empty.")
        
    # 3. Call Solver to Generate Solution
    print("Generating solution with Gemini...")
    try:
        solution = solver.generate_solution(
            problem_title=problem["title"],
            problem_description=problem["markdown_content"],
            difficulty=problem["difficulty"],
            starter_code=starter_code,
            language=lang_name
        )
    except Exception as e:
        print(f"Error generating solution: {e}")
        sys.exit(1)
        
    print("Solution generated successfully!")
    print(f"Complexity: Time: {solution.time_complexity} | Space: {solution.space_complexity}")
    
    # 4. Save Solution to Directory
    # Structure: solutions/<Difficulty>/<problem-title-slug>/
    repo_path = Path(args.repo).resolve()
    difficulty_dir = repo_path / "solutions" / problem["difficulty"]
    problem_dir = difficulty_dir / slug
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    solution_file = problem_dir / f"solution.{file_ext}"
    readme_file = problem_dir / "README.md"
    
    # Save solution code file
    with open(solution_file, "w", encoding="utf-8") as f:
        f.write(solution.code.strip() + "\n")
    print(f"Saved solution to {solution_file}")
    
    # Create problem README.md
    readme_content = f"""# {problem['title']}

**Difficulty:** {problem['difficulty']}
**LeetCode Link:** [LeetCode Problem URL](https://leetcode.com/problems/{slug}/)

## Problem Description
{problem['markdown_content']}

## Solution

- **Language:** {lang_name}
- **Time Complexity:** {solution.time_complexity}
- **Space Complexity:** {solution.space_complexity}

### Approach
{solution.explanation}

### Code
```{file_ext}
{solution.code.strip()}
```
"""
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Saved README to {readme_file}")
    
    # 5. Git commit and push workflow
    if args.push:
        print(f"Handling Git push for files in: {repo_path}")
        git = GitManager(str(repo_path))
        commit_message = f"docs: add solution for {problem['title']} ({problem['difficulty']}) in {lang_name}"
        
        if config.GITHUB_TOKEN and config.GITHUB_REPOSITORY:
            print("GITHUB_TOKEN and GITHUB_REPOSITORY detected. Pushing via GitHub REST API...")
            git.push_via_api(
                filepaths=[str(solution_file), str(readme_file)],
                message=commit_message,
                repo_owner_and_name=config.GITHUB_REPOSITORY,
                token=config.GITHUB_TOKEN,
                branch=config.DEFAULT_BRANCH
            )
        else:
            print("Using local git commands...")
            # Check if initialized
            if not git.is_git_repo():
                git.init_repo()
                
            git.add_file(str(solution_file))
            git.add_file(str(readme_file))
            
            committed = git.commit(commit_message)
            if committed:
                git.push(config.DEFAULT_BRANCH)
    else:
        print("Git push bypassed (--no-push flag active).")
        
    print("\nDone! Automation finished successfully.")

if __name__ == "__main__":
    main()
