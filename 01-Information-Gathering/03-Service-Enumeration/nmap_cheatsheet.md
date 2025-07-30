# Nmap Cheatsheet

Nmap ("Network Mapper") is a free and open-source network scanner used for host discovery, service enumeration, and vulnerability detection.

## Basic Scans

### Host Discovery
```bash
# Ping scan (no port scan)
nmap -sn 192.168.1.0/24

# Skip host discovery (treat all hosts as online)
nmap -Pn 192.168.1.1

# TCP SYN ping
nmap -PS -v 192.168.1.1

# TCP ACK ping
nmap -PA -v 192.168.1.1

# UDP ping
nmap -PU -v 192.168.1.1
```

### Port Scanning Techniques
```bash
# TCP SYN Scan (Stealth scan, requires root)
nmap -sS 192.168.1.1

# TCP Connect Scan (No root required)
nmap -sT 192.168.1.1

# UDP Scan
nmap -sU -p 53,67,68,69,123,137-139,161,162,445,500,514,520,623,1434,1900,4500,5353,49152 192.168.1.1

# Comprehensive Scan (SYN, Service detection, OS detection, traceroute, scripts)
nmap -sS -sV -sC -O -T4 -A -p- -oA full_scan 192.168.1.1
```

### Port Specification
```bash
# Specific ports
nmap -p 22,80,443 192.168.1.1

# Port range
nmap -p 1-1000 192.168.1.1

# Top ports
nmap --top-ports 100 192.168.1.1

# All ports (1-65535)
nmap -p- 192.168.1.1
```

## Service and OS Detection

```bash
# Service version detection
nmap -sV 192.168.1.1

# OS detection
nmap -O 192.168.1.1

# Aggressive detection (OS, version, script scanning, and traceroute)
nmap -A 192.168.1.1

# Default NSE scripts (safe scripts)
nmap -sC 192.168.1.1
```

## NSE Scripting Engine

### Vulnerability Scans
```bash
# Safe scripts (won't crash services)
nmap --script "safe" 192.168.1.1

# Vulnerability scan
nmap --script vuln 192.168.1.1

# Specific vulnerability check
nmap --script smb-vuln-ms17-010 192.168.1.1
```

### Common NSE Scripts
```bash
# HTTP enumeration
nmap --script http-enum -p80,443,8080,8443 192.168.1.1

# SMB enumeration
nmap --script smb-enum-shares,smb-enum-users,smb-os-discovery -p445 192.168.1.1

# FTP anonymous login check
nmap --script ftp-anon -p21 192.168.1.1

# MySQL empty password check
nmap --script mysql-empty-password -p3306 192.168.1.1

# DNS zone transfer
dig axfr @192.168.1.1 example.com
```

## Firewall Evasion

```bash
# Fragment packets
nmap -f 192.168.1.1

# Use decoy IPs
nmap -D RND:10 192.168.1.1

# Idle zombie scan
nmap -sI zombie.example.com 192.168.1.1

# Source port specification
nmap --source-port 53 192.168.1.1

# Append random data
nmap --data-length 25 192.168.1.1

# Randomize target scan order
nmap --randomize-hosts 192.168.1.1/24

# Timing templates (0-5, higher is faster)
nmap -T4 192.168.1.1
```

## Output Formats

```bash
# Normal output to screen
nmap 192.168.1.1

# Output to file (normal, XML, grepable, all formats)
nmap -oN output.nmap -oX output.xml -oG output.gnmap -oA all_formats 192.168.1.1

# Resume a scan
nmap --resume output.gnmap
```

## Useful Nmap Commands for OSCP

### Quick Scan
```bash
nmap -sV -sC -oA quick_scan 192.168.1.1
```

### Full Port Scan
```bash
nmap -p- -sV -sC -oA full_scan 192.168.1.1
```

### UDP Top Ports
```bash
nmap -sU --top-ports 200 -oA udp_scan 192.168.1.1
```

### Web Vulnerability Scan
```bash
nmap -p80,443,8080,8443 --script http-vuln-* -oA web_vuln_scan 192.168.1.1
```

### SMB Vulnerability Scan
```bash
nmap -p445 --script smb-vuln-* -oA smb_vuln_scan 192.168.1.1
```

## Nmap Scripting Engine (NSE) Categories

| Category | Description | Example |
|----------|-------------|---------|
| auth | Authentication credentials | `--script=auth` |
| broadcast | Discover hosts by broadcasting | `--script=broadcast` |
| brute | Brute force attacks | `--script=brute` |
| default | Default scripts (safe) | `--script=default` |
| discovery | Service discovery | `--script=discovery` |
| dos | Denial of service checks | `--script=dos` |
| exploit | Exploit vulnerabilities | `--script=exploit` |
| external | External services (DNS, etc.) | `--script=external` |
| fuzzer | Fuzzing modules | `--script=fuzzer` |
| intrusive | Intrusive scripts (may crash services) | `--script=intrusive` |
| malware | Malware detection | `--script=malware` |
| safe | Safe scripts (won't crash services) | `--script=safe` |
| vuln | Vulnerability detection | `--script=vuln` |

## Common Ports and Services

| Port | Service | Protocol | Common Vulnerabilities |
|------|---------|----------|------------------------|
| 21 | FTP | TCP | Anonymous login, brute force |
| 22 | SSH | TCP | Weak passwords, outdated versions |
| 23 | Telnet | TCP | Plaintext credentials |
| 25 | SMTP | TCP | Open relay, enumeration |
| 53 | DNS | TCP/UDP | Zone transfers, cache snooping |
| 80/443 | HTTP/HTTPS | TCP | Web vulnerabilities |
| 110 | POP3 | TCP | Plaintext credentials |
| 139/445 | SMB | TCP | EternalBlue, SMB signing |
| 143 | IMAP | TCP | Plaintext credentials |
| 161/162 | SNMP | UDP | Default community strings |
| 389 | LDAP | TCP | Anonymous binds, injection |
| 1433 | MS-SQL | TCP | Weak credentials |
| 1521 | Oracle | TCP | Default credentials |
| 2049 | NFS | TCP | No root squash |
| 3306 | MySQL | TCP | Weak credentials |
| 3389 | RDP | TCP | BlueKeep, brute force |
| 5432 | PostgreSQL | TCP | Default credentials |
| 5900 | VNC | TCP | Weak authentication |
| 8080 | HTTP Proxy | TCP | Web vulnerabilities |

## Nmap Timing Templates

| Template | Description | Timing | Example |
|----------|-------------|--------|---------|
| -T0 | Paranoid | Very slow | `nmap -T0` |
| -T1 | Sneaky | Quite slow | `nmap -T1` |
| -T2 | Polite | Slower | `nmap -T2` |
| -T3 | Normal | Default | `nmap -T3` |
| -T4 | Aggressive | Faster | `nmap -T4` |
| -T5 | Insane | Very fast | `nmap -T5` |

## Useful NSE Scripts for OSCP

### HTTP
- `http-enum`: Enumerate common web applications
- `http-vuln-*`: Check for specific web vulnerabilities
- `http-shellshock`: Check for Shellshock vulnerability
- `http-wordpress-enum`: Enumerate WordPress installations

### SMB
- `smb-enum-shares`: Enumerate SMB shares
- `smb-enum-users`: Enumerate SMB users
- `smb-os-discovery`: Get OS information via SMB
- `smb-vuln-ms17-010`: Check for EternalBlue vulnerability
- `smb-vuln-ms08-067`: Check for MS08-067 vulnerability

### FTP
- `ftp-anon`: Check for anonymous FTP login
- `ftp-vsftpd-backdoor`: Check for vsFTPd backdoor

### SSH
- `sshv1`: Check for SSH protocol version 1
- `ssh-publickey-acceptance`: Check for weak SSH key exchange algorithms

### SMTP
- `smtp-commands`: Enumerate SMTP commands
- `smtp-enum-users`: Enumerate SMTP users
- `smtp-vuln-*`: Check for SMTP vulnerabilities

### SNMP
- `snmp-info`: Get SNMP information
- `snmp-interfaces`: Enumerate network interfaces via SNMP
- `snmp-sysdescr`: Get system description via SNMP

## Nmap Cheat Sheet Table

| Command | Description |
|---------|-------------|
| `nmap -sS -sV -sC -O -T4 -A -p- -oA full_scan` | Full TCP port scan with service/OS detection |
| `nmap -sU --top-ports 200 -oA udp_scan` | Top 200 UDP ports scan |
| `nmap --script vuln -p- -oA vuln_scan` | Vulnerability scan on all ports |
| `nmap -p80,443 --script http-enum,http-vuln-*` | Web vulnerability scan |
| `nmap -p445 --script smb-enum-*,smb-vuln-*` | SMB enumeration and vulnerability scan |
| `nmap -sn 192.168.1.0/24` | Ping sweep (host discovery only) |
| `nmap -sV --script="ftp-*" -p21` | FTP service scan |
| `nmap -sV --script=ssh2-enum-algos -p22` | SSH encryption algorithms |
| `nmap --script http-wordpress-enum --script-args type="plugins"` | WordPress plugin enumeration |

## Tips for OSCP Exam

1. **Start with a quick scan** to identify open ports and services
2. **Use version detection** (`-sV`) to identify service versions
3. **Run vulnerability scripts** (`--script vuln`) to find potential vulnerabilities
4. **Check for default credentials** on services like FTP, SSH, and web applications
5. **Document everything** with `-oA` for all output formats
6. **Use timing templates** (`-T4`) for faster scans in the exam
7. **Don't forget UDP scans** as they often reveal interesting services
8. **Check for web applications** on non-standard ports
9. **Look for SMB shares** with anonymous access
10. **Always check for outdated software** that might have known vulnerabilities
