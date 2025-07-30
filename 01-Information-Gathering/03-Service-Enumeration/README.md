# Service Enumeration

Service enumeration is the process of identifying and gathering detailed information about network services running on target systems. This phase helps identify potential vulnerabilities and misconfigurations in services.

## 📋 Table of Contents

1. [Common Services](#common-services)
2. [Service-Specific Enumeration](#service-specific-enumeration)
3. [Banner Grabbing](#banner-grabbing)
4. [Vulnerability Identification](#vulnerability-identification)
5. [Tools & Commands](#-tools--commands)
6. [Best Practices](#-best-practices)

## Common Services

### Web Services (HTTP/HTTPS)
- Web server software (Apache, Nginx, IIS)
- Web application frameworks
- Directory and file enumeration
- Web technologies in use

### File Sharing Services
- SMB/CIFS (Windows file sharing)
- NFS (Network File System)
- FTP/FTPS/SFTP

### Remote Access Services
- SSH (Secure Shell)
- RDP (Remote Desktop Protocol)
- VNC (Virtual Network Computing)
- Telnet

### Database Services
- MySQL/MariaDB
- Microsoft SQL Server
- PostgreSQL
- Oracle
- MongoDB

## Service-Specific Enumeration

### SMB Enumeration
```bash
# List shares
smbclient -L //192.168.1.100 -N

# Connect to a share
smbclient //192.168.1.100/share -N

# Nmap SMB scripts
nmap --script=smb-enum-shares,smb-enum-users,smb-os-discovery -p139,445 192.168.1.100
```

### FTP Enumeration
```bash
# Anonymous FTP check
ftp 192.168.1.100
# Username: anonymous
# Password: anonymous@

# Nmap FTP scripts
nmap --script=ftp-anon,ftp-brute,ftp-vsftpd-backdoor -p21 192.168.1.100
```

### SSH Enumeration
```bash
# SSH version check
nc -nv 192.168.1.100 22

# Nmap SSH scripts
nmap --script=ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -p22 192.168.1.100
```

## Banner Grabbing

### Manual Banner Grabbing
```bash
# Using netcat
nc -nv 192.168.1.100 80
GET / HTTP/1.1
Host: example.com

# Using telnet
telnet 192.168.1.100 80
GET / HTTP/1.1
Host: example.com
```

### Automated Banner Grabbing
```bash
# Nmap service detection
nmap -sV --version-intensity 5 -p- 192.168.1.100

# Nmap banner grab script
nmap --script=banner -p- 192.168.1.100
```

## Vulnerability Identification

### Common Vulnerabilities
- Default credentials
- Outdated software versions
- Misconfigurations
- Known vulnerabilities (CVE)

### Vulnerability Scanning
```bash
# Nmap vulnerability scripts
nmap --script=vuln -p- 192.168.1.100

# Search for known exploits
searchsploit "apache 2.4.29"
```

## 🛠 Tools & Commands

| Tool | Purpose | Example |
|------|---------|---------|
| Nmap | Service detection | `nmap -sV -sC -p- 192.168.1.100` |
| smbclient | SMB enumeration | `smbclient -L //192.168.1.100 -N` |
| enum4linux | Windows/Samba enumeration | `enum4linux -a 192.168.1.100` |
| Searchsploit | Exploit database search | `searchsploit apache 2.4.29` |
| Nikto | Web server scanning | `nikto -h http://192.168.1.100` |

## 📝 Best Practices

1. Document all discovered services and versions
2. Check for default credentials
3. Look for known vulnerabilities in the identified versions
4. Be thorough but mindful of service impact
5. Organize findings by service type and potential risk

## 📚 Resources

- [Nmap Scripting Engine](https://nmap.org/book/nse.html)
- [SANS Ports and Services](https://www.sans.org/security-resources/tcpip.pdf)
- [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/)
- [CVE Details](https://www.cvedetails.com/)

## ⚠️ Legal Considerations

- Only enumerate services on systems you own or have permission to test
- Be aware of and comply with all applicable laws and regulations
- Document your authorization and scope
- Be prepared to provide evidence of authorization if questioned
