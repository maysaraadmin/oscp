# OSINT Techniques

Open Source Intelligence (OSINT) involves collecting and analyzing publicly available information about a target. This information can be used to build a comprehensive profile of the target organization, its employees, and its digital footprint.

## 📋 Table of Contents

1. [People and Organizations](#people-and-organizations)
2. [Email and Username Enumeration](#email-and-username-enumeration)
3. [Social Media Intelligence](#social-media-intelligence)
4. [Code and Document Search](#code-and-document-search)
5. [Tools & Resources](#-tools--resources)
6. [Best Practices](#-best-practices)

## People and Organizations

### Company Information
- Official websites and subdomains
- Business registries
- Financial records
- Job postings
- Press releases

### Employee Information
- LinkedIn profiles
- Company directories
- Conference talks and publications
- GitHub/GitLab contributions

### Commands
```bash
# theHarvester for domain and email enumeration
theHarvester -d example.com -b google,linkedin,github

# Hunter.io for email pattern discovery
# Visit: https://hunter.io/

# BuiltWith for technology profiling
# Visit: https://builtwith.com/
```

## Email and Username Enumeration

### Email Discovery
- Pattern guessing (first.last@, f.last@, etc.)
- Breach databases
- Public PGP keys
- GitHub commits

### Username Enumeration
- Social media platforms
- Code repositories
- Forum posts
- Paste sites

### Commands
```bash
# Holehe for email checking
holehe --only-used example@example.com

# sherlock for username enumeration
python3 sherlock username

# GHunt for Google account information
python3 ghunt email example@example.com
```

## Social Media Intelligence

### Platform-Specific Search
- Twitter advanced search
- LinkedIn company pages and employees
- Facebook Graph Search
- Instagram geolocation data

### Tools
- Maltego for visualization
- SpiderFoot for automated OSINT
- Social-Engineer Toolkit (SET)
- Twint for Twitter intelligence

## Code and Document Search

### Code Repositories
- GitHub/GitLab/Bitbucket search
- Commit history
- API keys and credentials
- Configuration files

### Document Search
- Google Dorking
- Shodan/Censys
- Public document repositories
- Wayback Machine archives

### Commands
```bash
# Gitrob for GitHub repository scanning
gitrob example-org

# TruffleHog for finding secrets
trufflehog --regex --entropy=False https://github.com/example/repo.git

# Googler for Google searches
googler -w example.com
```

## 🛠 Tools & Resources

| Tool | Purpose | Link |
|------|---------|------|
| theHarvester | Email and domain enumeration | [GitHub](https://github.com/laramies/theHarvester) |
| Maltego | Link analysis and data mining | [Website](https://www.maltego.com/) |
| SpiderFoot | OSINT automation | [GitHub](https://github.com/smicallef/spiderfoot) |
| Recon-ng | Full-featured recon framework | [GitHub](https://github.com/lanmaster53/recon-ng) |
| sherlock | Username enumeration | [GitHub](https://github.com/sherlock-project/sherlock) |
| Holehe | Check email accounts | [GitHub](https://github.com/megadose/holehe) |
| GHunt | Google account investigation | [GitHub](https://github.com/mxrch/GHunt) |
| OSINT Framework | Collection of OSINT tools | [Website](https://osintframework.com/) |

## 📝 Best Practices

1. Document all findings with timestamps and sources
2. Use multiple sources to verify information
3. Respect privacy and terms of service
4. Organize findings by category and reliability
5. Maintain a clean separation between different targets
6. Use virtual machines or containers for tools
7. Keep tools and wordlists updated

## 📚 Resources

- [OSINT Framework](https://osintframework.com/)
- [Awesome OSINT](https://github.com/jivoi/awesome-osint)
- [IntelTechniques Tools](https://inteltechniques.com/tools/)
- [OSINT Dojo](https://www.osintdojo.com/)
- [Bellingcat's Online Investigation Toolkit](https://docs.google.com/spreadsheets/d/18rtqh8EG2q1xBo2cLNyhIDuK9jrPGWFYF4w0j9F7wA4/)

## ⚠️ Legal and Ethical Considerations

- Only collect publicly available information
- Respect privacy laws (GDPR, CCPA, etc.)
- Do not engage in harassment or doxxing
- Document your methodology and sources
- Be prepared to explain your actions and findings
