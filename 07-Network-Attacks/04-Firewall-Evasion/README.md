# Firewall Evasion

Firewall evasion techniques help bypass network security controls to access restricted services. This guide covers common firewall evasion methods for the OSCP exam.

## 📋 Table of Contents
1. [Port Scanning Evasion](#port-scanning-evasion)
2. [Fragmentation](#fragmentation)
3. [Source Port Manipulation](#source-port-manipulation)
4. [IP and MAC Spoofing](#ip-and-mac-spoofing)
5. [Proxies and Tunnels](#proxies-and-tunnels)
6. [Defense](#-defense)
7. [Practice](#-practice)

## Port Scanning Evasion

### Nmap Timing Options
```bash
# Slow scan (T0-T1)
nmap -T0 -sS TARGET_IP

# Fast scan (T4-T5)
nmap -T4 -sS TARGET_IP

# Randomize host order
nmap --randomize-hosts TARGET_RANGE
```

### Decoy Scan
```bash
# Use decoy IPs (ME is your real IP)
nmap -D RND:10 ME TARGET_IP

# Specify decoy IPs
nmap -D 192.168.1.100,192.168.1.101,ME TARGET_IP
```

### Idle Scan
```bash
# Find a zombie host (must be idle)
nmap -sI ZOMBIE_IP TARGET_IP
```

## Fragmentation

### IP Fragmentation
```bash
# Fragment packets (8 bytes)
nmap -f TARGET_IP

# Specify fragment size (16 bytes)
nmap --mtu 16 TARGET_IP

# More aggressive fragmentation
nmap -f -f --mtu 8 TARGET_IP
```

### TCP Fragmentation
```bash
# Fragment TCP packets
nmap --scan-delay 1ms --max-hostgroup 1 TARGET_IP
```

## Source Port Manipulation

### Source Port Specification
```bash
# Use common source port (e.g., 53 for DNS)
nmap --source-port 53 TARGET_IP

# Random source port
nmap --randomize-ports TARGET_IP
```

### Spoofing Source IP
```bash
# Spoof source IP (requires root)
nmap -S SPOOFED_IP TARGET_IP

# With decoy
nmap -S SPOOFED_IP -D RND:10 TARGET_IP
```

## IP and MAC Spoofing

### MAC Address Spoofing
```bash
# Change MAC address
macchanger -m 00:11:22:33:44:55 eth0

# Random MAC address
macchanger -r eth0
```

### ARP Spoofing
```bash
# ARP spoofing with arpspoof
arpspoof -i eth0 -t TARGET_IP ROUTER_IP
```

## Proxies and Tunnels

### SSH Tunneling
```bash
# Local port forwarding
ssh -L 8080:TARGET_IP:80 user@JUMP_SERVER

# Dynamic port forwarding (SOCKS proxy)
ssh -D 1080 user@JUMP_SERVER
```

### HTTP/HTTPS Tunneling
```bash
# Using httptunnel
hts --forward-port localhost:22 80
htc --forward-port 8080 TUNNEL_SERVER:80
```

## 🛡 Defense

### Detection
- Monitor for unusual scan patterns
- Watch for IP/MAC address changes
- Use IDS/IPS systems

### Prevention
- Implement egress filtering
- Use stateful firewalls
- Enable logging and monitoring
- Use network segmentation
- Keep systems updated

## 🛠 Tools

### Scanning
- **Nmap**: Feature-rich network scanner
- **Hping3**: Packet crafting tool
- **Scapy**: Packet manipulation library

### Spoofing
- **Macchanger**: MAC address changer
- **Arpspoof**: ARP spoofing tool
- **Ettercap**: Comprehensive MITM suite

### Tunneling
- **SSH**: Secure shell tunneling
- **Chisel**: Fast TCP/UDP tunnel
- **Ngrok**: Secure tunnels to localhost

## 📚 Resources
- [Nmap Firewall Evasion](https://nmap.org/book/man-bypass-firewalls-ids.html)
- [Firewall Evasion Techniques](https://www.varonis.com/blog/firewall-evasion-techniques/)
- [HackTricks - Firewall Bypass](https://book.hacktricks.xyz/generic-methodologies-and-resources/firewall-bypass)

## 🎯 Practice
1. Try scanning a target with different Nmap timing options
2. Practice using decoy and fragmented scans
3. Set up a lab environment to test firewall rules
4. Experiment with different tunneling techniques

## ⚠️ Legal Note
Only perform firewall evasion on systems you own or have explicit permission to test. Unauthorized testing is illegal.
