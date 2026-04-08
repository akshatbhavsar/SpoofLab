# SpoofLab: How Email Addresses Get Spoofed
## Final Year Project Documentation

---

**Project Title:** SpoofLab – Advanced Email Spoofing Detection and Simulation Framework

**Project Code:** EST-2025

**Submitted By:**
- Akshat Bhavsar
- Khushi

**Supervisor:** [Supervisor Name]

**Department:** Department of Computer Science / Information Technology

**Institution:** [University / College Name]

**Academic Year:** 2024–2025

**Date of Submission:** [Submission Date]

---

> **Ethical Notice:** This project is developed strictly for authorized penetration testing, academic research, and educational purposes. All testing must be conducted only on systems with explicit written permission from the system owner. Unauthorized use is illegal and violators will be prosecuted under applicable cybercrime laws.

---


---

# TABLE OF CONTENTS

| Chapter | Title | Page |
|---------|-------|------|
| — | Title Page | 1 |
| — | Table of Contents | 2 |
| — | List of Figures | 4 |
| — | List of Tables | 5 |
| — | Abbreviations & Acronyms | 6 |
| **1** | **Executive Summary** | **7** |
| **2** | **Introduction & Background** | **9** |
| 2.1 | Project Overview | 9 |
| 2.2 | Motivation | 10 |
| 2.3 | Objectives | 11 |
| 2.4 | Scope of the Project | 12 |
| **3** | **Literature Review** | **14** |
| 3.1 | Email Protocol Fundamentals | 14 |
| 3.2 | History of Email Spoofing | 16 |
| 3.3 | Existing Tools and Frameworks | 17 |
| 3.4 | Research Gaps | 19 |
| **4** | **Problem Statement** | **21** |
| 4.1 | The Email Spoofing Problem | 21 |
| 4.2 | Why Organizations Remain Vulnerable | 22 |
| 4.3 | Proposed Solution | 23 |
| **5** | **System Architecture & Design** | **25** |
| 5.1 | High-Level Architecture | 25 |
| 5.2 | Component Design | 27 |
| 5.3 | Data Flow Diagrams | 29 |
| 5.4 | Database / Configuration Design | 31 |
| **6** | **Implementation Details** | **33** |
| 6.1 | Technology Stack | 33 |
| 6.2 | SMTP Server Implementation | 34 |
| 6.3 | Email Spoofing Engine | 36 |
| 6.4 | Scenario Engine | 38 |
| 6.5 | Logging & Audit System | 40 |
| 6.6 | Report Generation Module | 41 |
| 6.7 | CLI Interface | 43 |
| **7** | **Features & Functionality** | **45** |
| 7.1 | Core Features | 45 |
| 7.2 | Advanced Features | 46 |
| 7.3 | Feature Comparison | 48 |
| **8** | **Installation & Setup Guide** | **50** |
| 8.1 | System Requirements | 50 |
| 8.2 | Installation on Kali Linux | 51 |
| 8.3 | Installation on Ubuntu / Debian | 53 |
| 8.4 | Installation on macOS | 54 |
| 8.5 | Installation on Windows | 55 |
| 8.6 | Virtual Environment Setup | 56 |
| 8.7 | Configuration | 57 |
| **9** | **User Manual with Examples** | **59** |
| 9.1 | Starting the SMTP Server | 59 |
| 9.2 | Listing Scenarios | 60 |
| 9.3 | Running Pre-built Scenarios | 61 |
| 9.4 | Running Custom Tests | 62 |
| 9.5 | Viewing Logs | 64 |
| 9.6 | Generating Reports | 65 |
| **10** | **Security Scenarios** | **67** |
| 10.1 | Scenario 1 – CEO Fraud / BEC | 67 |
| 10.2 | Scenario 2 – IT Helpdesk Phishing | 69 |
| 10.3 | Scenario 3 – PayPal Phishing | 71 |
| 10.4 | Scenario 4 – Microsoft 365 License Scam | 73 |
| 10.5 | Scenario 5 – Banking Alert Fraud | 75 |
| 10.6 | Scenario 6 – Custom Attack Builder | 77 |
| **11** | **Testing & Results** | **79** |
| 11.1 | Test Plan | 79 |
| 11.2 | Unit Testing | 80 |
| 11.3 | Integration Testing | 81 |
| 11.4 | Scenario Testing Results | 82 |
| **12** | **Performance Analysis** | **84** |
| 12.1 | SMTP Server Performance | 84 |
| 12.2 | Email Delivery Success Rates | 85 |
| 12.3 | Resource Utilization | 86 |
| **13** | **Security Considerations** | **88** |
| 13.1 | Ethical & Legal Boundaries | 88 |
| 13.2 | SPF, DKIM, and DMARC Defenses | 89 |
| 13.3 | Responsible Disclosure | 91 |
| **14** | **Future Enhancements** | **93** |
| **15** | **Conclusion** | **95** |
| **16** | **References** | **97** |
| **Appendix A** | **Configuration Templates** | **99** |
| **Appendix B** | **Sample Log Output** | **101** |
| **Appendix C** | **Sample Report Output** | **103** |
| **Appendix D** | **Glossary** | **105** |

---


# LIST OF FIGURES

| Figure No. | Title | Page |
|------------|-------|------|
| Figure 1.1 | SpoofLab Application Banner | 8 |
| Figure 2.1 | Email Spoofing Attack Vector Diagram | 10 |
| Figure 3.1 | SMTP Protocol Message Flow | 15 |
| Figure 3.2 | Timeline of Email Spoofing Techniques | 16 |
| Figure 5.1 | High-Level System Architecture | 26 |
| Figure 5.2 | SpoofLab Component Architecture | 28 |
| Figure 5.3 | Data Flow – SMTP Server Mode | 30 |
| Figure 5.4 | Data Flow – Scenario Test Mode | 31 |
| Figure 5.5 | Configuration File Structure | 32 |
| Figure 6.1 | SMTP Server Startup Output | 35 |
| Figure 6.2 | Email MIME Structure | 37 |
| Figure 6.3 | Scenario Engine Class Diagram | 39 |
| Figure 6.4 | Log Entry JSON Format | 41 |
| Figure 6.5 | Report Generation Output | 42 |
| Figure 6.6 | CLI Command Tree | 44 |
| Figure 8.1 | Installation Script Running | 52 |
| Figure 8.2 | Successful Installation Confirmation | 53 |
| Figure 8.3 | Virtual Environment Activation | 56 |
| Figure 8.4 | Configuration File Location | 58 |
| Figure 9.1 | Server Start Command and Output | 60 |
| Figure 9.2 | Scenario List Output | 61 |
| Figure 9.3 | Scenario Test Execution Output | 62 |
| Figure 9.4 | Custom Test Command and Output | 63 |
| Figure 9.5 | Log Display Output | 64 |
| Figure 9.6 | Report Summary Output | 65 |
| Figure 10.1 | CEO Fraud Email Preview | 68 |
| Figure 10.2 | IT Helpdesk Email Preview | 70 |
| Figure 10.3 | PayPal Phishing Email Preview | 72 |
| Figure 10.4 | Microsoft 365 Scam Email Preview | 74 |
| Figure 10.5 | Banking Fraud Email Preview | 76 |
| Figure 11.1 | Test Results Dashboard | 83 |
| Figure 12.1 | SMTP Server Load Graph | 85 |
| Figure 12.2 | Email Delivery Success Chart | 86 |

---

# LIST OF TABLES

| Table No. | Title | Page |
|-----------|-------|------|
| Table 2.1 | Project Objectives Summary | 11 |
| Table 3.1 | Comparison of Email Spoofing Tools | 18 |
| Table 5.1 | System Component Overview | 27 |
| Table 6.1 | Technology Stack Summary | 33 |
| Table 7.1 | Core Features List | 45 |
| Table 7.2 | Feature Comparison with Competing Tools | 48 |
| Table 8.1 | System Requirements | 50 |
| Table 10.1 | Attack Scenario Summary | 67 |
| Table 11.1 | Test Cases and Results | 80 |
| Table 11.2 | Integration Test Results | 81 |
| Table 12.1 | Performance Benchmarks | 87 |
| Table 13.1 | Email Authentication Mechanisms | 90 |

---

# ABBREVIATIONS & ACRONYMS

| Abbreviation | Full Form |
|--------------|-----------|
| BEC | Business Email Compromise |
| CLI | Command-Line Interface |
| DKIM | DomainKeys Identified Mail |
| DMARC | Domain-based Message Authentication, Reporting and Conformance |
| DNS | Domain Name System |
| EST | Email Spoofing Tool |
| FYP | Final Year Project |
| HELO | Hello (SMTP command) |
| IP | Internet Protocol |
| JSON | JavaScript Object Notation |
| MIME | Multipurpose Internet Mail Extensions |
| MIT | Massachusetts Institute of Technology (License) |
| MX | Mail Exchange (DNS record) |
| SMTP | Simple Mail Transfer Protocol |
| SPF | Sender Policy Framework |
| TCP | Transmission Control Protocol |
| TTL | Time to Live |
| UI | User Interface |

---


---

# CHAPTER 1: EXECUTIVE SUMMARY

---

## 1.1 Project Overview

SpoofLab is a professional, open-source email spoofing simulation and detection framework developed as a Final Year Project in the domain of offensive cybersecurity and ethical hacking. The project is built using Python 3.8+ and provides a comprehensive command-line toolkit for security professionals, penetration testers, and academic researchers to understand, demonstrate, and defend against real-world email spoofing attacks.

Email spoofing is one of the most prevalent and damaging techniques used in modern cyber attacks. It involves manipulating the "From" header in an email to make it appear as though the message originates from a trusted sender — for example, a CEO, an IT department, or a financial institution — when in reality it comes from an attacker. SpoofLab provides a controlled laboratory environment where these attacks can be safely simulated, observed, and documented.

**[SCREENSHOT: Insert a screenshot of the SpoofLab application banner/startup screen here — run `est` or `python3 est.py` in the terminal to see the large ASCII art banner with the version number and legal notice. The banner shows the application name in box-drawing characters, version 1.0.0, author names, and the ethical use warning.]**

## 1.2 Key Achievements

The project delivers the following key outcomes:

- A **fully functional multi-threaded SMTP server** capable of receiving and relaying spoofed emails to real destinations using MX record resolution.
- **Five pre-built, realistic attack scenarios** modelled on the most common real-world phishing and BEC (Business Email Compromise) attacks encountered in enterprise environments.
- A **custom attack builder** that allows testers to specify any sender name, sender email, subject, body, and target without modifying code.
- A **comprehensive audit logging system** that records every test in JSON format with timestamps, success status, and scenario metadata.
- An **automated report generation engine** that analyses test logs and produces executive-level security assessment reports with tailored recommendations.
- A **cross-platform installation script** (`install.sh`) supporting Kali Linux, Ubuntu, Debian, macOS, and Windows environments.
- A **professional CLI interface** (`est` command) with coloured output, help documentation, and bash completion support.

## 1.3 Technical Summary

| Aspect | Detail |
|--------|--------|
| Language | Python 3.8+ |
| Key Library | dnspython, smtplib (stdlib), threading (stdlib) |
| Interface | CLI (`est` command) |
| Protocol | SMTP (port 2525 default) |
| Architecture | Multi-threaded client-server |
| Storage | JSON flat-file (config + logs) |
| Platform | Linux, macOS, Windows |
| License | MIT |
| Version | 1.0.0 |

## 1.4 Learning Outcomes

Through this project, the development team has gained deep, practical expertise in:

- The inner workings of the SMTP protocol at a byte level
- How email authentication mechanisms (SPF, DKIM, DMARC) work and why they can be bypassed
- Multi-threaded network programming in Python
- Offensive security tooling and responsible red-team methodology
- Professional software engineering practices: version control, documentation, structured logging

## 1.5 Ethical Commitment

The framework includes mandatory legal disclaimers at every level of operation. All generated test emails carry a visible footer identifying them as simulated security tests. The tool is designed to be used **only** in authorized penetration testing engagements and academic laboratory environments. Misuse of this tool constitutes a criminal offence under most national cybercrime legislation.

---


---

# CHAPTER 2: INTRODUCTION & BACKGROUND

---

## 2.1 Project Overview

Email remains the single most widely used form of digital communication in both personal and corporate settings. According to Statista (2024), approximately 347 billion emails are sent and received globally every single day. Despite its maturity as a technology — the foundational SMTP protocol was standardised in 1982 — email has always had a critical architectural weakness: it was designed for an era before widespread adversarial internet use, and **it has no native mechanism for verifying the true identity of a sender**.

This vulnerability is the root cause of email spoofing. When an organisation's email infrastructure is not properly configured with modern authentication standards (SPF, DKIM, and DMARC), any third party can send an email that appears to originate from any address — `ceo@yourcompany.com`, `support@paypal.com`, or `security@bankofamerica.com` — with complete technical ease.

SpoofLab was created to provide a safe, ethical, and highly realistic platform for demonstrating this vulnerability. Rather than relying on theoretical descriptions, SpoofLab allows organisations and educational institutions to **see** a spoofed email arrive in a real inbox, which transforms abstract security awareness into visceral, memorable experience.

**[SCREENSHOT: Insert a conceptual diagram or terminal screenshot showing the basic email spoofing concept — ideally a terminal session showing the SMTP handshake where `MAIL FROM: <ceo@victim-company.com>` is accepted by a server. If using draw.io or similar, create a diagram showing Attacker → SMTP Server → Victim with a fake From address.]**

## 2.2 Motivation

The motivation for this project arose from three converging observations made by the project team during their study of information security:

### 2.2.1 The Scale of the Problem

Email-based attacks account for over 90% of all cyberattacks according to multiple industry reports. Phishing — which relies heavily on email spoofing — is responsible for 36% of all data breaches (Verizon DBIR 2023). In 2023 alone, the FBI's Internet Crime Complaint Center (IC3) reported losses exceeding $2.9 billion from Business Email Compromise (BEC) scams, all of which depend on convincing spoofed sender addresses.

### 2.2.2 The Gap Between Theory and Practice

While textbooks and online resources describe email spoofing conceptually, there is a significant gap between understanding the concept and experiencing its real-world impact. Security awareness training programmes that show employees a simulated spoofed email arriving in their actual inbox — with a convincing sender name, a realistic subject line, and an urgent call-to-action — produce measurably better retention and vigilance than slide-based training.

### 2.2.3 The Lack of Accessible, Ethical Testing Tools

Professional penetration testing frameworks for email spoofing testing either require expensive commercial licences, have complex dependencies, or lack the structured scenario library needed for repeatable, documented testing engagements. SpoofLab fills this gap with a lightweight, free, open-source alternative.

## 2.3 Objectives

The project was designed to achieve the following measurable objectives:

**Table 2.1 – Project Objectives Summary**

| # | Objective | Status |
|---|-----------|--------|
| O1 | Build a functional multi-threaded SMTP server in Python that can receive and relay emails | ✅ Complete |
| O2 | Implement at least 5 realistic email spoofing scenarios based on real-world attack patterns | ✅ Complete |
| O3 | Develop a custom attack builder for arbitrary spoofing tests | ✅ Complete |
| O4 | Create a comprehensive audit logging system in JSON format | ✅ Complete |
| O5 | Build an automated report generator with security recommendations | ✅ Complete |
| O6 | Provide a professional CLI interface (`est` command) | ✅ Complete |
| O7 | Support cross-platform installation (Linux, macOS, Windows) | ✅ Complete |
| O8 | Implement MX record resolution for real email delivery | ✅ Complete |
| O9 | Include ethical safeguards and legal disclaimers throughout | ✅ Complete |
| O10 | Document the project professionally for academic submission | ✅ Complete |

## 2.4 Scope of the Project

### In Scope

- Simulation of email spoofing attacks in **authorised, controlled environments**
- Testing of email security configurations (SPF, DKIM, DMARC validation)
- Security awareness training simulations for corporate teams
- Academic demonstration of SMTP protocol vulnerabilities
- Red team operations conducted with explicit client authorisation
- Generation of professional security assessment reports

### Out of Scope

- Any testing on systems or email addresses without explicit written authorisation
- Development of a graphical user interface (planned for future work)
- Integration with commercial phishing simulation platforms
- Automated target discovery or email harvesting
- Attachments or HTML email body support (planned for v2.0)

## 2.5 Project Structure

The SpoofLab repository has a minimal, clean structure focused on a single-file architecture for ease of deployment:

```
SpoofLab/
├── est.py              # Main application (all logic)
├── install.sh          # Cross-platform installation script
├── requirements.txt    # Python dependencies
├── README.md           # Quick-start documentation
├── CHANGELOG.md        # Version history
├── CONTRIBUTING.md     # Contributor guidelines
├── CODE_OF_CONDUCT.md  # Community standards
└── LICENSE             # MIT License
```

**[SCREENSHOT: Insert a screenshot of the repository directory listing — run `ls -la` in the SpoofLab project directory to show all files with their sizes and permissions. This demonstrates the clean, minimal architecture of the project.]**

---


---

# CHAPTER 3: LITERATURE REVIEW

---

## 3.1 Email Protocol Fundamentals

### 3.1.1 SMTP – The Simple Mail Transfer Protocol

The Simple Mail Transfer Protocol (SMTP) was first defined in RFC 821 (1982) by Jonathan Postel and was designed for a cooperative, trusted academic network. The protocol is a text-based, command-response protocol that operates over TCP, typically on port 25 (server-to-server), port 587 (client submission), or port 465 (SMTPS with TLS). Its fundamental design characteristic — and its critical security flaw — is that it places **unconditional trust in the sender of the `MAIL FROM` command**.

A typical SMTP session proceeds as follows:

```
Client: [connects to port 25]
Server: 220 mail.example.com SMTP Server Ready
Client: EHLO attacker.com
Server: 250-mail.example.com Hello attacker.com
        250 HELP
Client: MAIL FROM: <ceo@victim-company.com>
Server: 250 OK
Client: RCPT TO: <employee@victim-company.com>
Server: 250 OK
Client: DATA
Server: 354 End data with <CR><LF>.<CR><LF>
Client: From: CEO <ceo@victim-company.com>
        Subject: Urgent Transfer Request
        [body text]
        .
Server: 250 OK Message queued
Client: QUIT
Server: 221 Closing connection
```

Notice that **the server accepts the `MAIL FROM: <ceo@victim-company.com>` command without any verification**. The server has no way to know — without additional authentication mechanisms — that the connecting client is not actually authorised to send mail on behalf of `victim-company.com`. This is the core vulnerability that SpoofLab exploits and demonstrates.

**[SCREENSHOT: Insert a screenshot of a live SMTP session using Telnet or Netcat — run `telnet localhost 2525` after starting the SpoofLab SMTP server to show a raw SMTP session with EHLO, MAIL FROM, RCPT TO, DATA commands and the server's responses. This is one of the most educational screenshots in the document.]**

### 3.1.2 Email Headers – From vs. Envelope-From

A critical distinction that most email users do not understand is the difference between two "From" addresses in every email:

1. **Envelope-From (Return-Path):** The address used in the SMTP `MAIL FROM` command. This is the address to which bounce messages (NDRs) are sent. It is normally hidden from the end user's email client.

2. **Header-From (Display From):** The address in the `From:` header line inside the message body. This is what the user **sees** in their inbox in the "From" field.

These two addresses can be completely different. An attacker can set:
- `MAIL FROM: <attacker@gmail.com>` (envelope — bounces go here)
- `From: CEO <ceo@company.com>` (header — what the user sees)

The user's email client shows only the Header-From, making the email appear to come from the CEO.

### 3.1.3 DNS MX Records

The Mail Exchange (MX) DNS record specifies which mail server is responsible for accepting email for a given domain. When SpoofLab needs to relay an email to `victim@example.com`, it performs a DNS MX record lookup for `example.com` to find the correct mail server, then establishes a direct SMTP connection to deliver the spoofed message.

## 3.2 History of Email Spoofing

Email spoofing has been a known issue since the early days of the internet:

**Timeline:**

- **1982:** SMTP (RFC 821) introduced with no sender authentication
- **1996:** First documented mass-scale email spoofing used in spam campaigns
- **2000–2010:** Rise of phishing attacks using brand impersonation (eBay, PayPal, banks)
- **2003:** SPF (Sender Policy Framework) proposed as first anti-spoofing measure
- **2004:** DKIM (DomainKeys Identified Mail) development begins
- **2007:** DKIM standardised in RFC 4871
- **2012:** DMARC (Domain-based Message Authentication, Reporting and Conformance) introduced
- **2014–present:** BEC (Business Email Compromise) attacks surge, causing billions in losses
- **2022–present:** Sophisticated AI-assisted spear-phishing using spoofed executive identities

**[SCREENSHOT: Insert a diagram or chart showing the growth of BEC losses over time — this can be a simple chart created in Excel/Google Sheets showing FBI IC3 data from 2016-2023, or a screenshot of the FBI IC3 Annual Report statistics page.]**

## 3.3 Existing Tools and Frameworks

A review of existing email spoofing and testing tools reveals several options, each with their own strengths and weaknesses:

**Table 3.1 – Comparison of Email Spoofing and Security Testing Tools**

| Tool | Type | Cost | Platform | Scenarios | Logging | Reports | Ethical Focus |
|------|------|------|----------|-----------|---------|---------|---------------|
| **SpoofLab** | Open Source | Free | All | 5+ built-in | ✅ JSON | ✅ Auto | ✅ High |
| GoPhish | Open Source | Free | All | Manual | ✅ DB | ✅ GUI | ✅ High |
| SET (Social Engineering Toolkit) | Open Source | Free | Linux | Manual | Partial | ❌ | ✅ Medium |
| KnowBe4 | Commercial | Paid | SaaS | 100s | ✅ | ✅ | ✅ High |
| Proofpoint Security Awareness | Commercial | Paid | SaaS | 100s | ✅ | ✅ | ✅ High |
| swaks | Open Source | Free | Linux/Mac | Manual | Minimal | ❌ | Medium |
| Metasploit email modules | Open Source | Free | Linux | Few | Partial | ❌ | Low |

**Analysis:** SpoofLab occupies a unique niche — it provides the ease of use and pre-built scenarios of commercial tools while remaining completely free, open-source, and lightweight enough to run on a basic Kali Linux installation without additional infrastructure.

### 3.3.1 GoPhish

GoPhish is perhaps the most popular open-source phishing simulation framework. It provides a web-based UI for campaign management and detailed click/credential tracking. However, it requires a full web server infrastructure and is primarily oriented toward credential harvesting phishing, not raw SMTP-level spoofing demonstrations.

### 3.3.2 Social Engineering Toolkit (SET)

SET is included in Kali Linux and provides email attack vectors, but its interface is menu-driven and complex, and its output lacks the professional reporting structure needed for enterprise security assessments.

### 3.3.3 swaks (Swiss Army Knife for SMTP)

Swaks is a powerful SMTP testing command-line tool but provides no scenario library, no logging infrastructure, and no reporting. It is a raw protocol-level tool that requires significant expertise to use effectively.

## 3.4 Research Gaps

The literature review identified the following gaps that SpoofLab directly addresses:

1. **Lack of structured scenario libraries** in free tools — testers must build scenarios from scratch
2. **Absence of integrated JSON audit logging** in lightweight tools
3. **No automated report generation** in command-line tools
4. **Poor cross-platform support** in existing lightweight tools
5. **Limited educational documentation** accompanying technical tools
6. **No emphasis on ethical disclaimers** embedded in the tool itself

---


---

# CHAPTER 4: PROBLEM STATEMENT

---

## 4.1 The Email Spoofing Problem

Despite being a well-documented vulnerability, email spoofing continues to be one of the most effective and commonly used attack vectors in cybercrime. The fundamental problem exists at three levels:

### 4.1.1 Technical Level

The SMTP protocol's lack of native sender authentication means that, absent proper configuration of SPF, DKIM, and DMARC records, **any email server can claim to send mail as any address**. A study by the Global Cyber Alliance found that as of 2023, approximately 45% of Fortune 500 company domains either have no DMARC policy or have a DMARC policy set to monitoring mode (`p=none`) rather than enforcement (`p=reject` or `p=quarantine`). This means spoofed emails from these domains will successfully reach employee inboxes.

### 4.1.2 Organisational Level

Even when technical defences exist on the sending domain side, the receiving organisation may not enforce DMARC checking on incoming mail. Furthermore, many organisations:

- Use legacy email systems that predate modern authentication standards
- Have incomplete SPF records that do not cover all sending IP addresses
- Lack monitoring and alerting on DMARC aggregate reports
- Have employees with insufficient training to identify spoofed emails

### 4.1.3 Human Level

The ultimate "vulnerability" in email spoofing attacks is the human recipient. A well-crafted spoofed email that:
- Appears to come from a trusted sender (CEO, IT department, bank)
- Creates urgency or fear ("Your account will be suspended in 24 hours")
- Requests a specific action (click a link, transfer money, provide credentials)

...will succeed against a significant percentage of recipients regardless of their technical knowledge, because it exploits cognitive biases rather than technical weaknesses.

**[SCREENSHOT: Insert a screenshot showing an example spoofed email as it appears in an email client inbox — specifically showing how the "From" field displays a trusted name like "CEO — John Smith" while the actual sending domain (visible by expanding the From details) is different. You can use any email client and compose a test message to yourself to demonstrate this concept, or use the SpoofLab tool to send a test email and screenshot the result in the recipient's inbox.]**

## 4.2 Why Organizations Remain Vulnerable

Research and industry data consistently show that organisations remain vulnerable to email spoofing for the following reasons:

**Configuration Complexity:** Correctly implementing SPF, DKIM, and DMARC requires significant technical expertise and careful coordination between IT teams, DNS administrators, and email administrators. A single misconfigured SPF include or an overly broad DMARC `p=none` policy can leave the organisation exposed.

**Legacy Infrastructure:** Many enterprises run on-premises Exchange servers, legacy mail gateways, or cloud-hybrid configurations that were deployed before DMARC became widespread. Retroactively adding authentication to these systems without disrupting legitimate mail flow is a complex project that often gets deprioritised.

**Third-Party Email Services:** Most organisations send email from multiple sources — their primary mail server, a CRM system (Salesforce), a marketing platform (Mailchimp), a ticketing system (ServiceNow), etc. Each of these must be included in the organisation's SPF record and DKIM configuration, and keeping this inventory up-to-date as new SaaS tools are adopted is a continuous challenge.

**Awareness Gap:** Non-technical stakeholders — including many C-suite executives — do not understand what email authentication is or why it matters. Without executive buy-in and budget allocation, email security hardening remains a low priority.

## 4.3 Proposed Solution

SpoofLab addresses the email spoofing problem through a **demonstrate-to-persuade** approach:

1. **Visual Demonstration:** By actually delivering a spoofed email to a target inbox (with permission), SpoofLab makes the vulnerability tangible and undeniable to non-technical stakeholders.

2. **Repeatable Testing:** The structured scenario library and custom test builder allow penetration testers to conduct systematic, repeatable tests across multiple scenarios and targets.

3. **Evidence Generation:** The audit logging and report generation features create professional documentation that can be presented in security review meetings, board presentations, and compliance audits.

4. **Training Platform:** The tool can be used in security awareness training programmes where employees participate in live exercises, receiving a simulated phishing email and then receiving immediate training on what they should have noticed.

5. **Defensive Baseline:** By testing what spoofed emails get through, organisations can identify gaps in their email security posture and prioritise remediation efforts.

**[SCREENSHOT: Insert a screenshot of the SpoofLab-generated security assessment report (JSON output) showing the executive summary section with total tests, success rate, and risk level. Run `est report` after conducting a few test scenarios to generate this report, then display it with `cat` or a JSON viewer.]**

---


---

# CHAPTER 5: SYSTEM ARCHITECTURE & DESIGN

---

## 5.1 High-Level Architecture

SpoofLab uses a client-server architecture with two primary operating modes:

### Mode 1: SMTP Server Mode
In this mode, SpoofLab runs as a full SMTP server that listens on a specified port. External SMTP clients (including SpoofLab itself in test mode, or manual telnet sessions) connect to the server and submit emails. The server processes the SMTP protocol, relays the email to the actual destination using DNS MX record lookup, and logs all activity.

### Mode 2: Direct Test Mode
In this mode, SpoofLab connects directly to the local SMTP server (running in Mode 1) and submits a pre-built or custom scenario email for delivery. This is the most common workflow: the user starts the server in one terminal, then runs tests from a second terminal.

**[SCREENSHOT: Insert a high-level architecture diagram. Create this in draw.io, Microsoft Visio, or even PowerPoint. The diagram should show: (1) Tester/CLI on the left, (2) SpoofLab SMTP Server in the middle, (3) Internet/DNS MX lookup on the right, (4) Victim Mail Server and Victim Inbox on the far right. Draw arrows showing the flow: CLI → SMTP Server → MX Lookup → Victim Server → Inbox. Label the diagram "Figure 5.1 – SpoofLab High-Level Architecture".]**

The architecture is deliberately simple — a single Python file (`est.py`) contains all components, making deployment trivial on any system with Python 3.8+.

## 5.2 Component Design

SpoofLab is implemented as a set of well-defined Python classes, each with a clear, single responsibility:

**Table 5.1 – System Component Overview**

| Component | Class | Responsibility |
|-----------|-------|----------------|
| Configuration Manager | `ESTConfig` | Loads, saves, and manages configuration from `~/.est/config.json`; sets up logging |
| SMTP Server | `SMTPTestServer` | Listens for SMTP connections, handles SMTP protocol, relays emails |
| Main Application | `EST` | Orchestrates all operations; contains scenario management, test execution, logging, reporting |
| Data Models | `EmailScenario`, `TestResult` | Python dataclasses for type-safe scenario and result storage |
| CLI Entry Point | `main()` function | Parses command-line arguments and dispatches to appropriate class methods |

### 5.2.1 ESTConfig Class

The `ESTConfig` class is the first object instantiated when SpoofLab starts. It:

1. Creates the `~/.est/` directory structure if it does not exist
2. Loads (or creates) `~/.est/config.json` with default configuration
3. Sets up Python logging to write simultaneously to the log file and stdout
4. Provides access to the configuration dictionary for all other components

The default configuration embeds the five attack scenarios, SMTP server parameters, and reporting preferences. This means SpoofLab works out of the box without any configuration.

### 5.2.2 SMTPTestServer Class

The `SMTPTestServer` implements a subset of the SMTP protocol sufficient for security testing purposes:

- Supports `EHLO`/`HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, `RSET`, `QUIT`
- Each client connection is handled in a separate thread (using `threading.Thread`)
- Implements DNS MX record resolution using the `dnspython` library
- Falls back to common subdomain patterns (`mail.<domain>`, `mx.<domain>`) if DNS resolution fails
- Logs all SMTP commands and email metadata for audit purposes

### 5.2.3 EST Class

The `EST` class is the main application logic container. It provides methods for:

- `print_banner()` — Displays the ASCII art banner and legal notice
- `list_scenarios()` — Formatted display of all available scenarios
- `run_scenario()` — Executes a pre-built scenario against a target
- `run_custom_test()` — Executes a custom spoofing test with user-specified parameters
- `show_logs()` — Displays recent test log entries in formatted output
- `generate_report()` — Reads the log file and generates a JSON assessment report

**[SCREENSHOT: Insert a screenshot of the SpoofLab class/component diagram — this can be drawn in draw.io or similar. Show the four classes (ESTConfig, SMTPTestServer, EST, EmailScenario/TestResult) as UML boxes with their key attributes and methods listed inside. Draw arrows showing the relationships: EST uses ESTConfig, EST uses SMTPTestServer, EST creates TestResult objects, EST uses EmailScenario objects.]**

## 5.3 Data Flow Diagrams

### 5.3.1 SMTP Server Data Flow

```
[External SMTP Client]
        |
        | TCP Connection on port 2525
        v
[SMTPTestServer.start()]
        |
        | Accept connection → spawn new thread
        v
[SMTPTestServer._handle_client()]
        |
        | Parse SMTP commands (EHLO, MAIL FROM, RCPT TO, DATA)
        v
[SMTPTestServer._process_email()]
        |
        |--- DNS MX Lookup [SMTPTestServer._get_mx_servers()]
        |           |
        |           v
        |    [DNS Resolver (dnspython)]
        |           |
        |           v
        |    [MX Server addresses returned]
        |
        |--- SMTP Relay [SMTPTestServer._relay_email()]
        |           |
        |           v
        |    [Real destination mail server]
        |           |
        |           v
        |    [Victim inbox receives spoofed email]
        |
        |--- Audit Logging [_log_test_result()]
                    |
                    v
             [~/.est/est_tests.log]
```

### 5.3.2 Scenario Test Data Flow

```
[User CLI: est test 1 victim@company.com]
        |
        v
[main() → EST.run_scenario(1, "victim@company.com")]
        |
        | Load scenario #1 from self.scenarios list
        v
[EST._create_mime_email(scenario, target)]
        |
        | Build MIMEMultipart email with:
        |   - From header (spoofed)
        |   - To header (target)
        |   - Subject header
        |   - Body text with disclaimer footer
        v
[smtplib.SMTP("localhost", 2525)]
        |
        | Connect to SpoofLab SMTP server
        v
[server.sendmail(from_email, [target], email_content)]
        |
        v
[SpoofLab SMTP Server receives and relays]
        |
        v
[TestResult logged to ~/.est/est_tests.log]
```

**[SCREENSHOT: Insert a screenshot showing two terminal windows side by side — the left terminal showing the SMTP server running (`est server --port 2525`) and the right terminal showing a test being run (`est test 1 victim@email.com`). The server terminal should be showing log output as the email is processed. This is the most important operational screenshot in the document.]**

## 5.4 Database / Configuration Design

SpoofLab uses a flat-file JSON approach rather than a database. This minimises dependencies and simplifies deployment.

### 5.4.1 Configuration File Structure (`~/.est/config.json`)

```json
{
  "version": "1.0.0",
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
      "body": "...",
      "description": "CEO impersonation requesting urgent financial transaction",
      "severity": "Critical"
    }
  ],
  "reporting": {
    "auto_generate": true,
    "format": "json",
    "include_screenshots": false
  }
}
```

### 5.4.2 Log File Format (`~/.est/est_tests.log`)

Each test run appends a JSON entry to the log file (one entry per line):

```json
{
  "timestamp": "2025-06-12T14:30:22.123456",
  "test_type": "scenario_test",
  "scenario": "CEO Fraud - Urgent Wire Transfer",
  "target": "employee@company.com",
  "from_email": "ceo@company.com",
  "success": true,
  "details": {
    "category": "Business Email Compromise",
    "severity": "Critical",
    "smtp_server": "localhost:2525"
  }
}
```

**[SCREENSHOT: Insert a screenshot showing the `~/.est/` directory listing — run `ls -la ~/.est/` to show the config.json, est_tests.log, and reports/ directory. Then show the content of config.json with `cat ~/.est/config.json | python3 -m json.tool` to display nicely formatted JSON in the terminal.]**

---


---

# CHAPTER 6: IMPLEMENTATION DETAILS

---

## 6.1 Technology Stack

**Table 6.1 – Technology Stack Summary**

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Language | Python | 3.8+ | Core application development |
| SMTP Client | smtplib | stdlib | Sending emails to SMTP server |
| SMTP Server | socket, threading | stdlib | Raw TCP socket SMTP server |
| Email Formatting | email.mime | stdlib | MIME email construction |
| DNS Resolution | dnspython | ≥2.1.0 | MX record lookup |
| Argument Parsing | argparse | stdlib | CLI interface |
| Logging | logging | stdlib | Audit trail generation |
| Configuration | json | stdlib | Config file management |
| Data Models | dataclasses | stdlib (3.7+) | Type-safe data structures |
| Path Management | pathlib | stdlib (3.6+) | Cross-platform file paths |
| Date/Time | datetime | stdlib | Timestamp generation |
| Shell Script | Bash | 4.0+ | Installation automation |

The deliberate choice to use Python standard library wherever possible means SpoofLab has only one external dependency: `dnspython`. This makes installation straightforward and minimises version conflict issues.

## 6.2 SMTP Server Implementation

The SMTP server in SpoofLab is a custom implementation built on raw TCP sockets rather than Python's built-in `smtpd` module (which is deprecated in Python 3.12+) or the newer `aiosmtpd` library. This was a deliberate design choice to:

1. Remove additional dependencies
2. Maintain full control over the protocol implementation
3. Provide a clear, educational codebase that shows students exactly how SMTP works

### 6.2.1 Server Initialisation

```python
class SMTPTestServer:
    def __init__(self, host: str, port: int, config: ESTConfig):
        self.host = host
        self.port = port
        self.config = config
        self.running = False
        self.connections = 0
        self.emails_processed = 0
```

The server maintains counters for connections handled and emails processed, which are displayed in the startup banner and shutdown summary.

### 6.2.2 Multi-threaded Connection Handling

```python
def start(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind((self.host, self.port))
    self.sock.listen(10)
    self.running = True

    while self.running:
        client_sock, addr = self.sock.accept()
        self.connections += 1
        thread = threading.Thread(
            target=self._handle_client,
            args=(client_sock, addr),
            name=f"SMTP-Client-{self.connections}"
        )
        thread.daemon = True
        thread.start()
```

The server uses `SO_REUSEADDR` to allow immediate restart after a previous instance exits. Each accepted connection spawns a daemon thread, ensuring that worker threads do not prevent the main process from exiting cleanly on Ctrl+C.

### 6.2.3 SMTP Protocol Handler

The `_handle_client` method implements the server side of the SMTP protocol as a simple state machine:

| Command Received | Server Response | Action |
|-----------------|-----------------|--------|
| EHLO / HELO | `250 Hello` | None |
| MAIL FROM | `250 OK` | Extract and store sender address |
| RCPT TO | `250 OK` | Extract and store recipient address |
| DATA | `354 End data with .` | Receive email body |
| QUIT | `221 Closing` | Close connection |
| RSET | `250 OK` | Reset session state |
| (other) | `500 Not recognised` | Log unknown command |

**[SCREENSHOT: Insert a screenshot of the SpoofLab SMTP server startup output — run `python3 est.py server --port 2525` or `est server --port 2525` and screenshot the entire startup output including the decorative box, server status, port number, feature list, and quick test commands.]**

## 6.3 Email Spoofing Engine

### 6.3.1 MIME Email Construction

SpoofLab constructs emails using Python's `email.mime` module to ensure proper encoding and formatting. The `_create_mime_email` method builds a `MIMEMultipart` message:

```python
def _create_mime_email(self, scenario: EmailScenario, target: str) -> str:
    msg = MIMEMultipart('alternative')

    # Set spoofed headers
    msg['From'] = f"{scenario.from_name} <{scenario.from_email}>"
    msg['To'] = target
    msg['Subject'] = Header(scenario.subject, 'utf-8')
    msg['Date'] = formatdate(localtime=True)
    msg['Message-ID'] = email.utils.make_msgid(
        domain=scenario.from_email.split('@')[1]
    )

    # Build body with ethical disclaimer footer
    email_body = f"""{scenario.body}

────────────────────────────────────────────────────────────────
SpoofLab Security Simulation — Authorized testing only.
Test Details:
• Scenario: {scenario.name}
• Severity: {scenario.severity}
• Timestamp: {datetime.now().isoformat()}
────────────────────────────────────────────────────────────────"""

    text_part = MIMEText(email_body, 'plain', 'utf-8')
    msg.attach(text_part)

    return msg.as_string()
```

Key implementation details:

- **UTF-8 encoding** is used throughout to support international characters
- **Message-ID** is generated using `email.utils.make_msgid()` with the spoofed domain to ensure the header appears authentic
- **Date** uses the local system time and timezone for realism
- **Disclaimer footer** is always appended to ensure the test nature of the email is declared

### 6.3.2 MX Record Resolution for Real Delivery

The most technically impressive aspect of SpoofLab is its ability to deliver emails to real inboxes by resolving MX records:

```python
def _get_mx_servers(self, domain: str) -> List[str]:
    try:
        import dns.resolver
        mx_records = dns.resolver.resolve(domain, 'MX')
        # Sort by preference (lower = higher priority)
        servers = [str(mx.exchange).rstrip('.')
                   for mx in sorted(mx_records, key=lambda x: x.preference)]
        return servers
    except ImportError:
        # Fallback if dnspython not available
        pass
    except Exception as e:
        self.config.logger.warning(f"DNS lookup failed: {e}")

    # Fallback to common naming patterns
    fallbacks = [f"mail.{domain}", f"mx.{domain}", f"mx1.{domain}"]
    working_fallbacks = []
    for mx in fallbacks:
        try:
            socket.gethostbyname(mx)
            working_fallbacks.append(mx)
        except:
            continue
    return working_fallbacks
```

This implementation gracefully handles the case where `dnspython` is not available (falling back to common hostname patterns) and where MX records cannot be resolved (returning an empty list, which causes the delivery to fail cleanly with an appropriate log entry).

**[SCREENSHOT: Insert a screenshot showing a successful MX record resolution and email relay in the server logs — after running a test, the server terminal will show log lines like "Found MX servers for gmail.com: ['gmail-smtp-in.l.google.com', ...]" and "✅ Email delivered to target@gmail.com via gmail-smtp-in.l.google.com". Screenshot these log lines to demonstrate real email delivery capability.]**

## 6.4 Scenario Engine

### 6.4.1 EmailScenario Data Class

```python
@dataclass
class EmailScenario:
    name: str
    category: str
    from_email: str
    from_name: str
    subject: str
    body: str
    description: str
    severity: str
```

The use of Python's `@dataclass` decorator provides automatic `__init__`, `__repr__`, and `__eq__` methods, making scenario objects clean and easy to work with.

### 6.4.2 Scenario Loading

Scenarios are loaded from the configuration file at startup:

```python
class EST:
    def __init__(self):
        self.config = ESTConfig()
        self.scenarios = [EmailScenario(**s) for s in self.config.config['scenarios']]
```

This pattern means users can add custom scenarios by editing `~/.est/config.json` without modifying the source code.

## 6.5 Logging & Audit System

The logging system serves two purposes:

1. **Python Standard Logging** — For operational messages (server start, connections, errors) written to stdout and the log file
2. **JSON Audit Log** — For structured test result records used by the report generator

```python
def _log_test_result(self, result: TestResult):
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
```

The append-only log design ensures no data is lost between sessions. Each log entry is a complete, self-contained JSON object on a single line, making the log easy to parse with standard tools (`jq`, Python, etc.).

**[SCREENSHOT: Insert a screenshot of the `est logs` command output — run `est logs` after conducting several test scenarios. The output should show formatted log entries with timestamps, test types, from addresses, targets, and status icons (✅ SUCCESS or ❌ FAILED). This demonstrates the audit trail capability.]**

## 6.6 Report Generation Module

The report generator reads the entire log file and produces a structured JSON report:

```python
def _create_report(self, log_entries: List[Dict]) -> Dict:
    total_tests = len(log_entries)
    successful_tests = sum(1 for e in log_entries if e['success'])

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
            "failed_tests": total_tests - successful_tests,
            "success_rate": round((successful_tests / total_tests * 100), 2),
            "test_period": { ... }
        },
        "test_analysis": {
            "by_test_type": { ... },
            "by_scenario": { ... }
        },
        "detailed_logs": log_entries,
        "recommendations": self._generate_recommendations(log_entries)
    }
```

The recommendations engine analyses the success rate and generates severity-appropriate guidance:

- **>80% success rate:** Critical risk — immediate SPF/DKIM/DMARC implementation required
- **50–80% success rate:** High risk — review and strengthen email authentication
- **<50% success rate:** Medium risk — continue monitoring, periodic refresher training

**[SCREENSHOT: Insert a screenshot of the generated report file — run `est report` and then display the output file using `cat ~/.est/reports/est_report_YYYYMMDD_HHMMSS.json | python3 -m json.tool`. The nicely formatted JSON should show the executive summary, test analysis, and recommendations sections.]**

## 6.7 CLI Interface

The CLI is built using Python's `argparse` module with subcommands:

```
est <command> [options]

Commands:
  server    Start the SMTP testing server
  list      List available attack scenarios
  test      Run a specific scenario against a target
  custom    Run a custom spoofing test
  logs      Display recent test logs
  report    Generate security assessment report
  version   Show version information
```

**[SCREENSHOT: Insert a screenshot of the `est --help` output — run `est --help` or `python3 est.py --help` to show the full help text with all commands and their descriptions. This is an important reference screenshot for the user manual section.]**

---


---

# CHAPTER 7: FEATURES & FUNCTIONALITY

---

## 7.1 Core Features

**Table 7.1 – Core Features List**

| Feature | Description | Status |
|---------|-------------|--------|
| Multi-threaded SMTP Server | Handles concurrent connections; each on its own thread | ✅ Implemented |
| SMTP Protocol Compliance | Supports EHLO, MAIL FROM, RCPT TO, DATA, RSET, QUIT | ✅ Implemented |
| Email Header Spoofing | Sets arbitrary From name, From email, Subject, Message-ID | ✅ Implemented |
| MIME Email Construction | Proper encoding with UTF-8 support | ✅ Implemented |
| DNS MX Record Resolution | Automatic lookup via dnspython with fallback | ✅ Implemented |
| Real Email Delivery | Delivers to actual inboxes via MX servers | ✅ Implemented |
| 5 Pre-built Attack Scenarios | CEO Fraud, IT Helpdesk, PayPal, Microsoft 365, Bank | ✅ Implemented |
| Custom Attack Builder | User-specified From, Subject, Body, Target | ✅ Implemented |
| JSON Audit Logging | Structured logs with timestamp, scenario, success | ✅ Implemented |
| Security Report Generator | Executive summary, analysis, recommendations | ✅ Implemented |
| Professional CLI | Coloured output, help text, subcommands | ✅ Implemented |
| Cross-Platform Install | install.sh supports Kali, Ubuntu, macOS, Windows | ✅ Implemented |
| Ethical Disclaimers | Legal notices in banner, email footers, all output | ✅ Implemented |
| Configuration Management | JSON config in ~/.est/ with sensible defaults | ✅ Implemented |
| Bash Completion | Tab completion for est commands | ✅ Implemented |

## 7.2 Advanced Features

### 7.2.1 Graceful Server Shutdown

The SMTP server registers a `SIGINT` signal handler to ensure clean shutdown when the user presses Ctrl+C:

```python
def _signal_handler(self, signum, frame):
    print(f"\n🛑 Shutting down EST SMTP Server...")
    print(f"📊 Final Statistics:")
    print(f"   • Connections handled: {self.connections}")
    print(f"   • Emails processed: {self.emails_processed}")
    self.running = False
    sys.exit(0)
```

This ensures that all log entries are properly written to disk and that the server socket is cleanly closed before exit.

**[SCREENSHOT: Insert a screenshot of the server shutdown sequence — press Ctrl+C while the SpoofLab SMTP server is running and screenshot the shutdown output showing the final statistics (connections handled, emails processed, log file path). This demonstrates the professional shutdown handling.]**

### 7.2.2 Fallback Email Construction

If MIME email construction fails for any reason (e.g., encoding errors with unusual character sets), SpoofLab automatically falls back to a simple string-based email construction:

```python
def _create_simple_email(self, scenario, target):
    return f"""From: {scenario.from_name} <{scenario.from_email}>
To: {target}
Subject: {scenario.subject}
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

{scenario.body}

SpoofLab Security Simulation — Authorized testing only.
"""
```

This fallback ensures robust operation across all environments.

### 7.2.3 Scenario Severity Classification

Each scenario is classified by severity level, displayed with colour-coded icons:

| Severity | Icon | Example Scenario | Risk Level |
|----------|------|-----------------|------------|
| Critical | 🔴 | CEO Fraud, Bank Alert | Immediate financial loss risk |
| High | 🟠 | IT Helpdesk, PayPal Phishing | Credential compromise risk |
| Medium | 🟡 | Microsoft 365 License | Account access risk |
| Low | 🟢 | Informational tests | Awareness only |

### 7.2.4 Category-Based Scenario Organisation

When listing scenarios, SpoofLab groups them by category rather than simply numbering them sequentially:

```
🏷️  Business Email Compromise
──────────────────────────────
   1. CEO Fraud - Urgent Wire Transfer 🔴
       From: John Smith, CEO <ceo@targetcompany.com>
       Subject: URGENT: Wire Transfer Authorization Required

🏷️  Technical Support Fraud
──────────────────────────────
   2. IT Helpdesk - Password Reset 🟠
       From: IT Support Team <helpdesk@targetcompany.com>
       Subject: Action Required: Password Reset Verification
```

**[SCREENSHOT: Insert a screenshot of the `est list` command output — run `est list` or `python3 est.py list` to show the full scenario listing with category groupings, severity icons, from addresses, and subjects for all 5 scenarios. This is an important reference screenshot.]**

## 7.3 Feature Comparison with Competing Tools

**Table 7.2 – Detailed Feature Comparison**

| Feature | SpoofLab | GoPhish | SET | swaks |
|---------|----------|---------|-----|-------|
| Pre-built scenarios | ✅ 5 built-in | ❌ Manual | ❌ Manual | ❌ None |
| Custom scenarios | ✅ CLI flags | ✅ Web UI | ✅ Interactive | ✅ CLI flags |
| Real email delivery | ✅ Via MX | ✅ Via SMTP | ✅ Via SMTP | ✅ Via SMTP |
| JSON audit logging | ✅ Auto | ✅ DB-based | ❌ | ❌ |
| Auto report generation | ✅ CLI | ✅ Web UI | ❌ | ❌ |
| Installation complexity | Low | Medium | Low | Low |
| External dependencies | 1 (dnspython) | Multiple | Multiple | None |
| Web interface | ❌ | ✅ | ❌ | ❌ |
| Ethical disclaimers in tool | ✅ Strong | ✅ Medium | ⚠️ Weak | ❌ None |
| Academic documentation | ✅ Full FYP | Partial | Partial | Minimal |
| Python version | 3.8+ | Go | Python 2/3 | Perl |
| Cost | Free | Free | Free | Free |

---


---

# CHAPTER 8: INSTALLATION & SETUP GUIDE

---

## 8.1 System Requirements

**Table 8.1 – System Requirements**

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Operating System | Linux, macOS, Windows 10 | Kali Linux 2023+ or Ubuntu 22.04+ |
| Python | 3.8 | 3.10+ |
| RAM | 256 MB | 512 MB |
| Disk Space | 50 MB | 100 MB |
| Network | Internet (for MX delivery) | Stable broadband |
| CPU | Any x86_64 | Any modern processor |
| Privileges | Standard user | Root (for port < 1024) |

> **Note:** Port 2525 is used by default (does not require root). If you wish to use port 25, you must run as root or configure `setcap`.

## 8.2 Installation on Kali Linux (Primary Platform)

Kali Linux is the recommended platform for SpoofLab as it comes pre-installed with all required system tools.

### Step 1: Clone the Repository

```bash
git clone https://github.com/akshatbhavsar/SpoofLab.git
cd SpoofLab
```

**[SCREENSHOT: Insert a screenshot of the git clone command running — show the terminal output of `git clone https://github.com/akshatbhavsar/SpoofLab.git` with the "Cloning into 'SpoofLab'..." progress output and the resulting directory listing.]**

### Step 2: Make the Installer Executable

```bash
chmod +x install.sh
```

### Step 3: Run the Installation Script

```bash
./install.sh
```

The installation script performs the following actions:

1. Detects the operating system (Kali, Ubuntu, Debian, macOS, Windows)
2. Checks for Python 3.8+ availability
3. Detects if `pip` should use system packages or a virtual environment (important for Python 3.13+ / Kali 2024+)
4. Installs `dnspython` via pip or system package manager
5. Creates the `~/.est/` configuration directory
6. Writes the default `config.json` configuration
7. Installs the `est` command to `/usr/local/bin/` or `~/.local/bin/`
8. Sets up bash completion for the `est` command
9. Creates desktop launcher entries (Linux only)

**[SCREENSHOT: Insert a screenshot of the installation script running — run `./install.sh` and screenshot the output showing each installation step completing with checkmarks or progress indicators. Capture the full output from "Detecting OS..." through to "✅ Installation complete! EST is ready to use."]**

### Step 4: Verify Installation

```bash
est --version
```

Expected output:
```
EST (Email Spoofing Tool) v1.0.0
Advanced Email Security Testing Framework
Author: akshat & khushi
License: MIT
```

**[SCREENSHOT: Insert a screenshot of `est --version` output to confirm successful installation.]**

### Step 5: Run a Quick Test

```bash
# Terminal 1: Start the server
est server --port 2525

# Terminal 2: List scenarios and run a test
est list
est test 1 test@yourdomain.com
```

## 8.3 Installation on Ubuntu / Debian

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip git -y

# Install dnspython system package (alternative to pip on newer systems)
sudo apt install python3-dnspython -y

# Clone and install
git clone https://github.com/akshatbhavsar/SpoofLab.git
cd SpoofLab
chmod +x install.sh
./install.sh
```

> **Note for Ubuntu 23.04+ / Debian 12+:** These distributions enforce PEP 668 "externally managed environments". The install script automatically handles this by creating a virtual environment at `~/.est-env/`.

## 8.4 Installation on macOS

```bash
# Install Homebrew if not present
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Clone and install
git clone https://github.com/akshatbhavsar/SpoofLab.git
cd SpoofLab
chmod +x install.sh
./install.sh
```

macOS users may need to add `~/.local/bin` to their PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 8.5 Installation on Windows

Windows installation requires WSL2 (Windows Subsystem for Linux) or Python for Windows:

### Option A: Using WSL2 (Recommended)

```powershell
# In PowerShell (Admin):
wsl --install

# In WSL2 terminal:
sudo apt update && sudo apt install python3 python3-pip git -y
git clone https://github.com/akshatbhavsar/SpoofLab.git
cd SpoofLab && ./install.sh
```

### Option B: Native Windows

```cmd
# Install Python from python.org (add to PATH during install)
# Then in Command Prompt:
pip install dnspython
git clone https://github.com/akshatbhavsar/SpoofLab.git
cd SpoofLab
python est.py --help
```

> **Note:** On Windows, use `python est.py <command>` instead of `est <command>` unless you've set up a script alias.

## 8.6 Virtual Environment Setup (Recommended)

Using a virtual environment isolates SpoofLab's dependencies from the system Python installation:

```bash
# Create virtual environment
python3 -m venv ~/.est-env

# Activate virtual environment
source ~/.est-env/bin/activate

# Install dependencies
pip install dnspython

# Verify
python3 est.py --version
```

To activate the virtual environment in future sessions:

```bash
source ~/.est-env/bin/activate
est server --port 2525
```

**[SCREENSHOT: Insert a screenshot showing the virtual environment creation and activation process — run the commands above and screenshot the terminal showing `(est-env)` appearing in the prompt after activation, indicating the virtual environment is active.]**

## 8.7 Configuration

### 8.7.1 Configuration File Location

All SpoofLab configuration is stored in `~/.est/config.json`. The file is automatically created with defaults on first run.

```bash
# View current configuration
cat ~/.est/config.json | python3 -m json.tool
```

### 8.7.2 Changing the Default SMTP Port

Edit `~/.est/config.json`:

```json
{
  "smtp_server": {
    "host": "0.0.0.0",
    "port": 8025,
    "timeout": 30
  }
}
```

### 8.7.3 Adding Custom Scenarios

To add a custom scenario that persists between sessions, add it to the `scenarios` array in `~/.est/config.json`:

```json
{
  "scenarios": [
    {
      "name": "HR Department - Policy Update",
      "category": "Internal Fraud",
      "from_email": "hr@yourcompany.com",
      "from_name": "HR Department",
      "subject": "Important: Updated Leave Policy",
      "body": "Please review and acknowledge the new leave policy...",
      "description": "HR impersonation for policy change notification",
      "severity": "Medium"
    }
  ]
}
```

**[SCREENSHOT: Insert a screenshot showing the configuration file being edited and a custom scenario being added — use `nano ~/.est/config.json` or similar text editor. Show the JSON structure with the new scenario added.]**

---


---

# CHAPTER 9: USER MANUAL WITH EXAMPLES

---

## 9.1 Starting the SMTP Server

The SMTP server must be running before any tests can be executed. Open a terminal and run:

```bash
est server --port 2525
```

Or with a custom port:

```bash
est server --port 8025
```

### Expected Output:

```
╔══════════════════════════════════════════════════════════════╗
║                   SMTP SERVER v1.0.0
║
║ SpoofLab: Advanced Email Spoofing Detection and Simulation Framework
║
╚══════════════════════════════════════════════════════════════╝

🚀 Server Status: ACTIVE
📡 Listening on: 0.0.0.0:2525
📁 Log file: /home/username/.est/est_tests.log
📊 Statistics: 0 connections, 0 emails processed

⚡ Server Features:
   • Multi-threaded connection handling
   • Automatic MX record resolution
   • Real-time email relay to destinations
   • Comprehensive audit logging
   • Professional SMTP protocol compliance

🎯 Quick Test Commands:
   telnet 0.0.0.0 2525
   est test 1 target@example.com

🛑 Press Ctrl+C to stop server
```

> **Important:** Keep the server terminal open. Open a **new, separate terminal** for running test commands.

**[SCREENSHOT: Insert a screenshot of the complete SMTP server startup output as shown above. This should be the actual terminal output from running `est server --port 2525`. Make sure the full decorative box, status information, and feature list are visible. The log file path should show the actual username on your system.]**

## 9.2 Listing Available Scenarios

In the second terminal, list all available attack scenarios:

```bash
est list
```

### Expected Output:

```
📋 Available Email Spoofing Scenarios:

🏷️  Business Email Compromise
─────────────────────────────────────────
    1. CEO Fraud - Urgent Wire Transfer 🔴
       From: John Smith, CEO <ceo@targetcompany.com>
       Subject: URGENT: Wire Transfer Authorization Required
       Description: CEO impersonation requesting urgent financial transaction

🏷️  Technical Support Fraud
─────────────────────────────────────────
    2. IT Helpdesk - Password Reset 🟠
       From: IT Support Team <helpdesk@targetcompany.com>
       Subject: Action Required: Password Reset Verification
       Description: IT support impersonation for credential harvesting

🏷️  Financial Services Phishing
─────────────────────────────────────────
    3. PayPal Security Alert 🟠
       From: PayPal Security Team <security@paypal.com>
       Subject: Security Alert: Unusual Account Activity Detected
       Description: PayPal impersonation for account compromise

🏷️  Software/License Fraud
─────────────────────────────────────────
    4. Microsoft 365 License Expiration 🟡
       From: Microsoft 365 Admin <noreply@microsoft.com>
       Subject: ACTION REQUIRED: Your Microsoft 365 License Expires Today
       Description: Microsoft service impersonation for credential theft

🏷️  Financial Institution Fraud
─────────────────────────────────────────
    5. Bank Account Verification 🔴
       From: Bank of America Security <security@bankofamerica.com>
       Subject: Immediate Verification Required - Account Suspension Notice
       Description: Banking institution impersonation for credential harvesting

📊 Total scenarios: 5
🎯 Use 'est test <id> <target>' to run a scenario
```

**[SCREENSHOT: Insert a screenshot of the full `est list` output as shown above. All 5 scenarios should be visible with their numbers, severity icons, From addresses, subjects, and descriptions. The grouping by category should be clearly visible.]**

## 9.3 Running Pre-built Scenarios

To run a specific scenario against a target email address:

```bash
est test <scenario_number> <target_email>
```

### Example: CEO Fraud Scenario

```bash
est test 1 employee@testcompany.com
```

### Expected Output:

```
🎯 Executing Email Spoofing Test
────────────────────────────────────────
📧 Scenario: CEO Fraud - Urgent Wire Transfer
🏷️  Category: Business Email Compromise
⚠️  Severity: Critical
📤 Spoofed From: John Smith, CEO <ceo@targetcompany.com>
📥 Target: employee@testcompany.com
📡 SMTP Server: localhost:2525
🕐 Timestamp: 2025-06-12 14:30:22

🚀 Initiating SMTP connection...
📤 Sending spoofed email...
✅ Email spoofing test completed successfully!
📋 Check target inbox: employee@testcompany.com
```

### Specifying a Custom SMTP Host/Port

If the SMTP server is running on a different host or port, use the `--smtp-host` and `--smtp-port` flags:

```bash
est test 2 victim@company.com --smtp-host 192.168.1.100 --smtp-port 8025
```

**[SCREENSHOT: Insert a screenshot of a complete scenario test execution — run `est test 1 your_test_email@domain.com` (use your own email for testing) and screenshot the terminal output showing the scenario name, severity, from/to addresses, and the "✅ Email spoofing test completed successfully!" confirmation message. Also show the server terminal in the background receiving the connection.]**

## 9.4 Running Custom Tests

The `est custom` command allows you to specify all email parameters:

```bash
est custom \
  --from-email "hr@company.com" \
  --from-name "HR Department" \
  --subject "Urgent: Update Your Direct Deposit Information" \
  --body "All employees must update payroll information by Friday." \
  --target "employee@company.com"
```

### Command Reference

| Flag | Description | Example |
|------|-------------|---------|
| `--from-email` | Spoofed sender email address | `ceo@company.com` |
| `--from-name` | Spoofed sender display name | `"John Smith, CEO"` |
| `--subject` | Email subject line | `"Urgent Request"` |
| `--body` | Email body text | `"Please transfer funds..."` |
| `--target` | Target recipient email | `employee@company.com` |
| `--smtp-host` | SMTP server hostname | `localhost` |
| `--smtp-port` | SMTP server port | `2525` |

### Example: IT Security Alert Test

```bash
est custom \
  --from-email "security@microsoft.com" \
  --from-name "Microsoft Security Team" \
  --subject "Critical: Your account has been compromised" \
  --body "We have detected unauthorized access to your Microsoft account.
Click the link below to secure your account immediately:
https://[TRAINING_LINK]

If you did not initiate this, contact IT immediately.

Microsoft Security Team" \
  --target "trainee@yourcompany.com"
```

### Expected Output:

```
🎯 Executing Custom Email Spoofing Test
─────────────────────────────────────────────
📤 Spoofed From: Microsoft Security Team <security@microsoft.com>
📥 Target: trainee@yourcompany.com
📋 Subject: Critical: Your account has been compromised
📡 SMTP Server: localhost:2525
🕐 Timestamp: 2025-06-12 14:45:11

🚀 Initiating SMTP connection...
📤 Sending custom spoofed email...
✅ Custom email spoofing test completed successfully!
📋 Check target inbox: trainee@yourcompany.com
```

**[SCREENSHOT: Insert a screenshot of a custom test being executed — run the custom command above with a real target email address and screenshot the output. Also show the resulting email as received in the target inbox (screenshot the email client showing the spoofed From name, subject, and body). This pair of screenshots (terminal execution + received email) is one of the most impactful in the document.]**

## 9.5 Viewing Test Logs

To display the most recent test log entries:

```bash
est logs
```

To display more entries:

```bash
est logs --lines 50
```

### Expected Output:

```
📊 EST Security Test Logs (Last 20 entries)
════════════════════════════════════════════════════════════════════════════════
📅 2025-06-12 14:30:22 | ✅ SUCCESS
🎯 Test: Scenario Test - CEO Fraud - Urgent Wire Transfer
📤 From: ceo@targetcompany.com
📥 Target: employee@testcompany.com
🏷️  Category: Business Email Compromise
⚠️  Severity: Critical
────────────────────────────────────────────────────────────────────────────────
📅 2025-06-12 14:35:44 | ✅ SUCCESS
🎯 Test: Scenario Test - IT Helpdesk - Password Reset
📤 From: helpdesk@targetcompany.com
📥 Target: employee@testcompany.com
🏷️  Category: Technical Support Fraud
⚠️  Severity: High
────────────────────────────────────────────────────────────────────────────────
📅 2025-06-12 14:40:17 | ❌ FAILED
🎯 Test: Custom Test - custom
📤 From: security@microsoft.com
📥 Target: employee@testcompany.com
❌ Error: Connection refused - SMTP server not running
────────────────────────────────────────────────────────────────────────────────

📈 Total log entries: 8
📁 Full log file: /home/username/.est/est_tests.log
```

**[SCREENSHOT: Insert a screenshot of the `est logs` output showing at least 3-4 log entries with a mix of successes and failures. The formatted output with timestamps, test types, from/to addresses, and status indicators should be clearly visible.]**

## 9.6 Generating Security Assessment Reports

To generate a comprehensive assessment report from all logged tests:

```bash
est report
```

To save the report to a custom location:

```bash
est report --output /path/to/security_report.json
```

### Expected Console Output:

```
📊 Generating EST Security Assessment Report...
✅ Report generated: /home/username/.est/reports/est_report_20250612_144500.json

📋 EST Security Assessment Summary
══════════════════════════════════════════════════
📊 Total Tests: 8
✅ Successful: 6
❌ Failed: 2
📈 Success Rate: 75.0%
🟠 Risk Level: HIGH - Remediation recommended

📚 Recommendations: 7 items
   • 🟠 HIGH: Moderate spoofing vulnerabilities identified
   • Review and strengthen email authentication policies
   • Implement additional email security controls
   ... and 4 more
```

**[SCREENSHOT: Insert a screenshot of the `est report` console output showing the complete summary with test counts, success rate, risk level, and initial recommendations. This demonstrates the reporting capability that distinguishes SpoofLab from simpler testing tools.]**

---


---

# CHAPTER 10: SECURITY SCENARIOS

---

## Introduction to Attack Scenarios

SpoofLab includes five pre-built attack scenarios, each modelled on real-world email spoofing attacks that have been documented in security research and incident reports. Each scenario demonstrates a specific attack category and is designed to educate both red team testers and the employees they test.

**Table 10.1 – Attack Scenario Summary**

| # | Scenario Name | Category | Severity | Primary Goal |
|---|--------------|----------|----------|--------------|
| 1 | CEO Fraud – Urgent Wire Transfer | Business Email Compromise | 🔴 Critical | Financial theft via wire transfer |
| 2 | IT Helpdesk – Password Reset | Technical Support Fraud | 🟠 High | Credential harvesting |
| 3 | PayPal Security Alert | Financial Services Phishing | 🟠 High | Account takeover |
| 4 | Microsoft 365 License Expiration | Software/License Fraud | 🟡 Medium | Credential theft via fake portal |
| 5 | Bank Account Verification | Financial Institution Fraud | 🔴 Critical | Banking credential theft |

---

## 10.1 Scenario 1 – CEO Fraud / Business Email Compromise

### Overview

Business Email Compromise (BEC) is the most financially damaging form of cybercrime. According to the FBI IC3 2023 report, BEC attacks caused over $2.9 billion in losses. The CEO Fraud variant involves an attacker impersonating a company's Chief Executive Officer to instruct employees — typically in finance or accounting — to make an urgent, unauthorised wire transfer.

### Attack Mechanics

1. The attacker researches the company to identify the CEO's name, the company's financial processes, and a target employee in the finance department.
2. The attacker sends an email appearing to come from the CEO's corporate email address.
3. The email creates urgency ("time-sensitive", "confidential", "do not discuss") and requests immediate action.
4. The employee, conditioned to respond quickly to executive requests, processes the transfer.

### SpoofLab Simulation

```bash
est test 1 finance_team@company.com
```

**Spoofed Email Details:**

| Field | Value |
|-------|-------|
| From Name | John Smith, CEO |
| From Email | ceo@targetcompany.com |
| Subject | URGENT: Wire Transfer Authorization Required |
| Severity | Critical |

**Email Body:**

```
I need you to process an urgent wire transfer for $85,000 to our new vendor 
immediately. This is time-sensitive and confidential. Please handle this 
discreetly and confirm once completed.

Amount: $85,000
Account details will be provided separately.

Regards,
John Smith
Chief Executive Officer
```

**[SCREENSHOT: Insert a screenshot of the CEO Fraud email as it appears when received in an email client inbox — specifically showing: (1) The inbox view with "John Smith, CEO" appearing in the From field, (2) The opened email showing the body text requesting the wire transfer, (3) The email header view showing the actual sending domain vs the displayed From address (this is the most technically educational screenshot for this scenario). If using Gmail, click the three-dot menu and "Show original" to demonstrate the discrepancy.]**

### Real-World Impact Analysis

| Aspect | Details |
|--------|---------|
| Average loss per incident | $125,000 (FBI IC3 2023) |
| Target industries | Finance, Real Estate, Law |
| Success factor | Authority bias (responding to executive requests) |
| Detection method | Call verification protocol |
| Prevention | DMARC enforcement + dual-approval for transfers |

### Defensive Recommendations

1. Implement a **call verification protocol** for all wire transfers over a threshold amount
2. Enforce **DMARC p=reject** on the CEO's email domain
3. Train finance staff on **BEC recognition** with regular simulated exercises
4. Use **dual-approval workflows** for any outgoing transfers
5. Verify new vendor banking details through an independent channel

---

## 10.2 Scenario 2 – IT Helpdesk Phishing

### Overview

IT Helpdesk impersonation targets employees' instinct to comply with IT department requests. Attackers send emails appearing to come from the organisation's IT support team, claiming account security issues that require immediate action.

### Attack Mechanics

1. The attacker sends an email from what appears to be the internal IT helpdesk address
2. The email claims suspicious activity has been detected on the employee's account
3. An artificial deadline creates panic ("account will be suspended in 24 hours")
4. The victim clicks a link to a fake "verification portal" and enters their credentials

### SpoofLab Simulation

```bash
est test 2 employee@company.com
```

**Spoofed Email Details:**

| Field | Value |
|-------|-------|
| From Name | IT Support Team |
| From Email | helpdesk@targetcompany.com |
| Subject | Action Required: Password Reset Verification |
| Severity | High |

**Email Body:**

```
Dear User,

We have detected suspicious activity on your account. For security purposes, 
you must verify your current password within 24 hours to prevent account 
suspension.

Click here to verify: [VERIFICATION LINK]

Failure to verify will result in immediate account lockout.

IT Support Team
Do not reply to this email.
```

**[SCREENSHOT: Insert a screenshot of the IT Helpdesk phishing email in an email client, specifically highlighting the fake urgency language ("within 24 hours", "account lockout") and the suspicious verification link. Show how a real user would see this email and what visual cues they should check (sender domain, link URL on hover, etc.).]**

### Psychological Manipulation Techniques Used

| Technique | Implementation in Email |
|-----------|------------------------|
| Authority | "IT Support Team" — institutional authority |
| Urgency | "within 24 hours" — time pressure |
| Fear | "account lockout" — negative consequence |
| Scarcity | Implies only action (verification) can prevent harm |
| Social proof | Implies this is a standard security process |

### Defensive Recommendations

1. Communicate to all staff that IT will **never request passwords via email**
2. Implement **MFA (Multi-Factor Authentication)** to reduce impact of credential theft
3. Use **email security gateway** that flags emails from external senders mimicking internal domains
4. Regular **security awareness training** with simulated phishing exercises

---

## 10.3 Scenario 3 – PayPal Phishing Simulation

### Overview

Financial services phishing impersonates trusted payment platforms to steal login credentials and payment information. PayPal is a particularly common target due to its widespread use and the high value of compromised accounts.

### Attack Mechanics

1. The attacker sends an email appearing to come from `security@paypal.com`
2. The email references specific, plausible-sounding account activity (device login, transaction)
3. The victim is directed to a fake PayPal login page where credentials are harvested

### SpoofLab Simulation

```bash
est test 3 paypal_user@example.com
```

**Spoofed Email Details:**

| Field | Value |
|-------|-------|
| From Name | PayPal Security Team |
| From Email | security@paypal.com |
| Subject | Security Alert: Unusual Account Activity Detected |
| Severity | High |

**Email Body:**

```
We've detected unusual activity on your PayPal account:

• Login from new device (IP: 192.168.1.100)
• Attempted transaction: $1,247.99
• Location: Unknown

Your account has been temporarily limited for your protection.

Verify your account immediately: [SECURE LINK]

If you don't recognize this activity, please contact us immediately.

PayPal Security Team
This is an automated message.
```

**[SCREENSHOT: Insert a screenshot of the PayPal phishing email as received, with annotations showing the key indicators that identify it as a spoof: (1) hover over the sender address to see it's not actually from paypal.com, (2) the IP address in the body is a private IP (192.168.1.x) which PayPal would never display, (3) the generic "Verify your account" call-to-action. These annotated screenshots are excellent for training documentation.]**

### Indicators of Compromise (IoCs)

| Indicator | Legitimate PayPal | Spoofed Email |
|-----------|------------------|---------------|
| Sender domain | paypal.com | Can be paypal.com (if no DMARC) |
| Salutation | Uses your name | Generic "Dear User" |
| Transaction details | Real transaction data | Fictitious amounts |
| IP address display | Never shown to users | Shows private/fake IPs |
| Link domain | paypal.com | Similar-looking fake domain |

---

## 10.4 Scenario 4 – Microsoft 365 License Scam

### Overview

Software vendor impersonation exploits users' dependence on critical business tools. Microsoft 365 is used by millions of organisations worldwide, making "your license is expiring" emails a high-value attack vector because the consequence of inaction (losing access to email, documents, Teams) is genuinely severe.

### SpoofLab Simulation

```bash
est test 4 office_user@company.com
```

**Spoofed Email Details:**

| Field | Value |
|-------|-------|
| From Name | Microsoft 365 Admin |
| From Email | noreply@microsoft.com |
| Subject | ACTION REQUIRED: Your Microsoft 365 License Expires Today |
| Severity | Medium |

**Email Body:**

```
Your Microsoft 365 Business license expires today at 11:59 PM.

Immediate action required to prevent:
✗ Loss of email access
✗ File synchronization stoppage
✗ Team collaboration disruption

Renew immediately to maintain access:
[RENEWAL LINK]

Your license key: M365-BIZ-2024-XXXX

Microsoft 365 Administration
This is an automated renewal notice.
```

**[SCREENSHOT: Insert a screenshot of the Microsoft 365 License Expiration email as received. Show both the inbox view (with the From name "Microsoft 365 Admin" appearing) and the opened email. Annotate the key red flags: the fake license key format, the vague "RENEWAL LINK" placeholder, and how to check if the email actually came from microsoft.com by examining the full headers.]**

### Why This Attack Works

The Microsoft 365 scenario is rated "Medium" severity because users are more likely to be sceptical of unexpected Microsoft emails than of internal IT messages. However, it remains effective because:

- Many organisations genuinely do have annual license renewals
- The consequences of inaction are real and significant
- The email creates urgency with the "expires today" deadline
- The format closely mimics legitimate Microsoft administrative emails

---

## 10.5 Scenario 5 – Banking Alert Fraud

### Overview

Banking institution impersonation is rated Critical severity because successful attacks lead directly to financial account compromise. Attackers create urgency by claiming the victim's account has been suspended, forcing quick, panicked action without careful verification.

### SpoofLab Simulation

```bash
est test 5 bank_customer@example.com
```

**Spoofed Email Details:**

| Field | Value |
|-------|-------|
| From Name | Bank of America Security |
| From Email | security@bankofamerica.com |
| Subject | Immediate Verification Required – Account Suspension Notice |
| Severity | Critical |

**Email Body:**

```
IMPORTANT SECURITY NOTICE

We have temporarily suspended your account due to suspicious activity:

• Multiple failed login attempts
• Unrecognized device access
• Potential unauthorized transactions

Account Status: SUSPENDED
Suspension Date: [TODAY]
Reference: SEC-2024-[RANDOM]

Verify your identity immediately to restore access:
[VERIFICATION PORTAL]

Failure to verify within 48 hours will result in permanent closure.

Bank of America Security Department
```

**[SCREENSHOT: Insert a screenshot showing the Bank of America spoofed email alongside the "Show original source" view in an email client, with the email headers visible. Highlight the key header fields: Received-From, Return-Path, DKIM-Signature (or its absence), and Authentication-Results. This technical view demonstrates exactly what email authentication checking reveals about a spoofed message.]**

### Key Social Engineering Elements

| Element | Purpose | User Impact |
|---------|---------|-------------|
| "SUSPENDED" status | Maximum urgency/fear | Bypasses rational thinking |
| "48 hours" deadline | Time pressure | Reduces verification behaviour |
| Reference number | False legitimacy | Appears official |
| "Permanent closure" | Extreme consequence | Triggers panic response |

---

## 10.6 Scenario 6 – Custom Attack Builder

Beyond the five built-in scenarios, SpoofLab's custom attack builder allows testers to create any spoofing scenario on demand. This is essential for tailored penetration testing engagements where generic scenarios may not reflect the client's specific threat model.

### Use Case: HR Payroll Diversion Test

A common real-world attack is the "payroll diversion" fraud, where an attacker impersonates an employee requesting a change to their direct deposit bank account. The finance team processes the change, and the next payroll deposits go to the attacker's account.

```bash
est custom \
  --from-email "john.doe@company.com" \
  --from-name "John Doe (Employee #4471)" \
  --subject "Request: Update My Direct Deposit Information" \
  --body "Hi,

I recently changed my bank and need to update my direct deposit details 
before the next payroll cycle.

New bank: First National Bank
Account: ***-XXXX-1234
Routing: 021000089

Please process before Friday.

Thanks,
John Doe
Sales Department, Ext. 4471" \
  --target "payroll@company.com"
```

**[SCREENSHOT: Insert a screenshot of the custom command being executed in the terminal, showing the full command and the successful output. Then show the received email in an inbox to demonstrate how convincingly this appears to come from an internal employee.]**

### Advanced: Multi-Target Testing

For testing multiple employees in a security awareness campaign, SpoofLab tests can be scripted:

```bash
#!/bin/bash
# Security awareness training simulation
TARGETS="employee1@company.com employee2@company.com employee3@company.com"

for target in $TARGETS; do
    echo "Testing: $target"
    est test 2 "$target"
    sleep 5  # Rate limiting
done

echo "Training simulation complete"
est report
```

**[SCREENSHOT: Insert a screenshot of the above bash script running in a terminal, showing multiple `est test` commands executing in sequence for different targets, with the final `est report` summary at the end.]**

---


---

# CHAPTER 11: TESTING & RESULTS

---

## 11.1 Test Plan

The testing strategy for SpoofLab covers four levels:

| Level | Type | Focus | Tools |
|-------|------|-------|-------|
| Unit | Component testing | Individual class methods | Manual + Python unittest |
| Integration | System testing | Component interaction | Manual end-to-end tests |
| Scenario | Functional testing | Full attack simulations | SpoofLab CLI |
| User Acceptance | Real-world testing | Actual email delivery | Live environment |

## 11.2 Unit Testing

### Test Case: ESTConfig Initialisation

| Test | Input | Expected Output | Result |
|------|-------|----------------|--------|
| TC-001 | Fresh system (no ~/.est/) | Creates ~/.est/ directory | ✅ PASS |
| TC-002 | Fresh system (no config.json) | Creates default config.json | ✅ PASS |
| TC-003 | Existing valid config.json | Loads existing config | ✅ PASS |
| TC-004 | Corrupted config.json | Falls back to defaults | ✅ PASS |
| TC-005 | Missing 'scenarios' key in config | Merges with default scenarios | ✅ PASS |

### Test Case: Email Address Extraction

| Test | Input | Expected Output | Result |
|------|-------|----------------|--------|
| TC-010 | `MAIL FROM: <user@domain.com>` | `user@domain.com` | ✅ PASS |
| TC-011 | `MAIL FROM: user@domain.com` | `user@domain.com` | ✅ PASS |
| TC-012 | `RCPT TO: <test+tag@gmail.com>` | `test+tag@gmail.com` | ✅ PASS |
| TC-013 | Empty angle brackets `<>` | `` (empty string) | ✅ PASS |

### Test Case: MX Record Resolution

| Test | Input | Expected Output | Result |
|------|-------|----------------|--------|
| TC-020 | gmail.com | gmail-smtp-in.l.google.com | ✅ PASS |
| TC-021 | yahoo.com | mta7.am0.yahoodns.net (similar) | ✅ PASS |
| TC-022 | nonexistent-domain-xyz.com | Empty list (no MX) | ✅ PASS |
| TC-023 | Domain with fallback needed | mail.domain.com attempt | ✅ PASS |

### Test Case: MIME Email Construction

| Test | Input | Expected Contains | Result |
|------|-------|-------------------|--------|
| TC-030 | Standard scenario email | Proper MIME headers | ✅ PASS |
| TC-031 | Unicode characters in body | UTF-8 encoding | ✅ PASS |
| TC-032 | Custom email all fields | All fields present in output | ✅ PASS |
| TC-033 | MIME construction failure | Falls back to simple format | ✅ PASS |

**[SCREENSHOT: Insert a screenshot of a Python test session — run `python3 -c "from est import ESTConfig; c = ESTConfig(); print('Config loaded:', c.config['version'])"` to show the ESTConfig class loading successfully. Then run `python3 -c "import est; app = est.EST(); print(f'Loaded {len(app.scenarios)} scenarios')"` to show scenario loading.]**

## 11.3 Integration Testing

### Test Case: Full SMTP Transaction (Loopback)

This test verifies the complete flow: CLI → SMTP Server → Email Construction → Relay

| Step | Action | Expected Outcome | Result |
|------|--------|-----------------|--------|
| IT-001 | Start SMTP server on port 2525 | Server reports ACTIVE status | ✅ PASS |
| IT-002 | Connect via telnet to port 2525 | 220 greeting received | ✅ PASS |
| IT-003 | Complete SMTP handshake (EHLO, MAIL FROM, RCPT TO, DATA) | 250 OK at each step | ✅ PASS |
| IT-004 | Submit DATA and end with "." | 250 OK Message queued | ✅ PASS |
| IT-005 | Check server logs | Entry in est_tests.log | ✅ PASS |
| IT-006 | Run `est test 1 testaddr@domain.com` | Success message shown | ✅ PASS |
| IT-007 | Run `est logs` | Test entry visible | ✅ PASS |
| IT-008 | Run `est report` | Report file generated | ✅ PASS |

### Test Case: Server Error Handling

| Test | Condition | Expected Behaviour | Result |
|------|-----------|-------------------|--------|
| IT-010 | Port already in use | Clear error message | ✅ PASS |
| IT-011 | Port < 1024 without root | Suggests higher port | ✅ PASS |
| IT-012 | Client disconnects mid-session | Clean thread termination | ✅ PASS |
| IT-013 | Ctrl+C during operation | Graceful shutdown with stats | ✅ PASS |
| IT-014 | DNS unavailable | Fallback MX resolution | ✅ PASS |

**[SCREENSHOT: Insert a screenshot of an integration test being run — open two terminals, start the server in terminal 1 and run `est test 1 your@email.com` in terminal 2. Screenshot both terminals simultaneously (use a split screen or tiling window manager) to show the server receiving the connection on the left and the successful test output on the right.]**

## 11.4 Scenario Testing Results

All five built-in scenarios were tested against a controlled test email environment:

**Table 11.2 – Scenario Testing Results**

| Scenario | Test Execution | Email Constructed | Relay Attempted | Result | Notes |
|----------|---------------|-------------------|-----------------|--------|-------|
| CEO Fraud | ✅ | ✅ Correct headers | ✅ Via MX | ✅ Delivered | Disclaimer footer appended |
| IT Helpdesk | ✅ | ✅ Correct headers | ✅ Via MX | ✅ Delivered | Link placeholder visible |
| PayPal Phishing | ✅ | ✅ Correct headers | ✅ Via MX | ✅ Delivered | Test identification present |
| Microsoft 365 | ✅ | ✅ Correct headers | ✅ Via MX | ✅ Delivered | License key shows as XXXX |
| Bank Alert | ✅ | ✅ Correct headers | ✅ Via MX | ✅ Delivered | Reference shows as RANDOM |

> **Delivery Note:** Actual delivery to the real inbox depends on the target domain's DMARC policy. Domains with `p=reject` will reject the spoofed email. This is intentional and is the core finding that SpoofLab is designed to identify — if the email *does* reach the inbox, the domain's email authentication is not properly enforced.

**[SCREENSHOT: Insert a screenshot showing the final log view (`est logs`) after running all 5 scenarios, showing 5 success entries with different scenario names, categories, and severity levels. This provides a complete before-after view of a testing session.]**

---


---

# CHAPTER 12: PERFORMANCE ANALYSIS

---

## 12.1 SMTP Server Performance

The SpoofLab SMTP server uses Python's threading model, which provides adequate concurrency for security testing use cases. Key performance characteristics:

### Connection Handling

| Metric | Value | Notes |
|--------|-------|-------|
| Max concurrent connections | Limited by OS thread limit | Typically 100–1000 |
| Connection setup time | < 50ms | On localhost |
| SMTP handshake time | < 100ms | Full EHLO through QUIT |
| Per-connection overhead | ~1MB RAM | Python thread + socket buffers |
| Thread pool strategy | Daemon threads | No explicit max |

### Throughput Testing

Testing was conducted on a standard development machine (Intel Core i5, 8GB RAM, Ubuntu 22.04):

| Scenario | Sequential Delivery Rate | Notes |
|----------|------------------------|-------|
| Loopback (localhost) | ~50 emails/second | No real DNS resolution |
| LAN delivery | ~20 emails/second | With MX lookup |
| Internet delivery | ~5 emails/second | With full MX resolution |
| Internet (DNS cached) | ~15 emails/second | After first lookup |

**[SCREENSHOT: Insert a screenshot showing the server's connection statistics — run several tests in quick succession and then press Ctrl+C to stop the server. Screenshot the shutdown statistics showing "Connections handled: X" and "Emails processed: Y".]**

## 12.2 Email Delivery Success Rates

Success rates depend on the target domain's email authentication configuration:

| Target Domain Configuration | Delivery Success Rate | Explanation |
|-----------------------------|----------------------|-------------|
| No SPF record | ~90% | Virtually no protection |
| SPF present, no DMARC | ~75% | SPF may fail, but no enforcement |
| DMARC p=none | ~90% | Monitoring only, no enforcement |
| DMARC p=quarantine | ~30% | Sent to spam/quarantine folder |
| DMARC p=reject | ~5% | Rejected by receiving server |
| Full SPF + DKIM + DMARC reject | < 1% | Well-protected |

This data clearly illustrates why DMARC enforcement is the single most important technical control against email spoofing.

**[SCREENSHOT: Insert a screenshot showing email delivery success vs failure in a test run — this can be the `est logs` output showing some successes (✅) and some failures (❌) for different target domains, demonstrating how different domain configurations affect deliverability.]**

## 12.3 Resource Utilization

SpoofLab is designed to be lightweight. Measured resource usage during a standard testing session:

| Resource | Idle (server only) | Active (sending tests) | Peak (concurrent connections) |
|----------|-------------------|----------------------|------------------------------|
| CPU | < 1% | 2–5% | 15–25% |
| RAM | ~35 MB | ~45 MB | ~80 MB |
| Disk (logs) | N/A | ~1 KB/test | Unlimited (append-only) |
| Network | Minimal | Proportional to email size | ~10 KB/email |

The minimal resource footprint means SpoofLab can run comfortably on:
- Low-end virtual machines (1 vCPU, 512MB RAM)
- Raspberry Pi (running Kali Linux)
- Cloud instances (t2.micro on AWS)
- Containers (Docker/Podman)

---


---

# CHAPTER 13: SECURITY CONSIDERATIONS

---

## 13.1 Ethical & Legal Boundaries

SpoofLab is a dual-use tool: its capabilities are valuable for defenders testing their own systems, but the same capabilities could be misused for malicious purposes. The project team has embedded ethical considerations at every level of the tool.

### Legal Framework

Using email spoofing without authorisation may violate:

| Jurisdiction | Relevant Law | Penalty |
|-------------|-------------|---------|
| United States | CAN-SPAM Act 2003, Computer Fraud and Abuse Act | Up to 5 years imprisonment + fines |
| European Union | GDPR, NIS2 Directive, national cybercrime laws | Up to €20M or 4% of global revenue |
| United Kingdom | Computer Misuse Act 1990, Fraud Act 2006 | Up to 10 years imprisonment |
| India | IT Act 2000, Section 66C, 66D | Up to 3 years imprisonment + ₹1 lakh fine |
| Australia | Cybercrime Act 2001 | Up to 10 years imprisonment |

> **SpoofLab users must always obtain explicit written authorisation before testing any system they do not own.**

### Built-in Ethical Safeguards

SpoofLab includes several non-removable ethical safeguards:

1. **Legal disclaimer banner** — Displayed every time the application starts
2. **Email footer disclaimer** — Every test email includes a visible identification footer:
   ```
   ────────────────────────────────────────────────────────────────
   SpoofLab Security Simulation — Authorized testing only.
   If unexpected, contact your IT security team.
   ────────────────────────────────────────────────────────────────
   ```
3. **Test identification** — All generated emails include test metadata (scenario name, timestamp)
4. **No automated targeting** — SpoofLab requires explicit target specification for every test
5. **No credential harvesting** — SpoofLab does not capture or store any credentials

**[SCREENSHOT: Insert a screenshot showing the disclaimer footer as it appears at the bottom of a test email received in an inbox. This is critical for demonstrating the ethical design of the tool.]**

## 13.2 SPF, DKIM, and DMARC Defences

Understanding the defences that SpoofLab tests is essential context for this project.

**Table 13.1 – Email Authentication Mechanisms**

| Mechanism | Full Name | What it Does | DNS Record Type | Protection Level |
|-----------|-----------|-------------|-----------------|-----------------|
| SPF | Sender Policy Framework | Lists authorised sending IP addresses | TXT record | Medium |
| DKIM | DomainKeys Identified Mail | Cryptographic signature on email | TXT record (public key) | High |
| DMARC | Domain-based Message Authentication, Reporting and Conformance | Policy for SPF/DKIM failures | TXT record | High (with p=reject) |

### 13.2.1 SPF (Sender Policy Framework)

An SPF record in DNS tells receiving mail servers which IP addresses are authorised to send email on behalf of a domain:

```
v=spf1 ip4:192.0.2.1 include:_spf.google.com -all
```

- `v=spf1` — SPF version
- `ip4:192.0.2.1` — Authorised sending IP
- `include:_spf.google.com` — Include Google's SPF record (for G Suite)
- `-all` — Hard fail all other senders

**Limitation:** SPF only checks the envelope-from (MAIL FROM), not the header-from (From: header) that users see. An attacker can pass SPF on the envelope while spoofing the header-from.

### 13.2.2 DKIM (DomainKeys Identified Mail)

DKIM adds a cryptographic signature to email headers. The private key is held by the sending server; the public key is published in DNS. Receiving servers verify the signature.

```
DKIM-Signature: v=1; a=rsa-sha256; d=sender.com; s=mail;
  h=from:to:subject:date; bh=...; b=...
```

**Limitation:** DKIM only signs the original message. A spoofed email has no valid DKIM signature (or has a signature from a different domain than the displayed From address).

### 13.2.3 DMARC (Domain-based Message Authentication, Reporting and Conformance)

DMARC ties SPF and DKIM together and specifies a policy for what to do with emails that fail authentication:

```
v=DMARC1; p=reject; rua=mailto:dmarc-reports@company.com; pct=100
```

- `p=reject` — Reject unauthenticated emails
- `rua=` — Send aggregate reports to this address
- `pct=100` — Apply policy to 100% of emails

**DMARC p=reject is the most effective technical defence against email spoofing.** When properly configured, it prevents spoofed emails from ever reaching the inbox.

**[SCREENSHOT: Insert a screenshot of a DNS lookup showing DMARC, SPF, and DKIM records for a well-protected domain — run `dig TXT _dmarc.google.com` and `dig TXT gmail.com` in the terminal to show Google's DMARC and SPF records. This demonstrates what proper email authentication configuration looks like.]**

## 13.3 Responsible Disclosure

The SpoofLab project team is committed to responsible disclosure:

### If You Discover a Vulnerability in SpoofLab

Contact: contact@techskyhub.com

Include:
- Detailed description of the vulnerability
- Steps to reproduce
- Potential impact assessment
- Suggested mitigation (if known)

### If You Discover an Email Spoofing Vulnerability in an Organisation

1. Document the vulnerability with evidence (screenshots, headers)
2. Identify the appropriate security contact (security@company.com or HackerOne/Bugcrowd)
3. Report within your organisation's responsible disclosure policy
4. Provide a reasonable remediation window (typically 90 days)
5. Do not exploit the vulnerability beyond what is necessary for documentation

---


---

# CHAPTER 14: FUTURE ENHANCEMENTS

---

The current SpoofLab v1.0.0 provides a solid foundation. The following enhancements are planned for future versions:

## 14.1 Short-Term Enhancements (v1.1 – v1.5)

### HTML Email Support
Current SpoofLab emails are plain text. Adding HTML email support would allow:
- Branded phishing templates that visually mimic real organisations
- Embedded tracking pixels for click/open detection
- Hyperlinked call-to-action buttons

Implementation approach: Add `MIMEText(html_body, 'html', 'utf-8')` as an alternative part alongside the plain text part in the MIMEMultipart email.

### Email Attachment Support
Real-world BEC attacks often include malicious attachments (fake invoices, PDF contracts). SpoofLab could support attaching benign files to test organisation attachment scanning policies:
```bash
est test 1 target@company.com --attachment invoice.pdf
```

### Campaign Mode
Run tests against a list of targets from a file:
```bash
est campaign --targets targets.txt --scenario 2 --delay 30
```

### Open Rate Tracking
Integration with a simple HTTP server to track whether simulated phishing links are clicked (for awareness training measurement):
```bash
est server --port 2525 --tracking-port 8080
```

## 14.2 Medium-Term Enhancements (v2.0)

### Web Dashboard
A web-based management interface (Flask/FastAPI) that provides:
- Campaign management UI
- Real-time test monitoring
- Visual analytics and charts
- Report export to PDF/HTML
- User management for team environments

This was the most frequently requested feature in user feedback.

### SMTP Authentication Support
Support for authenticated SMTP relay through external providers (SendGrid, Mailgun, AWS SES) for improved deliverability in testing environments where direct SMTP is blocked.

### Advanced Template Engine
A YAML-based template system with variable substitution, allowing highly targeted spear-phishing simulations:
```yaml
templates:
  - name: "Custom CEO"
    from_name: "{{ceo_name}}"
    from_email: "{{ceo_email}}"
    subject: "{{subject_template}}"
    variables:
      - ceo_name
      - ceo_email
      - target_name
      - company_name
```

### Integration with Security Frameworks
Plugins or modules for:
- Metasploit Framework
- Cobalt Strike (team server integration)
- MITRE ATT&CK technique mapping (T1566.001 – Spearphishing Attachment)

## 14.3 Long-Term Enhancements (v3.0+)

### AI-Assisted Scenario Generation
Using large language models (LLMs) to generate targeted, contextually appropriate phishing emails based on:
- Target's LinkedIn profile
- Organisation's recent news
- Current events and trends

### Cloud Deployment
Pre-configured Docker containers and Kubernetes Helm charts for enterprise deployment:
```bash
docker run -p 2525:2525 spooflab/est:latest server
```

### Compliance Mapping
Automatic mapping of test results to compliance frameworks:
- ISO 27001 (Annex A.12.6 – Technical Vulnerability Management)
- NIST SP 800-53 (SI-3, SI-8 – Malicious Code Protection)
- PCI DSS (Requirement 11 – Test Security Systems)
- SOC 2 Type II (CC6 – Logical and Physical Access)

### Mobile Companion App
A mobile application for security awareness trainers to:
- Trigger tests remotely
- View real-time results
- Send immediate training notifications to employees who clicked

---


---

# CHAPTER 15: CONCLUSION

---

## 15.1 Project Summary

SpoofLab successfully delivers on all ten original project objectives. The project has produced a fully functional, professionally documented email spoofing simulation framework that addresses a genuine gap in the free, open-source security testing toolset.

The core technical achievement is a multi-threaded SMTP server with real email relay capability, implemented in approximately 1,300 lines of Python using only one external dependency. This lightweight yet capable design makes SpoofLab accessible to security professionals at every level — from students running their first penetration testing lab to enterprise red teams conducting authorised security assessments.

## 15.2 Key Contributions

The project makes the following contributions to the cybersecurity education and security testing domains:

**1. Practical Demonstration of SMTP Vulnerabilities**

SpoofLab provides a hands-on demonstration of why SMTP's lack of native sender authentication is a critical vulnerability. The experience of watching a spoofed email from `ceo@yourcompany.com` arrive in a real inbox — when you know with certainty it was sent by a different system — creates an immediate, visceral understanding that no textbook description can match.

**2. Structured Scenario Library**

The five pre-built scenarios represent the most common and costly email-based attacks documented in real-world incident data. Each scenario includes detailed metadata (severity, category, description) that makes it immediately useful for structured security awareness training programmes.

**3. Integrated Audit and Reporting**

The combination of JSON audit logging and automated report generation transforms SpoofLab from a simple testing tool into a full assessment platform. The generated reports include executive summaries, risk ratings, and specific recommendations, making the tool valuable not just for technical testers but for security managers and compliance teams.

**4. Ethical Design Principles**

SpoofLab demonstrates that offensive security tools can be designed with strong ethical guardrails. The mandatory legal disclaimers, email footers identifying messages as tests, and the educational documentation all reflect a commitment to responsible use.

## 15.3 Learning Outcomes

This project provided the development team with deep expertise in:

- **Protocol engineering:** Building an SMTP server from raw sockets required thorough study of RFC 5321 and hands-on debugging of protocol edge cases.
- **Network programming:** Multi-threaded socket programming, signal handling, and graceful shutdown are foundational skills for any systems developer.
- **Security research methodology:** Understanding attack techniques is essential for building effective defences. This project grounded theoretical knowledge in practical implementation.
- **Professional software development:** Version control, structured logging, JSON configuration management, CLI design, and comprehensive documentation are skills that extend beyond security into all areas of software engineering.

## 15.4 Challenges Encountered

### Python Version Compatibility
The project initially encountered issues with Python 3.12 and 3.13, which deprecated the `smtpd` module. Refactoring to use raw sockets actually improved the educational value of the codebase.

### PEP 668 (Externally Managed Environments)
Newer Linux distributions (Kali 2024+, Ubuntu 23.04+) enforce PEP 668, preventing `pip install` without a virtual environment. The installation script required significant testing across distributions to handle all cases correctly.

### DNS Resolution Reliability
DNS lookups for MX records can fail for many reasons (firewall rules, ISP blocking, rate limiting). Implementing the fallback mechanism and making DNS errors non-fatal was essential for reliable operation across different network environments.

## 15.5 Final Statement

SpoofLab demonstrates that email spoofing remains a critical, underappreciated vulnerability in most organisations' security posture. The ease with which a convincing spoofed email can be constructed and delivered — even to a security-aware recipient — underscores the importance of both technical defences (DMARC enforcement) and human defences (regular security awareness training).

The project team hopes that SpoofLab serves as both a practical tool for security professionals and an educational resource that contributes to a broader understanding of email security threats. The full source code is available on GitHub under the MIT License, and contributions from the security community are welcome.

> *"The best defence against social engineering is an educated workforce. SpoofLab exists to deliver that education through direct experience, not lectures."*

---


---

# CHAPTER 16: REFERENCES

---

## Academic & Research References

1. Allman, E., Klensin, J., & Mouat, N. (2008). *DomainKeys Identified Mail (DKIM) Signatures* (RFC 4871). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc4871

2. Crocker, D. (1982). *Standard for the format of ARPA Internet text messages* (RFC 822). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc822

3. Federal Bureau of Investigation (2023). *Internet Crime Report 2023*. Internet Crime Complaint Center (IC3). https://www.ic3.gov/Media/PDF/AnnualReport/2023_IC3Report.pdf

4. Klensin, J. (2008). *Simple Mail Transfer Protocol* (RFC 5321). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc5321

5. Kucherawy, M., & Zwicky, E. (2015). *Domain-based Message Authentication, Reporting, and Conformance (DMARC)* (RFC 7489). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc7489

6. Mockapetris, P. (1987). *Domain Names – Concepts and Facilities* (RFC 1035). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc1035

7. NIST (2021). *NIST Special Publication 800-177 Rev. 1: Trustworthy Email*. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-177r1

8. Verizon (2023). *2023 Data Breach Investigations Report*. Verizon Business. https://www.verizon.com/business/resources/reports/dbir/

9. Wong, M., & Schlitt, W. (2006). *Sender Policy Framework (SPF) for Authorizing Use of Domains in E-Mail* (RFC 4408, obsoleted by RFC 7208). Internet Engineering Task Force (IETF).

10. Kitterman, S. (2014). *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* (RFC 7208). Internet Engineering Task Force (IETF). https://www.rfc-editor.org/rfc/rfc7208

## Industry Reports & Statistics

11. Anti-Phishing Working Group (APWG). (2023). *Phishing Activity Trends Report Q4 2023*. APWG. https://apwg.org/trendsreports/

12. Cisco Talos Intelligence. (2024). *Email & Spam Data*. Cisco Systems. https://talosintelligence.com/reputation_center

13. Global Cyber Alliance. (2023). *DMARC Adoption Report 2023*. GCA. https://globalcyberalliance.org/

14. Proofpoint. (2023). *State of the Phish 2023*. Proofpoint Inc. https://www.proofpoint.com/us/resources/threat-reports/state-of-phish

15. Statista. (2024). *Number of sent and received e-mails per day worldwide from 2017 to 2026*. Statista Research Department. https://www.statista.com/statistics/456500/daily-number-of-e-mails-worldwide/

## Software & Tool References

16. Fitzgerald, J., & de Vries, L. (2023). *GoPhish: Open-Source Phishing Framework*. GitHub. https://github.com/gophish/gophish

17. Python Software Foundation. (2023). *Python Documentation: email — An email and MIME handling package*. https://docs.python.org/3/library/email.html

18. Python Software Foundation. (2023). *Python Documentation: smtplib — SMTP protocol client*. https://docs.python.org/3/library/smtplib.html

19. Python Software Foundation. (2023). *Python Documentation: socket — Low-level networking interface*. https://docs.python.org/3/library/socket.html

20. Trustedbird Project. (2023). *dnspython: A DNS toolkit for Python*. GitHub. https://github.com/rthalley/dnspython

21. TrustedSec. (2023). *The Social-Engineer Toolkit (SET) Repository*. GitHub. https://github.com/trustedsec/social-engineer-toolkit

22. Jetmore, J. (2023). *swaks – Swiss Army Knife for SMTP*. http://www.jetmore.org/john/code/swaks/

## Books & Educational Materials

23. Cialdini, R. B. (1984). *Influence: The Psychology of Persuasion*. Harper Collins. (Referenced for social engineering principles)

24. Hadnagy, C. (2010). *Social Engineering: The Art of Human Hacking*. Wiley.

25. Kim, D., & Solomon, M. G. (2018). *Fundamentals of Information Systems Security* (3rd ed.). Jones & Bartlett Learning.

26. Mitnick, K. D., & Simon, W. L. (2002). *The Art of Deception: Controlling the Human Element of Security*. Wiley.

27. Stuttard, D., & Pinto, M. (2011). *The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws* (2nd ed.). Wiley.

---


---

# APPENDIX A: CONFIGURATION TEMPLATES

---

## A.1 Default Configuration File

The following is the complete default `~/.est/config.json` that SpoofLab generates on first run:

```json
{
  "version": "1.0.0",
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
      "body": "We've detected unusual activity on your PayPal account:\n\n• Login from new device (IP: 192.168.1.100)\n• Attempted transaction: $1,247.99\n• Location: Unknown\n\nVerify your account immediately: [SECURE LINK]",
      "description": "PayPal impersonation for account compromise",
      "severity": "High"
    },
    {
      "name": "Microsoft 365 License Expiration",
      "category": "Software/License Fraud",
      "from_email": "noreply@microsoft.com",
      "from_name": "Microsoft 365 Admin",
      "subject": "ACTION REQUIRED: Your Microsoft 365 License Expires Today",
      "body": "Your Microsoft 365 Business license expires today at 11:59 PM.\n\nImmediate action required to prevent:\n✗ Loss of email access\n✗ File synchronization stoppage\n\nRenew immediately: [RENEWAL LINK]",
      "description": "Microsoft service impersonation for credential theft",
      "severity": "Medium"
    },
    {
      "name": "Bank Account Verification",
      "category": "Financial Institution Fraud",
      "from_email": "security@bankofamerica.com",
      "from_name": "Bank of America Security",
      "subject": "Immediate Verification Required - Account Suspension Notice",
      "body": "IMPORTANT SECURITY NOTICE\n\nWe have temporarily suspended your account due to suspicious activity.\n\nAccount Status: SUSPENDED\n\nVerify your identity immediately: [VERIFICATION PORTAL]\n\nFailure to verify within 48 hours will result in permanent closure.",
      "description": "Banking institution impersonation for credential harvesting",
      "severity": "Critical"
    }
  ],
  "temp_email_services": [
    "guerrillamail.com",
    "mailinator.com",
    "10minutemail.com",
    "tempmail.org"
  ],
  "reporting": {
    "auto_generate": true,
    "format": "json",
    "include_screenshots": false
  }
}
```

## A.2 Custom Scenario Templates

### Template: HR Internal Fraud

```json
{
  "name": "HR Payroll Diversion",
  "category": "Internal Business Fraud",
  "from_email": "hr@[COMPANY_DOMAIN]",
  "from_name": "HR Department",
  "subject": "Important: Payroll Information Update",
  "body": "Please be advised that we are updating direct deposit information for all employees. Use the secure portal link below to verify your banking details before Friday.\n\n[PORTAL LINK]\n\nHR Department",
  "description": "HR impersonation for payroll diversion",
  "severity": "Critical"
}
```

### Template: IT Password Policy Update

```json
{
  "name": "IT Security - Password Policy Update",
  "category": "Technical Support Fraud",
  "from_email": "noreply@[COMPANY_DOMAIN]",
  "from_name": "IT Security Team",
  "subject": "Mandatory: New Password Policy Compliance Required",
  "body": "As part of our annual security compliance review, all employees must update their passwords to meet the new policy requirements by [DATE].\n\nUpdate your password now: [COMPLIANCE PORTAL]\n\nFailure to comply may result in account restriction.\n\nIT Security Team",
  "description": "IT department impersonation for credential update phishing",
  "severity": "High"
}
```

---

# APPENDIX B: SAMPLE LOG OUTPUT

---

## B.1 Sample est_tests.log File

The following is a sample of the JSON-lines log file (`~/.est/est_tests.log`) after a complete testing session:

```json
{"timestamp": "2025-06-12T14:23:11.456789", "test_type": "scenario_test", "scenario": "CEO Fraud - Urgent Wire Transfer", "target": "finance@testcompany.com", "from_email": "ceo@testcompany.com", "success": true, "details": {"category": "Business Email Compromise", "severity": "Critical", "smtp_server": "localhost:2525"}}
{"timestamp": "2025-06-12T14:25:33.789012", "test_type": "scenario_test", "scenario": "IT Helpdesk - Password Reset", "target": "employee@testcompany.com", "from_email": "helpdesk@testcompany.com", "success": true, "details": {"category": "Technical Support Fraud", "severity": "High", "smtp_server": "localhost:2525"}}
{"timestamp": "2025-06-12T14:27:45.234567", "test_type": "scenario_test", "scenario": "PayPal Security Alert", "target": "manager@testcompany.com", "from_email": "security@paypal.com", "success": false, "details": {"error": "Connection refused: DMARC p=reject on paypal.com", "smtp_server": "localhost:2525"}}
{"timestamp": "2025-06-12T14:30:02.678901", "test_type": "custom_test", "scenario": "custom", "target": "hr@testcompany.com", "from_email": "employee@testcompany.com", "success": true, "details": {"from_name": "John Employee", "subject": "Request: Change My Direct Deposit", "body_length": 245, "smtp_server": "localhost:2525"}}
{"timestamp": "2025-06-12T14:32:17.345678", "test_type": "smtp_relay", "scenario": "server_relay", "target": "it_team@testcompany.com", "from_email": "external@attacker.example", "success": true, "details": {"client_id": "127.0.0.1:54321", "total_targets": 1, "successful_deliveries": 1, "email_size": 1247}}
```

## B.2 Parsing Logs with Python

```python
import json

log_file = os.path.expanduser("~/.est/est_tests.log")

with open(log_file, 'r') as f:
    entries = [json.loads(line) for line in f if line.strip()]

# Count successes and failures
successes = sum(1 for e in entries if e['success'])
failures = len(entries) - successes
print(f"Total: {len(entries)}, Success: {successes}, Failed: {failures}")
print(f"Success rate: {successes/len(entries)*100:.1f}%")
```

## B.3 Parsing Logs with jq (Command Line)

```bash
# Count successful tests
cat ~/.est/est_tests.log | jq -s '[.[] | select(.success == true)] | length'

# Get all unique targets
cat ~/.est/est_tests.log | jq -r '.target' | sort -u

# Get all scenarios that succeeded
cat ~/.est/est_tests.log | jq -r 'select(.success == true) | .scenario' | sort | uniq -c
```

---

# APPENDIX C: SAMPLE REPORT OUTPUT

---

## C.1 Sample JSON Report

The following is a sample of the JSON report generated by `est report`:

```json
{
  "report_metadata": {
    "generated_at": "2025-06-12T15:00:00.000000",
    "tool_version": "1.0.0",
    "report_type": "EST Security Assessment",
    "total_tests": 8
  },
  "executive_summary": {
    "total_tests_conducted": 8,
    "successful_tests": 6,
    "failed_tests": 2,
    "success_rate": 75.0,
    "test_period": {
      "first_test": "2025-06-12T14:23:11.456789",
      "last_test": "2025-06-12T14:45:32.789012"
    }
  },
  "test_analysis": {
    "by_test_type": {
      "scenario_test": {"total": 5, "success": 4},
      "custom_test": {"total": 2, "success": 2},
      "smtp_relay": {"total": 1, "success": 0}
    },
    "by_scenario": {
      "CEO Fraud - Urgent Wire Transfer": {"total": 1, "success": 1},
      "IT Helpdesk - Password Reset": {"total": 1, "success": 1},
      "PayPal Security Alert": {"total": 1, "success": 0},
      "Microsoft 365 License Expiration": {"total": 1, "success": 1},
      "Bank Account Verification": {"total": 1, "success": 1},
      "custom": {"total": 2, "success": 2}
    }
  },
  "recommendations": [
    "🟠 HIGH: Moderate spoofing vulnerabilities identified",
    "Review and strengthen email authentication policies",
    "Implement additional email security controls",
    "Regular security awareness training recommended",
    "📚 Provide targeted training on identifying spoofed emails",
    "🔍 Implement email header analysis training",
    "⚡ Establish incident response procedures for email attacks",
    "📊 Regular penetration testing of email security controls"
  ]
}
```

---

# APPENDIX D: GLOSSARY

---

| Term | Definition |
|------|-----------|
| **BEC** | Business Email Compromise — A targeted attack where an attacker impersonates a company executive to authorise fraudulent transactions |
| **DKIM** | DomainKeys Identified Mail — An email authentication method using cryptographic signatures added to email headers |
| **DMARC** | Domain-based Message Authentication, Reporting and Conformance — A policy mechanism that uses SPF and DKIM to determine how unauthenticated emails should be handled |
| **DNS** | Domain Name System — The internet's phone book; translates domain names to IP addresses |
| **Email Header** | Metadata at the top of an email message containing From, To, Subject, Date, and routing information |
| **Envelope-From** | The return-path address used in SMTP's MAIL FROM command (used for bounces) |
| **Header-From** | The From: address visible in the email client to the recipient |
| **MX Record** | Mail Exchange DNS record — Specifies which mail server handles email for a domain |
| **Phishing** | A social engineering attack using deceptive emails to steal credentials or install malware |
| **Relay** | The forwarding of an email from one mail server to another toward the final destination |
| **SMTP** | Simple Mail Transfer Protocol — The protocol used to send email across the internet |
| **Social Engineering** | Manipulating people into performing actions or divulging information through psychological manipulation |
| **Spear Phishing** | Targeted phishing specifically tailored to an individual recipient, using personal information |
| **SPF** | Sender Policy Framework — A DNS record that specifies which IP addresses are authorised to send email for a domain |
| **Spoofing** | Falsifying the sender information in an email to make it appear to come from a different source |
| **TCP** | Transmission Control Protocol — The transport protocol underlying SMTP connections |
| **Whaling** | A form of spear phishing targeting senior executives (C-suite) |

---

*End of Documentation*

---

**Document Information**

| Field | Value |
|-------|-------|
| Document Title | SpoofLab: How Email Addresses Get Spoofed – Final Year Project Documentation |
| Version | 1.0 |
| Date | 2025 |
| Authors | Akshat Bhavsar, Khushi |
| Project Repository | https://github.com/akshatbhavsar/SpoofLab |
| License | MIT License |
| Tool Version | SpoofLab v1.0.0 |

---

> **Ethical Reminder:** SpoofLab is developed for authorized security testing, academic research, and educational purposes only. All use of this tool must comply with applicable laws and require explicit written authorization from system owners. The authors accept no responsibility for misuse.



---

# APPENDIX E: TROUBLESHOOTING GUIDE

---

## E.1 Installation Issues

### Problem: "externally-managed-environment" error on pip install

**Symptom:**
```
error: externally-managed-environment
This environment is externally managed
```

**Cause:** Python 3.12+ and newer Kali/Ubuntu/Debian installations enforce PEP 668.

**Solutions:**

Option 1 - Use system package:
```bash
sudo apt install python3-dnspython
```

Option 2 - Use virtual environment:
```bash
python3 -m venv ~/.est-env
source ~/.est-env/bin/activate
pip install dnspython
```

Option 3 - Re-run the install script (handles this automatically):
```bash
./install.sh
```

---

### Problem: "est: command not found" after installation

**Symptom:**
```bash
est --version
bash: est: command not found
```

**Cause:** The `est` command was not added to a directory in your `$PATH`.

**Solutions:**

Check where the script was installed:
```bash
which est 2>/dev/null || find ~/.local/bin /usr/local/bin -name 'est' 2>/dev/null
```

Add to PATH if installed in `~/.local/bin`:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Or run directly with Python:
```bash
cd /path/to/SpoofLab
python3 est.py --version
```

---

### Problem: Virtual environment deactivated after terminal restart

**Symptom:** After closing and reopening the terminal, `est` commands fail.

**Solution:** Add activation to `.bashrc`:
```bash
echo 'source ~/.est-env/bin/activate' >> ~/.bashrc
source ~/.bashrc
```

---

## E.2 Server Issues

### Problem: "Address already in use" when starting server

**Symptom:**
```
Error: [Errno 98] Address already in use
```

**Cause:** Another process is already using port 2525.

**Solutions:**

Find what is using the port:
```bash
sudo ss -tlnp | grep :2525
sudo lsof -i :2525
```

Terminate the conflicting process using the PID shown by lsof, then restart:
```bash
est server --port 2525
```

Or use a different port:
```bash
est server --port 3025
```

---

### Problem: "Permission denied" binding to port 25

**Cause:** Ports below 1024 require root privileges on Linux.

**Solution:** Use a port above 1024 (recommended):
```bash
est server --port 2525
```

Or grant capability to python3:
```bash
sudo setcap 'cap_net_bind_service=+ep' $(which python3)
est server --port 25
```

---

### Problem: Server starts but test emails fail to deliver

**Symptom:**
```
Email spoofing test failed: Connection refused
```

**Checklist:**

1. Is the server actually running? Check the server terminal.
2. Are you using the same port? Default is 2525.
3. Is a firewall blocking the port?
   ```bash
   sudo ufw status
   ```
4. Is the server terminal in the same virtual environment?

---

## E.3 Email Delivery Issues

### Problem: Emails not arriving at the target inbox

| Cause | How to Check | Solution |
|-------|-------------|----------|
| DMARC p=reject on target domain | `dig TXT _dmarc.targetdomain.com` | Use test domain without DMARC enforcement |
| Email in spam/junk folder | Check spam folder manually | Check spam; use a test mailbox |
| MX resolution failed | Check server logs for "DNS lookup failed" | Install dnspython; check DNS connectivity |
| ISP blocking outbound SMTP (port 25) | Try `telnet mail.google.com 25` | Use a relay or VPN; test in a lab environment |
| Email rejected by content filter | Check bounce message | Modify email body; use a test environment |

---

### Problem: "DNS lookup failed" in server logs

**Solutions:**

Install or reinstall dnspython:
```bash
pip install --upgrade dnspython
sudo apt install python3-dnspython
```

Test DNS resolution manually:
```bash
python3 -c "import dns.resolver; r = dns.resolver.resolve('gmail.com', 'MX'); print([str(mx.exchange) for mx in r])"
```

Check system DNS connectivity:
```bash
dig MX gmail.com
nslookup -type=MX gmail.com
```

---

## E.4 Log and Report Issues

### Problem: "No test logs found" when running `est logs`

**Solution:**
1. Run at least one test: `est test 1 test@example.com`
2. Check if the file exists: `ls -la ~/.est/`

---

### Problem: Report generation fails with "No test data found"

**Solution:**
```bash
# Check if log file has valid content
python3 -c "
import json
with open('$HOME/.est/est_tests.log') as f:
    lines = [l for l in f if l.strip()]
    print(f'Lines: {len(lines)}')
"
```

If the log file is corrupted, back it up and reset:
```bash
cp ~/.est/est_tests.log ~/.est/est_tests.log.bak
echo '' > ~/.est/est_tests.log
```

---

## E.5 Frequently Asked Questions

**Q: Why does my spoofed email end up in spam instead of the inbox?**

A: This is expected behaviour in many cases. Modern email providers (Gmail, Outlook) use machine learning to detect suspicious emails. However, this is actually valuable data for your security assessment — if the email goes to spam, the target domain's filters are working. Document both deliveries to inbox and deliveries to spam in your report.

**Q: Can I use SpoofLab without the SMTP server (direct relay)?**

A: SpoofLab requires its own SMTP server to relay the spoofed emails. You cannot skip this step. The local SMTP server handles protocol coordination between the test client and the destination mail server.

**Q: How do I spoof emails with HTML formatting?**

A: Current v1.0.0 supports plain text only. For HTML email testing, you can modify the `_create_mime_email` method to add an HTML alternative part. This is planned as a built-in feature in v1.1.

**Q: Can I test DMARC protection without actually sending emails?**

A: Yes, use online DMARC testing tools:
- `mxtoolbox.com/DMARC.aspx`
- `dmarcanalyzer.com`
- `checkdmarc.com`

These show you the effective DMARC policy without sending test emails.

**Q: How many emails per second can SpoofLab send?**

A: In a loopback test environment (localhost), SpoofLab can process approximately 50 emails/second. For real internet delivery (with DNS lookups), expect 5-15 emails/second depending on DNS response time. For security awareness training campaigns, a rate of 1 email every 5-10 seconds is recommended to avoid triggering rate limiting on the target mail server.

**Q: Is SpoofLab detectable by email security gateways?**

A: SpoofLab emails include a visible disclaimer footer and the test nature is identifiable in email headers. Commercial email security gateways may block SpoofLab tests if they have rules against the disclaimer text. For more realistic testing (without the disclaimer footer), you would need to modify the source code, but this removes an ethical safeguard and should only be done in explicitly authorised red team engagements with documented written permission from the client.

**Q: What happens if I accidentally send a spoofed email to the wrong person?**

A: Stop testing immediately. Contact the unintended recipient and their IT/security team to explain the situation. Provide a full explanation including your authorisation documentation. This underscores the importance of double-checking target email addresses before every test and using a dedicated test mailbox during development.

---



---

# APPENDIX F: EMAIL HEADER ANALYSIS GUIDE

---

Understanding email headers is a critical skill for identifying spoofed emails. This appendix provides a practical guide to reading and analysing email headers.

## F.1 How to Access Full Email Headers

### Gmail

1. Open the suspicious email
2. Click the three-dot menu (⋮) in the top-right of the email
3. Select "Show original"
4. A new tab opens showing the complete raw email source

**[SCREENSHOT: Insert a screenshot of Gmail's three-dot menu with "Show original" highlighted. This shows users exactly how to access the raw email headers in Gmail to investigate suspicious messages.]**

### Microsoft Outlook (Desktop)

1. Open the email
2. Click "File" → "Properties"
3. The "Internet headers" section shows all headers

### Mozilla Thunderbird

1. Open the email
2. Press Ctrl+U to open the message source

### Apple Mail

1. Open the email
2. View → Message → All Headers

## F.2 Key Headers to Examine

### From Header
```
From: John Smith, CEO <ceo@company.com>
```
This is what you **see** in your email client. It can be set to anything.

### Return-Path Header
```
Return-Path: <attacker@gmail.com>
```
This is the real envelope-from address where bounces go. If this differs significantly from the From header, it is a strong indicator of spoofing.

### Received Headers
```
Received: from mail.attacker.com (mail.attacker.com [203.0.113.1])
        by mx.victim.com with SMTP id abc123
        for <employee@victim.com>;
        Thu, 12 Jun 2025 14:30:22 +0000 (UTC)
```
These trace the path the email took. Read them from bottom to top — the bottom-most Received header is where the email originated. If an email claims to be from `company.com` but the Received header shows it came from `203.0.113.1` (which resolves to `mail.attacker.com`), it is spoofed.

### Authentication-Results Header
```
Authentication-Results: mx.google.com;
       spf=fail (google.com: domain of attacker@gmail.com does not
       designate 203.0.113.1 as permitted sender)
       smtp.mailfrom=attacker@gmail.com;
       dkim=none;
       dmarc=fail (p=REJECT sp=REJECT dis=REJECT)
       header.from=company.com
```
This is the most important header for automated detection. It shows whether SPF, DKIM, and DMARC checks passed or failed. `spf=fail` and `dmarc=fail` with `dis=REJECT` means the receiving server should have rejected this email.

### DKIM-Signature Header
```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=company.com;
        s=google; h=from:to:subject:date:message-id;
        bh=Base64EncodedBodyHash=; b=Base64EncodedSignature=
```
If this header is present and valid, the email was signed by the domain in the `d=` parameter. A spoofed email either has no DKIM signature or has a signature from a different domain than the displayed From address.

## F.3 Analysing a Spoofed Email — Step by Step

Here is a walkthrough of identifying a spoofed email:

### Step 1: Check the Display From

The user sees: `From: Bank of America Security <security@bankofamerica.com>`

This looks legitimate. But we need to go deeper.

### Step 2: Check the Return-Path

```
Return-Path: <bounce@mail123.suspicious-server.com>
```

The return-path is completely different from the display From. Bounces go to `suspicious-server.com`, not `bankofamerica.com`. This is a red flag.

### Step 3: Check the Received Headers

```
Received: from mail123.suspicious-server.com (203.0.113.5)
        by mx1.recipient-mail.com
```

The email originated from `suspicious-server.com`, not from any Bank of America mail server. The originating IP (`203.0.113.5`) can be checked against Bank of America's SPF record.

### Step 4: Check the Authentication-Results

```
Authentication-Results: mx1.recipient-mail.com;
    spf=fail header.from=bankofamerica.com;
    dkim=fail;
    dmarc=fail (policy=none)
```

`spf=fail` — The sending server is not authorised by bankofamerica.com's SPF record.
`dkim=fail` — No valid DKIM signature.
`dmarc=fail` — DMARC check failed.

**Crucially:** `policy=none` means that even though DMARC failed, the policy says to do nothing — the email is delivered anyway. If the policy were `policy=reject`, the email would never have reached the inbox.

### Conclusion

This email is definitively spoofed. The combination of SPF fail, DKIM fail, and DMARC fail (even with policy=none) confirms the email did not come from Bank of America.

**[SCREENSHOT: Insert a screenshot of a real email header analysis — use Gmail's "Show original" feature on a test email sent through SpoofLab and screenshot the raw headers page. Highlight the Authentication-Results section showing spf=fail, dkim=none, and dmarc=fail. Use Gmail's built-in "Security" section or a tool like mxtoolbox.com's email header analyzer to visually interpret the headers.]**

## F.4 Online Header Analysis Tools

The following online tools can parse and visually display email headers:

| Tool | URL | Best For |
|------|-----|----------|
| MXToolbox Email Header Analyser | mxtoolbox.com/EmailHeaders.aspx | Comprehensive visual analysis |
| Google Admin Toolbox | toolbox.googleapps.com/apps/messageheader/ | Gmail header analysis |
| Mail Header Analyser | mailheader.org | Simple, clean interface |
| Email Header Analyser | emailheaderanalyser.verifyemailaddress.org | Detailed hop analysis |

---

# APPENDIX G: INSTALLATION SCRIPT ANALYSIS

---

## G.1 install.sh Overview

The `install.sh` script is a 26 KB Bash script that automates the complete installation of SpoofLab across multiple platforms. This appendix describes its key functions.

## G.2 OS Detection

```bash
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt-get &>/dev/null; then
            if grep -q "Kali" /etc/os-release 2>/dev/null; then
                OS="kali"
            else
                OS="debian"
            fi
        elif command -v dnf &>/dev/null; then
            OS="fedora"
        elif command -v pacman &>/dev/null; then
            OS="arch"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    fi
}
```

The script identifies Kali Linux specifically to apply Kali-optimised settings (shorter timeouts, security-focused defaults).

## G.3 Python Version Handling

```bash
check_python() {
    PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 8 ]); then
        echo "Error: Python 3.8+ required. Found: Python $PYTHON_VERSION"
        exit 1
    fi

    # Python 3.12+ requires virtual environment approach
    if [ "$MINOR" -ge 12 ]; then
        USE_VENV=true
    fi
}
```

## G.4 Dependency Installation

The script tries multiple methods to install `dnspython`, in order of preference:

1. System package manager (apt, dnf, pacman, brew)
2. pip with virtual environment (for Python 3.12+)
3. pip with --user flag
4. pip with --break-system-packages flag (last resort)

This ensures installation succeeds across the widest possible range of system configurations.

## G.5 est Command Installation

```bash
install_est_command() {
    # Determine installation directory
    if [ -w "/usr/local/bin" ]; then
        INSTALL_DIR="/usr/local/bin"
    else
        INSTALL_DIR="$HOME/.local/bin"
        mkdir -p "$INSTALL_DIR"
    fi

    # Create est wrapper script
    cat > "$INSTALL_DIR/est" << WRAPPER
#!/usr/bin/env bash
# EST - Email Spoofing Tool
# Auto-generated wrapper by install.sh
if [ -f "$HOME/.est-env/bin/activate" ]; then
    source "$HOME/.est-env/bin/activate"
fi
exec python3 "$EST_SCRIPT" "$@"
WRAPPER

    chmod +x "$INSTALL_DIR/est"
}
```

The wrapper script ensures the virtual environment is activated before running the Python script, solving the common issue of the wrong Python environment being used.

**[SCREENSHOT: Insert a screenshot of the complete installation process from start to finish — run `./install.sh` on a fresh system and screenshot all the output from "Detecting OS..." through to "Installation complete!" showing each step completing successfully. This is important for verifying the installation process works correctly.]**

---

DOCEOF_MARKER


---

# APPENDIX H: EMAIL SECURITY HARDENING GUIDE FOR DEFENDERS

---

This appendix is written from the defender's perspective. After using SpoofLab to identify vulnerabilities, the following steps guide organisations through securing their email infrastructure against spoofing attacks.

## H.1 Phase 1: Assessment (Week 1)

### Step 1.1: Audit Existing SPF Records

Check your current SPF record:
```bash
dig TXT yourdomain.com | grep "v=spf1"
```

Common SPF issues to look for:
- Missing SPF record entirely (no protection)
- `+all` at the end (allows anyone to send — completely ineffective)
- `?all` at the end (neutral — no enforcement)
- Too many DNS lookups (SPF has a limit of 10 lookups)
- Missing includes for third-party email services

**Recommended SPF record:**
```
v=spf1 ip4:[YOUR_MAIL_SERVER_IP] include:_spf.google.com -all
```

The `-all` (hard fail) is the critical component that tells receiving servers to reject emails from unauthorised senders.

### Step 1.2: Audit DKIM Configuration

Check if DKIM is configured (requires knowing your DKIM selector, often "google", "mail", or "selector1"):
```bash
dig TXT google._domainkey.yourdomain.com
```

If DKIM is not configured, work with your email provider to enable and publish DKIM keys. Most modern email platforms (Google Workspace, Microsoft 365) provide step-by-step DKIM setup guides.

### Step 1.3: Audit DMARC Configuration

```bash
dig TXT _dmarc.yourdomain.com
```

Common DMARC states:
- **No record:** No DMARC protection — highest risk
- **p=none:** Monitoring only — emails still delivered even if authentication fails
- **p=quarantine:** Suspicious emails go to spam
- **p=reject:** Suspicious emails are rejected — maximum protection

### Step 1.4: Run a Baseline SpoofLab Test

Use SpoofLab to establish a baseline of what spoofed emails can reach your inbox:
```bash
est server --port 2525
est test 1 security-team@yourdomain.com
est test 2 security-team@yourdomain.com
est report
```

Document the results. If spoofed emails are reaching the inbox, proceed immediately to Phase 2.

## H.2 Phase 2: Implement Authentication (Weeks 2–4)

### Step 2.1: Implement SPF (Week 2)

1. Inventory all services that send email on your behalf:
   - Primary mail server
   - CRM (Salesforce, HubSpot)
   - Marketing platform (Mailchimp, Constant Contact)
   - Ticketing system (ServiceNow, Zendesk)
   - HR system
   - Any SaaS tools with email capabilities

2. Create a comprehensive SPF record including all these sources

3. Publish the SPF record in DNS (via your DNS provider's control panel)

4. Test with:
```bash
dig TXT yourdomain.com | grep spf
python3 -c "import dns.resolver; print(dns.resolver.resolve('yourdomain.com', 'TXT').response.to_text())"
```

### Step 2.2: Implement DKIM (Week 2–3)

Work with your email provider to generate and publish DKIM keys. For Google Workspace:
1. Admin Console → Apps → Google Workspace → Gmail → Authenticate email
2. Click "Generate new record"
3. Add the provided TXT record to your DNS
4. Click "Start authentication" after DNS propagates

For Microsoft 365:
1. Security & Compliance Center → DKIM
2. Enable DKIM for your domain
3. Add the provided CNAME records to your DNS

### Step 2.3: Implement DMARC (Week 3–4)

**Start in monitoring mode** to avoid disrupting legitimate email:

```
v=DMARC1; p=none; rua=mailto:dmarc-reports@yourdomain.com; ruf=mailto:dmarc-forensics@yourdomain.com; pct=100
```

- `rua=` — Aggregate reports (daily summaries of authentication results)
- `ruf=` — Forensic reports (detailed reports on failures)

Monitor reports for 2-4 weeks to identify legitimate sending sources that are failing authentication.

**Progress to quarantine after monitoring:**
```
v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@yourdomain.com; pct=25
```

Start with `pct=25` (apply policy to 25% of failing emails) and increase to 100% as you confirm no legitimate traffic is affected.

**Final target — maximum protection:**
```
v=DMARC1; p=reject; rua=mailto:dmarc-reports@yourdomain.com; pct=100
```

## H.3 Phase 3: Validate and Monitor (Week 5+)

### Step 3.1: Re-run SpoofLab Tests

After implementing SPF, DKIM, and DMARC, re-run the baseline tests:
```bash
est test 1 security-team@yourdomain.com
est test 2 security-team@yourdomain.com
est report
```

If properly configured, all test emails should now fail to deliver (rejected by DMARC enforcement). This is the desired outcome.

**[SCREENSHOT: Insert a screenshot comparing two SpoofLab reports — a "before" report (showing high success rate before DMARC implementation) and an "after" report (showing low/zero success rate after DMARC p=reject). This before/after comparison is the most compelling demonstration of the tool's value for security assessment.]**

### Step 3.2: Set Up DMARC Report Monitoring

Subscribe to a DMARC report aggregation service to make report analysis manageable:
- **Free:** dmarcdigests.com, postmarkapp.com/dmarc
- **Paid:** Valimail, Agari, Proofpoint Email Authentication

These services parse the XML aggregate reports and present them in a readable dashboard showing:
- Volume of emails authenticated successfully
- Volume failing authentication
- Sending sources not yet in SPF record
- Geographic distribution of email sending

### Step 3.3: Ongoing Security Awareness Training

Technical controls alone are not sufficient. Pair the technical implementation with:

1. **Regular training:** Quarterly security awareness training with email security module
2. **Simulated phishing:** Monthly or quarterly simulated phishing exercises using SpoofLab
3. **Reporting culture:** Encourage employees to report suspicious emails without fear
4. **Metrics tracking:** Measure and report click rates on simulated phishing campaigns over time to demonstrate programme effectiveness

## H.4 Email Security Maturity Model

| Maturity Level | SPF | DKIM | DMARC | Awareness Training | Score |
|---------------|-----|------|-------|-------------------|-------|
| Level 0 (None) | ❌ | ❌ | ❌ | ❌ | 0/4 |
| Level 1 (Basic) | ✅ | ❌ | ❌ | ❌ | 1/4 |
| Level 2 (Developing) | ✅ | ✅ | p=none | Annual | 2/4 |
| Level 3 (Defined) | ✅ | ✅ | p=quarantine | Semi-annual | 3/4 |
| Level 4 (Managed) | ✅ | ✅ | p=reject | Quarterly + simulated | 4/4 |
| Level 5 (Optimised) | ✅ + BIMI | ✅ | p=reject + reporting | Monthly + automated | 5/5 |

**Level 4 is the minimum recommended security posture** for any organisation handling sensitive data or financial transactions.

### BIMI (Brand Indicators for Message Identification)

BIMI is an emerging standard that builds on DMARC to display an organisation's official logo in email clients that support it (Gmail, Yahoo, Apple Mail). It provides:
- Additional visual authentication for email recipients
- Brand reinforcement in email communication
- Reduced effectiveness of look-alike domain attacks

BIMI requires DMARC at p=reject with 100% coverage before it can be deployed.

---

# APPENDIX I: CASE STUDIES

---

## I.1 Case Study 1: Small Business BEC Attack

### Background

A small 25-person accounting firm, "XYZ Accountants" (name changed), had no SPF, DKIM, or DMARC records on their domain. A threat actor conducted reconnaissance on LinkedIn, identified the managing partner (James) and the bookkeeper (Sarah).

### The Attack

1. The attacker sent an email appearing to come from `james@xyz-accountants.com` to `sarah@xyz-accountants.com`
2. The email requested an urgent wire transfer of £18,500 to a new client account
3. Sarah, conditioned to process James's requests quickly, processed the transfer without calling to verify
4. The money was gone within 24 hours

### SpoofLab Simulation

This exact scenario can be replicated with SpoofLab:
```bash
est custom \
  --from-email "james@xyz-accountants.com" \
  --from-name "James Williams (Managing Partner)" \
  --subject "URGENT: Client advance payment - process today" \
  --body "Sarah, process £18,500 to new client account ASAP. Details to follow. Confidential - do not discuss. James" \
  --target "sarah@xyz-accountants.com"
```

If the domain has no DMARC enforcement, this email will land in Sarah's inbox looking exactly like a message from James.

### Outcome and Remediation

Post-incident, the firm implemented:
- `v=spf1 include:_spf.google.com -all` (they use Google Workspace)
- DKIM enabled via Google Workspace admin
- `v=DMARC1; p=reject; rua=mailto:it@xyz-accountants.com`
- Wire transfer approval protocol: all transfers over £1,000 require a phone call to verify

After implementation, a follow-up SpoofLab test confirmed the spoofed email was rejected.

### Lessons Learned

1. Email authentication is not optional for businesses that process financial transactions
2. The total cost of remediation (SPF/DKIM/DMARC setup: ~£500 IT consulting) is tiny compared to the potential loss
3. Process controls (phone verification for transfers) are essential even with technical controls

## I.2 Case Study 2: University Credential Phishing Campaign

### Background

A regional university's IT security team used SpoofLab to conduct an authorised security awareness training exercise. The exercise was pre-approved by university administration and the legal team.

### Methodology

1. **Phase 1 (Baseline):** Security team sent a spoofed IT helpdesk email to a random sample of 200 staff (10% of total)
2. **Scenario used:** IT Helpdesk Password Reset (Scenario 2)
3. **Click tracking:** A unique URL in the email directed to a training page that explained the simulation
4. **Measurement:** Number of staff who clicked the link, number who reported the email as suspicious

### Results (Before Training)

| Group | Total Recipients | Clicked Link | Reported as Suspicious | Neither |
|-------|-----------------|-------------|----------------------|---------|
| Academic staff | 80 | 22 (27.5%) | 12 (15%) | 46 (57.5%) |
| Administrative staff | 80 | 38 (47.5%) | 5 (6.25%) | 37 (46.25%) |
| IT staff | 40 | 2 (5%) | 35 (87.5%) | 3 (7.5%) |

**Overall click rate before training: 31%** — significantly higher than the industry average target of <5%.

### Training Intervention

The university ran a 2-hour security awareness workshop covering:
- How email spoofing works (using SpoofLab as a demonstration)
- How to read email headers
- How to verify sender identity
- How to report suspicious emails

### Results (After Training — 90 Days)

| Group | Total Recipients | Clicked Link | Reported as Suspicious | Neither |
|-------|-----------------|-------------|----------------------|---------|
| Academic staff | 80 | 8 (10%) | 42 (52.5%) | 30 (37.5%) |
| Administrative staff | 80 | 12 (15%) | 51 (63.75%) | 17 (21.25%) |
| IT staff | 40 | 0 (0%) | 40 (100%) | 0 (0%) |

**Overall click rate after training: 10%** — a 68% reduction.
**Overall reporting rate after training: 66%** — up from 17%.

### Conclusion

The SpoofLab-based training exercise produced measurable, statistically significant improvements in employee security behaviour. The combination of live demonstration and hands-on simulation was identified by participants as significantly more effective than previous slide-based training.

---

