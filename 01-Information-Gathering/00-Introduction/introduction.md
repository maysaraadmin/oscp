# OSCP Study Notes - Introduction

Welcome to my OSCP (Offensive Security Certified Professional) study notes. This document serves as a comprehensive guide for preparing for the OSCP certification exam, covering various penetration testing techniques, tools, and methodologies.

## Table of Contents
- [Getting Started](#getting-started)
- [Basic Linux Commands](#basic-linux-commands)
- [File Operations](#file-operations)
- [Permissions](#permissions)
- [Networking](#networking)
- [Study Tips](#study-tips)
- [Useful Commands](#useful-commands)

## Getting Started

1. **Setting Up Your Environment**
   - Install Kali Linux or your preferred penetration testing distribution
   - Set up a virtual lab environment
   - Install essential tools and dependencies

2. **Connecting to the Lab**
   ```bash
   # Create a directory for your work
   mkdir -p ~/offsec
   
   # Locate and connect to the VPN
   locate pen200.ovpn
   sudo openvpn pen200.ovpn
   ```

## Basic Linux Commands

### File Operations
```bash
# List files
ls

# List files with details
ls -l

# List all files including hidden ones
ls -la

# Create a new file
touch filename.txt

# Move/rename files
mv oldname.txt newname.txt

# Copy files
cp source.txt destination/
```

### Permissions
```bash
# View file permissions
ls -l filename

# Make a file executable
chmod +x script.py

# Remove execute permission
chmod -x script.py

# Set specific permissions (e.g., rwxr-xr--)
chmod 754 filename
```

## Networking

### Basic Network Commands
```bash
# Check network interfaces
ip a
ifconfig

# Test network connectivity
ping 192.168.1.1

# DNS lookups
nslookup example.com
host example.com
dig example.com

# WHOIS lookup
whois example.com
```

### Network Scanning
```bash
# Basic port scan with nmap
nmap -sS -T4 192.168.1.1

# Scan specific ports
nmap -p 22,80,443 192.168.1.1

# Service version detection
nmap -sV -sC 192.168.1.1
```

## Study Tips

1. **Document Everything**
   - Take detailed notes of all commands and their outputs
   - Document your methodology and thought process
   - Keep track of findings and potential attack vectors

2. **Practice Regularly**
   - Work on HTB (Hack The Box) machines
   - Practice on VulnHub VMs
   - Set up your own vulnerable VMs for practice

3. **Time Management**
   - Allocate specific time slots for different topics
   - Practice under exam-like conditions
   - Take regular breaks to avoid burnout

## Useful Commands

### File Operations
```bash
# Find files by name
find / -name "*.txt" 2>/dev/null

# Search for text in files
grep -r "search_term" /path/

# Update the file database
sudo updatedb
```

### Network Discovery
```bash
# Quick host discovery
for ip in $(seq 1 254); do ping -c 1 192.168.1.$ip | grep "bytes from" & done

# DNS enumeration
for ip in $(seq 200 254); do host 1.1.1.$ip; done | grep -v "not found"
```

### Web Application Testing
```bash
# Web directory brute-forcing
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt

# Subdomain enumeration
sublist3r -d example.com
```

## Next Steps
1. Review the [Reconnaissance](01-reconnaissance/README.md) section for information gathering techniques
2. Practice the commands in a controlled environment
3. Document your progress and findings

Remember: The key to success in OSCP is practice, persistence, and thorough documentation.
