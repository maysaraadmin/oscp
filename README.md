# OSCP Study Notes

Welcome to my OSCP (Offensive Security Certified Professional) study notes repository. This collection is designed to help me (and others) prepare for the OSCP certification exam by providing organized, practical, and comprehensive security testing knowledge.

## 📚 Table of Contents

1. [Introduction](00-introduction/README.md)
2. [Reconnaissance](01-reconnaissance/README.md)
   - [Active Reconnaissance](01-reconnaissance/active_recon.md)
   - [DNS Enumeration](01-reconnaissance/dns_enumeration.md)
   - [Recon Notes](01-reconnaissance/recon_notes.md)
3. [Scanning](02-scanning/README.md)
   - [Nmap Cheatsheet](02-scanning/nmap_cheatsheet.md)
   - [Vulnerability Scanning](02-scanning/vulnerability_scanning.md)
4. [Exploitation](03-exploitation/README.md)
   - [Exploit Development](03-exploitation/exploit_development.md)
   - [Manual Exploitation](03-exploitation/manual_exploitation.md)
   - [Metasploit Cheatsheet](03-exploitation/metasploit_cheatsheet.md)
5. [Web Application Security](04-web/README.md)
   - [Web Application Attacks](04-web/attacks/web_application_attacks.md)
   - [Client-side Attacks](04-web/client_side_attacks.md)
   - [SQL Injection](04-web/sql_injection/sql_injection.md)
6. [Post-Exploitation](05-post-exploitation/README.md)
   - [Windows Privilege Escalation](05-post-exploitation/windows_privilege_escalation.md)
7. [Password Attacks](06-password-attacks/README.md)
   - [Password Attacks Guide](06-password-attacks/password_attacks.md)

## 📁 Repository Structure

```
oscp/
├── 00-introduction/
│   └── introduction.md
├── 01-reconnaissance/
│   ├── active_recon.md
│   ├── dns_enumeration.md
│   └── recon_notes.md
├── 02-scanning/
│   ├── nmap_cheatsheet.md
│   └── vulnerability_scanning.md
├── 03-exploitation/
│   ├── exploit_development.md
│   ├── manual_exploitation.md
│   └── metasploit_cheatsheet.md
├── 04-web/
│   ├── attacks/
│   │   └── web_application_attacks.md
│   ├── client_side_attacks.md
│   └── sql_injection/
│       └── sql_injection.md
├── 05-post-exploitation/
│   └── windows_privilege_escalation.md
└── 06-password-attacks/
    └── password_attacks.md
│       └── linux_pe.md
├── 04-web/
│   ├── web_enumeration.md
│   ├── sql_injection.md
│   ├── xss_csrf.md
│   └── file_inclusion.md
├── 05-post-exploitation/
│   ├── lateral_movement.md
│   └── persistence.md
├── 06-password-attacks/
│   ├── hash_cracking.md
│   └── password_spraying.md
└── resources/
    ├── useful_commands.md
    ├── common_ports.md
    └── tools_installation.md
```

## 📚 Study Methodology

1. **Hands-on Practice**: All techniques are meant to be practiced in a controlled lab environment.
2. **Progressive Learning**: Start with basic concepts and gradually move to advanced topics.
3. **Documentation**: Keep detailed notes of findings, commands, and techniques.
4. **Review**: Regularly revisit and update notes based on new knowledge.

## 🛠 Tools Used

- **Reconnaissance**: Nmap, Recon-ng, theHarvester
- **Vulnerability Scanning**: Nessus, OpenVAS, Nikto
- **Exploitation**: Metasploit, Searchsploit, Custom Scripts
- **Password Attacks**: Hashcat, John the Ripper
- **Web Application Testing**: Burp Suite, OWASP ZAP, SQLmap
- **Post-Exploitation**: Mimikatz, PowerSploit, BloodHound

## 🔒 Legal & Ethical Considerations

- These notes are for educational purposes only.
- Only test systems you own or have explicit permission to test.
- Always follow responsible disclosure practices.
- Be aware of and comply with all applicable laws and regulations.

## 📝 Usage

1. Clone this repository: `git clone [repository-url]`
2. Navigate to the relevant section
3. Follow the notes and practice in your lab environment
4. Contribute improvements via pull requests

## 📅 Progress Tracker

- [ ] Complete Reconnaissance Section
- [ ] Master Scanning Techniques
- [ ] Practice Exploitation
- [ ] Web Application Testing
- [ ] Post-Exploitation Techniques
- [ ] Practice Exams

## 📚 Resources

- [Offensive Security PWK Course](https://www.offensive-security.com/pwk-oscp/)
- [OSCP Exam Guide](https://www.offensive-security.com/documentation/penetration-testing-with-kali.pdf)
- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)

## 🤝 Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting pull requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.