import os
import random
import subprocess
import datetime
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_PAT = os.getenv("GITHUB_PAT")
REPO_NAME = "nahmadpushes"
REPO_PATH = f"/home/{GITHUB_USERNAME}/{REPO_NAME}"
REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

# Random commit messages
COMMIT_MESSAGES = [
    "Refactor code",
    "Fix typo",
    "Update README",
    "Improve performance",
    "Fix minor bug",
    "Add comments",
    "Optimize imports",
    "Polish code",
    "Clean up code",
    "Update documentation",
    "Improve efficiency",
    "Simplify logic",
    "Remove unused variables",
    "Fix formatting",
    "Update .gitignore",
    "Improve error handling",
    "Add unit tests",
    "Refactor functions",
    "Update dependencies"
]

# Random file names for more natural commits
FILE_NAMES = [
    "activity.txt",
    "README.md",
    "main.py",
    "config.py",
    "utils.py",
    "requirements.txt",
    "changelog.md",
    "index.html",
    "style.css",
    "app.js"
]

def make_commit(batch_size=10):
    for _ in range(batch_size):
        # Choose a random file to modify for more natural commits
        file_name = random.choice(FILE_NAMES)
        file_path = os.path.join(REPO_PATH, file_name)

        # Create the file if it doesn't exist
        os.makedirs(REPO_PATH, exist_ok=True)
        with open(file_path, "a") as f:
            f.write(f"Update on {datetime.datetime.now()}\n")

        # Set the remote URL with the PAT
        subprocess.run(["git", "-C", REPO_PATH, "remote", "set-url", "origin", REPO_URL])

        # Add, commit, and push
        subprocess.run(["git", "-C", REPO_PATH, "add", "."])
        commit_message = random.choice(COMMIT_MESSAGES)
        subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", commit_message])
        time.sleep(random.randint(1, 5))  # Add a small random delay to avoid looking too robotic
    subprocess.run(["git", "-C", REPO_PATH, "push"])

if __name__ == "__main__":
    print(randinteger = random.randint(1,2))
    make_commit(batch_size=randinteger)  # Increase the batch size for more green
    print("Commit batch pushed successfully!")
