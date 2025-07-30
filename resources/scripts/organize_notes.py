import os
import shutil
from pathlib import Path

# Define the new directory structure
structure = {
    "01-Information-Gathering": [
        "01-Passive-Recon",
        "02-Active-Recon",
        "03-Service-Enumeration",
        "04-Web-App-Enumeration",
        "05-OSINT-Techniques"
    ],
    "02-Vulnerability-Assessment": [
        "01-Manual-Identification",
        "02-Automated-Scanning",
        "03-Common-Vulnerabilities",
        "04-Risk-Assessment",
        "05-Buffer-Overflows"
    ],
    "03-Exploitation": [
        "01-Client-Side-Attacks",
        "02-Web-Exploitation",
        "03-Password-Attacks",
        "04-Exploit-Development"
    ],
    "04-Post-Exploitation": [
        "01-Linux-Privilege-Escalation",
        "02-Windows-Privilege-Escalation",
        "03-Lateral-Movement"
    ],
    "05-Active-Directory": [
        "01-Enumeration",
        "02-Initial-Access",
        "03-Lateral-Movement",
        "04-Domain-Privilege-Escalation"
    ],
    "06-Password-Cracking": [
        "01-Hash-Types",
        "02-Password-Cracking-Tools",
        "03-Password-Spraying",
        "04-Wordlist-Generation"
    ],
    "07-Network-Attacks": [
        "01-MITM-Attacks",
        "02-Network-Sniffing",
        "03-VPN-Tunneling",
        "04-Firewall-Evasion"
    ],
    "08-Metasploit": [
        "01-Introduction",
        "02-Payloads",
        "03-Post-Exploitation"
    ],
    "09-Reporting": [
        "01-Report-Writing",
        "02-Proof-Collection",
        "03-Remediation"
    ],
    "10-Practice-Labs": [
        "01-Vulnerable-Machines",
        "02-Proof-of-Concepts",
        "03-Exam-Preparation"
    ],
    "resources": [
        "cheatsheets",
        "scripts",
        "wordlists"
    ]
}

# Create the directory structure
base_path = Path(__file__).parent

for parent, children in structure.items():
    (base_path / parent).mkdir(exist_ok=True)
    for child in children:
        (base_path / parent / child).mkdir(exist_ok=True, parents=True)
    
    # Add README to parent directories
    with open(base_path / parent / "README.md", "w") as f:
        f.write(f"# {parent.replace('-', ' ')}\n\nThis directory contains notes and resources for {parent.replace('-', ' ')}.\n")

print("Directory structure has been organized.")

# Note: This script only creates the directory structure.
# You'll need to manually move existing files to their new locations.
# Would you like me to create a script to help with moving existing files as well?
