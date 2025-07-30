# Web Application Enumeration

Web application enumeration involves identifying and analyzing web applications to understand their structure, functionality, and potential vulnerabilities. This is a critical step in web application penetration testing.

## 📋 Table of Contents

1. [Web Server Fingerprinting](#web-server-fingerprinting)
2. [Directory and File Enumeration](#directory-and-file-enumeration)
3. [Technology Identification](#technology-identification)
4. [Content Discovery](#content-discovery)
5. [Tools & Commands](#-tools--commands)
6. [Best Practices](#-best-practices)

## Web Server Fingerprinting

Identify the web server software and version:
- HTTP headers
- Server tokens
- Default pages
- Error messages

### Commands
```bash
# Using curl for headers
curl -I http://example.com

# Using nmap
nmap --script=http-headers -p80,443,8080 example.com

# Using whatweb
whatweb -a 3 http://example.com
```

## Directory and File Enumeration

Discover hidden directories and files:
- Common backup files
- Configuration files
- Source code
- Administrative interfaces

### Commands
```bash
# Using Gobuster
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt

# Using Dirsearch
python3 dirsearch.py -u http://example.com -e php,html,txt

# Using Dirb
dirb http://example.com /usr/share/wordlists/dirb/common.txt
```

## Technology Identification

Identify web technologies in use:
- Programming languages
- Frameworks
- Content Management Systems (CMS)
- JavaScript libraries

### Commands
```bash
# Using Wappalyzer (browser extension)
# Visit the website with Wappalyzer enabled

# Using BuiltWith
# Visit https://builtwith.com/

# Using whatweb
whatweb -a 3 http://example.com
```

## Content Discovery

Discover interesting content and functionality:
- Login pages
- Search functionality
- File uploads
- Contact forms
- API endpoints

### Commands
```bash
# Using Burp Suite
# Spider the application and review the site map

# Using OWASP ZAP
# Run the spider against the target

# Using custom wordlists
gobuster dir -u http://example.com -w custom_wordlist.txt -x php,txt,html
```

## 🛠 Tools & Commands

| Tool | Purpose | Example |
|------|---------|---------|
| Gobuster | Directory/file brute force | `gobuster dir -u http://example.com -w wordlist.txt` |
| Dirsearch | Web path scanner | `python3 dirsearch.py -u http://example.com -e php` |
| Nikto | Web server scanner | `nikto -h http://example.com` |
| WhatWeb | Web technology detector | `whatweb -a 3 http://example.com` |
| Burp Suite | Web proxy and scanner | GUI-based |
| OWASP ZAP | Web app scanner | GUI-based |
| Wappalyzer | Browser extension for tech detection | Browser-based |

## 📝 Best Practices

1. Start with passive reconnaissance
2. Use multiple tools for comprehensive coverage
3. Document all findings with screenshots
4. Be mindful of rate limiting
5. Respect robots.txt (but don't rely on it for security)
6. Look for common backup file extensions (.bak, .old, .swp, etc.)
7. Check for version control files (.git/, .svn/)

## 📚 Resources

- [OWASP Testing Guide - Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/)
- [SecLists - Collection of multiple types of lists](https://github.com/danielmiessler/SecLists)
- [Dirsearch - Web path scanner](https://github.com/maurosoria/dirsearch)
- [Gobuster - Directory/File/DNS busting tool](https://github.com/OJ/gobuster)

## ⚠️ Legal Considerations

- Only enumerate web applications you own or have permission to test
- Be aware of and comply with all applicable laws and regulations
- Document your authorization and scope
- Be prepared to provide evidence of authorization if questioned
