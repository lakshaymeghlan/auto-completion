import os
import random
import subprocess
from datetime import datetime, timedelta

def generate_commits(start_date, end_date):
    """Generate GitHub commits between start_date and end_date with random intensity and skipped days."""
    current_date = start_date
    
    while current_date <= end_date:
        if random.random() < 0.2:  # 20% chance to skip a day
            current_date += timedelta(days=1)
            continue
        
        intensity = random.choice(['light', 'mid', 'dark'])
        num_commits = {
            'light': random.randint(1, 3),
            'mid': random.randint(4, 7),
            'dark': random.randint(8, 12)
        }[intensity]
        
        for _ in range(num_commits):
            commit_message = f"Auto-generated commit on {current_date.strftime('%Y-%m-%d')}"
            
            with open("dummy.txt", "a") as f:
                f.write(commit_message + "\n")
            
            env = os.environ.copy()
            env['GIT_COMMITTER_DATE'] = current_date.strftime('%Y-%m-%dT%H:%M:%S')
            env['GIT_AUTHOR_DATE'] = current_date.strftime('%Y-%m-%dT%H:%M:%S')
            
            subprocess.run(["git", "add", "dummy.txt"], env=env)
            subprocess.run(["git", "commit", "-m", commit_message], env=env)
        
        current_date += timedelta(days=1)

def push_changes():
    """Force push commits to GitHub."""
    subprocess.run(["git", "push", "--force", "origin", "main"])

def main():
    start_date = datetime(2025, 1, 1)
    end_date = datetime.today()
    
    generate_commits(start_date, end_date)
    push_changes()
    
    print("✅ Contributions added successfully! Wait a few minutes for GitHub to update.")

if __name__ == "__main__":
    main()
