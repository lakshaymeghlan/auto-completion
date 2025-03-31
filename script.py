import os
import random
import subprocess
from datetime import datetime, timedelta

def generate_commits(start_date, end_date, intensity):
    """Generate GitHub commits between start_date and end_date with the given intensity."""
    current_date = start_date
    
    while current_date <= end_date:
        num_commits = {
            'light': random.randint(1, 3),
            'mid': random.randint(4, 7),
            'dark': random.randint(8, 12)
        }.get(intensity, 1)
        
        for _ in range(num_commits):
            commit_message = f"Auto-generated commit on {current_date.strftime('%Y-%m-%d')}"
            
            with open("dummy.txt", "a") as f:
                f.write(commit_message + "\n")
            
            subprocess.run(["git", "add", "dummy.txt"])
            subprocess.run(["git", "commit", "-m", commit_message, "--date", current_date.strftime('%Y-%m-%d %H:%M:%S')])
        
        current_date += timedelta(days=1)

def push_changes():
    """Push commits to GitHub."""
    subprocess.run(["git", "push", "origin", "main"])

def main():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 3, 31)
    intensity = input("Enter intensity (light, mid, dark): ")
    
    generate_commits(start_date, end_date, intensity)
    push_changes()
    
    print("✅ Contributions added successfully!")

if __name__ == "__main__":
    main()
