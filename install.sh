#!/bin/bash
#
# EST - Email Spoofing Tool
# Professional Installation Script for Linux Systems (Fixed for Python 3.13+)
#
# Author: Security Research Team
# Version: 1.0.0
# License: MIT
#

set -e

# Colors for output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly PURPLE='\033[0;35m'
readonly CYAN='\033[0;36m'
readonly NC='\033[0m' # No Color

# Tool configuration
readonly TOOL_NAME="SpoofLab: Advanced Email Spoofing Detection and Simulation Framework"
readonly TOOL_VERSION="1.0.0"
readonly TOOL_AUTHOR="Akshat & khushi "
readonly INSTALL_DIR="/opt/est"
readonly BIN_LINK="/usr/local/bin/est"
readonly DESKTOP_DIR="/usr/share/applications"
readonly ICON_DIR="/usr/share/pixmaps"
readonly VENV_DIR="$HOME/.est-env"

# Status functions
print_banner() {
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║                    EST INSTALLER v${TOOL_VERSION}                      ║${NC}"
    echo -e "${BLUE}║              Email Spoofing Tool - Professional              ║${NC}"
    echo -e "${BLUE}║                                                              ║${NC}"
    echo -e "${BLUE}║     Advanced Email Security Assessment Framework             ║${NC}"
    echo -e "${BLUE}║     For Authorized Penetration Testing Only                  ║${NC}"
    echo -e "${BLUE}║     Educational & Research Purposes                          ║${NC}"
    echo -e "${BLUE}║                                                              ║${NC}"
    echo -e "${BLUE}║  Author: ${TOOL_AUTHOR}${NC}${BLUE}                                      ║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo
}

print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

print_step() {
    echo -e "${PURPLE}[→]${NC} $1"
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
       print_error "Please don't run this script as root!"
       echo -e "${YELLOW}💡 Run as regular user with sudo access: ./install.sh${NC}"
       exit 1
    fi
}

# Check system compatibility
check_system() {
    print_step "Checking system compatibility..."
    
    # Check OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        print_status "Linux system detected"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        print_status "macOS system detected"
    else
        print_warning "Unsupported OS detected, proceeding anyway..."
    fi
    
    # Check Python 3
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        echo "Please install Python 3.8 or higher:"
        echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
        echo "  CentOS/RHEL:   sudo yum install python3 python3-pip"
        echo "  macOS:         brew install python3"
        exit 1
    fi
    
    # Check Python version
    PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
        print_status "Python $PYTHON_VERSION detected (compatible)"
        
        # Check if Python 3.13+ (externally managed environment)
        if [ "$PYTHON_MINOR" -ge 13 ]; then
            print_warning "Python 3.13+ detected - will use virtual environment"
            USE_VENV=true
        else
            USE_VENV=false
        fi
    else
        print_error "Python 3.8+ required, found $PYTHON_VERSION"
        exit 1
    fi
    
    # Check if we're on Kali Linux
    if [ -f /etc/os-release ]; then
        if grep -q "Kali" /etc/os-release; then
            print_status "Kali Linux detected - using optimized installation"
            IS_KALI=true
            USE_VENV=true  # Always use venv on Kali
        else
            IS_KALI=false
        fi
    fi
    
    print_status "System compatibility check passed"
}

# Install system dependencies
install_dependencies() {
    print_step "Installing system dependencies..."
    
    # Detect package manager and install dependencies
    if command -v apt &> /dev/null; then
        print_info "Using apt package manager (Debian/Ubuntu/Kali)"
        sudo apt update
        
        # Install core dependencies
        sudo apt install -y \
            python3-dev \
            python3-pip \
            python3-setuptools \
            python3-wheel \
            python3-venv \
            telnet \
            dnsutils \
            curl \
            git
        
        # Install Python DNS library via apt (preferred for system packages)
        if sudo apt install -y python3-dnspython; then
            print_status "DNS library installed via system package manager"
            SYSTEM_DNS_INSTALLED=true
        else
            print_warning "System DNS package not available, will install via pip"
            SYSTEM_DNS_INSTALLED=false
        fi
        
    elif command -v yum &> /dev/null; then
        print_info "Using yum package manager (CentOS/RHEL)"
        sudo yum update -y
        sudo yum install -y \
            python3-devel \
            python3-pip \
            python3-setuptools \
            python3-venv \
            telnet \
            bind-utils \
            curl \
            git
        SYSTEM_DNS_INSTALLED=false
        
    elif command -v dnf &> /dev/null; then
        print_info "Using dnf package manager (Fedora)"
        sudo dnf update -y
        sudo dnf install -y \
            python3-devel \
            python3-pip \
            python3-setuptools \
            python3-venv \
            telnet \
            bind-utils \
            curl \
            git \
            python3-dns
        SYSTEM_DNS_INSTALLED=true
        
    elif command -v pacman &> /dev/null; then
        print_info "Using pacman package manager (Arch Linux)"
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm \
            python \
            python-pip \
            python-setuptools \
            python-virtualenv \
            inetutils \
            bind \
            curl \
            git \
            python-dnspython
        SYSTEM_DNS_INSTALLED=true
            
    elif command -v brew &> /dev/null; then
        print_info "Using Homebrew (macOS)"
        brew install python3 telnet
        SYSTEM_DNS_INSTALLED=false
        
    else
        print_warning "Unknown package manager, will install Python dependencies manually"
        SYSTEM_DNS_INSTALLED=false
    fi
    
    print_status "System dependencies installed successfully"
}

# Setup Python environment
setup_python_environment() {
    print_step "Setting up Python environment..."
    
    if [ "$USE_VENV" = true ]; then
        print_info "Creating isolated Python virtual environment..."
        
        # Remove existing venv if it exists
        if [ -d "$VENV_DIR" ]; then
            print_warning "Removing existing virtual environment..."
            rm -rf "$VENV_DIR"
        fi
        
        # Create new virtual environment
        python3 -m venv "$VENV_DIR"
        print_status "Virtual environment created at $VENV_DIR"
        
        # Activate virtual environment
        source "$VENV_DIR/bin/activate"
        print_status "Virtual environment activated"
        
        # Upgrade pip in virtual environment
        pip install --upgrade pip setuptools wheel
        
        # Install Python dependencies in virtual environment
        print_info "Installing Python dependencies in virtual environment..."
        if [ "$SYSTEM_DNS_INSTALLED" = false ]; then
            pip install dnspython
            print_status "DNS library installed in virtual environment"
        else
            print_status "Using system DNS library"
        fi
        
        PYTHON_ENV="venv"
        
    else
        print_info "Using system Python environment..."
        
        # Try to install dependencies
        print_info "Installing Python dependencies..."
        
        # Try different installation methods
        if pip3 install --user dnspython setuptools wheel 2>/dev/null; then
            print_status "Dependencies installed via pip --user"
        elif pip3 install --user --break-system-packages dnspython setuptools wheel 2>/dev/null; then
            print_status "Dependencies installed with system override"
        elif [ "$SYSTEM_DNS_INSTALLED" = true ]; then
            print_status "Using system-installed DNS library"
        else
            print_error "Failed to install Python dependencies"
            echo "Please install manually:"
            echo "  sudo apt install python3-dnspython  # Debian/Ubuntu"
            echo "  pip3 install --user dnspython        # Manual install"
            exit 1
        fi
        
        PYTHON_ENV="system"
    fi
    
    print_status "Python environment setup completed ($PYTHON_ENV)"
}

# Create installation directories
setup_directories() {
    print_step "Setting up installation directories..."
    
    # Create main installation directory
    if [ ! -d "$INSTALL_DIR" ]; then
        sudo mkdir -p "$INSTALL_DIR"
        sudo chown $USER:$(id -gn) "$INSTALL_DIR"
        print_status "Created installation directory: $INSTALL_DIR"
    fi
    
    # Create subdirectories
    sudo mkdir -p "$INSTALL_DIR"/{bin,lib,docs,examples}
    sudo chown -R $USER:$(id -gn) "$INSTALL_DIR"
    
    # Create user configuration directory
    USER_CONFIG_DIR="$HOME/.est"
    mkdir -p "$USER_CONFIG_DIR"/{reports,logs,scenarios}
    print_status "Created user configuration directory: $USER_CONFIG_DIR"
    
    print_status "Directory structure created"
}

# Install EST tool
install_tool() {
    print_step "Installing EST tool..."
    
    # Check if main script exists
    if [ ! -f "est.py" ]; then
        print_error "est.py not found in current directory"
        echo "Please ensure you have the EST source files:"
        echo "  - est.py (main application)"
        echo "  - requirements.txt (dependencies)"
        echo "  - README.md (documentation)"
        exit 1
    fi
    
    # Copy main application
    cp est.py "$INSTALL_DIR/bin/"
    chmod +x "$INSTALL_DIR/bin/est.py"
    print_status "Installed main application"
    
    # Create wrapper script based on Python environment
    create_wrapper_script
    
    # Create symbolic link
    sudo ln -sf "$INSTALL_DIR/bin/est" "$BIN_LINK"
    print_status "Created system-wide command link"
    
    # Copy documentation
    if [ -f "README.md" ]; then
        cp README.md "$INSTALL_DIR/docs/"
        print_status "Installed documentation"
    fi
    
    # Copy requirements.txt if it exists
    if [ -f "requirements.txt" ]; then
        cp requirements.txt "$INSTALL_DIR/docs/"
        print_status "Installed requirements file"
    fi
    
    # Copy other documentation files
    for doc in CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE; do
        if [ -f "$doc" ]; then
            cp "$doc" "$INSTALL_DIR/docs/"
        fi
    done
    
    # Copy examples if they exist
    if [ -d "examples" ]; then
        cp -r examples/* "$INSTALL_DIR/examples/"
        print_status "Installed example configurations"
    fi
    
    print_status "EST tool installation completed"
}

# Create wrapper script for better user experience
create_wrapper_script() {
    if [ "$USE_VENV" = true ]; then
        # Create wrapper that uses virtual environment
        cat > "$INSTALL_DIR/bin/est" << EOF
#!/bin/bash
#
# EST - Email Spoofing Tool Wrapper Script (Virtual Environment)
# This script activates the virtual environment and runs EST
#

INSTALL_DIR="$INSTALL_DIR"
MAIN_SCRIPT="\$INSTALL_DIR/bin/est.py"
VENV_DIR="$VENV_DIR"

# Check if virtual environment exists
if [ ! -d "\$VENV_DIR" ]; then
    echo "❌ EST virtual environment not found at \$VENV_DIR"
    echo "💡 Try reinstalling: ./install.sh"
    exit 1
fi

# Check if main script exists
if [ ! -f "\$MAIN_SCRIPT" ]; then
    echo "❌ EST installation not found at \$INSTALL_DIR"
    echo "💡 Try reinstalling: ./install.sh"
    exit 1
fi

# Activate virtual environment and execute
source "\$VENV_DIR/bin/activate"
exec python3 "\$MAIN_SCRIPT" "\$@"
EOF
    else
        # Create wrapper for system Python
        cat > "$INSTALL_DIR/bin/est" << EOF
#!/bin/bash
#
# EST - Email Spoofing Tool Wrapper Script (System Python)
# This script provides a clean interface to the EST tool
#

INSTALL_DIR="$INSTALL_DIR"
MAIN_SCRIPT="\$INSTALL_DIR/bin/est.py"

# Check if main script exists
if [ ! -f "\$MAIN_SCRIPT" ]; then
    echo "❌ EST installation not found at \$INSTALL_DIR"
    echo "💡 Try reinstalling: ./install.sh"
    exit 1
fi

# Add install directory to Python path
export PYTHONPATH="\$INSTALL_DIR/lib:\$PYTHONPATH"

# Execute main script with all arguments
exec python3 "\$MAIN_SCRIPT" "\$@"
EOF
    fi
    
    chmod +x "$INSTALL_DIR/bin/est"
    print_status "Created wrapper script for $PYTHON_ENV environment"
}

# Create desktop entry for GUI environments
create_desktop_entry() {
    print_step "Creating desktop integration..."
    
    # Create desktop entry
    DESKTOP_FILE="$HOME/.local/share/applications/est.desktop"
    mkdir -p "$(dirname "$DESKTOP_FILE")"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Name=EST - Email Spoofing Tool
Comment=Professional Email Security Assessment Framework
GenericName=Security Testing Tool
Exec=gnome-terminal --title="EST - Email Spoofing Tool" -- est
Icon=security-high
Terminal=true
Type=Application
Categories=Security;Network;Development;
Keywords=email;security;testing;penetration;spoofing;assessment;
StartupNotify=true
EOF
    
    # Create system-wide desktop entry (if possible)
    if [ -w "$DESKTOP_DIR" ] || sudo [ -w "$DESKTOP_DIR" ] 2>/dev/null; then
        sudo cp "$DESKTOP_FILE" "$DESKTOP_DIR/" 2>/dev/null || true
        print_status "Created desktop entry"
    else
        print_status "Created user desktop entry"
    fi
    
    print_status "Desktop integration completed"
}

# Create comprehensive documentation
create_documentation() {
    print_step "Creating documentation..."
    
    DOC_DIR="$INSTALL_DIR/docs"
    
    # Create quick start guide
    cat > "$DOC_DIR/QUICKSTART.md" << 'EOF'
# EST Quick Start Guide

## Basic Commands

### Start SMTP Server
```bash
# Start on unprivileged port (recommended)
est server --port 2525

# Start on standard SMTP port (requires sudo)
sudo est server --port 25
```

### List Attack Scenarios
```bash
est list
```

### Run Security Test
```bash
# Execute predefined scenario
est test 1 target@company.com

# Custom spoofing test
est custom --from-email "ceo@company.com" \
           --from-name "John Smith" \
           --subject "Urgent Request" \
           --body "Please handle this immediately" \
           --target "employee@company.com"
```

### Monitor and Report
```bash
# View test logs
est logs --lines 50

# Generate assessment report
est report
```

## Configuration

- Config file: `~/.est/config.json`
- Log files: `~/.est/est_tests.log`
- Reports: `~/.est/reports/`

## Troubleshooting

If you encounter Python environment issues:

### Virtual Environment Issues
```bash
# Check if virtual environment is active
echo $VIRTUAL_ENV

# Manually activate if needed
source ~/.est-env/bin/activate

# Reinstall if corrupted
rm -rf ~/.est-env
./install.sh
```

### System Python Issues
```bash
# Install missing dependencies
sudo apt install python3-dnspython

# Use system override if needed
pip3 install --user --break-system-packages dnspython
```

## Support

- Documentation: /opt/est/docs/
- Examples: /opt/est/examples/
- Issues: https://github.com/your-org/EST/issues
EOF

    # Create troubleshooting guide
    cat > "$DOC_DIR/TROUBLESHOOTING.md" << 'EOF'
# EST Troubleshooting Guide

## Python Environment Issues

### Virtual Environment Not Found
**Problem**: EST can't find virtual environment
**Solution**: 
```bash
# Reinstall EST
./install.sh

# Or manually recreate
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install dnspython
```

### Externally Managed Environment Error
**Problem**: pip install fails with "externally-managed-environment"
**Solution**:
```bash
# Option 1: Use virtual environment (recommended)
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install dnspython

# Option 2: Use system packages
sudo apt install python3-dnspython

# Option 3: Override (use with caution)
pip3 install --user --break-system-packages dnspython
```

## Common Issues

### Port Permission Denied
**Problem**: Cannot bind to port 25
**Solution**: 
```bash
# Use unprivileged port
est server --port 2525

# OR run as root for port 25
sudo est server --port 25
```

### DNS Resolution Failures
**Problem**: Cannot resolve MX records
**Solution**:
```bash
# Install DNS library
sudo apt install python3-dnspython

# Verify DNS functionality
dig MX example.com
```

### Email Delivery Failures
**Problem**: Emails not reaching targets
**Solution**:
1. Check SMTP server logs: `est logs`
2. Verify target domain: `dig MX target-domain.com`
3. Test with temporary email: `est test 1 test@guerrillamail.com`

### Command Not Found
**Problem**: `est` command not available
**Solution**:
```bash
# Reinstall tool
./install.sh

# Or run directly
python3 /opt/est/bin/est.py --help

# Check if virtual environment is needed
source ~/.est-env/bin/activate
est --help
```

### Module Import Errors
**Problem**: Missing Python modules
**Solution**:
```bash
# For virtual environment
source ~/.est-env/bin/activate
pip install dnspython

# For system installation
sudo apt install python3-dnspython

# Check Python path
python3 -c "import dns.resolver; print('DNS module working')"
```

## Kali Linux Specific

### Python 3.13+ Issues
Kali Linux uses Python 3.13+ which has stricter package management:

```bash
# Always use virtual environment on Kali
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install dnspython

# Or use system packages
sudo apt install python3-dnspython
```

### Network Interface Issues
```bash
# Bind to specific interface
est server --host 192.168.1.100 --port 2525

# Check network interfaces
ip addr show
```
EOF

    print_status "Documentation created"
}

# Install bash completion
install_bash_completion() {
    print_step "Installing bash completion..."
    
    COMPLETION_DIR="/etc/bash_completion.d"
    COMPLETION_FILE="$COMPLETION_DIR/est"
    
    if [ -d "$COMPLETION_DIR" ]; then
        cat > "/tmp/est_completion" << 'EOF'
# EST bash completion
_est_completion() {
    local cur prev commands
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="server list test custom logs report"
    
    case ${prev} in
        est)
            COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
            return 0
            ;;
        server)
            COMPREPLY=( $(compgen -W "--host --port" -- ${cur}) )
            return 0
            ;;
        test)
            COMPREPLY=( $(compgen -W "1 2 3 4 5" -- ${cur}) )
            return 0
            ;;
        logs)
            COMPREPLY=( $(compgen -W "--lines" -- ${cur}) )
            return 0
            ;;
        report)
            COMPREPLY=( $(compgen -W "--output" -- ${cur}) )
            return 0
            ;;
        custom)
            COMPREPLY=( $(compgen -W "--from-email --from-name --subject --body --target" -- ${cur}) )
            return 0
            ;;
    esac
}

complete -F _est_completion est
EOF
        
        if sudo mv "/tmp/est_completion" "$COMPLETION_FILE" 2>/dev/null; then
            print_status "Bash completion installed"
        else
            print_warning "Could not install bash completion (permissions)"
        fi
    else
        print_warning "Bash completion directory not found, skipping"
    fi
}

# Verify installation
verify_installation() {
    print_step "Verifying installation..."
    
    # Check if command is available
    if command -v est &> /dev/null; then
        print_status "EST command available system-wide"
    else
        print_error "EST command not found in PATH"
        return 1
    fi
    
    # Check if help works
    if est --help &> /dev/null; then
        print_status "EST help command functional"
    else
        print_error "EST help command failed"
        return 1
    fi
    
    # Check configuration directory
    if [ -d "$HOME/.est" ]; then
        print_status "User configuration directory exists"
    else
        print_error "User configuration directory missing"
        return 1
    fi
    
    # Check virtual environment if used
    if [ "$USE_VENV" = true ]; then
        if [ -d "$VENV_DIR" ]; then
            print_status "Virtual environment exists at $VENV_DIR"
        else
            print_error "Virtual environment missing"
            return 1
        fi
    fi
    
    # Test basic functionality
    if est list &> /dev/null; then
        print_status "EST basic functionality working"
    else
        print_warning "EST basic test failed (may work anyway)"
    fi
    
    print_status "Installation verification completed successfully"
}

# Display post-installation information
show_post_install_info() {
    echo
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                   INSTALLATION COMPLETE!                     ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo
    echo -e "${CYAN}🚀 EST v${TOOL_VERSION} successfully installed!${NC}"
    echo
    echo -e "${BLUE}📍 Installation Details:${NC}"
    echo -e "   📂 Installation Directory: ${INSTALL_DIR}"
    echo -e "   🔗 System Command: ${BIN_LINK}"
    echo -e "   ⚙️  User Config: ~/.est/"
    echo -e "   📚 Documentation: ${INSTALL_DIR}/docs/"
    if [ "$USE_VENV" = true ]; then
        echo -e "   🐍 Python Environment: Virtual environment at $VENV_DIR"
    else
        echo -e "   🐍 Python Environment: System Python"
    fi
    echo
    echo -e "${BLUE}🎯 Quick Start Commands:${NC}"
    echo -e "${YELLOW}   est server --port 2525${NC}        # Start SMTP server"
    echo -e "${YELLOW}   est list${NC}                     # List attack scenarios"
    echo -e "${YELLOW}   est test 1 target@email.com${NC}  # Run CEO fraud test"
    echo -e "${YELLOW}   est logs${NC}                     # View test logs"
    echo -e "${YELLOW}   est --help${NC}                   # Show all options"
    echo
    echo -e "${BLUE}📖 Getting Started:${NC}"
    echo -e "   1. Start EST server: ${YELLOW}est server --port 2525${NC}"
    echo -e "   2. Get temp email from: ${YELLOW}https://guerrillamail.com${NC}"
    echo -e "   3. Run first test: ${YELLOW}est test 1 your-temp-email@guerrillamail.com${NC}"
    echo -e "   4. Check results: ${YELLOW}est logs${NC}"
    echo
    echo -e "${BLUE}📚 Documentation:${NC}"
    echo -e "   • Quick Start: ${INSTALL_DIR}/docs/QUICKSTART.md"
    echo -e "   • Troubleshooting: ${INSTALL_DIR}/docs/TROUBLESHOOTING.md"
    echo -e "   • Full README: ${INSTALL_DIR}/docs/README.md"
    echo
    if [ "$USE_VENV" = true ]; then
        echo -e "${BLUE}🐍 Python Environment:${NC}"
        echo -e "   • Virtual environment: ${VENV_DIR}"
        echo -e "   • Isolated from system Python"
        echo -e "   • Compatible with Python 3.13+"
        echo
    fi
    echo -e "${RED}⚠️  IMPORTANT LEGAL REMINDER:${NC}"
    echo -e "${RED}   EST is for authorized security testing and education only!${NC}"
    echo -e "${RED}   Always obtain explicit written permission before testing.${NC}"
    echo
    echo -e "${PURPLE}💡 Need help? Run: ${YELLOW}est --help${NC} ${PURPLE}or check the documentation${NC}"
    echo
}

# Cleanup function
cleanup() {
    print_info "Cleaning up temporary files..."
    rm -f /tmp/est_*
    
    # Deactivate virtual environment if active
    if [ "$VIRTUAL_ENV" != "" ]; then
        deactivate 2>/dev/null || true
    fi
}

# Signal handlers
trap cleanup EXIT

# Main installation process
main() {
    print_banner
    
    echo -e "${YELLOW}⚠️  This will install EST (Email Spoofing Tool) system-wide${NC}"
    echo -e "${YELLOW}   Installation directory: ${INSTALL_DIR}${NC}"
    echo -e "${YELLOW}   System command: ${BIN_LINK}${NC}"
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        if [[ "$PYTHON_VERSION" > "3.12" ]]; then
            echo -e "${YELLOW}   Python $PYTHON_VERSION detected - will use virtual environment${NC}"
        fi
    fi
    echo
    read -p "Continue with installation? (y/N): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "Installation cancelled by user"
        exit 0
    fi
    
    echo
    print_info "Starting EST installation process..."
    echo
    
    # Run installation steps
    check_root
    check_system
    echo
    
    install_dependencies
    echo
    
    setup_python_environment
    echo
    
    setup_directories
    echo
    
    install_tool
    echo
    
    create_desktop_entry
    echo
    
    create_documentation
    echo
    
    install_bash_completion
    echo
    
    if verify_installation; then
        echo
        show_post_install_info
    else
        print_error "Installation verification failed"
        echo "Please check the error messages above and retry installation"
        exit 1
    fi
}

# Check if required files exist
if [ ! -f "est.py" ]; then
    print_error "Required file 'est.py' not found in current directory"
    echo
    echo "Please ensure you have the following EST files:"
    echo "  • est.py (main application)"
    echo "  • install.sh (this installer)"
    echo "  • README.md (documentation)"
    echo "  • requirements.txt (dependencies)"
    echo
    echo "Download from: https://github.com/techsky-eh/EST"
    exit 1
fi

# Execute main installation
main "$@"