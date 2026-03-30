#!/usr/bin/env python3
"""
SpoofLab: Advanced Email Spoofing Detection and Simulation Framework


Author: Security Research Team
Version: 1.0.0
License: MIT
Repository: https://github.com/your-org/EST

LEGAL NOTICE:
This tool is designed for authorized security testing, penetration testing,
and educational purposes only. Users must obtain explicit written permission
before testing any systems they do not own. Unauthorized use of this tool
may violate local, state, and federal laws.

The developers assume no liability and are not responsible for any misuse
or damage caused by this program.
"""

import sys
import os
import json
import argparse
import socket
import threading
import smtplib
import time
import subprocess
import signal
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging
from dataclasses import dataclass
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formatdate
import email.utils

# Version and metadata
__version__ = "1.0.0"
__author__ = "akshat & khushi "
__license__ = "MIT"
__description__ = "Professional Email Security Assessment Framework"

@dataclass
class EmailScenario:
    """Data class for email spoofing scenarios"""
    name: str
    category: str
    from_email: str
    from_name: str
    subject: str
    body: str
    description: str
    severity: str

@dataclass
class TestResult:
    """Data class for test results"""
    timestamp: str
    test_type: str
    scenario: str
    target: str
    from_email: str
    success: bool
    details: Dict

class ESTConfig:
    """Configuration manager for EST"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".est"
        self.config_file = self.config_dir / "config.json"
        self.log_file = self.config_dir / "est_tests.log"
        self.reports_dir = self.config_dir / "reports"
        
        # Create directories
        self.config_dir.mkdir(exist_ok=True)
        self.reports_dir.mkdir(exist_ok=True)
        
        # Load configuration
        self.config = self._load_config()
        
        # Setup logging
        self._setup_logging()
    
    def _load_config(self) -> Dict:
        """Load configuration from file"""
        default_config = {
            "version": __version__,
            "smtp_server": {
                "host": "0.0.0.0",
                "port": 2525,
                "timeout": 30
            },
            "scenarios": [
                {
                    "name": "CEO Fraud - Urgent Wire Transfer",
                    "category": "Business Email Compromise",
                    "from_email": "ceo@targetcompany.com",
                    "from_name": "John Smith, CEO",
                    "subject": "URGENT: Wire Transfer Authorization Required",
                    "body": "I need you to process an urgent wire transfer for $85,000 to our new vendor immediately. This is time-sensitive and confidential. Please handle this discreetly and confirm once completed.\n\nAmount: $85,000\nAccount details will be provided separately.\n\nRegards,\nJohn Smith\nChief Executive Officer",
                    "description": "CEO impersonation requesting urgent financial transaction",
                    "severity": "Critical"
                },
                {
                    "name": "IT Helpdesk - Password Reset",
                    "category": "Technical Support Fraud",
                    "from_email": "helpdesk@targetcompany.com",
                    "from_name": "IT Support Team",
                    "subject": "Action Required: Password Reset Verification",
                    "body": "Dear User,\n\nWe have detected suspicious activity on your account. For security purposes, you must verify your current password within 24 hours to prevent account suspension.\n\nClick here to verify: [VERIFICATION LINK]\n\nFailure to verify will result in immediate account lockout.\n\nIT Support Team\nDo not reply to this email.",
                    "description": "IT support impersonation for credential harvesting",
                    "severity": "High"
                },
                {
                    "name": "PayPal Security Alert",
                    "category": "Financial Services Phishing",
                    "from_email": "security@paypal.com",
                    "from_name": "PayPal Security Team",
                    "subject": "Security Alert: Unusual Account Activity Detected",
                    "body": "We've detected unusual activity on your PayPal account:\n\n• Login from new device (IP: 192.168.1.100)\n• Attempted transaction: $1,247.99\n• Location: Unknown\n\nYour account has been temporarily limited for your protection.\n\nVerify your account immediately: [SECURE LINK]\n\nIf you don't recognize this activity, please contact us immediately.\n\nPayPal Security Team\nThis is an automated message.",
                    "description": "PayPal impersonation for account compromise",
                    "severity": "High"
                },
                {
                    "name": "Microsoft 365 License Expiration",
                    "category": "Software/License Fraud",
                    "from_email": "noreply@microsoft.com",
                    "from_name": "Microsoft 365 Admin",
                    "subject": "ACTION REQUIRED: Your Microsoft 365 License Expires Today",
                    "body": "Your Microsoft 365 Business license expires today at 11:59 PM.\n\nImmediate action required to prevent:\n✗ Loss of email access\n✗ File synchronization stoppage\n✗ Team collaboration disruption\n\nRenew immediately to maintain access:\n[RENEWAL LINK]\n\nYour license key: M365-BIZ-2024-XXXX\n\nMicrosoft 365 Administration\nThis is an automated renewal notice.",
                    "description": "Microsoft service impersonation for credential theft",
                    "severity": "Medium"
                },
                {
                    "name": "Bank Account Verification",
                    "category": "Financial Institution Fraud",
                    "from_email": "security@bankofamerica.com",
                    "from_name": "Bank of America Security",
                    "subject": "Immediate Verification Required - Account Suspension Notice",
                    "body": "IMPORTANT SECURITY NOTICE\n\nWe have temporarily suspended your account due to suspicious activity:\n\n• Multiple failed login attempts\n• Unrecognized device access\n• Potential unauthorized transactions\n\nAccount Status: SUSPENDED\nSuspension Date: [TODAY]\nReference: SEC-2024-[RANDOM]\n\nVerify your identity immediately to restore access:\n[VERIFICATION PORTAL]\n\nFailure to verify within 48 hours will result in permanent closure.\n\nBank of America Security Department",
                    "description": "Banking institution impersonation for credential harvesting",
                    "severity": "Critical"
                }
            ],
            "temp_email_services": [
                "guerrillamail.com",
                "sharklasers.com", 
                "mailinator.com",
                "10minutemail.com",
                "tempmail.org",
                "yopmail.com"
            ],
            "reporting": {
                "auto_generate": True,
                "format": "json",
                "include_screenshots": False
            }
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                # Merge with defaults to ensure all keys exist
                for key in default_config:
                    if key not in loaded_config:
                        loaded_config[key] = default_config[key]
                return loaded_config
            except Exception as e:
                print(f"⚠️  Error loading config: {e}")
                return default_config
        else:
            self._save_config(default_config)
            return default_config
    
    def _save_config(self, config: Dict):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"⚠️  Error saving config: {e}")
    
    def _setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('EST')

class SMTPTestServer:
    """Professional SMTP server for security testing"""
    
    def __init__(self, host: str, port: int, config: ESTConfig):
        self.host = host
        self.port = port
        self.config = config
        self.running = False
        self.connections = 0
        self.emails_processed = 0
        
    def start(self):
        """Start the SMTP testing server"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            self.sock.listen(10)
            self.running = True
            
            print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    EST SMTP SERVER v{__version__}                    ║
║              Email Spoofing Tool - Server Mode               ║
╚══════════════════════════════════════════════════════════════╝

🚀 Server Status: ACTIVE
📡 Listening on: {self.host}:{self.port}
📁 Log file: {self.config.log_file}
📊 Statistics: {self.connections} connections, {self.emails_processed} emails processed

⚡ Server Features:
   • Multi-threaded connection handling
   • Automatic MX record resolution
   • Real-time email relay to destinations
   • Comprehensive audit logging
   • Professional SMTP protocol compliance

🎯 Quick Test Commands:
   telnet {self.host} {self.port}
   est test 1 target@example.com
   
🛑 Press Ctrl+C to stop server
            """)
            
            # Handle Ctrl+C gracefully
            signal.signal(signal.SIGINT, self._signal_handler)
            
            while self.running:
                try:
                    client_sock, addr = self.sock.accept()
                    self.connections += 1
                    thread = threading.Thread(
                        target=self._handle_client, 
                        args=(client_sock, addr),
                        name=f"SMTP-Client-{self.connections}"
                    )
                    thread.daemon = True
                    thread.start()
                except Exception as e:
                    if self.running:
                        self.config.logger.error(f"Accept error: {e}")
                        
        except Exception as e:
            print(f"❌ Server startup failed: {e}")
            if self.port <= 1024:
                print("💡 Try using a higher port number (e.g., --port 2525)")
        finally:
            if hasattr(self, 'sock'):
                self.sock.close()
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        print(f"\n\n🛑 Shutting down EST SMTP Server...")
        print(f"📊 Final Statistics:")
        print(f"   • Connections handled: {self.connections}")
        print(f"   • Emails processed: {self.emails_processed}")
        print(f"   • Log file: {self.config.log_file}")
        self.running = False
        sys.exit(0)
    
    def _handle_client(self, client_sock, addr):
        """Handle individual SMTP client connections"""
        client_id = f"{addr[0]}:{addr[1]}"
        
        try:
            self.config.logger.info(f"New SMTP connection from {client_id}")
            
            # SMTP session state
            mail_from = ""
            rcpt_to = []
            
            # Send greeting
            client_sock.send(f"220 EST-SMTP-{__version__} Security Testing Server Ready\r\n".encode())
            
            while self.running:
                try:
                    data = client_sock.recv(4096).decode('utf-8', errors='ignore').strip()
                    if not data:
                        break
                    
                    # Log command
                    self.config.logger.debug(f"[{client_id}] Command: {data}")
                    
                    cmd = data.upper()
                    
                    if cmd.startswith("EHLO") or cmd.startswith("HELO"):
                        response = f"250-EST-SMTP Hello {addr[0]}\r\n250 HELP\r\n"
                        client_sock.send(response.encode())
                        
                    elif cmd.startswith("MAIL FROM:"):
                        mail_from = self._extract_email(data)
                        self.config.logger.info(f"[{client_id}] Spoofed sender: {mail_from}")
                        client_sock.send(b"250 OK\r\n")
                        
                    elif cmd.startswith("RCPT TO:"):
                        rcpt = self._extract_email(data)
                        rcpt_to.append(rcpt)
                        self.config.logger.info(f"[{client_id}] Target: {rcpt}")
                        client_sock.send(b"250 OK\r\n")
                        
                    elif cmd == "DATA":
                        client_sock.send(b"354 End data with <CR><LF>.<CR><LF>\r\n")
                        
                        # Receive email data
                        email_data = ""
                        while True:
                            line = client_sock.recv(4096).decode('utf-8', errors='ignore')
                            email_data += line
                            if line.endswith('\r\n.\r\n'):
                                break
                        
                        # Process email
                        success = self._process_email(mail_from, rcpt_to, email_data[:-5], client_id)
                        self.emails_processed += 1
                        
                        if success:
                            client_sock.send(b"250 OK Message queued for delivery\r\n")
                        else:
                            client_sock.send(b"550 Message delivery failed\r\n")
                        
                        # Reset session
                        mail_from = ""
                        rcpt_to = []
                        
                    elif cmd == "QUIT":
                        client_sock.send(b"221 EST-SMTP closing connection\r\n")
                        break
                        
                    elif cmd.startswith("RSET"):
                        mail_from = ""
                        rcpt_to = []
                        client_sock.send(b"250 OK\r\n")
                        
                    else:
                        client_sock.send(b"500 Command not recognized\r\n")
                        
                except socket.timeout:
                    break
                except Exception as e:
                    self.config.logger.error(f"[{client_id}] Command processing error: {e}")
                    break
                    
        except Exception as e:
            self.config.logger.error(f"[{client_id}] Connection error: {e}")
        finally:
            client_sock.close()
            self.config.logger.info(f"[{client_id}] Connection closed")
    
    def _extract_email(self, smtp_line: str) -> str:
        """Extract email address from SMTP command"""
        match = re.search(r'<(.+?)>', smtp_line)
        if match:
            return match.group(1)
        parts = smtp_line.split()
        return parts[-1].strip('<>') if len(parts) > 1 else ""
    
    def _process_email(self, mail_from: str, rcpt_to: List[str], email_data: str, client_id: str) -> bool:
        """Process and relay spoofed email"""
        self.config.logger.info(f"[{client_id}] Processing spoofed email from {mail_from} to {rcpt_to}")
        
        success_count = 0
        for rcpt in rcpt_to:
            if self._relay_email(mail_from, rcpt, email_data):
                success_count += 1
        
        # Log test result
        result = TestResult(
            timestamp=datetime.now().isoformat(),
            test_type="smtp_relay",
            scenario="server_relay",
            target=", ".join(rcpt_to),
            from_email=mail_from,
            success=success_count > 0,
            details={
                "client_id": client_id,
                "total_targets": len(rcpt_to),
                "successful_deliveries": success_count,
                "email_size": len(email_data)
            }
        )
        
        self._log_test_result(result)
        
        return success_count > 0
    
    def _relay_email(self, mail_from: str, rcpt_to: str, email_data: str) -> bool:
        """Relay email to destination"""
        try:
            domain = rcpt_to.split('@')[1]
            mx_servers = self._get_mx_servers(domain)
            
            self.config.logger.info(f"Attempting relay to {rcpt_to} via {len(mx_servers)} MX servers")
            
            for mx_server in mx_servers:
                try:
                    server = smtplib.SMTP(mx_server, 25, timeout=15)
                    server.set_debuglevel(0)
                    
                    # Ensure proper encoding
                    full_email = f"From: {mail_from}\r\nTo: {rcpt_to}\r\n{email_data}"
                    full_email_bytes = full_email.encode('utf-8')
                    server.sendmail(mail_from, [rcpt_to], full_email_bytes)
                    server.quit()
                    
                    self.config.logger.info(f"✅ Email delivered to {rcpt_to} via {mx_server}")
                    return True
                    
                except Exception as e:
                    self.config.logger.warning(f"❌ Relay failed via {mx_server}: {str(e)[:60]}...")
                    continue
            
            self.config.logger.error(f"❌ All relay attempts failed for {rcpt_to}")
            return False
            
        except Exception as e:
            self.config.logger.error(f"❌ Relay error for {rcpt_to}: {e}")
            return False
    
    def _get_mx_servers(self, domain: str) -> List[str]:
        """Get MX servers for domain"""
        try:
            import dns.resolver
            mx_records = dns.resolver.resolve(domain, 'MX')
            servers = [str(mx.exchange).rstrip('.') for mx in sorted(mx_records, key=lambda x: x.preference)]
            self.config.logger.debug(f"Found MX servers for {domain}: {servers}")
            return servers
        except ImportError:
            self.config.logger.warning("DNS library not available, using fallbacks")
        except Exception as e:
            self.config.logger.warning(f"DNS lookup failed for {domain}: {e}")
        
        # Fallback servers
        fallbacks = [f"mail.{domain}", f"mx.{domain}", f"mx1.{domain}"]
        working_fallbacks = []
        
        for mx in fallbacks:
            try:
                socket.gethostbyname(mx)
                working_fallbacks.append(mx)
            except:
                continue
        
        return working_fallbacks
    
    def _log_test_result(self, result: TestResult):
        """Log test result to file"""
        try:
            log_entry = {
                "timestamp": result.timestamp,
                "test_type": result.test_type,
                "scenario": result.scenario,
                "target": result.target,
                "from_email": result.from_email,
                "success": result.success,
                "details": result.details
            }
            
            with open(self.config.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
        except Exception as e:
            self.config.logger.error(f"Failed to log test result: {e}")

class EST:
    """Main EST application class"""
    
    def __init__(self):
        self.config = ESTConfig()
        self.scenarios = [EmailScenario(**s) for s in self.config.config['scenarios']]
    
    def print_banner(self):
        """Print professional banner"""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    EST - Email Spoofing Tool                 ║
║              Professional Security Assessment v{__version__}         ║
║                                                              ║
║    Advanced Email Security Testing Framework                 ║
║    For Authorized Penetration Testing Only                   ║
║    Educational & Research Purposes                           ║
║                                                              ║
║  Author: {__author__}                                      ║
║  License: {__license__}                                                ║
╚══════════════════════════════════════════════════════════════╝

⚠️  LEGAL NOTICE: This tool is for authorized security testing only.
   Obtain explicit written permission before testing any systems.
   Unauthorized use may violate applicable laws and regulations.
        """
        print(banner)
    
    def list_scenarios(self):
        """List all available test scenarios"""
        print("\n📋 Available Email Spoofing Scenarios:\n")
        
        categories = {}
        for i, scenario in enumerate(self.scenarios, 1):
            if scenario.category not in categories:
                categories[scenario.category] = []
            categories[scenario.category].append((i, scenario))
        
        for category, scenarios in categories.items():
            print(f"🏷️  {category}")
            print("─" * (len(category) + 5))
            
            for idx, scenario in scenarios:
                severity_icon = {
                    "Critical": "🔴",
                    "High": "🟠", 
                    "Medium": "🟡",
                    "Low": "🟢"
                }.get(scenario.severity, "⚪")
                
                print(f"   {idx:2d}. {scenario.name} {severity_icon}")
                print(f"       From: {scenario.from_name} <{scenario.from_email}>")
                print(f"       Subject: {scenario.subject}")
                print(f"       Description: {scenario.description}")
                print()
        
        print(f"📊 Total scenarios: {len(self.scenarios)}")
        print(f"🎯 Use 'est test <id> <target>' to run a scenario")
    
    def run_scenario(self, scenario_id: int, target: str, smtp_host: str = "localhost", smtp_port: int = 2525) -> bool:
        """Run a specific spoofing scenario"""
        try:
            scenario = self.scenarios[scenario_id - 1]
        except IndexError:
            print(f"❌ Invalid scenario ID: {scenario_id}")
            print(f"💡 Available scenarios: 1-{len(self.scenarios)}")
            return False
        
        print(f"\n🎯 Executing Email Spoofing Test")
        print(f"─" * 40)
        print(f"📧 Scenario: {scenario.name}")
        print(f"🏷️  Category: {scenario.category}")
        print(f"⚠️  Severity: {scenario.severity}")
        print(f"📤 Spoofed From: {scenario.from_name} <{scenario.from_email}>")
        print(f"📥 Target: {target}")
        print(f"📡 SMTP Server: {smtp_host}:{smtp_port}")
        print(f"🕐 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        try:
            # Create professional email content using MIME
            email_content = self._create_mime_email(scenario, target)
            
            # Send via SMTP
            print("🚀 Initiating SMTP connection...")
            server = smtplib.SMTP(smtp_host, smtp_port, timeout=30)
            
            print("📤 Sending spoofed email...")
            server.sendmail(scenario.from_email, [target], email_content)
            server.quit()
            
            print("✅ Email spoofing test completed successfully!")
            print(f"📋 Check target inbox: {target}")
            
            # Log the test
            result = TestResult(
                timestamp=datetime.now().isoformat(),
                test_type="scenario_test",
                scenario=scenario.name,
                target=target,
                from_email=scenario.from_email,
                success=True,
                details={
                    "category": scenario.category,
                    "severity": scenario.severity,
                    "smtp_server": f"{smtp_host}:{smtp_port}"
                }
            )
            
            self._log_test_result(result)
            return True
            
        except Exception as e:
            print(f"❌ Email spoofing test failed: {e}")
            print(f"💡 Verify SMTP server is running: est server --port {smtp_port}")
            
            # Log failed test
            result = TestResult(
                timestamp=datetime.now().isoformat(),
                test_type="scenario_test",
                scenario=scenario.name,
                target=target,
                from_email=scenario.from_email,
                success=False,
                details={
                    "error": str(e),
                    "smtp_server": f"{smtp_host}:{smtp_port}"
                }
            )
            
            self._log_test_result(result)
            return False
    
    def run_custom_test(self, from_email: str, from_name: str, subject: str, 
                       body: str, target: str, smtp_host: str = "localhost", 
                       smtp_port: int = 2525) -> bool:
        """Run custom spoofing test"""
        print(f"\n🎯 Executing Custom Email Spoofing Test")
        print(f"─" * 45)
        print(f"📤 Spoofed From: {from_name} <{from_email}>")
        print(f"📥 Target: {target}")
        print(f"📋 Subject: {subject}")
        print(f"📡 SMTP Server: {smtp_host}:{smtp_port}")
        print(f"🕐 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        try:
            # Create MIME email with proper encoding
            email_content = self._create_custom_mime_email(from_email, from_name, subject, body, target)
            
            print("🚀 Initiating SMTP connection...")
            server = smtplib.SMTP(smtp_host, smtp_port, timeout=30)
            
            print("📤 Sending custom spoofed email...")
            server.sendmail(from_email, [target], email_content)
            server.quit()
            
            print("✅ Custom email spoofing test completed successfully!")
            print(f"📋 Check target inbox: {target}")
            
            # Log the test
            result = TestResult(
                timestamp=datetime.now().isoformat(),
                test_type="custom_test",
                scenario="custom",
                target=target,
                from_email=from_email,
                success=True,
                details={
                    "from_name": from_name,
                    "subject": subject,
                    "body_length": len(body),
                    "smtp_server": f"{smtp_host}:{smtp_port}"
                }
            )
            
            self._log_test_result(result)
            return True
            
        except Exception as e:
            print(f"❌ Custom email spoofing test failed: {e}")
            
            # Log failed test
            result = TestResult(
                timestamp=datetime.now().isoformat(),
                test_type="custom_test",
                scenario="custom",
                target=target,
                from_email=from_email,
                success=False,
                details={
                    "error": str(e),
                    "smtp_server": f"{smtp_host}:{smtp_port}"
                }
            )
            
            self._log_test_result(result)
            return False
    
    def show_logs(self, lines: int = 20):
        """Display recent test logs"""
        if not self.config.log_file.exists():
            print("📝 No test logs found")
            print(f"💡 Run some tests first, then check: {self.config.log_file}")
            return
        
        print(f"\n📊 EST Security Test Logs (Last {lines} entries)")
        print("═" * 80)
        
        try:
            with open(self.config.log_file, 'r') as f:
                log_lines = f.readlines()
            
            recent_logs = log_lines[-lines:] if len(log_lines) > lines else log_lines
            
            for line in recent_logs:
                try:
                    entry = json.loads(line.strip())
                    timestamp = entry['timestamp'][:19].replace('T', ' ')
                    
                    status = "✅ SUCCESS" if entry['success'] else "❌ FAILED"
                    test_type = entry['test_type'].replace('_', ' ').title()
                    
                    print(f"📅 {timestamp} | {status}")
                    print(f"🎯 Test: {test_type} - {entry['scenario']}")
                    print(f"📤 From: {entry['from_email']}")
                    print(f"📥 Target: {entry['target']}")
                    
                    if 'details' in entry and entry['details']:
                        details = entry['details']
                        if 'category' in details:
                            print(f"🏷️  Category: {details['category']}")
                        if 'severity' in details:
                            print(f"⚠️  Severity: {details['severity']}")
                        if 'error' in details:
                            print(f"❌ Error: {details['error']}")
                    
                    print("─" * 80)
                    
                except json.JSONDecodeError:
                    continue
            
            print(f"📈 Total log entries: {len(log_lines)}")
            print(f"📁 Full log file: {self.config.log_file}")
            
        except Exception as e:
            print(f"❌ Error reading logs: {e}")
    
    def generate_report(self, output_file: Optional[str] = None):
        """Generate comprehensive test report"""
        if not self.config.log_file.exists():
            print("❌ No test data available for report generation")
            return
        
        print("📊 Generating EST Security Assessment Report...")
        
        try:
            # Read all log entries
            with open(self.config.log_file, 'r') as f:
                log_entries = [json.loads(line.strip()) for line in f if line.strip()]
            
            if not log_entries:
                print("❌ No test data found in logs")
                return
            
            # Generate report
            report = self._create_report(log_entries)
            
            # Save report
            if not output_file:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = self.config.reports_dir / f"est_report_{timestamp}.json"
            
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"✅ Report generated: {output_file}")
            self._print_report_summary(report)
            
        except Exception as e:
            print(f"❌ Report generation failed: {e}")
    
    def _create_report(self, log_entries: List[Dict]) -> Dict:
        """Create comprehensive assessment report"""
        total_tests = len(log_entries)
        successful_tests = sum(1 for entry in log_entries if entry['success'])
        failed_tests = total_tests - successful_tests
        
        # Analyze by test type
        test_types = {}
        for entry in log_entries:
            test_type = entry['test_type']
            if test_type not in test_types:
                test_types[test_type] = {'total': 0, 'success': 0}
            test_types[test_type]['total'] += 1
            if entry['success']:
                test_types[test_type]['success'] += 1
        
        # Analyze by scenario
        scenarios = {}
        for entry in log_entries:
            scenario = entry['scenario']
            if scenario not in scenarios:
                scenarios[scenario] = {'total': 0, 'success': 0}
            scenarios[scenario]['total'] += 1
            if entry['success']:
                scenarios[scenario]['success'] += 1
        
        # Time analysis
        timestamps = [entry['timestamp'] for entry in log_entries]
        first_test = min(timestamps) if timestamps else None
        last_test = max(timestamps) if timestamps else None
        
        return {
            "report_metadata": {
                "generated_at": datetime.now().isoformat(),
                "tool_version": __version__,
                "report_type": "EST Security Assessment",
                "total_tests": total_tests
            },
            "executive_summary": {
                "total_tests_conducted": total_tests,
                "successful_tests": successful_tests,
                "failed_tests": failed_tests,
                "success_rate": round((successful_tests / total_tests * 100), 2) if total_tests > 0 else 0,
                "test_period": {
                    "first_test": first_test,
                    "last_test": last_test
                }
            },
            "test_analysis": {
                "by_test_type": test_types,
                "by_scenario": scenarios
            },
            "detailed_logs": log_entries,
            "recommendations": self._generate_recommendations(log_entries)
        }
    
    def _generate_recommendations(self, log_entries: List[Dict]) -> List[str]:
        """Generate security recommendations based on test results"""
        recommendations = []
        
        successful_tests = sum(1 for entry in log_entries if entry['success'])
        total_tests = len(log_entries)
        success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
        
        if success_rate > 80:
            recommendations.extend([
                "🔴 CRITICAL: High email spoofing success rate detected",
                "Implement SPF, DKIM, and DMARC email authentication",
                "Configure email security gateways with spoofing detection",
                "Conduct immediate security awareness training"
            ])
        elif success_rate > 50:
            recommendations.extend([
                "🟠 HIGH: Moderate spoofing vulnerabilities identified",
                "Review and strengthen email authentication policies",
                "Implement additional email security controls",
                "Regular security awareness training recommended"
            ])
        else:
            recommendations.extend([
                "🟡 MEDIUM: Some spoofing attempts successful",
                "Continue monitoring email security controls",
                "Periodic security awareness refresher training",
                "Regular testing of email authentication mechanisms"
            ])
        
        recommendations.extend([
            "📚 Provide targeted training on identifying spoofed emails",
            "🔍 Implement email header analysis training",
            "⚡ Establish incident response procedures for email attacks",
            "📊 Regular penetration testing of email security controls"
        ])
        
        return recommendations
    
    def _print_report_summary(self, report: Dict):
        """Print report summary to console"""
        summary = report['executive_summary']
        
        print(f"\n📋 EST Security Assessment Summary")
        print("═" * 50)
        print(f"📊 Total Tests: {summary['total_tests_conducted']}")
        print(f"✅ Successful: {summary['successful_tests']}")
        print(f"❌ Failed: {summary['failed_tests']}")
        print(f"📈 Success Rate: {summary['success_rate']}%")
        
        if summary['success_rate'] > 80:
            print("🔴 Risk Level: CRITICAL - Immediate action required")
        elif summary['success_rate'] > 50:
            print("🟠 Risk Level: HIGH - Remediation recommended")
        else:
            print("🟡 Risk Level: MEDIUM - Monitoring advised")
        
        print(f"\n📚 Recommendations: {len(report['recommendations'])} items")
        for rec in report['recommendations'][:3]:
            print(f"   • {rec}")
        if len(report['recommendations']) > 3:
            print(f"   ... and {len(report['recommendations']) - 3} more")
    
    def _create_mime_email(self, scenario: EmailScenario, target: str) -> str:
        """Create professional MIME email content with proper encoding"""
        try:
            # Create MIME message
            msg = MIMEMultipart('alternative')
            
            # Set headers with proper encoding
            msg['From'] = f"{scenario.from_name} <{scenario.from_email}>"
            msg['To'] = target
            msg['Subject'] = Header(scenario.subject, 'utf-8')
            msg['Date'] = formatdate(localtime=True)
            msg['Message-ID'] = email.utils.make_msgid(domain=scenario.from_email.split('@')[1])
            
            # Create email body with disclaimer
            email_body = f"""{scenario.body}

────────────────────────────────────────────────────────────────
This email was sent using EST (Email Spoofing Tool) for authorized
security testing purposes. If you received this email unexpectedly,
please contact your IT security team immediately.

Test Details:
• Scenario: {scenario.name}
• Category: {scenario.category}
• Severity: {scenario.severity}
• Timestamp: {datetime.now().isoformat()}

EST v{__version__} - Professional Email Security Assessment Framework
────────────────────────────────────────────────────────────────"""
            
            # Create text part with proper encoding
            text_part = MIMEText(email_body, 'plain', 'utf-8')
            msg.attach(text_part)
            
            return msg.as_string()
            
        except Exception as e:
            self.config.logger.error(f"MIME email creation failed: {e}")
            # Fallback to simple string method
            return self._create_simple_email(scenario, target)
    
    def _create_custom_mime_email(self, from_email: str, from_name: str, subject: str, body: str, target: str) -> str:
        """Create custom MIME email with proper encoding"""
        try:
            # Create MIME message
            msg = MIMEMultipart('alternative')
            
            # Set headers with proper encoding
            msg['From'] = f"{from_name} <{from_email}>"
            msg['To'] = target
            msg['Subject'] = Header(subject, 'utf-8')
            msg['Date'] = formatdate(localtime=True)
            msg['Message-ID'] = email.utils.make_msgid(domain=from_email.split('@')[1])
            
            # Create email body with disclaimer
            email_body = f"""{body}

────────────────────────────────────────────────────────────────
This email was sent using EST (Email Spoofing Tool) for authorized
security testing purposes. If you received this email unexpectedly,
please contact your IT security team immediately.

EST v{__version__} - Professional Email Security Assessment Framework
────────────────────────────────────────────────────────────────"""
            
            # Create text part with proper encoding
            text_part = MIMEText(email_body, 'plain', 'utf-8')
            msg.attach(text_part)
            
            return msg.as_string()
            
        except Exception as e:
            self.config.logger.error(f"Custom MIME email creation failed: {e}")
            # Fallback to simple string method
            return self._create_simple_custom_email(from_email, from_name, subject, body, target)
    
    def _create_simple_email(self, scenario: EmailScenario, target: str) -> str:
        """Fallback method to create simple email content"""
        return f"""From: {scenario.from_name} <{scenario.from_email}>
To: {target}
Subject: {scenario.subject}
Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')}
Message-ID: <{int(time.time())}.{hash(target) % 10000}@{scenario.from_email.split('@')[1]}>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

{scenario.body}

────────────────────────────────────────────────────────────────
This email was sent using EST (Email Spoofing Tool) for authorized
security testing purposes. If you received this email unexpectedly,
please contact your IT security team immediately.

Test Details:
• Scenario: {scenario.name}
• Category: {scenario.category}
• Severity: {scenario.severity}
• Timestamp: {datetime.now().isoformat()}

EST v{__version__} - Professional Email Security Assessment Framework
────────────────────────────────────────────────────────────────
"""
    
    def _create_simple_custom_email(self, from_email: str, from_name: str, subject: str, body: str, target: str) -> str:
        """Fallback method to create simple custom email content"""
        return f"""From: {from_name} <{from_email}>
To: {target}
Subject: {subject}
Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')}
Message-ID: <{int(time.time())}.{hash(target) % 10000}@{from_email.split('@')[1]}>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

{body}

────────────────────────────────────────────────────────────────
This email was sent using EST (Email Spoofing Tool) for authorized
security testing purposes. If you received this email unexpectedly,
please contact your IT security team immediately.

EST v{__version__} - Professional Email Security Assessment Framework
────────────────────────────────────────────────────────────────
"""
    
    def _log_test_result(self, result: TestResult):
        """Log test result"""
        try:
            log_entry = {
                "timestamp": result.timestamp,
                "test_type": result.test_type,
                "scenario": result.scenario,
                "target": result.target,
                "from_email": result.from_email,
                "success": result.success,
                "details": result.details
            }
            
            with open(self.config.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
            self.config.logger.info(f"Test logged: {result.test_type} - {result.scenario}")
                
        except Exception as e:
            self.config.logger.error(f"Failed to log test result: {e}")

def main():
    """Main application entry point"""
    parser = argparse.ArgumentParser(
        prog='est',
        description='EST - Professional Email Spoofing Tool for Security Assessment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  est server --port 2525                    Start SMTP testing server
  est list                                  List available spoofing scenarios
  est test 1 target@company.com             Run CEO fraud scenario
  est custom --from-email "ceo@company.com" \\
         --from-name "John Smith" \\
         --subject "Urgent Request" \\
         --body "Please handle this" \\
         --target "user@company.com"        Run custom spoofing test
  est logs --lines 50                       View recent test logs
  est report                                Generate assessment report

EST v{__version__} - Professional Email Security Assessment Framework
Author: {__author__} | License: {__license__}

⚠️  LEGAL NOTICE: For authorized security testing only.
   Obtain explicit written permission before testing any systems.
        """
    )
    
    parser.add_argument('--version', action='version', version=f'EST v{__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Server command
    server_parser = subparsers.add_parser('server', help='Start SMTP testing server')
    server_parser.add_argument('--host', default='0.0.0.0', 
                              help='Host to bind to (default: 0.0.0.0)')
    server_parser.add_argument('--port', type=int, default=2525,
                              help='Port to bind to (default: 2525)')
    
    # List command
    subparsers.add_parser('list', help='List available spoofing scenarios')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Run spoofing scenario')
    test_parser.add_argument('scenario', type=int, 
                            help='Scenario ID (use "list" to see available)')
    test_parser.add_argument('target', help='Target email address')
    test_parser.add_argument('--smtp-host', default='localhost',
                            help='SMTP server hostname (default: localhost)')
    test_parser.add_argument('--smtp-port', type=int, default=2525,
                            help='SMTP server port (default: 2525)')
    
    # Custom test command
    custom_parser = subparsers.add_parser('custom', help='Run custom spoofing test')
    custom_parser.add_argument('--from-email', required=True,
                              help='Spoofed sender email address')
    custom_parser.add_argument('--from-name', required=True,
                              help='Spoofed sender display name')
    custom_parser.add_argument('--subject', required=True,
                              help='Email subject line')
    custom_parser.add_argument('--body', required=True,
                              help='Email body content')
    custom_parser.add_argument('--target', required=True,
                              help='Target email address')
    custom_parser.add_argument('--smtp-host', default='localhost',
                              help='SMTP server hostname (default: localhost)')
    custom_parser.add_argument('--smtp-port', type=int, default=2525,
                              help='SMTP server port (default: 2525)')
    
    # Logs command
    logs_parser = subparsers.add_parser('logs', help='View test logs')
    logs_parser.add_argument('--lines', type=int, default=20,
                            help='Number of recent log entries to display (default: 20)')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate assessment report')
    report_parser.add_argument('--output', help='Output file path (default: auto-generated)')
    
    args = parser.parse_args()
    
    # Initialize EST
    est = EST()
    
    # Handle commands
    if not args.command:
        est.print_banner()
        parser.print_help()
        return
    
    if args.command == 'server':
        # Check port permissions
        if args.port <= 1024 and os.geteuid() != 0:
            print(f"❌ Port {args.port} requires root privileges!")
            print(f"💡 Solutions:")
            print(f"   1. Run as root: sudo est server --port {args.port}")
            print(f"   2. Use unprivileged port: est server --port 2525")
            sys.exit(1)
        
        server = SMTPTestServer(args.host, args.port, est.config)
        try:
            server.start()
        except KeyboardInterrupt:
            pass
    
    elif args.command == 'list':
        est.print_banner()
        est.list_scenarios()
    
    elif args.command == 'test':
        est.print_banner()
        success = est.run_scenario(args.scenario, args.target, args.smtp_host, args.smtp_port)
        sys.exit(0 if success else 1)
    
    elif args.command == 'custom':
        est.print_banner()
        success = est.run_custom_test(
            args.from_email, args.from_name, args.subject, 
            args.body, args.target, args.smtp_host, args.smtp_port
        )
        sys.exit(0 if success else 1)
    
    elif args.command == 'logs':
        est.print_banner()
        est.show_logs(args.lines)
    
    elif args.command == 'report':
        est.print_banner()
        est.generate_report(args.output)

if __name__ == "__main__":
    main()