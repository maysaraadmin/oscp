# Password Cracking Tools

This guide covers essential password cracking tools and techniques for the OSCP exam, including Hashcat, John the Ripper, and more.

## 📋 Table of Contents
1. [Hashcat](#hashcat)
2. [John the Ripper](#john-the-ripper)
3. [Hydra](#hydra)
4. [Medusa](#medusa)
5. [Custom Wordlists](#custom-wordlists)
6. [Practice](#-practice)

## Hashcat

### Installation
```bash
# Kali Linux
sudo apt install hashcat

# Windows
# Download from https://hashcat.net/hashcat/
```

### Basic Usage
```bash
# List available hash modes
hashcat --help | grep "\-m"

# Basic syntax
hashcat -m [hash_mode] [hash_file] [wordlist] [options]

# Example: Crack MD5 hashes
hashcat -m 0 hashes.txt rockyou.txt

# Show cracked passwords
hashcat -m 0 hashes.txt rockyou.txt --show
```

### Common Hash Modes
- **0**: MD5
- **1000**: NTLM
- **1800**: SHA-512 (Unix)
- **3200**: bcrypt
- **5600**: NetNTLMv2
- **13100**: Kerberos TGS-REP

### Attack Modes
```bash
# Dictionary attack
hashcat -m 0 -a 0 hashes.txt wordlist.txt

# Combination attack
hashcat -m 0 -a 1 hashes.txt wordlist1.txt wordlist2.txt

# Mask attack (Brute-force)
hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?l?l?l?l

# Hybrid attack (Wordlist + Mask)
hashcat -m 0 -a 6 hashes.txt wordlist.txt ?d?d?d
```

## John the Ripper

### Installation
```bash
# Kali Linux
sudo apt install john

# Windows
# Download from https://www.openwall.com/john/
```

### Basic Usage
```bash
# Basic syntax
john [options] [hash_file]

# Auto-detect hash type and crack
john hashes.txt

# Specify wordlist
john --wordlist=rockyou.txt hashes.txt

# Show cracked passwords
john --show hashes.txt
```

### Format-Specific Cracking
```bash
# NTLM hashes
john --format=nt hashes.txt

# Unix shadow file
unshadow passwd.txt shadow.txt > unix.txt
john --format=sha512crypt unix.txt
```

## Hydra

### Installation
```bash
# Kali Linux
sudo apt install hydra
```

### Basic Usage
```bash
# SSH brute-force
hydra -l username -P wordlist.txt ssh://TARGET_IP

# HTTP POST form
hydra -l admin -P wordlist.txt TARGET_IP http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid"

# FTP brute-force
hydra -L users.txt -P passwords.txt ftp://TARGET_IP
```

## Medusa

### Installation
```bash
# Kali Linux
sudo apt install medusa
```

### Basic Usage
```bash
# SSH brute-force
medusa -h TARGET_IP -u username -P wordlist.txt -M ssh

# FTP brute-force
medusa -h TARGET_IP -U users.txt -P passwords.txt -M ftp
```

## Custom Wordlists

### Crunch
```bash
# Generate all possible 8-character lowercase combinations
crunch 8 8 -o wordlist.txt

# Custom charset
crunch 4 6 0123456789 -o numbers.txt
```

### Cewl
```bash
# Generate wordlist from website
cewl https://example.com -d 2 -m 5 -w wordlist.txt
```

### CUPP
```bash
# Interactive mode
python3 cupp.py -i

# Generate wordlist from profile
python3 cupp.py -l user_profile.json
```

## 🛠 Tools

### Password Cracking
- **Hashcat**: Fast password recovery tool
- **John the Ripper**: Feature-rich password cracker
- **Hydra**: Network login cracker
- **Medusa**: Parallel network login cracker

### Wordlist Generation
- **Crunch**: Generate wordlists
- **Cewl**: Website wordlist generator
- **CUPP**: Common User Passwords Profiler
- **rsmangler**: Wordlist mutation tool

## 📚 Resources
- [Hashcat Wiki](https://hashcat.net/wiki/)
- [John the Ripper Documentation](https://www.openwall.com/john/doc/)
- [PentestMonkey Cheat Sheets](http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats)
- [WeakPass Wordlists](https://weakpass.com/)

## 🎯 Practice
1. Try cracking password hashes from [Crack Me If You Can](https://www.vulnhub.com/entry/crack-me-if-you-can-2019,397/)
2. Practice with [Hack The Box](https://www.hackthebox.com/) machines
3. Set up your own test environment with known passwords

## ⚠️ Legal Note
Only perform password cracking on systems you own or have explicit permission to test. Unauthorized testing is illegal.
