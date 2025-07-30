# Scanning

This directory contains notes and techniques for the scanning phase of penetration testing, focusing on identifying open ports, services, and vulnerabilities.

## Contents

- [Nmap Cheatsheet](nmap_cheatsheet.md) - Quick reference for Nmap commands
- [Vulnerability Scanning](vulnerability_scanning.md) - Techniques for identifying vulnerabilities

## Key Concepts

- **Port Scanning**: Identifying open ports and services
- **Service Version Detection**: Determining service versions
- **Vulnerability Assessment**: Identifying potential vulnerabilities
- **Network Mapping**: Creating a map of the target network

## Tools

- `nmap`
- `masscan`
- `unicornscan`
- `nikto` (for web applications)
- `OpenVAS` (for vulnerability scanning)

## Best Practices

- Always understand what each scan does before running it
- Be mindful of network traffic and potential impact on target systems
- Document all scan results for later reference
- Use different scan types to get a complete picture
- Respect rate limiting to avoid detection or service disruption
