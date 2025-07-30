# Active Reconnaissance

Active reconnaissance involves directly interacting with the target's systems to gather information. Unlike passive recon, these techniques can be detected by the target.

## Table of Contents
- [Network Scanning with Nmap](#network-scanning-with-nmap)
  - [Basic Port Scanning](#basic-port-scanning)
  - [Service and Version Detection](#service-and-version-detection)
  - [NSE Scripting Engine](#nse-scripting-engine)
  - [Firewall/IDS Evasion](#firewallids-evasion)
- [Service Enumeration](#service-enumeration)
  - [HTTP/HTTPS Services](#httphttps-services)
  - [SMB Enumeration](#smb-enumeration)
  - [SNMP Enumeration](#snmp-enumeration)
  - [SMTP Enumeration](#smtp-enumeration)
- [Automated Enumeration](#automated-enumeration)
- [Defensive Considerations](#defensive-considerations)
- [Common Tools](#common-tools)

## Network Scanning with Nmap

### Basic Port Scanning

```bash
# Basic TCP SYN scan (Stealth scan) - Fast and reliable
# -sS: TCP SYN scan (half-open)
# -T4: Aggressive timing template
# -p-: All ports (1-65535)
# -oA: Output in all formats (nmap, gnmap, xml)
nmap -sS -T4 -p- -oA full_tcp_scan 192.168.1.1

# Quick scan (top 1000 ports)
# -F: Fast mode (scan fewer ports)
# -T4: Aggressive timing
nmap -T4 -F 192.168.1.1

# Scan specific ports
nmap -p21,22,80,443,445,3389 192.168.1.1

# Scan from a list of targets
nmap -iL targets.txt -oA network_scan

# Save output in all formats (-oA) and be verbose (-v)
nmap -v -sS -T4 -p- -oA full_scan 192.168.1.1

# Ping sweep to find live hosts
nmap -sn 192.168.1.0/24 -oG ping_sweep.txt
```

### Service and Version Detection

```bash
# Basic service detection
# -sV: Probe open ports to determine service/version info
# -sC: Run default scripts
nmap -sV -sC -p- -oA service_scan 192.168.1.1

# Aggressive scan (tries to detect OS, version, script scanning, and traceroute)
nmap -A -T4 -p- -oA aggressive_scan 192.168.1.1

# UDP scan (common ports)
# -sU: UDP scan
# --top-ports: Scan most common ports
nmap -sU -sV --top-ports 100 -oA udp_scan 192.168.1.1

# Comprehensive UDP scan (slower)
nmap -sU -p 53,67-69,123,135-139,161-162,445,500,514,520,623,1434,1900,4500,5353,49152-49154 -oA full_udp_scan 192.168.1.1
```

### Service Enumeration
```bash
# NSE Scripts for service enumeration
nmap -sV --script="banner,(default or safe or vuln or intrusive or discovery) and not broadcast" -p- -oA service_enum 192.168.1.1

# HTTP service enumeration
nmap --script=http-enum -p80,443,8080,8443 -oA http_enum 192.168.1.1
```

### Firewall/IDS Evasion
```bash
# Fragment packets
nmap -f 192.168.1.1

# Use decoy IPs
nmap -D RND:10 192.168.1.1

# Slow scan to avoid detection
nmap -T2 --max-parallelism 1 --max-scan-delay 100ms 192.168.1.1
```

## Web Application Enumeration

### Directory Bruteforcing
```bash
# Using Gobuster
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt -t 50 -x php,html,txt

# Using Dirsearch
python3 dirsearch.py -u http://example.com -e php,asp,aspx,jsp,html,zip,jar -t 50

# Using ffuf
ffuf -u http://example.com/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .php,.html,.txt
```

### Subdomain Enumeration
```bash
# Using ffuf
ffuf -u http://FUZZ.example.com -w subdomains.txt -o fuzzed_subdomains.json

# Using amass (active mode)
amass enum -active -d example.com -o amass_active_results.txt
```

### Web Technology Identification
```bash
# WhatWeb
whatweb -a 3 http://example.com

# Wappalyzer (browser extension)
# Available for Chrome and Firefox

# BuiltWith (online tool)
# https://builtwith.com/
```

## SMB Enumeration

```bash
# Basic SMB enumeration
enum4linux -a 192.168.1.1

# SMB version detection
nmap --script smb-os-discovery -p445 192.168.1.1

# List SMB shares
smbclient -L //192.168.1.1 -N

# Connect to SMB share
smbclient //192.168.1.1/sharename -N
```

## SNMP Enumeration

```bash
# SNMP version and system info
snmpwalk -v1 -c public 192.168.1.1

# Enumerate Windows users
snmpwalk -c public -v1 192.168.1.1 1.3.6.1.4.1.77.1.2.25

# Enumerate running processes
snmpwalk -c public -v1 192.168.1.1 1.3.6.1.2.1.25.4.2.1.2
```

## SMTP Enumeration

```bash
# SMTP version and banner
nc -nv 192.168.1.1 25

# Enumerate users with VRFY
for user in $(cat users.txt); do echo VRFY $user | nc -nv -w 1 192.168.1.1 25 2>/dev/null | grep ^"250"; done

# Using smtp-user-enum
smtp-user-enum -M VRFY -U users.txt -t 192.168.1.1
```

## DNS Enumeration (Active)

```bash
# Zone transfer attempt
dig axfr @ns1.example.com example.com

# Using dnsrecon
dnsrecon -d example.com -t axfr

# Using fierce
fierce --domain example.com
```

## Vulnerability Scanning

### Basic Vulnerability Scanning
```bash
# Nmap NSE vulnerability scripts
nmap --script vuln -p- -oA nmap_vuln_scan 192.168.1.1

# Nikto web scanner
nikto -h http://example.com -o nikto_scan.txt
```

### Automated Scanners
```bash
# OpenVAS/GVM
# Use the web interface at https://127.0.0.1:9392

# Nessus
# Commercial vulnerability scanner with web interface
```

## Password Spraying

```bash
# SMB password spray
for user in $(cat users.txt); do 
    for pass in $(cat passwords.txt); do 
        echo "$user:$pass" | smbclient -L //192.168.1.1 -U $user%$pass 2>&1 | grep -v "NT_STATUS_LOGON_FAILURE" && echo "[+] Found credentials: $user:$pass"; 
    done; 
done

# RDP password spray
hydra -L users.txt -P passwords.txt rdp://192.168.1.1
```

## Reporting Active Reconnaissance

Document all findings in a structured format:

```markdown
## Active Reconnaissance Report
- **Date**: [Date]
- **Target**: 192.168.1.1
- **Scan Type**: [TCP/UDP/Service]

### Open Ports & Services
| Port | Protocol | Service | Version |
|------|----------|---------|---------|
| 22/tcp | TCP | SSH | OpenSSH 7.9p1 |
| 80/tcp | TCP | HTTP | Apache httpd 2.4.41 |
| 443/tcp | TCP | HTTPS | Apache httpd 2.4.41 |

### Identified Vulnerabilities
1. **CVE-XXXX-XXXX**: [Vulnerability Description]
   - **Risk**: High/Medium/Low
   - **CVSS Score**: X.X
   - **Remediation**: [Recommended fix]

### Credentials Found
- Username: admin | Password: P@ssw0rd123
- Username: guest | Password: guest

### Recommendations
1. Update OpenSSH to the latest version
2. Disable weak cipher suites on the web server
3. Implement account lockout policies
4. Regular vulnerability scanning and patching
```

## Legal and Ethical Considerations

- Always obtain proper authorization before conducting active reconnaissance
- Be aware of scanning laws in your jurisdiction
- Respect rate limits and scanning policies
- Document all activities with timestamps
- Be prepared to provide evidence of authorization if questioned

## Tools for Active Recon

1. **Nmap** - Network scanning and service enumeration
2. **Metasploit Framework** - Exploitation and post-exploitation
3. **Burp Suite** - Web application testing
4. **OWASP ZAP** - Web application security scanner
5. **Hydra** - Network login cracker
6. **Responder** - LLMNR/NBT-NS/mDNS poisoner
7. **Impacket** - Collection of Python classes for network protocols

## Resources

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [SANS Top 20 Critical Security Controls](https://www.sans.org/critical-security-controls/)
