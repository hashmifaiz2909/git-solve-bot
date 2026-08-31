# 🤖 GitSolve Bot — Automated LeetCode Solver & GitHub Sync

An intelligent, autonomous bot that continuously fetches LeetCode problems, generates optimal solutions with detailed explanations and time/space complexity analysis using **Google Gemini 3.6 Flash**, and automatically commits and pushes them to GitHub.

---

## ✨ Key Features

- 🔄 **Continuous Autonomous Solving:** Automatically queries LeetCode GraphQL API for unsolved problems across Easy, Medium, and Hard difficulties.
- 🧠 **Powered by Gemini 3.6 Flash:** Generates verified, clean solutions in multiple languages (Python3, C++, Java, JavaScript, TypeScript, Go, Rust, etc.) along with complexity analysis and algorithmic explanations.
- 🚀 **Automated GitHub Synchronization:** Formats solutions with markdown descriptions and code files, commits them cleanly, and pushes them live to GitHub.
- 📊 **Progress & State Tracking:** Tracks solved problem slugs locally in `solved_problems.json` to avoid redundant problem attempts.
- 🛡️ **Built-in Resilience:** Automatic exponential backoff and rate-limit handling for API quotas.

---

## 📁 Repository Structure

```
git-solve-bot/
├── auto_runner.py          # Continuous automation runner
├── solver.py               # Gemini code generation & complexity analyzer
├── leetcode_client.py      # LeetCode GraphQL client
├── problem_tracker.py      # State tracking for solved problems
├── git_manager.py          # Git staging, committing, and GitHub push manager
├── config.py               # Environment configuration loader
├── solved_problems.json    # JSON list of solved problem slugs
├── requirements.txt        # Python dependencies
└── solutions/              # Generated LeetCode solutions
    ├── Easy/
    ├── Medium/
    └── Hard/
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- A GitHub Personal Access Token with `repo` scope

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hashmifaiz2909/git-solve-bot.git
   cd git-solve-bot
   ```

2. **Set up virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file from `.env.example`:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   GITHUB_TOKEN=your_github_personal_access_token
   GITHUB_REPOSITORY=hashmifaiz2909/git-solve-bot
   DEFAULT_LANGUAGE=python3
   DEFAULT_BRANCH=main
   ```

---

## 🤖 Running the Bot

### Continuous Mode (Run Forever)
```bash
python auto_runner.py
```

### Solve a Fixed Number of Problems
```bash
python auto_runner.py --count 10
```

### Filter by Difficulty & Language
```bash
python auto_runner.py --difficulty Medium --lang python3
```

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
