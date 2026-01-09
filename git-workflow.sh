#!/bin/bash

# GitHub Auto-Commit and Push Script
# Usage: ./git-workflow.sh [commit_message]

set -e  # Exit on any error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install git first."
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository. Please run 'git init' first."
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
print_status "Current branch: $CURRENT_BRANCH"

# Add all untracked files
print_status "Adding untracked files..."
git add .

# Check if there are any changes to commit
if git diff --cached --quiet; then
    print_warning "No changes to commit. Working directory is clean."
    exit 0
fi

# Get commit message
if [ -n "$1" ]; then
    COMMIT_MESSAGE="$1"
else
    # Generate automatic commit message based on changes
    NEW_FILES=$(git diff --cached --name-status | grep "^A" | wc -l)
    MODIFIED_FILES=$(git diff --cached --name-status | grep "^M" | wc -l)
    DELETED_FILES=$(git diff --cached --name-status | grep "^D" | wc -l)

    COMMIT_MESSAGE="Auto-commit: $NEW_FILES new files, $MODIFIED_FILES modified, $DELETED_FILES deleted ($(date '+%Y-%m-%d %H:%M:%S'))"
fi

# Create commit
print_status "Creating commit with message: $COMMIT_MESSAGE"
git commit -m "$COMMIT_MESSAGE"

# Check if we need to push to remote
if git remote | grep -q origin; then
    # Check if current branch tracks a remote branch
    if git rev-parse --abbrev-ref $CURRENT_BRANCH@{upstream} > /dev/null 2>&1; then
        print_status "Pushing to remote repository..."
        if git push; then
            print_success "Successfully pushed to remote repository"
        else
            print_error "Failed to push to remote repository"
            exit 1
        fi
    else
        print_warning "Current branch '$CURRENT_BRANCH' is not tracking a remote branch."
        print_status "Pushing with -u flag to set upstream..."
        if git push -u origin $CURRENT_BRANCH; then
            print_success "Successfully set upstream and pushed to remote"
        else
            print_error "Failed to push to remote repository"
            exit 1
        fi
    fi
else
    print_warning "No remote repository configured"
    print_status "To add a remote repository, run:"
    print_status "git remote add origin <repository-url>"
fi

print_success "Git workflow completed successfully!"