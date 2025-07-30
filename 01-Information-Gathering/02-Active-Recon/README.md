# Active Reconnaissance

Active reconnaissance involves directly interacting with target systems to gather information. This phase helps identify live hosts, open ports, and running services, but it's more detectable than passive reconnaissance.

## 📋 Table of Contents

1. [Host Discovery](#host-discovery)
2. [Port Scanning](#port-scanning)
3. [Service Enumeration](#service-enumeration)
4. [Network Mapping](#network-mapping)
5. [Tools & Commands](#-tools--commands)
6. [Best Practices](#-best-practices)

## Host Discovery

Identify live hosts on the network:
- ICMP echo requests (ping sweeps)
- ARP scans (local networks)
- TCP/UDP discovery

### Commands
```bash
# Ping sweep
nmap -sn 192.168.1.0/24

# ARP scan (local network)
nmap -PR -sn 192.168.1.0/24

# TCP SYN ping
nmap -PS -sn 192.168.1.0/24
```

## Port Scanning

Discover open ports and services:
- TCP connect scan
- SYN scan (stealth scan)
- UDP scan
- Version detection

### Commands
```bash
# Basic TCP scan
nmap -sS -p- -T4 -oA tcp_scan 192.168.1.100

# UDP top 1000 ports
nmap -sU --top-ports 1000 -oA udp_scan 192.168.1.100

# Service version detection
nmap -sV -sC -p- -oA service_scan 192.168.1.100
```

## Service Enumeration

Gather detailed information about discovered services:
- Banner grabbing
- Service-specific enumeration
- Default credentials checking
- Vulnerability scanning

### Commands
```bash
# Banner grabbing with netcat
nc -nv 192.168.1.100 80

# HTTP service enumeration
nmap --script=http-enum -p80,443,8080 192.168.1.100

# SMB service enumeration
nmap --script=smb-enum-shares,smb-os-discovery -p139,445 192.168.1.100
```

## Network Mapping

Create a map of the target network:
- Traceroute analysis
- Network topology mapping
- Device fingerprinting
- OS detection

### Commands
```bash
# Traceroute
traceroute 192.168.1.100

# OS detection
nmap -O 192.168.1.100

# Network mapping with Nmap
nmap -sn -PE --traceroute 192.168.1.0/24
```

## 🛠 Tools & Commands

| Tool | Purpose | Example |
|------|---------|---------|
| Nmap | Network scanning | `nmap -sS -sV -p- -T4 target` |
| Masscan | Fast port scanning | `masscan -p1-65535 --rate 1000 192.168.1.100` |
| Recon-ng | Web reconnaissance | `use recon/domains-hosts/bing_domain_web` |
| Nikto | Web server scanning | `nikto -h http://example.com` |
| Gobuster | Directory/File brute force | `gobuster dir -u http://example.com -w wordlist.txt` |

## 📝 Best Practices

1. Always get proper authorization before scanning
2. Start with less intrusive scans
3. Be mindful of network performance impact
4. Document all findings and commands used
5. Respect rate limits and network policies
6. Be prepared to explain your actions

## 📚 Resources

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [Nmap Scripting Engine](https://nmap.org/book/nse.html)
- [Recon-ng Documentation](https://github.com/lanmaster53/recon-ng)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

## ⚠️ Legal Considerations

- Only scan systems you own or have explicit permission to test
- Be aware of and comply with all applicable laws and regulations
- Document your authorization and scope
- Be prepared to provide evidence of authorization if questioned
