import os
import shutil
from pathlib import Path

def cleanup():
    base_path = Path(__file__).parent
    
    # Directories to remove (after verifying they're empty)
    dirs_to_remove = [
        "00-introduction",
        "01-reconnaissance",
        "02-scanning",
        "03-exploitation",
        "04-web",
        "05-post-exploitation",
        "06-Web-App-Pentesting",
        "06-password-attacks",
        "07-Password-Cracking",
        "08-Network-Attacks",
        "09-Metasploit",
        "10-Reporting"
    ]
    
    # Files to move to resources
    files_to_move = {
        "LICENSE": "resources",
        "README.md": "resources",
        "move_files.py": "resources/scripts",
        "organize_notes.py": "resources/scripts"
    }
    
    # Move files first
    print("Moving files to resources...")
    for file, dest in files_to_move.items():
        src = base_path / file
        dest_dir = base_path / dest
        dest_dir.mkdir(parents=True, exist_ok=True)
        if src.exists():
            try:
                shutil.move(str(src), str(dest_dir / file))
                print(f"Moved {file} to {dest}/")
            except Exception as e:
                print(f"Error moving {file}: {e}")
    
    # Remove empty directories
    print("\nRemoving empty directories...")
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            try:
                # Only remove if directory is empty
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    print(f"Removed empty directory: {dir_name}")
                else:
                    print(f"Directory not empty, skipping: {dir_name}")
            except Exception as e:
                print(f"Error removing {dir_name}: {e}")
    
    print("\nCleanup complete!")
    print("Please review the following directories as they may contain files:")
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            print(f"- {dir_name}")

if __name__ == "__main__":
    print("This script will help clean up the OSCP study notes directory.")
    print("It will move configuration files to the resources directory and remove empty directories.")
    input("Press Enter to continue or Ctrl+C to cancel...")
    cleanup()
