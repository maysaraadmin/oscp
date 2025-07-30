# Network Attacks

Welcome to the Network Attacks section of the OSCP study guide. This section covers various network-based attacks and techniques used to exploit network protocols and services during penetration testing.

## 📋 Table of Contents

1. [Man-in-the-Middle (MITM)](01-MITM/README.md)
   - ARP spoofing
   - DNS spoofing
   - SSL stripping
   - LLMNR/NBT-NS poisoning
   - Rogue DHCP servers

2. [Sniffing & Traffic Analysis](02-Sniffing/README.md)
   - Wireshark filters
   - tcpdump usage
   - Extracting credentials
   - Protocol analysis
   - Traffic redirection

3. [VPN & Tunneling](03-VPN-Tunneling/README.md)
   - SSH tunneling
   - Chisel
   - Ligolo-ng
   - DNS tunneling
   - ICMP tunneling

4. [Firewall & IDS Evasion](04-Firewall-Evasion/README.md)
   - Port knocking
   - Packet fragmentation
   - IP spoofing
   - Proxy chains
   - Encryption and obfuscation

## 🛠 Tools

- **MITM**: Ettercap, BetterCAP, Responder
- **Sniffing**: Wireshark, tcpdump, TShark, NetworkMiner
- **Tunneling**: Chisel, Ligolo-ng, ngrok, Plink
- **Evasion**: Nmap (fragmentation, decoys), Proxychains, Metasploit encoders

## 📚 Resources

- [Wireshark Documentation](https://www.wireshark.org/docs/)
- [MITM Framework](https://github.com/byt3bl33d3r/MITMf)
- [Chisel Documentation](https://github.com/jpillora/chisel)
- [Ligolo-ng](https://github.com/nicocha30/ligolo-ng)
- [Nmap Firewall Evasion](https://nmap.org/book/man-bypass-firewalls-ids.html)

## 📝 Best Practices

- Always get proper authorization before conducting network attacks
- Document all network segments and devices
- Be aware of network monitoring systems
- Understand the impact of network disruptions
- Have a rollback plan for any changes made

## 📅 Study Plan

1. Learn basic network protocols and their vulnerabilities
2. Practice with Wireshark and tcpdump for traffic analysis
3. Set up a lab environment for MITM attacks
4. Learn about tunneling techniques
5. Practice firewall and IDS evasion methods

## ⚠️ Legal and Ethical Considerations

- Only perform network attacks on networks you own or have explicit permission to test
- Be aware of laws regarding network monitoring and interception
- Document all actions and obtain necessary permissions
- Avoid disrupting production network services
