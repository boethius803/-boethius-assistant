#!/bin/bash
# Auto-backup script for Boethius

cd /home/node/.openclaw/workspace

# Add all changes
git add -A

# Check if there are changes
if git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit with timestamp
git commit -m "Auto-backup $(date '+%Y-%m-%d %H:%M')"

# Push to GitHub (token from git remote)
git push

echo "Backup complete: $(date)"
