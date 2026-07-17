"""
auto_runner.py
Continuously fetches random unsolved LeetCode problems, solves them
with Gemini, and pushes solutions to GitHub.

Usage:
    ./venv/bin/python auto_runner.py
    ./venv/bin/python auto_runner.py --count 5             # Solve exactly 5 problems then stop
    ./venv/bin/python auto_runner.py --delay 60            # 60 second pause between problems
    ./venv/bin/python auto_runner.py --difficulty Easy     # Only solve Easy problems
    ./venv/bin/python auto_runner.py --lang python3        # Use Python3
    ./venv/bin/python auto_runner.py --no-push             # Don't push to GitHub
"""
import argparse
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

import config
import leetcode_client as leetcode
import solver
import problem_tracker
from git_manager import GitManager

BANNER = """
╔══════════════════════════════════════════════╗
║      GitSolve Auto-Runner  🤖                ║
║  Continuously Solving LeetCode → GitHub      ║
╚══════════════════════════════════════════════╝
"""


def ts() -> str:
    """Returns a formatted timestamp string."""
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def solve_one(slug: str, lang: str, push: bool, repo_path: Path) -> bool:
    """
    Fetches, solves and (optionally) pushes one problem.
    Returns True on full success, False on failure.
    """
    # 1. Fetch problem
    print(f"\n{ts()} Fetching '{slug}' from LeetCode...")
    problem = leetcode.fetch_leetcode_problem(slug)
    print(f"{ts()} ✅ Fetched: {problem['title']} [{problem['difficulty']}]")

    # 2. Get starter code snippet
    snippet_data = solver.get_snippet_for_lang(problem["codeSnippets"], lang)
    lang_slug = snippet_data["langSlug"]
    starter_code = snippet_data["code"]
    lang_info = solver.LANG_MAP.get(lang_slug, {"ext": "txt", "name": lang_slug.capitalize()})
    file_ext = lang_info["ext"]
    lang_name = lang_info["name"]

    # 3. Generate solution via Gemini
    print(f"{ts()} 🤖 Calling Gemini to generate {lang_name} solution...")
    solution = solver.generate_solution(
        problem_title=problem["title"],
        problem_description=problem["markdown_content"],
        difficulty=problem["difficulty"],
        starter_code=starter_code,
        language=lang_name,
    )
    print(f"{ts()} ✅ Solution generated | Time: {solution.time_complexity} | Space: {solution.space_complexity}")

    # 4. Save files
    problem_dir = repo_path / "solutions" / problem["difficulty"] / slug
    problem_dir.mkdir(parents=True, exist_ok=True)
    solution_file = problem_dir / f"solution.{file_ext}"
    readme_file = problem_dir / "README.md"

    solution_file.write_text(solution.code.strip() + "\n", encoding="utf-8")

    readme_content = f"""# {problem['title']}

**Difficulty:** {problem['difficulty']}  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/{slug}/)

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
    readme_file.write_text(readme_content, encoding="utf-8")
    print(f"{ts()} 💾 Saved solution and README to {problem_dir}")

    # 5. Push to GitHub
    if push:
        commit_message = (
            f"feat: solve {problem['title']} [{problem['difficulty']}] in {lang_name}"
        )
        git = GitManager(str(repo_path))

        if config.GITHUB_TOKEN and config.GITHUB_REPOSITORY:
            print(f"{ts()} 🚀 Pushing via GitHub REST API...")
            success = git.push_via_api(
                filepaths=[str(solution_file), str(readme_file)],
                message=commit_message,
                repo_owner_and_name=config.GITHUB_REPOSITORY,
                token=config.GITHUB_TOKEN,
                branch=config.DEFAULT_BRANCH,
            )
            if not success:
                print(f"{ts()} ⚠️  Push returned errors (files may still have been uploaded).")
        else:
            print(f"{ts()} 🚀 Pushing via local git...")
            if not git.is_git_repo():
                git.init_repo()
            git.add_file(str(solution_file))
            git.add_file(str(readme_file))
            committed = git.commit(commit_message)
            if committed:
                git.push(config.DEFAULT_BRANCH)

    # 6. Mark as solved
    problem_tracker.mark_solved(slug)
    print(f"{ts()} ✅ '{problem['title']}' marked as solved.")
    return True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Auto-runner: continuously picks random LeetCode problems, solves with Gemini, pushes to GitHub."
    )
    parser.add_argument(
        "--count", "-c", type=int, default=0,
        help="Number of problems to solve then stop. 0 = run forever (default: 0)."
    )
    parser.add_argument(
        "--delay", "-d", type=float, default=30,
        help="Seconds to wait between problems (default: 30)."
    )
    parser.add_argument(
        "--difficulty", choices=["Easy", "Medium", "Hard"], default=None,
        help="Only solve problems of this difficulty (default: any)."
    )
    parser.add_argument(
        "--lang", "-l", default=config.DEFAULT_LANGUAGE,
        help=f"Programming language (default: {config.DEFAULT_LANGUAGE})."
    )
    parser.add_argument(
        "--no-push", action="store_true",
        help="Skip pushing to GitHub (dry run)."
    )
    parser.add_argument(
        "--repo", "-r", default=config.TARGET_REPO_PATH,
        help="Local path of the target Git repository."
    )
    return parser.parse_args()


def main():
    print(BANNER)
    args = parse_args()

    # Validate Gemini key
    config.validate_config()

    repo_path = Path(args.repo).resolve()
    push = not args.no_push

    print(f"{ts()} 📋 Mode    : {'Run forever' if args.count == 0 else f'Solve {args.count} problems'}")
    print(f"{ts()} 🌐 Language: {args.lang}")
    print(f"{ts()} 💪 Difficulty: {args.difficulty or 'Any'}")
    print(f"{ts()} ⏱️  Delay   : {args.delay}s between problems")
    print(f"{ts()} 🚀 Push    : {'Yes' if push else 'No (dry-run)'}")
    print()

    # Pre-fetch full problem list once
    print(f"{ts()} 🔄 Fetching LeetCode problem list...")
    try:
        all_problems = leetcode.fetch_all_problems()
    except Exception as e:
        print(f"{ts()} ❌ Failed to fetch problem list: {e}")
        sys.exit(1)
    print(f"{ts()} ✅ Loaded {len(all_problems)} free problems from LeetCode.")

    solved_count = 0
    failed_streak = 0
    MAX_FAILED_STREAK = 5

    while True:
        # Stop if count reached
        if args.count > 0 and solved_count >= args.count:
            print(f"\n{ts()} 🎉 Reached target of {args.count} problems. Done!")
            break

        # Reload solved set every iteration (to stay up-to-date)
        solved_slugs = problem_tracker.load_solved()

        # Pick next problem
        candidate = leetcode.pick_random_problem(
            all_problems,
            exclude_slugs=solved_slugs,
            difficulty=args.difficulty
        )
        if candidate is None:
            print(f"\n{ts()} 🏆 All available problems solved! Nothing left to do.")
            break

        slug = candidate["titleSlug"]
        print(f"\n{'─' * 60}")
        print(f"{ts()} 🎯 Next problem → {candidate['title']} [{candidate['difficulty']}] | {slug}")

        try:
            success = solve_one(slug, args.lang, push, repo_path)
            if success:
                solved_count += 1
                failed_streak = 0
                print(f"{ts()} 📊 Progress: {solved_count} solved this session | {len(solved_slugs) + 1} total solved")
        except Exception as e:
            failed_streak += 1
            print(f"{ts()} ❌ Error solving '{slug}': {e}")
            traceback.print_exc()
            # Mark as "attempted" to avoid retrying same broken problem immediately
            problem_tracker.mark_solved(slug)
            if failed_streak >= MAX_FAILED_STREAK:
                print(f"{ts()} 🛑 {MAX_FAILED_STREAK} consecutive failures — stopping.")
                break

        # Wait between problems
        if args.count == 0 or solved_count < args.count:
            print(f"\n{ts()} ⏳ Waiting {args.delay}s before next problem...")
            time.sleep(args.delay)


if __name__ == "__main__":
    main()
