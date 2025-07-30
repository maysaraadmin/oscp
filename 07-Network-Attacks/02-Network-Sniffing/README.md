# Network Sniffing

Network sniffing involves capturing and analyzing network traffic to extract sensitive information. This guide covers essential network sniffing techniques and tools for the OSCP exam.

## 📋 Table of Contents
1. [Passive Sniffing](#passive-sniffing)
2. [Active Sniffing](#active-sniffing)
3. [Protocol Analysis](#protocol-analysis)
4. [Wireshark](#wireshark)
5. [Tcpdump](#tcpdump)
6. [Defense](#-defense)
7. [Practice](#-practice)

## Passive Sniffing

### Promiscuous Mode
```bash
# Check interface mode
ip link show eth0
# Look for PROMISC in the output

# Enable promiscuous mode
sudo ip link set eth0 promisc on
```

### Monitor Mode (Wireless)
```bash
# Set interface to monitor mode
sudo airmon-ng start wlan0

# Verify mode
iwconfig wlan0mon
```

## Active Sniffing

### ARP Spoofing with Sniffing
```bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# ARP spoofing
arpspoof -i eth0 -t TARGET_IP ROUTER_IP
arpspoof -i eth0 -t ROUTER_IP TARGET_IP

# Now run your preferred sniffer
```

## Protocol Analysis

### HTTP Traffic
- **Credentials**: Look for POST requests to login pages
- **Sessions**: Check for cookies and tokens
- **Files**: Watch for file uploads/downloads

### FTP Traffic
- **Credentials**: Captured in plaintext
- **Files**: Transferred in clear text

### SMTP/POP3/IMAP
- **Emails**: May contain sensitive information
- **Credentials**: Often sent in plaintext

## Wireshark

### Installation
```bash
# Kali Linux
sudo apt install wireshark

# Windows
# Download from https://www.wireshark.org/
```

### Basic Usage
```bash
# Capture on specific interface
wireshark -i eth0

# Read from pcap file
wireshark -r capture.pcap

# Capture with display filter
wireshark -i eth0 -Y "http.request"
```

### Useful Display Filters
```
# HTTP requests
http.request

# HTTP POST requests
http.request.method == "POST"

# Filter by IP
ip.addr == 192.168.1.1

# Filter by protocol
ftp || tftp || http || smtp || pop || imap

# Filter by port
tcp.port == 21 || tcp.port == 22 || tcp.port == 80
```

## Tcpdump

### Basic Usage
```bash
# Basic capture
sudo tcpdump -i eth0

# Save to file
sudo tcpdump -i eth0 -w capture.pcap

# Read from file
tcpdump -r capture.pcap
```

### Useful Commands
```bash
# Capture specific host
sudo tcpdump -i eth0 host 192.168.1.100

# Capture specific port
sudo tcpdump -i eth0 port 80

# Capture traffic between two hosts
sudo tcpdump -i eth0 host 192.168.1.100 and 192.168.1.1

# Capture HTTP POST requests
sudo tcpdump -i eth0 -A -s 0 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354'
```

## 🛡 Defense

### Encryption
- **HTTPS**: For web traffic
- **SSH**: For remote access
- **VPN**: For secure communication

### Network Segmentation
- **VLANs**: Separate sensitive traffic
- **Port Security**: Prevent MAC flooding

### Monitoring
- **IDS/IPS**: Detect and prevent sniffing
- **SIEM**: Centralized logging and monitoring

## 🛠 Tools

### Sniffing Tools
- **Wireshark**: GUI network protocol analyzer
- **Tcpdump**: Command-line packet analyzer
- **Tshark**: CLI version of Wireshark
- **Dsniff**: Collection of tools for network auditing

### Analysis Tools
- **NetworkMiner**: Network forensic analysis
- **Xplico**: Network forensic analysis tool
- **CapAnalysis**: Web visual tool for pcap analysis

## 📚 Resources
- [Wireshark Display Filters](https://www.wireshark.org/docs/dfref/)
- [Tcpdump Examples](https://danielmiessler.com/study/tcpdump/)
- [Packet Analysis with Wireshark](https://www.practicalnetworking.net/series/packet-traveling/packet-traveling/)

## 🎯 Practice
1. Capture HTTP traffic and extract credentials
2. Analyze a pcap file from Wireshark sample captures
3. Create custom display filters for specific protocols
4. Practice with [picoCTF](https://picoctf.org/) networking challenges

## ⚠️ Legal Note
Only perform network sniffing on networks you own or have explicit permission to test. Unauthorized network monitoring is illegal.
