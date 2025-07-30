# Password Cracking

Welcome to the Password Cracking section of the OSCP study guide. This section covers techniques and tools for cracking passwords and hashes, which are essential skills for penetration testing and security assessments.

## 📋 Table of Contents

1. [Password Spraying](01-Password-Spraying/README.md)
   - Identifying authentication endpoints
   - Building username lists
   - Password policy analysis
   - Defensive measures

2. [Hash Extraction](02-Hash-Extraction/README.md)
   - Windows hashes (SAM, NTDS, LSASS)
   - Linux hashes (/etc/shadow, /etc/passwd)
   - Memory dumps (Mimikatz, pypykatz)
   - Network protocol hashes

3. [Hash Cracking](03-Hash-Cracking/README.md)
   - Hash identification
   - Dictionary attacks
   - Rule-based attacks
   - Brute force attacks
   - Mask attacks
   - Hybrid attacks

4. [Wordlist Generation](04-Wordlist-Generation/README.md)
   - Custom wordlist creation
   - Crunch
   - CUPP (Common User Passwords Profiler)
   - CeWL (Custom Word List generator)
   - Mentalist

## 🛠 Tools

- **Hash Cracking**: Hashcat, John the Ripper, hash-identifier
- **Password Spraying**: SprayingToolkit, Ncrack, Hydra, Medusa
- **Hash Extraction**: Mimikatz, secretsdump.py, pypykatz, LaZagne
- **Wordlist Tools**: Crunch, CUPP, CeWL, Mentalist
- **Online Tools**: CrackStation, Hashes.com, CMD5

## 📚 Resources

- [Hashcat Wiki](https://hashcat.net/wiki/)
- [OpenWall Wordlists](https://www.openwall.com/wordlists/)
- [SecLists](https://github.com/danielmiessler/SecLists)
- [Hashes.org](https://hashes.org/)
- [CrackStation](https://crackstation.net/)

## 📝 Best Practices

- Always get proper authorization before password cracking
- Be aware of account lockout policies
- Use appropriate wordlists for the target environment
- Document all cracking attempts and results
- Clean up any extracted credentials after testing

## 📅 Study Plan

1. Learn about different hash types and their formats
2. Practice with basic dictionary attacks
3. Move to more advanced techniques (rules, masks, hybrid)
4. Learn about password policy bypass techniques
5. Practice in a lab environment with various hash types

## ⚠️ Legal and Ethical Considerations

- Only crack passwords you own or have explicit permission to test
- Be aware of data protection laws regarding credential storage
- Never use cracked credentials outside the scope of engagement
- Securely delete any extracted credentials after testing
