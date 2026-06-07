# threatmapper
# AAiT OWASP Top 10 Lab

## Overview

AAiT OWASP Top 10 Lab is a web-based cybersecurity training and vulnerability assessment platform developed for educational purposes at Addis Ababa Institute of Technology (AAiT).

The system combines a vulnerability scanning engine with an interactive cyber range that allows students, developers, and security analysts to understand, identify, and exploit common web application vulnerabilities in a controlled environment.

The platform is designed to bridge the gap between theoretical cybersecurity education and practical hands-on experience by providing realistic attack scenarios based on OWASP security risks.

---
 ## System Requirements

* Operating System: Linux (recommended)
* Tested Environment: Arch Linux
* Python 3.x and required dependencies must be installed before running the application.

## Access Control Mechanism

The platform implements an additional verification layer before user authentication.

### Access Flow

1. The user accesses the platform.
2. A one-time verification code is generated and sent to the abrehamabebe1921@gmail.com email address.
3. The user enters the verification code.
4. Upon successful verification, the login page becomes accessible.
5. The user can then authenticate using their assigned credentials.

This mechanism helps prevent unauthorized access and demonstrates the implementation of multi-step authentication and email-based verification within the platform.

## Key Features

### Vulnerability Scanner Engine

The scanner engine supports three scanning methods:

#### 1. Manual Domain Scanning

Users can provide a domain or subdomain directly for assessment.

#### 2. TXT-Based Bulk Scanning

Users can upload a .txt file containing multiple subdomains for automated scanning.

#### 3. Source Code Analysis

Users can upload source code for security inspection and vulnerability detection.

---

### Supported Vulnerability Detection

The scanner can identify security weaknesses such as:

* SQL Injection (SQLi)
* Cross-Site Scripting (XSS)
* Broken Authentication
* Sensitive Data Exposure
* Security Misconfiguration
* Broken Access Control
* Command Injection
* Content Security Policy (CSP) Misconfiguration
* Open Redirect
* Server-Side Template Injection (SSTI)
* Insecure Direct Object Reference (IDOR)

---

## Cybersecurity Lab Environment

The platform includes intentionally vulnerable applications for hands-on training.

### Difficulty Levels

* Low
* Medium
* High

### Available Lab Modules

#### SQL Injection Lab

Learn authentication bypass, data extraction, and secure query implementation.

#### Cross-Site Scripting (XSS) Lab

Understand reflected, stored, and DOM-based XSS attacks.

#### Server-Side Template Injection (SSTI) Lab

Practice identifying and exploiting template injection vulnerabilities.

#### IDOR Lab

Explore access control weaknesses and unauthorized data access.

#### Brute Force Lab

Analyze weak authentication mechanisms and password attacks.

#### JWT Attack Lab

Understand JSON Web Token vulnerabilities, insecure secrets, and token manipulation attacks.

---

## User Roles

### Administrator

* Manage users
* Monitor platform activity
* Configure system settings
* Manage lab environments

### Security Analyst

* Run vulnerability assessments
* Review scan reports
* Analyze findings
* Generate security recommendations

### Developer

* Review vulnerabilities
* Analyze source code findings
* Learn secure coding practices
* Access training laboratories

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* PHP
* RESTful API Architecture

---

## Educational Objectives

The platform aims to:

* Improve cybersecurity awareness
* Teach secure coding practices
* Provide practical vulnerability assessment experience
* Simulate real-world web security challenges
* Support cybersecurity education and research at AAiT

---

## Intended Use

This project is intended strictly for:

* Cybersecurity education
* Security awareness training
* Academic research
* Ethical security testing in authorized environments

Unauthorized use against systems without permission is prohibited.

---

## Future Enhancements

* Automated report generation
* Threat intelligence integration
* Advanced vulnerability correlation
* Security dashboard analytics
* Multi-user lab environments
* AI-assisted vulnerability analysis

---
## Demonstration Notice

The email verification system must be completed before the login page can be accessed. For project evaluation, testing, or demonstration purposes, please contact the developer to obtain access instructions and test credentials.

**Developer:** Abrham Abebe

**Email:** [abrehamabebe1921@gmail.com](mailto:abrehamabebe1921@gmail.com)

##### Note

Source code is provided for academic review and educational purposes only. Certain modules, configurations, and demonstration environments may require authorization from the developer before access is granted.



