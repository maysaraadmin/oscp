# Metasploit Framework

Welcome to the Metasploit section of the OSCP study guide. This section covers the use of the Metasploit Framework for penetration testing, focusing on its role in the OSCP exam and ethical hacking.

## 📋 Table of Contents

1. [Payload Generation](01-Payload-Generation/README.md)
   - msfvenom usage
   - Payload types (reverse_tcp, bind_tcp, etc.)
   - Encoding and obfuscation
   - Payload generation for different platforms
   - Custom payload creation

2. [Post-Exploitation](02-Post-Exploitation/README.md)
   - Meterpreter basics
   - Privilege escalation
   - Pivoting and port forwarding
   - Post-exploitation modules
   - Persistence mechanisms

## 🛠 Tools

- **Metasploit Framework**: msfconsole, msfvenom, msfdb
- **Auxiliary Modules**: Port scanning, service enumeration, vulnerability scanning
- **Post-Exploitation**: Meterpreter, post modules, local exploit suggester
- **Integration**: Armitage, Cobalt Strike (commercial)

## 📚 Resources

- [Offensive Security's Metasploit Unleashed](https://www.offensive-security.com/metasploit-unleashed/)
- [Rapid7 Metasploit Documentation](https://docs.rapid7.com/metasploit/)
- [Metasploit GitHub Repository](https://github.com/rapid7/metasploit-framework)
- [Metasploit Cheat Sheet](https://www.sans.org/security-resources/sec560/misc_tools_sheet_v1.pdf)

## 📝 Best Practices

- Use Metasploit as a last resort in the OSCP exam
- Document all commands and modules used
- Be aware of antivirus and endpoint detection
- Clean up after testing
- Understand the underlying mechanisms of each attack

## 📅 Study Plan

1. Learn basic Metasploit commands and navigation
2. Practice payload generation with msfvenom
3. Understand Meterpreter and its capabilities
4. Learn about post-exploitation modules
5. Practice pivoting and lateral movement

## ⚠️ OSCP Exam Considerations

- Limited to one target machine in the exam
- Must demonstrate manual exploitation first
- Only use Metasploit when absolutely necessary
- Document the need for Metasploit in your report
- Be prepared to explain the Metasploit modules used
