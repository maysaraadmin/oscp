# DNS Enumeration

DNS enumeration is the process of locating all DNS servers and DNS records for an organization. This information helps map the organization's network and identify potential targets.

## Table of Contents
- [Basic DNS Queries](#basic-dns-queries)
  - [Using `host` command](#using-host-command)
  - [Using `dig` command](#using-dig-command)
  - [Using `nslookup`](#using-nslookup)
- [Advanced Enumeration](#advanced-enumeration)
  - [Zone Transfers](#zone-transfers)
  - [Subdomain Enumeration](#subdomain-enumeration)
  - [Brute Forcing Subdomains](#brute-forcing-subdomains)
- [Practical Examples](#practical-examples)
- [Common Tools](#common-tools)
- [Defensive Considerations](#defensive-considerations)

## Basic DNS Queries

### Using `host` command
```bash
# Basic DNS lookup (A record)
host example.com

# Find mail servers (MX records)
host -t mx example.com

# Find name servers (NS records)
host -t ns example.com

# Find text records (TXT records, often used for verification)
host -t txt example.com

# Find all records
host -a example.com

# Find PTR record (reverse DNS lookup)
host 8.8.8.8

# Find CNAME records
host -t cname www.example.com
```

### Using `dig` command
```bash
# Basic DNS lookup (A record)
dig example.com

# Query specific DNS server
dig @8.8.8.8 example.com

# Specific record types (MX, NS, TXT, etc.)
dig example.com MX
dig example.com NS
dig example.com TXT

# Detailed output with +trace for DNS resolution path
dig +trace example.com

# Short output format
dig +short example.com

# Query all record types
dig example.com ANY
```

### Using `nslookup`
```bash
# Interactive mode
nslookup
> set type=any
> example.com
> exit

# Command-line mode
nslookup -type=MX example.com
nslookup -type=NS example.com
nslookup -type=TXT example.com
```

## Advanced Enumeration

### Zone Transfers
Zone transfers replicate DNS records across DNS servers. If not properly secured, they can leak internal network information.

```bash
# Attempt a zone transfer using host
host -l example.com ns1.example.com

# Using dig for zone transfer
dig axfr @ns1.example.com example.com

# Using nslookup
nslookup
> server ns1.example.com
> set type=any
> ls -d example.com
```

### Subdomain Enumeration
```bash
# Using Google dorks
site:*.example.com

# Using sublist3r
sublist3r -d example.com -o subdomains.txt

# Using amass (more comprehensive)
amass enum -d example.com -o subdomains_amass.txt
```

### Brute Forcing Subdomains
```bash
# Using dnsrecon
dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t brt -c dnsrecon_results.csv

# Using gobuster
gobuster dns -d example.com -w /usr/share/wordlists/subdomains-top1m-5000.txt -o gobuster_results.txt
```

## Practical Examples

### Example 1: Basic DNS Recon
```bash
# Start with basic enumeration
host example.com
host -t mx example.com
host -t ns example.com
host -t txt example.com

# Try zone transfer on each nameserver
for ns in $(host -t ns example.com | cut -d' ' -f4); do
    echo "Trying zone transfer on $ns"
    host -l example.com $ns
    dig axfr @$ns example.com
done
```

### Example 2: Automated Enumeration Script
```bash
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <domain>"
    exit 1
fi

domain=$1
output_dir="dns_enum_$domain"
mkdir -p "$output_dir"

echo "[+] Starting DNS enumeration for $domain"

# Basic DNS records
echo "[+] Gathering basic DNS records"
host "$domain" > "$output_dir/basic_records.txt"
host -t mx "$domain" >> "$output_dir/basic_records.txt"
host -t ns "$domain" >> "$output_dir/basic_records.txt"
host -t txt "$domain" >> "$output_dir/basic_records.txt"

# Zone transfer attempts
echo "[+] Attempting zone transfers"
for ns in $(host -t ns "$domain" | cut -d' ' -f4); do
    echo "Trying zone transfer on $ns"
    host -l "$domain" "$ns" > "$output_dir/zone_transfer_${ns}.txt"
    dig axfr "@$ns" "$domain" >> "$output_dir/zone_transfer_dig_${ns}.txt"
done

echo "[+] DNS enumeration complete. Results saved to $output_dir/"
```

## Common Tools

1. **dnsrecon** - Comprehensive DNS enumeration tool
   ```bash
   dnsrecon -d example.com -t std,axfr,brt -D /usr/share/wordlists/dnsmap.txt -c results.csv
   ```

2. **Fierce** - DNS reconnaissance tool
   ```bash
   fierce --domain example.com --subdomains accounts,api,dev,staging
   ```

3. **Sublist3r** - Fast subdomains enumeration tool
   ```bash
   sublist3r -d example.com -o subdomains.txt
   ```

4. **Amass** - In-depth attack surface mapping
   ```bash
   amass enum -d example.com -o amass_results.txt
   ```

5. **MassDNS** - High-performance DNS stub resolver
   ```bash
   cat subdomains.txt | massdns -r /path/to/resolvers.txt -t A -o S -w results.txt
   ```

## Defensive Considerations

1. **Prevent Zone Transfers**
   - Restrict zone transfers to authorized servers only
   - Use Access Control Lists (ACLs) on DNS servers

2. **DNS Security Extensions (DNSSEC)**
   - Implement DNSSEC to prevent DNS spoofing
   - Validate DNS responses

3. **Logging and Monitoring**
   - Monitor for unusual DNS queries
   - Set up alerts for zone transfer attempts
   - Log all DNS queries for analysis

4. **Network Segmentation**
   - Place DNS servers in a DMZ
   - Implement network segmentation to limit exposure

5. **Regular Audits**
   - Regularly audit DNS configurations
   - Remove unnecessary DNS records
   - Update DNS software to patch vulnerabilities
dig example.com A      # IPv4 address
dig example.com AAAA   # IPv6 address
dig example.com MX     # Mail servers
dig example.com NS     # Name servers
dig example.com TXT    # Text records

# Query specific DNS server
dig @8.8.8.8 example.com

# Detailed output with all sections
dig example.com ANY +noall +answer

# Short output
dig +short example.com
```

## Zone Transfer Testing

Zone transfers (AXFR) replicate DNS data across DNS servers. Misconfigured DNS servers may allow anyone to perform a zone transfer, revealing all records for the domain.

### Testing for Zone Transfers
```bash
# Find name servers first
host -t ns example.com

# Attempt zone transfer on each name server
for ns in $(host -t ns example.com | cut -d" " -f4); do
    echo "Trying $ns";
    dig @$ns example.com axfr;
done

# Using dnsrecon for zone transfer
dnsrecon -d example.com -t axfr
```

## Subdomain Enumeration

### Using `dnsrecon`
```bash
# Basic enumeration
dnsrecon -d example.com

# Brute force subdomains
dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t brt

# Reverse DNS lookup for IP range
dnsrecon -r 192.168.1.0/24 -n 8.8.8.8
```

### Using `sublist3r`
```bash
# Basic usage
python3 sublist3r.py -d example.com -o subdomains.txt

# Enable all search engines
python3 sublist3r.py -d example.com -e all -o all_subdomains.txt
```

### Using `amass`
```bash
# Passive enumeration
amass enum -passive -d example.com -o amass_passive.txt

# Active enumeration (more thorough but noisier)
amass enum -active -d example.com -o amass_active.txt

# Visualize results
amass viz -d3 -d example.com -o amass_viz.html
```

## DNS Brute Forcing

### Using `dnsrecon`
```bash
dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t brt
```

### Using `gobuster`
```bash
gobuster dns -d example.com -w /usr/share/wordlists/dnsmap.txt -t 50 -o gobuster_dns.txt
```

### Using `ffuf`
```bash
ffuf -u http://FUZZ.example.com -w /usr/share/wordlists/dnsmap.txt -o fuzzed_domains.json
```

## DNS Cache Snooping

Check if a DNS server has cached a specific domain (indicates recent visits):
```bash
dig @dns-server example.com A +norecurse
```

## DNS Recon with Online Services

1. **SecurityTrails** - Comprehensive DNS historical data
   ```bash
   # Using SecurityTrails API
   curl "https://api.securitytrails.com/v1/domain/example.com" \
     -H "apikey: your_api_key"
   ```

2. **VirusTotal** - Check domain reputation and related domains
   ```bash
   # Using VirusTotal API
   curl --request GET \
     --url https://www.virustotal.com/api/v3/domains/example.com \
     --header 'x-apikey: your_api_key'
   ```

3. **ViewDNS.info** - Various DNS tools
   - https://viewdns.info/

## DNS Record Types to Check

| Record Type | Purpose | Example Command |
|-------------|---------|-----------------|
| A | IPv4 Address | `host -t A example.com` |
| AAAA | IPv6 Address | `host -t AAAA example.com` |
| MX | Mail Servers | `host -t MX example.com` |
| NS | Name Servers | `host -t NS example.com` |
| TXT | Text Records | `host -t TXT example.com` |
| CNAME | Canonical Name | `host -t CNAME example.com` |
| SOA | Start of Authority | `host -t SOA example.com` |
| PTR | Reverse DNS | `host -t PTR 1.1.1.1` |
| SRV | Service Records | `host -t SRV _ldap._tcp.example.com` |

## Automating DNS Enumeration

### Bash Script for Comprehensive DNS Enumeration
```bash
#!/bin/bash

domain=$1
output_dir="dns_enum_$domain"

# Create output directory
mkdir -p $output_dir

# Basic DNS records
echo "[+] Running basic DNS lookups..."
for type in A AAAA MX NS TXT SOA; do
    echo "  [+] $type records"
    host -t $type $domain | tee -a $output_dir/dns_records.txt
    echo ""
done

# Check for zone transfer
echo "[+] Testing for zone transfers..."
for ns in $(host -t ns $domain | cut -d" " -f4); do
    echo "  [+] Testing $ns"
    dig @$ns $domain axfr | tee -a $output_dir/zone_transfer.txt
done

# Subdomain enumeration
echo "[+] Enumerating subdomains..."
for word in $(cat /usr/share/wordlists/dnsmap.txt); do
    host "$word.$domain" | grep "has address" | tee -a $output_dir/subdomains.txt
done

echo "[+] DNS enumeration complete. Results saved to $output_dir/"
```

## Common DNS Tools

1. **dnsrecon** - Comprehensive DNS enumeration
2. **dnswalk** - DNS debugger
3. **fierce** - DNS reconnaissance tool
4. **dnsenum** - DNS enumeration tool
5. **sublist3r** - Subdomain enumeration tool
6. **amass** - In-depth attack surface mapping
7. **massdns** - High-performance DNS stub resolver

## Defensive Countermeasures

1. **Restrict Zone Transfers**
   - Only allow zone transfers to authorized DNS servers
   - Use TSIG (Transaction Signature) for secure zone transfers

2. **Rate Limiting**
   - Implement rate limiting on DNS queries
   - Block excessive queries from single IPs

3. **DNS Monitoring**
   - Monitor for unusual DNS queries
   - Set up alerts for zone transfer attempts

4. **DNSSEC**
   - Implement DNSSEC to prevent DNS spoofing
   - Validate DNS responses

## Reporting DNS Enumeration Results

```markdown
# DNS Enumeration Report
- **Date**: [Date]
- **Target Domain**: example.com

## Name Servers
1. ns1.example.com (192.168.1.1)
2. ns2.example.com (192.168.1.2)

## Mail Servers
1. mail.example.com (10.0.0.1)
   - Priority: 10

## Subdomains Found
- www.example.com
- mail.example.com
- dev.example.com
- test.example.com

## Security Issues
1. **Zone Transfer Vulnerability**
   - **Risk**: High
   - **Description**: Zone transfers are allowed to any IP address
   - **Recommendation**: Restrict zone transfers to authorized servers only

2. **Exposed Internal Infrastructure**
   - **Risk**: Medium
   - **Description**: Internal hostnames are exposed in DNS records
   - **Recommendation**: Use split-horizon DNS for internal/external resolution

## Recommendations
1. Implement DNSSEC
2. Review and update DNS records
3. Monitor DNS queries for suspicious activity
4. Restrict zone transfers to authorized servers only
```

## Resources

- [DNS Security Extensions (DNSSEC)](https://www.cloudflare.com/dns/dnssec/)
- [OWASP DNS Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DNS_Security_Cheat_Sheet.html)
- [IANA DNS Parameters](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)
