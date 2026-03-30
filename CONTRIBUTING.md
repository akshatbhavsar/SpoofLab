# Contributing to EST (Email Spoofing Tool)

Thank you for your interest in contributing to EST! This document provides guidelines and information for contributors.

## 🚨 Legal Notice

**IMPORTANT**: EST is designed for authorized security testing, penetration testing, and educational purposes only. By contributing to this project, you acknowledge that:

- You will only use EST for legitimate, authorized security testing
- You understand the legal implications of email spoofing tools
- You agree to obtain explicit written permission before testing any systems you do not own
- Unauthorized use may violate local, state, and federal laws

## 🎯 Ways to Contribute

### 1. Bug Reports
- Use GitHub Issues to report bugs
- Include detailed steps to reproduce
- Provide system information (OS, Python version)
- Include relevant log files or error messages

### 2. Feature Requests
- Propose new security testing scenarios
- Suggest improvements to existing functionality
- Request documentation enhancements

### 3. Code Contributions
- Fix bugs or implement new features
- Improve code quality and performance
- Add unit tests for new functionality
- Update documentation

### 4. Documentation
- Improve README or documentation
- Add examples and tutorials
- Fix typos or clarify instructions
- Translate documentation

## 🛠️ Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- pip3

### Getting Started

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/techsky-eh/EST.git
   cd EST
   ```

2. **Set up development environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate   # Windows
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Install in development mode
   pip install -e .
   ```

3. **Test the installation**
   ```bash
   python3 est.py --help
   ```

## 📋 Code Guidelines

### Python Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep lines under 88 characters when possible

### Security Considerations
- Never commit real email addresses or credentials
- Use placeholder domains for examples
- Ensure all test data is clearly marked as test data
- Review code for potential security vulnerabilities

### Testing
- Add unit tests for new functionality
- Test on multiple Python versions (3.8+)
- Verify functionality on different operating systems
- Test installation procedures

## 🔄 Pull Request Process

### Before Submitting
1. **Check existing issues** - Make sure your contribution isn't already being worked on
2. **Open an issue** - For significant changes, discuss your approach first
3. **Create a branch** - Use descriptive branch names like `fix-smtp-timeout` or `add-oauth-support`

### Submitting Your PR
1. **Clear description** - Explain what changes you made and why
2. **Link issues** - Reference related issues using `Fixes #123`
3. **Update documentation** - Include relevant documentation updates
4. **Add tests** - Include tests for new functionality

### PR Template
```
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that changes existing functionality)
- [ ] Documentation update

## Testing
- [ ] I have tested these changes locally
- [ ] I have added tests that prove my fix is effective
- [ ] I have updated documentation as needed

## Security Impact
- [ ] These changes do not introduce security vulnerabilities
- [ ] I have reviewed the code for potential security issues
- [ ] Documentation includes appropriate security warnings

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] My changes generate no new warnings
```

## 🧪 Testing Guidelines

### Running Tests
```bash
# Run all tests
python3 -m pytest

# Run specific test file
python3 -m pytest tests/test_smtp_server.py

# Run with coverage
python3 -m pytest --cov=est
```

### Test Categories
- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test component interactions
- **Security Tests**: Verify security features work correctly
- **Installation Tests**: Test installation procedures

## 📚 Documentation Standards

### Code Documentation
- Use Google-style docstrings
- Include parameter types and return values
- Provide usage examples where helpful

### README Updates
- Keep installation instructions current
- Update feature lists for new functionality
- Include relevant security warnings

## 🐛 Bug Report Template

When reporting bugs, please include:

```
**EST Version**: [e.g., 2.0.0]
**Python Version**: [e.g., 3.9.7]
**Operating System**: [e.g., Ubuntu 20.04]

**Description**
A clear description of the bug

**Steps to Reproduce**
1. Run command: `est server --port 2525`
2. Execute: `est test 1 test@example.com`
3. See error...

**Expected Behavior**
What you expected to happen

**Actual Behavior**
What actually happened

**Error Messages**
```
Include any error messages or logs
```

**Additional Context**
Any other context about the problem
```

## 🚀 Feature Request Template

```
**Feature Description**
A clear description of the feature you'd like to see

**Use Case**
Explain how this feature would be used

**Current Workaround**
How do you currently achieve this (if possible)?

**Additional Context**
Any other context, mockups, or examples
```

## 📋 Security Scenario Contributions

### Adding New Attack Scenarios
When contributing new email spoofing scenarios:

1. **Realistic**: Based on actual attack patterns
2. **Educational**: Include clear descriptions of the attack
3. **Ethical**: Include appropriate warnings and disclaimers
4. **Categorized**: Fit into existing categories or propose new ones
5. **Severity Rated**: Use Critical/High/Medium/Low severity levels

### Scenario Template
```python
{
    "name": "Brief Descriptive Name",
    "category": "Attack Category",
    "from_email": "spoofed@domain.com",
    "from_name": "Display Name",
    "subject": "Email Subject Line",
    "body": "Email body with clear attack simulation...",
    "description": "Educational description of the attack type",
    "severity": "Critical/High/Medium/Low"
}
```

## 📞 Getting Help

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussion
- **Security Issues**: Email security@your-domain.com (private disclosure)

### Code Review Process
1. All contributions require review by project maintainers
2. Reviews focus on functionality, security, and code quality
3. Address review feedback promptly
4. Maintainers will merge approved PRs

## 🏆 Recognition

Contributors will be:
- Added to the Contributors section in README.md
- Mentioned in release notes for significant contributions
- Given appropriate credit in documentation

## 📋 Contributor License Agreement

By contributing to EST, you agree that:
- Your contributions will be licensed under the same license as the project (MIT)
- You have the right to submit the contribution
- You understand this is an open source project

## ❓ Questions?

If you have questions about contributing:
1. Check existing GitHub Issues and Discussions
2. Read through this CONTRIBUTING.md file
3. Open a new GitHub Discussion for general questions
4. Open a GitHub Issue for specific bugs or feature requests

Thank you for helping make EST a better security testing tool! 🛡️