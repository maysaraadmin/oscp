import os
import shutil
from pathlib import Path

def move_remaining_files():
    base_path = Path(__file__).parent
    
    # Define source and destination mappings
    move_mapping = {
        # Introduction
        "00-introduction": "01-Information-Gathering/00-Introduction",
        
        # Information Gathering
        "01-reconnaissance/01-passive-recon": "01-Information-Gathering/01-Passive-Recon",
        "01-reconnaissance/02-active-recon": "01-Information-Gathering/02-Active-Recon",
        "01-reconnaissance/03-service-enumeration": "01-Information-Gathering/03-Service-Enumeration",
        "01-reconnaissance/04-web-enumeration": "01-Information-Gathering/04-Web-App-Enumeration",
        "01-reconnaissance/05-osint": "01-Information-Gathering/05-OSINT-Techniques",
        
        # Vulnerability Assessment
        "02-scanning/01-manual-identification": "02-Vulnerability-Assessment/01-Manual-Identification",
        "02-scanning/02-automated-scanning": "02-Vulnerability-Assessment/02-Automated-Scanning",
        "02-scanning/03-common-vulnerabilities": "02-Vulnerability-Assessment/03-Common-Vulnerabilities",
        
        # Web Application
        "04-web/01-owasp-top10": "03-Exploitation/02-Web-Exploitation/OWASP-Top10",
        "04-web/02-authentication-bypass": "03-Exploitation/02-Web-Exploitation/Authentication-Bypass",
        "04-web/03-file-inclusion": "03-Exploitation/02-Web-Exploitation/File-Inclusion",
        "04-web/04-cms-exploitation": "03-Exploitation/02-Web-Exploitation/CMS-Exploitation",
        
        # Password Cracking
        "06-password-attacks/01-password-spraying": "06-Password-Cracking/03-Password-Spraying",
        "06-password-attacks/02-wordlist-generation": "06-Password-Cracking/04-Wordlist-Generation",
        "07-Password-Cracking": "06-Password-Cracking",
        
        # Network Attacks
        "08-Network-Attacks": "07-Network-Attacks",
        
        # Metasploit
        "09-Metasploit": "08-Metasploit",
        
        # Reporting
        "10-Reporting": "09-Reporting"
    }
    
    print("Moving remaining files to their new locations...\n")
    
    for src, dest in move_mapping.items():
        src_path = base_path / src
        dest_path = base_path / dest
        
        if src_path.exists():
            try:
                # If source is a file, move it directly
                if src_path.is_file():
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src_path), str(dest_path))
                    print(f"Moved {src} to {dest}")
                # If source is a directory, move its contents
                elif src_path.is_dir():
                    dest_path.mkdir(parents=True, exist_ok=True)
                    for item in src_path.iterdir():
                        shutil.move(str(item), str(dest_path / item.name))
                    print(f"Moved contents of {src} to {dest}")
            except Exception as e:
                print(f"Error moving {src}: {e}")
    
    print("\nCleanup complete!")
    print("You can now safely remove any empty directories.")

if __name__ == "__main__":
    print("This script will move remaining files to their new locations.")
    print("Make sure to run this from the root of your OSCP study directory.")
    input("Press Enter to continue or Ctrl+C to cancel...")
    move_remaining_files()
