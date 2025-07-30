import os
import shutil
from pathlib import Path

def remove_empty_dirs():
    base_path = Path(__file__).parent
    
    # Directories to remove (if empty)
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
    
    # Scripts to move to resources/scripts
    scripts_to_move = [
        'cleanup.py',
        'final_cleanup.py',
        'identify_remaining.py',
        'move_files.py',
        'organize_notes.py',
        'remove_empty_dirs.py'
    ]
    
    # Move scripts first
    print("Moving scripts to resources/scripts...")
    dest_dir = base_path / 'resources' / 'scripts'
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    for script in scripts_to_move:
        src = base_path / script
        if src.exists():
            try:
                shutil.move(str(src), str(dest_dir / script))
                print(f"Moved {script} to resources/scripts/")
            except Exception as e:
                print(f"Error moving {script}: {e}")
    
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
    
    print("\nFinal cleanup complete!")
    print("Your OSCP study notes are now well organized.")

if __name__ == "__main__":
    print("This script will perform the final cleanup of empty directories.")
    print("It will also move all organization scripts to resources/scripts.")
    input("Press Enter to continue or Ctrl+C to cancel...")
    remove_empty_dirs()
