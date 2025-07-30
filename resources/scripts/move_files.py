import os
import shutil
from pathlib import Path

# Define the mapping of old directories to new locations
mapping = {
    # Information Gathering
    "00-introduction": "01-Information-Gathering/00-Introduction",
    "01-reconnaissance/01-passive-recon": "01-Information-Gathering/01-Passive-Recon",
    "01-reconnaissance/02-active-recon": "01-Information-Gathering/02-Active-Recon",
    "01-reconnaissance/03-service-enumeration": "01-Information-Gathering/03-Service-Enumeration",
    "01-reconnaissance/04-web-enumeration": "01-Information-Gathering/04-Web-App-Enumeration",
    "01-reconnaissance/05-osint": "01-Information-Gathering/05-OSINT-Techniques",
    
    # Vulnerability Assessment
    "02-scanning/01-manual-identification": "02-Vulnerability-Assessment/01-Manual-Identification",
    "02-scanning/02-automated-scanning": "02-Vulnerability-Assessment/02-Automated-Scanning",
    "02-scanning/03-common-vulnerabilities": "02-Vulnerability-Assessment/03-Common-Vulnerabilities",
    "02-scanning/04-risk-assessment": "02-Vulnerability-Assessment/04-Risk-Assessment",
    "02-Vulnerability-Assessment/04-Buffer-Overflows": "02-Vulnerability-Assessment/05-Buffer-Overflows",
    
    # Exploitation
    "03-exploitation/01-client-side-attacks": "03-Exploitation/01-Client-Side-Attacks",
    "03-exploitation/02-web-exploitation": "03-Exploitation/02-Web-Exploitation",
    "03-exploitation/03-password-attacks": "03-Exploitation/03-Password-Attacks",
    "03-exploitation/04-exploit-development": "03-Exploitation/04-Exploit-Development",
    
    # Post-Exploitation
    "04-Post-Exploitation/01-linux-privesc": "04-Post-Exploitation/01-Linux-Privilege-Escalation",
    "04-Post-Exploitation/02-windows-privesc": "04-Post-Exploitation/02-Windows-Privilege-Escalation",
    "04-post-exploitation/03-lateral-movement": "04-Post-Exploitation/03-Lateral-Movement",
    
    # Active Directory
    "05-Active-Directory/01-enumeration": "05-Active-Directory/01-Enumeration",
    "05-Active-Directory/02-initial-access": "05-Active-Directory/02-Initial-Access",
    "05-Active-Directory/03-lateral-movement": "05-Active-Directory/03-Lateral-Movement",
    "05-Active-Directory/04-domain-privesc": "05-Active-Directory/04-Domain-Privilege-Escalation",
    
    # Password Cracking
    "06-Password-Cracking/01-hash-types": "06-Password-Cracking/01-Hash-Types",
    "06-Password-Cracking/02-cracking-tools": "06-Password-Cracking/02-Password-Cracking-Tools",
    "06-password-attacks/01-password-spraying": "06-Password-Cracking/03-Password-Spraying",
    "06-password-attacks/02-wordlist-generation": "06-Password-Cracking/04-Wordlist-Generation",
    
    # Network Attacks
    "07-Network-Attacks/01-mitm": "07-Network-Attacks/01-MITM-Attacks",
    "07-Network-Attacks/02-sniffing": "07-Network-Attacks/02-Network-Sniffing",
    "07-Network-Attacks/03-vpn-tunneling": "07-Network-Attacks/03-VPN-Tunneling",
    "07-Network-Attacks/04-firewall-evasion": "07-Network-Attacks/04-Firewall-Evasion",
    
    # Metasploit
    "08-Metasploit/01-introduction": "08-Metasploit/01-Introduction",
    "08-Metasploit/02-payloads": "08-Metasploit/02-Payloads",
    "08-Metasploit/03-post-exploitation": "08-Metasploit/03-Post-Exploitation",
    
    # Reporting
    "09-Reporting/01-report-writing": "09-Reporting/01-Report-Writing",
    "09-Reporting/02-proof-collection": "09-Reporting/02-Proof-Collection",
    "09-Reporting/03-remediation": "09-Reporting/03-Remediation"
}

def move_files():
    base_path = Path(__file__).parent
    moved = 0
    errors = 0
    
    for old, new in mapping.items():
        old_path = base_path / old
        new_path = base_path / new
        
        if old_path.exists():
            try:
                # Create the destination directory if it doesn't exist
                new_path.parent.mkdir(parents=True, exist_ok=True)
                
                # If the old path is a directory, move its contents
                if old_path.is_dir():
                    for item in old_path.iterdir():
                        shutil.move(str(item), str(new_path / item.name))
                    print(f"Moved contents of {old} to {new}")
                else:
                    shutil.move(str(old_path), str(new_path))
                    print(f"Moved {old} to {new}")
                moved += 1
            except Exception as e:
                print(f"Error moving {old}: {e}")
                errors += 1
    
    print(f"\nOperation complete. Moved {moved} items with {errors} errors.")
    print("\nNote: Some directories might not have been moved automatically.")
    print("Please review the new structure and move any remaining files manually.")

if __name__ == "__main__":
    print("This script will move files to the new directory structure.")
    print("Please make sure you have a backup before proceeding.")
    input("Press Enter to continue or Ctrl+C to cancel...")
    move_files()
