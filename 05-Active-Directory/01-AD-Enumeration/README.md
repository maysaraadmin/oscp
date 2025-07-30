# Active Directory Enumeration

Active Directory (AD) enumeration is the process of gathering information about an AD environment. This guide covers techniques and tools for enumerating AD to identify potential attack vectors.

## 📋 Table of Contents
1. [Basic Concepts](#basic-concepts)
2. [Enumeration Without Credentials](#enumeration-without-credentials)
3. [Enumeration With Credentials](#enumeration-with-credentials)
4. [BloodHound](#bloodhound)
5. [Tools](#-tools)
6. [Practice](#-practice)

## Basic Concepts

### Key AD Components
- **Domain Controller (DC)**: Server that responds to authentication requests
- **Domain**: Collection of objects (users, groups, computers) that share a directory database
- **Forest**: Collection of domains that share a common schema and configuration
- **Organizational Unit (OU)**: Container for organizing AD objects
- **Group Policy Object (GPO)**: Collection of settings that define system behavior

### Common Naming Conventions
- **sAMAccountName**: User's login name (e.g., jdoe)
- **User Principal Name (UPN)**: Email-style login (e.g., jdoe@corp.local)
- **Distinguished Name (DN)**: Full path to an object (e.g., CN=John Doe,CN=Users,DC=corp,DC=local)
- **Security Identifier (SID)**: Unique identifier for security principals

## Enumeration Without Credentials

### Port Scanning
```bash
# Common AD ports
nmap -p 53,88,135,139,389,445,636,3268,3269 -sV -sC -oA ad_ports TARGET_IP
```

### RPC Client
```bash
rpcclient -U "" -N TARGET_IP
    enumdomusers
    enumdomgroups
    querydispinfo
    srvinfo
```

### LDAP Anonymous Binds
```bash
# Basic LDAP query
ldapsearch -x -H ldap://TARGET_IP -b "DC=corp,DC=local"

# Search for users
ldapsearch -x -H ldap://TARGET_IP -b "DC=corp,DC=local" "(objectClass=user)"
```

### SMB Enumeration
```bash
# List shares
smbclient -L //TARGET_IP -N

# Connect to a share
smbclient //TARGET_IP/ShareName -N

# Enumerate SMB with enum4linux
enum4linux -a TARGET_IP
```

## Enumeration With Credentials

### PowerView
```powershell
# Import module
Import-Module .\PowerView.ps1

# Get domain info
Get-NetDomain
Get-NetForest

# Enumerate users
Get-NetUser | select cn,description,lastlogon,logoncount,memberof

# Enumerate groups
Get-NetGroup -GroupName "Domain Admins"

# Find interesting shares
Find-InterestingDomainShareFile

# Check for constrained delegation
Get-DomainComputer -TrustedToAuth | select name,msds-allowedtodelegateto
```

### ActiveDirectory Module
```powershell
# Get domain info
Get-ADDomain

# Get domain users
Get-ADUser -Filter * -Properties * | select name,description,memberof

# Get domain computers
Get-ADComputer -Filter * -Properties *

# Get domain groups
Get-ADGroup -Filter * | select name

# Get group members
Get-ADGroupMember -Identity "Domain Admins" -Recursive
```

## BloodHound

### Data Collection
```powershell
# Using SharpHound (C#)
.\SharpHound.exe -c All

# Using PowerShell
Invoke-BloodHound -CollectionMethod All

# Using Python
bloodhound-python -d corp.local -u user -p 'password' -ns 10.10.10.10 -c All
```

### Analysis
1. **Shortest Path to Domain Admins**: Find quickest path to DA
2. **Kerberoastable Users**: Users with SPNs that can be kerberoasted
3. **AS-REP Roastable Users**: Users with Kerberos pre-authentication disabled
4. **Unconstrained Delegation**: Find computers with unconstrained delegation
5. **DCSync Rights**: Users with replication rights

## 🛠 Tools

### Enumeration Tools
- **PowerView**: PowerShell AD enumeration
- **BloodHound/SharpHound**: Visualize AD attack paths
- **Impacket**: Python tools for AD attacks
- **CrackMapExec**: Swiss army knife for AD environments
- **ADExplorer**: GUI tool for AD exploration
- **ldapsearch**: Command-line LDAP queries
- **rpcclient**: Samba tool for RPC enumeration

## 📚 Resources
- [HackTricks - Active Directory Methodology](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology)
- [PayloadsAllTheThings - Active Directory](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md)
- [BloodHound Documentation](https://bloodhound.readthedocs.io/)
- [AD Security - The Most Common Active Directory Security Issues](https://adsecurity.org/?p=3458)

## 🎯 Practice
1. [TryHackMe - Attacktive Directory](https://tryhackme.com/room/attacktivedirectory)
2. [Hack The Box - Active Directory Machines](https://www.hackthebox.com/)
3. [VulnHub - Flick](https://www.vulnhub.com/entry/flick-2,514/)

## ⚠️ Legal Note
Only perform AD enumeration on systems you own or have explicit permission to test. Unauthorized testing is illegal.
