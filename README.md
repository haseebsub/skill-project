# Skill Project

A project for developing and managing skills or assistants using Claude Code.

## 🚀 Quick Start

### Prerequisites
- Git installed on your system
- GitHub account (if pushing to remote)
- Claude Code (for skill development)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/haseebsub/skill-project.git
   cd skill-project
   ```

2. **Configure git (if needed):**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x git-workflow.sh
   ```

### 📝 Usage

#### Automatic Git Workflow
Use the provided scripts to automatically commit and push your changes:

**Bash (Linux/Mac):**
```bash
# Push with automatic commit message
./git-workflow.sh

# Push with custom commit message
./git-workflow.sh "Your custom commit message"
```

**PowerShell (Windows):**
```powershell
# Push with automatic commit message
.\git-workflow.ps1

# Push with custom commit message
.\git-workflow.ps1 -CommitMessage "Your custom commit message"
```

#### Manual Git Commands
```bash
# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to remote
git push
```

### 📁 Project Structure

```
skill-project/
├── README.md              # This file
├── claude.md             # Skill development guide
├── git-workflow.sh       # Bash script for automatic commits
├── git-workflow.ps1      # PowerShell script for automatic commits
└── .gitignore            # Git ignore file
```

## 🛠️ Development

### Creating Skills
Refer to `claude.md` for comprehensive guidelines on creating skills and assistants.

### Best Practices
- Always commit your work regularly
- Write meaningful commit messages
- Use the provided scripts for consistent workflow
- Keep your local repository in sync with remote

## 📚 Documentation

- **[Skill Development Guide](./claude.md)** - Complete guide for creating skills
- **[Git Workflow](#-usage)** - How to use the automatic git workflow

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Commit and push
6. Create a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related

- [Codelabs](https://codelabs.developers.google.com/?cat=Assistant)
- [Codelabs](https://codelabs.developers.google.com/?cat=Assistant)
- [API Best Practices](https://www.freecodecamp.org/news/rest-api-best-practices/)
- [Security Guidelines](https://owasp.org/)

---

**Note:** This project is designed to help you manage and develop skills efficiently. Always ensure your work is properly committed and pushed to avoid losing progress.