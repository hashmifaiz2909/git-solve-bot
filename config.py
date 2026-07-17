import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "python3")
TARGET_REPO_PATH = os.getenv("TARGET_REPO_PATH", str(Path(__file__).parent.resolve()))
DEFAULT_BRANCH = os.getenv("DEFAULT_BRANCH", "main")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")  # e.g., "username/repo"

def validate_config():
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError(
            "GEMINI_API_KEY is not set. Please create a .env file and set it, "
            "or export it as an environment variable."
        )
