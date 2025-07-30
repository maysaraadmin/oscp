# Reconnaissance Techniques

This document covers various reconnaissance techniques used during the information gathering phase of penetration testing. Reconnaissance is the first and most crucial step in the penetration testing process.

## Table of Contents
- [Domain Information Gathering](#domain-information-gathering)
- [Search Engine Reconnaissance](#search-engine-reconnaissance)
- [DNS Enumeration](#dns-enumeration)
- [Network Scanning](#network-scanning)
- [Service Enumeration](#service-enumeration)
- [Automated Tools](#automated-tools)
- [Defensive Considerations](#defensive-considerations)

## Domain Information Gathering

### WHOIS Lookup
```bash
# Basic WHOIS lookup for a domain
whois example.com

# WHOIS lookup for an IP address
whois 1.1.1.1

# Using specific WHOIS server
whois example.com -h whois.verisign-grs.com
```

### DNS Information
```bash
# Basic DNS lookup (A records)
host example.com

# MX record lookup (mail servers)
host -t mx example.com

# TXT record lookup (often contains SPF, DKIM, DMARC records)
host -t txt example.com

# Name server lookup
host -t ns example.com

# Reverse DNS lookup
host 1.1.1.1
```

## Search Engine Reconnaissance

### Google Dorks
```bash
# Basic site search
site:example.com

# Search for specific file types
site:example.com filetype:pdf
site:example.com filetype:txt

# Exclude file types
site:example.com -filetype:html

# Find directory listings
intitle:"index of" "parent directory" site:example.com

# Find configuration files
site:example.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini

# Find usernames
site:example.com intext:"@example.com"
```

### Specialized Search Engines
- [Shodan](https://www.shodan.io/) - Search engine for internet-connected devices
  ```
  hostname:example.com
  hostname:example.com port:22
  ```
- [Censys](https://search.censys.io/) - Another powerful search engine for devices
- [Netcraft](https://searchdns.netcraft.com/) - For DNS and web server information
- [Security Headers](https://securityheaders.com/) - Check security headers of websites

## DNS Enumeration

### Basic DNS Queries
```bash
# Get all DNS records
host -a example.com

# Check for zone transfer vulnerability
host -l example.com ns1.example.com

# Using dig for more detailed DNS information
dig any example.com @8.8.8.8
dig axfr @ns1.example.com example.com
```

### Subdomain Enumeration
```bash
# Using sublist3r
sublist3r -d example.com -o subdomains.txt

# Using amass (more comprehensive)
amass enum -d example.com -o amass_results.txt

# Using dnsrecon
dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t brt -c dnsrecon_results.csv
```

## Network Scanning

### Basic Port Scanning
```bash
# Quick TCP scan
tcping example.com 80

# Basic nmap scan
nmap -sS -T4 example.com

# Full port scan
nmap -p- -T4 -oA full_scan example.com
```

### Service Enumeration
```bash
# Service version detection
nmap -sV -sC -p- -oA service_scan example.com

# NSE scripts for common vulnerabilities
nmap --script vuln -p- -oA vuln_scan example.com
```

## Service-Specific Enumeration

### HTTP/HTTPS Services
```bash
# Check HTTP methods
curl -X OPTIONS http://example.com/ -v

# Check for directory listing
curl http://example.com/

# Check for common files
gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt
```

### SMTP Enumeration
```bash
# Connect to SMTP server
nc -nv 1.1.1.1 25

# Check for open relay
telnet 1.1.1.1 25
HELO test.com
MAIL FROM: test@test.com
RCPT TO: user@example.com
```

## Automated Tools

### Comprehensive Recon Tools
```bash
# TheHarvester - Email, subdomains, IPs, and more
theharvester -d example.com -b google -l 500 -f results.html

# Recon-ng - Full-featured web reconnaissance framework
recon-ng
> workspaces create example
> use recon/domains-hosts/brute_hosts
> set SOURCE example.com
> run
```

## Defensive Considerations

1. **Limit Public Information**
   - Use WHOIS privacy services
   - Limit information in DNS records
   - Regularly audit public-facing information

2. **Harden DNS Configuration**
   - Disable zone transfers to unauthorized hosts
   - Implement DNSSEC
   - Monitor for DNS queries and zone transfer attempts

3. **Network Monitoring**
   - Set up alerts for port scans and enumeration attempts
   - Monitor logs for suspicious activities
   - Implement rate limiting where possible

4. **Service Hardening**
   - Disable unnecessary services
   - Keep all services updated
   - Implement proper access controls

## Additional Resources
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [DNS Reconnaissance Techniques](https://book.hacktricks.xyz/network-services-pentesting/pentesting-dns)

Remember to always get proper authorization before performing any of these techniques on systems you don't own or have explicit permission to test.

---------------------------------------------------------------------
whois example.com -h 192.168.1.1
---------------------------------------------------------------------
whois 1.1.1.1 -h 1.1.1.1
---------------------------------------------------------------------
site: example.com
---------------------------------------------------------------------
site: example.com filetype:txt
---------------------------------------------------------------------
site:example.com -filetype:html
---------------------------------------------------------------------
intitle:"index of" "parent directory"
---------------------------------------------------------------------
https://searchdns.netcraft.com
---------------------------------------------------------------------
filename:users
---------------------------------------------------------------------
https://www.shodan.io/
---------------------------------------------------------------------
 hostname:example.com
 ---------------------------------------------------------------------
hostname:example.com port :"22"
--------------------------------------------------------------------
https://securityheaders.com/
---------------------------------------------------------------------
host example.com
---------------------------------------------------------------------
host -t mx example.com
---------------------------------------------------------------------
host -t txt example.com
---------------------------------------------------------------------
host www.example.com
---------------------------------------------------------------------
host idontexit.example.com
---------------------------------------------------------------------
cat list.txt
---------------------------------------------------------------------
 for ip in $(cat list.txt); do host $ip.example.com; done
--------------------------------------------------------------------- 
for ip in $(seq 200 254); do host 1.1.1.$ip; done | grep -v "not
found"
---------------------------------------------------------------------
dnsrecon -d example.com -t std
---------------------------------------------------------------------
cat list.txt
---------------------------------------------------------------------
dnsrecon -d example.com -D ~/list.txt -t brt
---------------------------------------------------------------------
dnsenum example.com
---------------------------------------------------------------------
nslookup mail.example.com
---------------------------------------------------------------------
nslookup 1.1.1.1 -type=TXT info.example.com  1.1.1.1
---------------------------------------------------------------------
 nc -nvv -w 1 -z 1.1.1.1 3388-3390
---------------------------------------------------------------------
  nc -nv -u -z -w 1 1.1.1.1 120-123
---------------------------------------------------------------------
  namp 1.1.1.1
---------------------------------------------------------------------
  namp -sT 1.1.1.1
---------------------------------------------------------------------
 nmap -sU 1.1.1.1
---------------------------------------------------------------------
nmap -sU -sS 1.1.1.1
---------------------------------------------------------------------
nmap -sn 1.1.1.1
---------------------------------------------------------------------
 nmap -v -sn 1.1.1.1-253 -oG ping-sweep.txt
---------------------------------------------------------------------
 grep Up ping-sweep.txt | cut -d " " -f 2
---------------------------------------------------------------------
 namp -p 80 1.1.1.1-253 -oG web-sweep.txt 
---------------------------------------------------------------------
 grep open web-sweep.txt | cut -d" " -f2
---------------------------------------------------------------------
 nmap -sT -A --top-ports=20 1.1.1.1-253 -oG top-port-sweep.txt
---------------------------------------------------------------------
 cat /usr/share/nmap/nmap-services
 ---------------------------------------------------------------------
  nmap -O 1.1.1.14 --osscan-guess
---------------------------------------------------------------------
 nmap -sT -A 1.1.1.1
---------------------------------------------------------------------
 nmap --script http-headers 1.1.1.1
---------------------------------------------------------------------
 namp --script-help https-headers
---------------------------------------------------------------------
 Test-NetConnection -Port 445 1.1.1.1
---------------------------------------------------------------------
nmap -v -p 139,445 -oG smb.txt 1.1.1.1-254
 ---------------------------------------------------------------------
 nbtscan -r 1.1.1.1/24
---------------------------------------------------------------------
 ls -1 /usr/share/nmap/scripts/smb*
---------------------------------------------------------------------
 nmap -v -p 139,445 --script smb-os-discovery 1.1.1.1
---------------------------------------------------------------------
 net view \\dc01 /all
---------------------------------------------------------------------
  nc -nv 1.1.1.1 25
---------------------------------------------------------------------
 Test-NetConnection -Port 25 1.1.1.1
---------------------------------------------------------------------
dism /online /Enable-Feature /FeatureName:TelnetClient
...
---------------------------------------------------------------------
telnet 1.1.1.1 25
---------------------------------------------------------------------
 nmap -sU --open -p 161 1.1.1.1-254 -oG open-snmp.txt
---------------------------------------------------------------------
 for ip in i $(seq 1 254); do echo 1.1.1.$ip; done > ips
---------------------------------------------------------------------
onesixtyone  -c community -i ips
---------------------------------------------------------------------
 snmpwalk -c public -v1 -t 10 1.1.1.1
---------------------------------------------------------------------
snmpwalk -c public -v1 1.1.1.1. 
---------------------------------------------------------------------