# Passive Reconnaissance

Passive reconnaissance involves gathering information about a target without directly interacting with the target's systems. This phase is crucial for understanding the target's digital footprint while remaining undetected.

## WHOIS Lookups

```bash
# Basic WHOIS lookup
domain="example.com"
whois $domain

# Using whois with specific server
whois example.com -h whois.verisign-grs.com

# WHOIS lookup for IP address
whois 192.168.1.1 -h whois.arin.net
```

## DNS Enumeration

```bash
# Basic DNS lookups
host example.com
host -t mx example.com      # Mail servers
host -t txt example.com     # TXT records
host -t ns example.com      # Name servers

# Reverse DNS lookup
host 8.8.8.8

# Using dig for detailed DNS information
dig example.com ANY +noall +answer
dig example.com MX +short

# DNS zone transfer attempt
dig axfr @ns1.example.com example.com
```

## Search Engine Reconnaissance

### Google Dorks
```
site:example.com
site:example.com filetype:pdf
site:example.com -www
intitle:"index of" "parent directory"
inurl:admin site:example.com
site:example.com intext:"username" OR "password"
```

### Shodan
```
# Basic search
hostname:example.com

# Search by service
http.title:"Example"
http.html:"login"

# Search by vulnerability
vuln:CVE-2014-0160
```

## Certificate Transparency Logs

```bash
# Using crt.sh
curl -s "https://crt.sh/?q=example.com&output=json" | jq '.[].name_value' | sort -u

# Using certspotter
curl -s "https://certspotter.com/api/v0/certs?domain=example.com" | jq '.[].dns_names[]' | sort -u
```

## Email Harvesting

```bash
# Using theHarvester
theHarvester -d example.com -b google,linkedin,pgp

# Using hunter.io (API required)
# hunter.io provides a web interface and API for email discovery
```

## Social Media & People Search

- LinkedIn: Search for employees and company information
- GitHub: Search for code, repositories, and potential leaks
- Twitter: Monitor for mentions and employee activity
- HaveIBeenPwned: Check for breached accounts

## Subdomain Enumeration

```bash
# Using Sublist3r
python3 sublist3r.py -d example.com -o subdomains.txt

# Using assetfinder
export API_KEY=your_virustotal_api_key
assetfinder --subs-only example.com | sort -u > subdomains.txt

# Using amass (passive mode)
amass enum -passive -d example.com -o amass_results.txt

# Using subfinder
subfinder -d example.com -o subfinder_results.txt
```

## Passive Vulnerability Assessment

```bash
# Using Nmap NSE scripts (non-intrusive)
nmap --script dns-brute.nse example.com

# Using Nikto (in safe mode)
nikto -h example.com -Tuning x 6
```

## Tools for Passive Recon

1. **Recon-ng**
   ```
   marketplace install all
   modules load recon/domains-hosts/brute_hosts/brute_hosts
   options set SOURCE example.com
   run
   ```

2. **Maltego**
   - Visual link analysis tool
   - Great for mapping relationships

3. **SpiderFoot**
   ```
   python3 sf.py -s example.com -q
   ```

## Legal Considerations

- Always check the terms of service for each tool and service
- Respect robots.txt files
- Be aware of rate limiting
- Document all findings with timestamps

## Reporting

Always document your findings in a structured format:

```markdown
## Passive Reconnaissance Report
- **Date**: [Date]
- **Target**: example.com

### Subdomains Found
- sub1.example.com
- sub2.example.com

### Email Addresses
- user@example.com
- admin@example.com

### Public IPs
- 192.0.2.1
- 198.51.100.1

### Potential Vulnerabilities
- Outdated software versions
- Exposed administrative interfaces

### Recommendations
- Review and update DNS records
- Implement rate limiting
- Monitor certificate transparency logs
```

## Resources

- [OWASP Testing Guide - Information Gathering](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/01-Information_Gathering/)
- [DNS Dumpster](https://dnsdumpster.com/)
- [ViewDNS.info](https://viewdns.info/)
- [SecurityTrails](https://securitytrails.com/)
