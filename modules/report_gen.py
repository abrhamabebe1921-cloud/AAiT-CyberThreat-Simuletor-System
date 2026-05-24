import os
import json
from datetime import datetime
from fpdf import FPDF


class ThreatMapperPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return  # No header on cover page
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 255, 136)
        self.cell(0, 10, 'THREATMAPPER | SECURITY ASSESSMENT REPORT', new_x='LMARGIN', new_y='NEXT', align='L')
        self.set_draw_color(0, 255, 136)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'CONFIDENTIAL - ThreatMapper v2.0 | Page {self.page_no()}', align='C')


SEVERITY_COLORS = {
    'Critical': (255, 59, 59),
    'High': (255, 140, 0),
    'Medium': (255, 193, 7),
    'Low': (0, 204, 106),
    'Info': (59, 130, 246),
}

# Extensive remediation dictionary
REMEDIATION_DB = {
    'Missing CSP': 'Implement a strict Content-Security-Policy header. Restrict default-src to self, and explicitly whitelist external domains.',
    'Missing X-Frame-Options': 'Set X-Frame-Options to DENY or SAMEORIGIN to prevent Clickjacking.',
    'Missing X-Content-Type-Options': 'Ensure the X-Content-Type-Options header is set to nosniff to prevent MIME-sniffing attacks.',
    'Server Version Exposed': 'Configure the web server to hide version information in headers (e.g., ServerTokens Prod in Apache).',
    'Weak Cookie Flags': 'Set HttpOnly and Secure flags on all session cookies to prevent XSS hijacking and network sniffing.',
    'CORS Misconfiguration': 'Do not use Access-Control-Allow-Origin: *. Restrict CORS origins to trusted domains only.',
    'Missing Strict-Transport-Security': 'Enable HTTP Strict Transport Security (HSTS) with a long max-age and includeSubDomains directive.',
    'Open MySQL Port': 'Block external access to port 3306 using iptables or a cloud firewall. Require VPN/SSH tunnel for DB administration.',
    'Default Credentials Detected': 'Immediately change all default vendor credentials. Implement strong password policies and MFA.',
    'Open SSH Port': 'Ensure SSH uses Key-Based authentication and disable Root login. Change default port if applicable.',
    'XSS Reflected': 'Ensure strict contextual output encoding. Use a modern web framework that auto-escapes HTML characters.',
    'SQL Injection Possible': 'Refactor database queries to use Parameterized Queries (Prepared Statements) or an Object Relational Mapper (ORM).',
    'Information Disclosure': 'Disable debug mode in production. Implement proper default generic error pages.',
    'Command Injection': 'Avoid passing user input to system shells. Use language-specific safe API methods (e.g. subprocess without shell).',
    'Broken Authentication': 'Implement robust session management, aggressive rate limiting, and temporary lockouts after failed attempts.',
    'Unrestricted File Upload': 'Validate all file uploads by checking magic bytes, use random file names, and store them outside the web root.',
    'Directory Listing Enabled': 'Disable directory browsing in the web server configuration (e.g., Options -Indexes in Apache / .htaccess).',
    'Weak TLS Version': 'Disable TLS 1.0 and 1.1. Force TLS 1.2 or 1.3 with strong cipher suites like AES-256-GCM.',
    'SSRF Detected': 'Implement an explicit whitelist of allowed domains/IPs for backend requests. Deny all private IP range resolution.',
    'Insecure Deserialization': 'Never deserialize untrusted data. Use safe data formats like JSON instead of pickle or Java Serialization.',
    'XXE Enabled': 'Disable XML External Entities and DTDs completely in your XML parser configuration.',
    'CSRF Vulnerability': 'Implement synchronized anti-CSRF tokens for all state-changing POST/PUT/DELETE requests.',
    'Path Traversal': 'Avoid direct file inclusion via user input. Whitelist allowed paths or sanitize input strictly using realpath checks.',
    'Open Redirect': 'Do not allow arbitrary URLs in redirect parameters. Validate redirects against an explicit white-list of trusted hosts.',
    'Weak Session Management': 'Ensure session IDs are long, random, and regenerated immediately upon user login. Set absolute session timeouts.',
    'BOLA (Broken Object Level Authorization)': 'Implement explicit server-side authorization checks on every data access request ensuring the user owns the specific object ID.',
    'JWT Misconfiguration': 'Use strong HMAC secrets or RSA keys. Strictly enforce the algorithm header (reject "none") and validate token expiration.',
    'Race Condition': 'Implement database row locking (e.g., SELECT ... FOR UPDATE) or mutexes around critical transaction code.',
    'Business Logic Flaw': 'Thoroughly map out application workflows and enforce rigid server-side state validation to prevent skipping steps.'
}


def generate_pdf_report(findings, scan_summary=None, filename=None):
    """Generate a highly professional pentest-style PDF security report."""
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'ThreatMapper_Report_{timestamp}.pdf'

    reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    filepath = os.path.join(reports_dir, filename)

    pdf = ThreatMapperPDF()
    pdf.alias_nb_pages()
    
    # ---------------- COVER PAGE ----------------
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.ln(50)
    pdf.set_font('Helvetica', 'B', 32)
    pdf.set_text_color(0, 255, 136)
    pdf.cell(0, 15, 'THREATMAPPER', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.set_font('Helvetica', '', 16)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, 'Vulnerability Assessment & Penetration Test Report', new_x='LMARGIN', new_y='NEXT', align='C')
    
    pdf.ln(40)
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 8, f'Date Generated: {datetime.now().strftime("%B %d, %Y - %H:%M:%S")}', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.cell(0, 8, 'Target Scope: Multiple Internal/External Assets', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.cell(0, 8, 'Classification: CONFIDENTIAL', new_x='LMARGIN', new_y='NEXT', align='C')
    
    pdf.set_y(250)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(255, 140, 0)
    pdf.cell(0, 6, 'Generated Automatically by ThreatMapper Security Engine', new_x='LMARGIN', new_y='NEXT', align='C')

    # ---------------- PAGE 2: EXEC SUMMARY ----------------
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(0, 255, 136)
    pdf.cell(0, 10, '1. Executive Summary', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

    total = len(findings)
    sev_counts = {}
    for f in findings:
        s = f.get('severity', 'Info')
        sev_counts[s] = sev_counts.get(s, 0) + 1

    risk = (sev_counts.get('Critical', 0) * 40 +
            sev_counts.get('High', 0) * 25 +
            sev_counts.get('Medium', 0) * 10 +
            sev_counts.get('Low', 0) * 3)
    risk_label = 'LOW' if risk < 30 else 'MEDIUM' if risk < 80 else 'HIGH' if risk < 150 else 'CRITICAL'

    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(200, 200, 200)
    pdf.multi_cell(0, 6,
        "This document outlines the findings of a comprehensive vulnerability assessment performed by ThreatMapper. "
        "The objective was to identify security misconfigurations, unpatched vulnerabilities, and structural weaknesses "
        "that could be exploited by malicious actors.\n\n"
        f"A total of {total} vulnerabilities were discovered across the in-scope assets."
    )
    pdf.ln(10)
    
    # Risk Score Block
    pdf.set_fill_color(20, 20, 20)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(100, 15, f' Overall System Risk: {risk_label} ', fill=True, border=1)
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(90, 15, f' Calculated Severity Score: {risk} ', fill=True, border=1, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(10)

    # Stats
    pdf.set_font('Helvetica', 'B', 12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, 'Vulnerability Breakdown:', new_x='LMARGIN', new_y='NEXT')
    
    for sev in ['Critical', 'High', 'Medium', 'Low', 'Info']:
        count = sev_counts.get(sev, 0)
        c = SEVERITY_COLORS.get(sev, (255, 255, 255))
        pdf.set_text_color(*c)
        pdf.cell(40, 8, f'  - {sev}: {count}', new_x='LMARGIN', new_y='NEXT')

    pdf.ln(10)

    # ---------------- PAGE 3: FINDINGS TABLE ----------------
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(0, 255, 136)
    pdf.cell(0, 10, '2. Findings Overview Matrix', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_fill_color(20, 20, 20)
    pdf.set_text_color(255, 140, 0)
    pdf.cell(35, 8, 'Target Host', border=1, fill=True)
    pdf.cell(60, 8, 'Vulnerability', border=1, fill=True)
    pdf.cell(20, 8, 'Severity', border=1, fill=True)
    pdf.cell(15, 8, 'CVSS', border=1, fill=True)
    pdf.cell(60, 8, 'OWASP Class', border=1, fill=True, new_x='LMARGIN', new_y='NEXT')

    pdf.set_font('Helvetica', '', 8)
    for f in findings:
        sev = f.get('severity', 'Info')
        color = SEVERITY_COLORS.get(sev, (200, 200, 200))
        pdf.set_text_color(*color)

        host = str(f.get('host', ''))[:20]
        issue = str(f.get('issue', ''))[:35]
        cvss = str(f.get('cvss', 'N/A'))
        owasp = str(f.get('owasp', 'N/A'))[:35]

        pdf.cell(35, 7, host, border=1)
        pdf.cell(60, 7, issue, border=1)
        pdf.cell(20, 7, sev, border=1)
        pdf.cell(15, 7, cvss, border=1)
        pdf.cell(60, 7, owasp, border=1, new_x='LMARGIN', new_y='NEXT')

    # ---------------- PAGE 4+: DETAILED FINDINGS ----------------
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, 'F')
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(0, 255, 136)
    pdf.cell(0, 10, '3. Detailed Vulnerability Analysis', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)

    # Sort findings by severity
    order = {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3, 'Info': 4}
    sorted_findings = sorted(findings, key=lambda x: order.get(x.get('severity', 'Info'), 5))

    for idx, f in enumerate(sorted_findings, 1):
        sev = f.get('severity', 'Info')
        issue = f.get('issue', 'Unknown Issue')
        host = f.get('host', 'Unknown Host')
        detail = f.get('detail', 'No technical details provided.')
        cvss = f.get('cvss', 'N/A')
        owasp = f.get('owasp', 'N/A')
        
        c = SEVERITY_COLORS.get(sev, (255, 255, 255))
        
        pdf.set_font('Helvetica', 'B', 12)
        pdf.set_text_color(*c)
        pdf.cell(0, 8, f"{idx}. {issue} [{sev}]", new_x='LMARGIN', new_y='NEXT')
        
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(180, 180, 180)
        
        # Info block
        pdf.set_fill_color(20, 20, 20)
        pdf.multi_cell(0, 6, f"Affected Host: {host}\nCVSS Base Score: {cvss}\nOWASP Category: {owasp}", fill=True)
        pdf.ln(2)
        
        # Tech Detail
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 6, "Technical Details / Proof of Concept:", new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(200, 200, 200)
        pdf.multi_cell(0, 6, detail)
        pdf.ln(2)
        
        # Remediation
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(0, 255, 136) # Green
        pdf.cell(0, 6, "Recommended Remediation:", new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(200, 200, 200)
        
        recommendation = REMEDIATION_DB.get(issue, "Follow standard secure coding practices. Refer to OWASP guidelines for mitigation techniques specific to this class of vulnerability.")
        pdf.multi_cell(0, 6, recommendation)
        pdf.ln(8)
        
        # Avoid orphan headers if nearing bottom of page
        if pdf.get_y() > 250:
            pdf.add_page()
            pdf.set_fill_color(0, 0, 0)
            pdf.rect(0, 0, 210, 297, 'F')

    pdf.output(filepath)
    return filepath
