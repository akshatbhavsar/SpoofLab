# EST - Email Spoofing Tool

<div align="center">

![EST Logo](https://img.shields.io/badge/EST-Email%20Spoofing%20Tool-red?style=for-the-badge&logo=security&logoColor=white)

[![Version](https://img.shields.io/badge/version-2.0.1-blue.svg)](https://github.com/techsky-eh/EST)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)](https://github.com/techsky-eh/EST)
[![Kali](https://img.shields.io/badge/Kali%20Linux-Compatible-purple.svg)](https://kali.org)

**Professional Email Security Assessment Framework**

*For authorized penetration testing, security research, and educational purposes*

</div>

## 🎯 Overview

EST (Email Spoofing Tool) is a comprehensive, professional-grade framework designed for authorized email security assessments, penetration testing, and cybersecurity education. This tool demonstrates email spoofing vulnerabilities and helps security professionals evaluate the effectiveness of email authentication mechanisms.

### ⚠️ Legal Disclaimer

**EST is intended for authorized security testing and educational purposes only.** Users must obtain explicit written permission before testing any systems they do not own or have authorization to test. Unauthorized use of this tool may violate local, state, and federal laws. The developers assume no liability for misuse or damage caused by this program.

## ✨ Key Features

### 🔧 Core Capabilities
- **Professional SMTP Server** - Multi-threaded, RFC-compliant SMTP server for testing
- **Pre-built Attack Scenarios** - 5 realistic email spoofing scenarios covering common attack vectors
- **Custom Test Creation** - Build and execute custom spoofing tests with full control
- **Comprehensive Logging** - Detailed audit trails for all security tests
- **Assessment Reporting** - Generate professional security assessment reports
- **Real-time Email Relay** - Automatic delivery to real email destinations for testing
- **Python 3.13+ Compatible** - Works with latest Python versions including Kali Linux

### 🎭 Attack Scenarios Included

| Scenario | Category | Severity | Description |
|----------|----------|----------|-------------|
| CEO Fraud | Business Email Compromise | 🔴 Critical | Executive impersonation for wire transfer fraud |
| IT Helpdesk | Technical Support Fraud | 🟠 High | IT support impersonation for credential harvesting |
| PayPal Security | Financial Services Phishing | 🟠 High | Payment service spoofing for account compromise |
| Microsoft 365 | Software/License Fraud | 🟡 Medium | License expiration scam for credential theft |
| Bank Alert | Financial Institution Fraud | 🔴 Critical | Banking institution impersonation |

### 🏗️ Architecture

```
EST Framework
├── SMTP Testing Server (Multi-threaded)
├── Scenario Engine (Pre-built + Custom)
├── Email Relay System (MX Resolution)
├── Audit & Logging System
├── Report Generation Engine
├── Python Environment Manager (3.13+ compatible)
└── Professional CLI Interface
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher (including Python 3.13+)
- Linux/macOS/Windows (optimized for Kali Linux)
- Network connectivity for email delivery testing

### Installation

#### 🐧 Kali Linux / Python 3.13+ (Recommended)

```bash
# Clone the repository
git clone https://github.com/techsky-eh/EST.git
cd EST

# Make installer executable
chmod +x install.sh

# Run the fixed installer (handles Python 3.13+ automatically)
./install.sh
```

The installer will automatically:
- Detect Python 3.13+ and create a virtual environment
- Install system dependencies via apt
- Handle externally-managed-environment issues
- Create isolated Python environment for EST

#### 🖥️ Other Linux Distributions

```bash
# Clone the repository
git clone https://github.com/techsky-eh/EST.git
cd EST

# Install dependencies
pip install -r requirements.txt

# Install system-wide (optional)
sudo ./install.sh
```

#### 🍎 macOS

```bash
# Install Python and dependencies
brew install python3 telnet

# Clone and install EST
git clone https://github.com/techsky-eh/EST.git
cd EST
./install.sh
```

### Basic Usage

```bash
# Start SMTP testing server
est server --port 2525

# List available attack scenarios
est list

# Execute CEO fraud scenario
est test 1 target@company.com

# Run custom spoofing test
est custom --from-email "ceo@company.com" \
           --from-name "John Smith, CEO" \
           --subject "Urgent Request" \
           --body "Please handle this immediately" \
           --target "employee@company.com"

# View test logs
est logs --lines 50

# Generate assessment report
est report
```

## 📚 Comprehensive Documentation

### Command Reference

#### Server Operations
```bash
# Start SMTP server (standard port, requires sudo)
sudo est server --port 25

# Start on unprivileged port (recommended)
est server --port 2525

# Bind to specific interface
est server --host 192.168.1.100 --port 2525
```

#### Testing Operations
```bash
# List all scenarios with details
est list

# Execute specific scenario by ID
est test <scenario_id> <target_email>

# Execute with custom SMTP server
est test 1 target@company.com --smtp-host mail.company.com --smtp-port 25

# Custom spoofing test
est custom --from-email <sender> \
           --from-name <display_name> \
           --subject <subject> \
           --body <message_body> \
           --target <target_email>
```

#### Monitoring & Reporting
```bash
# View recent test logs
est logs

# View more log entries
est logs --lines 100

# Generate comprehensive report
est report

# Generate report to specific file
est report --output /path/to/report.json
```

### Configuration

EST stores configuration in `~/.est/config.json`:

```json
{
  "version": "2.0.1",
  "smtp_server": {
    "host": "0.0.0.0",
    "port": 2525,
    "timeout": 30
  },
  "scenarios": [
    {
      "name": "Custom CEO Fraud",
      "category": "Business Email Compromise",
      "from_email": "ceo@yourcompany.com",
      "from_name": "Your CEO Name",
      "subject": "Urgent Business Matter",
      "body": "Custom email body...",
      "description": "Custom scenario description",
      "severity": "Critical"
    }
  ],
  "temp_email_services": [
    "guerrillamail.com",
    "mailinator.com"
  ]
}
```

## 🔬 Advanced Usage

### Professional Assessment Workflow

1. **Environment Setup**
   ```bash
   # Start EST server in isolated environment
   est server --port 2525
   ```

2. **Baseline Testing**
   ```bash
   # Test with temporary email addresses first
   est test 1 test@guerrillamail.com
   est test 2 test@mailinator.com
   ```

3. **Target Assessment**
   ```bash
   # Execute scenarios against target domain
   est test 1 employee@target-company.com
   est test 3 finance@target-company.com
   ```

4. **Custom Attack Simulation**
   ```bash
   # Company-specific spoofing tests
   est custom --from-email "ceo@target-company.com" \
              --from-name "Target CEO Name" \
              --subject "Quarterly Budget Review" \
              --body "Please review attached budget..." \
              --target "cfo@target-company.com"
   ```

5. **Results Analysis**
   ```bash
   # Review logs and generate report
   est logs --lines 100
   est report --output assessment_report.json
   ```

### Integration with Security Testing

EST integrates seamlessly with other security testing tools:

```bash
# Use with network analysis
tcpdump -i any port 25 &
est test 1 target@company.com

# Combine with social engineering toolkit
# Use EST for email component of broader campaigns

# Integration with reporting frameworks
est report --output ./reports/email_assessment.json
```

## 📊 Sample Output

### Scenario Execution
```
🎯 Executing Email Spoofing Test
────────────────────────────────────────
📧 Scenario: CEO Fraud - Urgent Wire Transfer
🏷️  Category: Business Email Compromise
⚠️  Severity: Critical
📤 Spoofed From: John Smith, CEO <ceo@targetcompany.com>
📥 Target: employee@company.com
📡 SMTP Server: localhost:2525
🕐 Timestamp: 2024-03-15 14:30:22

🚀 Initiating SMTP connection...
📤 Sending spoofed email...
✅ Email spoofing test completed successfully!
📋 Check target inbox: employee@company.com
```

### Assessment Report Summary
```
📋 EST Security Assessment Summary
══════════════════════════════════════════════════
📊 Total Tests: 15
✅ Successful: 12
❌ Failed: 3
📈 Success Rate: 80.0%
🔴 Risk Level: CRITICAL - Immediate action required

📚 Recommendations: 8 items
   • 🔴 CRITICAL: High email spoofing success rate detected
   • Implement SPF, DKIM, and DMARC email authentication
   • Configure email security gateways with spoofing detection
   ... and 5 more
```

## 🛡️ Security Best Practices

### For Security Professionals
- **Always obtain written authorization** before conducting tests
- **Use isolated test environments** when possible
- **Document all testing activities** for compliance
- **Follow responsible disclosure** for any vulnerabilities found
- **Respect privacy and confidentiality** of all test data

### Recommended Test Environment
- Isolated network segment for testing
- Virtual machines for server deployment
- Temporary email services for initial validation
- Proper logging and monitoring infrastructure

### Legal Compliance
- Obtain explicit written permission from system owners
- Ensure compliance with local and international laws
- Document the scope and limitations of testing
- Maintain confidentiality of test results
- Follow organizational security policies

## 🔧 Troubleshooting

### Python 3.13+ / Kali Linux Issues

**Problem**: `externally-managed-environment` error
```bash
# Solution 1: Use the fixed installer (automatically creates venv)
./install.sh

# Solution 2: Manual virtual environment
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install dnspython

# Solution 3: Use system packages
sudo apt install python3-dnspython
```

**Problem**: Virtual environment not found
```bash
# Solution: Reinstall or recreate environment
rm -rf ~/.est-env
./install.sh

# Or manually recreate
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install -r requirements.txt
```

### Common Issues

**Port Permission Denied**
```bash
# Solution: Use unprivileged port or run as root
est server --port 2525
# OR
sudo est server --port 25
```

**DNS Resolution Failures**
```bash
# Install DNS library
sudo apt install python3-dnspython
# OR in virtual environment
source ~/.est-env/bin/activate
pip install dnspython
```

**Email Delivery Failures**
```bash
# Check SMTP server logs
est logs

# Verify target email service is accessible
dig MX target-domain.com

# Test with known working temporary email services
est test 1 test@guerrillamail.com
```

**Command Not Found**
```bash
# Run directly if not installed system-wide
python3 est.py --help

# Or reinstall
./install.sh

# Check if virtual environment is needed
source ~/.est-env/bin/activate
est --help
```

### Environment Verification

```bash
# Check EST installation
est --help

# Verify Python environment
python3 -c "import dns.resolver; print('DNS module working')"

# Check virtual environment (if used)
echo $VIRTUAL_ENV

# Test basic functionality
est list
```

## 🎓 Educational Use Cases

### Security Awareness Training
- Demonstrate realistic email spoofing attacks
- Show participants how phishing emails are crafted
- Test user awareness and response procedures
- Provide hands-on experience with email security

### Academic Research
- Study email authentication mechanisms
- Analyze effectiveness of security controls
- Research social engineering techniques
- Develop new detection methods

### Penetration Testing (Authorized)
- Assess organizational email security posture
- Test effectiveness of SPF/DKIM/DMARC policies
- Evaluate user susceptibility to social engineering
- Validate email security gateway configurations

## 🤝 Contributing

We welcome contributions from the security community:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed
- Ensure compatibility with Python 3.8+
- Test with both virtual environments and system Python

## 🐧 Kali Linux Optimization

EST is specifically optimized for Kali Linux:

### Features
- **Automatic virtual environment setup** for Python 3.13+
- **System package integration** with apt
- **Network interface binding** for pentesting environments
- **Integration with Kali tools** and workflows

### Installation
```bash
# One-command installation on Kali
./install.sh

# Manual method for Kali
sudo apt install python3-dnspython telnet dnsutils
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install setuptools wheel
python3 est.py --help
```

### Usage in Penetration Testing
```bash
# Professional pentest workflow
est server --port 2525 &
est test 1 target@victim.com
est report --output /root/pentest-reports/email-assessment.json

# Integration with other tools
tcpdump -i any port 25 &
est test 1 target@example.com
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Changelog

### v2.0.1 (2025-06-12)
- **Fixed Python 3.13+ compatibility** - Automatic virtual environment creation
- **Enhanced Kali Linux support** - Optimized installation for latest Kali
- **Improved error handling** - Better externally-managed-environment handling
- **Updated documentation** - Comprehensive troubleshooting for modern Python
- **System package integration** - Prefer apt packages over pip when available

### v2.0.0 (2025-06-12)
- Complete rewrite for professional security testing
- Multi-threaded SMTP server with real-time email relay
- 5 realistic attack scenarios covering major threat vectors
- Professional CLI interface with comprehensive logging
- Cross-platform compatibility and desktop integration

## 🙏 Acknowledgments

- Security research community for vulnerability insights
- Email authentication standards organizations
- Open source contributors and maintainers
- Educational institutions supporting cybersecurity research
- Kali Linux team for providing excellent penetration testing platform

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/techsky-eh/EST/issues)
- **Documentation**: [Wiki](https://github.com/techsky-eh/EST/wiki)
- **Security Reports**: contact@techskyhub.com
- **General Questions**: contact@techskyhub.com

### Quick Support

For common issues:
1. **Python 3.13+ problems**: Use `./install.sh` (auto-creates venv)
2. **Kali Linux issues**: Install via `sudo apt install python3-dnspython`
3. **Permission errors**: Use `est server --port 2525` instead of port 25
4. **Command not found**: Run `source ~/.est-env/bin/activate` then try again

---

<div align="center">

**EST v2.0.1** - Professional Email Security Assessment Framework

Compatible with Python 3.8+ including Python 3.13+ and Kali Linux

Made with ❤️ by the Tech Sky - Security Research Team

</div>