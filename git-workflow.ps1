#!/usr/bin/env pwsh

# PowerShell GitHub Auto-Commit and Push Script
# Usage: ./git-workflow.ps1 [-CommitMessage "your message"]

param(
    [string]$CommitMessage
)

# Colors for output
$GREEN = [ConsoleColor]::Green
$BLUE = [ConsoleColor]::Cyan
$YELLOW = [ConsoleColor]::Yellow
$RED = [ConsoleColor]::Red

# Function to print colored output
function Write-Status {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor $BLUE
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor $GREEN
}

function Write-WarningMsg {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor $YELLOW
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor $RED
}

# Check if git is installed
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed. Please install git first."
    exit 1
}

# Check if we're in a git repository
if (-not (Test-Path .git)) {
    Write-Error "Not in a git repository. Please run 'git init' first."
    exit 1
}

# Get current branch
$CurrentBranch = git rev-parse --abbrev-ref HEAD
Write-Status "Current branch: $CurrentBranch"

# Add all untracked files
Write-Status "Adding untracked files..."
git add .

# Check if there are any changes to commit
if (git diff --cached --quiet) {
    Write-WarningMsg "No changes to commit. Working directory is clean."
    exit 0
}

# Get commit message
if ($CommitMessage) {
    $FinalCommitMessage = $CommitMessage
} else {
    # Generate automatic commit message based on changes
    $DiffStatus = git diff --cached --name-status
    $NewFiles = ($DiffStatus | Where-Object { $_ -match "^A" }).Count
    $ModifiedFiles = ($DiffStatus | Where-Object { $_ -match "^M" }).Count
    $DeletedFiles = ($DiffStatus | Where-Object { $_ -match "^D" }).Count

    $FinalCommitMessage = "Auto-commit: $NewFiles new files, $ModifiedFiles modified, $DeletedFiles deleted ($(Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))"
}

# Create commit
Write-Status "Creating commit with message: $FinalCommitMessage"
git commit -m $FinalCommitMessage

# Check if we need to push to remote
$HasRemote = git remote | Select-String -Pattern "origin" -Quiet
if ($HasRemote) {
    # Check if current branch tracks a remote branch
    try {
        $UpstreamBranch = git rev-parse --abbrev-ref "$CurrentBranch@{upstream}"
        $HasUpstream = $true
    } catch {
        $HasUpstream = $false
    }

    if ($HasUpstream) {
        Write-Status "Pushing to remote repository..."
        if (git push) {
            Write-Success "Successfully pushed to remote repository"
        } else {
            Write-Error "Failed to push to remote repository"
            exit 1
        }
    } else {
        Write-WarningMsg "Current branch '$CurrentBranch' is not tracking a remote branch."
        Write-Status "Pushing with -u flag to set upstream..."
        if (git push -u origin $CurrentBranch) {
            Write-Success "Successfully set upstream and pushed to remote"
        } else {
            Write-Error "Failed to push to remote repository"
            exit 1
        }
    }
} else {
    Write-WarningMsg "No remote repository configured"
    Write-Status "To add a remote repository, run:"
    Write-Status "git remote add origin <repository-url>"
}

Write-Success "Git workflow completed successfully!"