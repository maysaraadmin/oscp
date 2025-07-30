import os
import shutil
from pathlib import Path

def organize_remaining_files():
    base_path = Path(__file__).parent
    
    # Define source and destination mappings
    move_mapping = {
        # Reconnaissance files
        "01-reconnaissance/active_recon.md": "01-Information-Gathering/02-Active-Recon/active_recon.md",
        "01-reconnaissance/dns_enumeration.md": "01-Information-Gathering/02-Active-Recon/dns_enumeration.md",
        "01-reconnaissance/passive_recon.md": "01-Information-Gathering/01-Passive-Recon/passive_recon.md",
        "01-reconnaissance/recon_notes.md": "01-Information-Gathering/01-Passive-Recon/recon_notes.md",
        
        # Scanning files
        "02-scanning/nmap_cheatsheet.md": "01-Information-Gathering/03-Service-Enumeration/nmap_cheatsheet.md",
        "02-scanning/vulnerability_scanning.md": "02-Vulnerability-Assessment/02-Automated-Scanning/vulnerability_scanning.md",
        
        # Exploitation files
        "03-exploitation/exploit_development.md": "03-Exploitation/04-Exploit-Development/exploit_development.md",
        "03-exploitation/metasploit_cheatsheet.md": "08-Metasploit/02-Payloads/metasploit_cheatsheet.md",
        "03-exploitation/privilege_escalation/linux_pe.md": "04-Post-Exploitation/01-Linux-Privilege-Escalation/linux_pe.md",
        "03-exploitation/privilege_escalation/windows_pe.md": "04-Post-Exploitation/02-Windows-Privilege-Escalation/windows_pe.md",
        
        # Web files
        "04-web/client_side_attacks.md": "03-Exploitation/01-Client-Side-Attacks/client_side_attacks.md",
        "04-web/attacks/web_application_attacks.md": "03-Exploitation/02-Web-Exploitation/web_application_attacks.md",
        "04-web/sql_injection/sql_injection.md": "03-Exploitation/02-Web-Exploitation/sql_injection.md",
        
        # Post-Exploitation files
        "05-post-exploitation/windows_privilege_escalation.md": "04-Post-Exploitation/02-Windows-Privilege-Escalation/windows_privilege_escalation.md",
        
        # Password attacks
        "06-password-attacks/password_attacks.md": "06-Password-Cracking/password_attacks.md",
        
        # Web App Pentesting
        "06-Web-App-Pentesting/README.md": "03-Exploitation/02-Web-Exploitation/README_web_app_pentesting.md"
    }
    
    print("Organizing remaining files...\n")
    
    for src, dest in move_mapping.items():
        src_path = base_path / src
        dest_path = base_path / dest
        
        if src_path.exists():
            try:
                # Create parent directory if it doesn't exist
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Move the file
                shutil.move(str(src_path), str(dest_path))
                print(f"Moved {src} to {dest}")
                
                # If the source directory is now empty, remove it
                if src_path.parent.exists() and not any(src_path.parent.iterdir()):
                    src_path.parent.rmdir()
                    print(f"Removed empty directory: {src_path.parent}")
                    
            except Exception as e:
                print(f"Error moving {src}: {e}")
    
    # Remove any empty directories
    print("\nRemoving any empty directories...")
    for root, dirs, files in os.walk(base_path, topdown=False):
        try:
            for dir_name in dirs:
                dir_path = Path(root) / dir_name
                if dir_path.exists() and not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    print(f"Removed empty directory: {dir_path.relative_to(base_path)}")
        except Exception as e:
            print(f"Error removing {dir_path.relative_to(base_path)}: {e}")
    
    print("\nOrganization complete!")
    print("All files have been moved to their appropriate locations.")

if __name__ == "__main__":
    print("This script will organize any remaining files into the new directory structure.")
    print("Make sure to run this from the root of your OSCP study directory.")
    input("Press Enter to continue or Ctrl+C to cancel...")
    organize_remaining_files()
