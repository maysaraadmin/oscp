# Passive Reconnaissance

Passive reconnaissance is the process of gathering information about a target without directly interacting with it. This phase is crucial for understanding the target's digital footprint while remaining undetected.

## 📋 Table of Contents

1. [WHOIS Lookups](#whois-lookups)
2. [DNS Reconnaissance](#dns-reconnaissance)
3. [Search Engine Reconnaissance](#search-engine-reconnaissance)
4. [Social Media & OSINT](#social-media--osint)
5. [Tools & Commands](#-tools--commands)
6. [Best Practices](#-best-practices)

## WHOIS Lookups

WHOIS lookups provide information about domain registration, including:
- Domain owner details
- Registration and expiration dates
- Name servers
- Registrar information

### Commands
```bash
whois example.com
whois -h whois.iana.org example.com
```

## DNS Reconnaissance

Gather DNS information to map out the target's infrastructure:
- DNS records (A, AAAA, MX, TXT, etc.)
- Subdomains
- DNS zone transfers

### Commands
```bash
dig example.com ANY
dig example.com AXFR @ns1.example.com
nslookup -type=any example.com
host -a example.com
```

## Search Engine Reconnaissance

Leverage search engines to find publicly available information:
- Google dorking
- Shodan/Censys searches
- GitHub/GitLab repositories
- Public documents and presentations

### Google Dorks
```
site:example.com filetype:pdf
site:example.com inurl:admin
site:example.com intitle:"index of" password
```

## Social Media & OSINT

Gather information from social media and other open sources:
- Employee information
- Technology stack
- Job postings
- Public code repositories

### Tools
- theHarvester
- Maltego
- SpiderFoot
- Recon-ng
- OSINT Framework

## 🛠 Tools & Commands

| Tool | Purpose | Example |
|------|---------|---------|
| theHarvester | Email, subdomains, IPs | `theHarvester -d example.com -b all` |
| Maltego | Visual link analysis | GUI-based |
| Recon-ng | Full-featured recon | `use recon/domains-hosts/brute_hosts` |
| dnsrecon | DNS enumeration | `dnsrecon -d example.com` |
| sublist3r | Subdomain enumeration | `sublist3r -d example.com` |

## 📝 Best Practices

1. Document all findings with timestamps
2. Use multiple tools to verify information
3. Respect robots.txt and terms of service
4. Stay within legal boundaries
5. Organize findings by type and source

## 📚 Resources

- [OSINT Framework](https://osintframework.com/)
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- [Shodan Search](https://www.shodan.io/)
- [Censys Search](https://censys.io/)
- [OSINT Dojo](https://www.osintdojo.com/)

## ⚠️ Legal Considerations

- Only gather information from public sources
- Respect privacy laws and regulations
- Do not attempt to access unauthorized systems
- Document your methodology and sources
