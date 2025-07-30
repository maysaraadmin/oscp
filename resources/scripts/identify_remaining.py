import os
from pathlib import Path

def find_remaining_files():
    base_path = Path(__file__).parent
    
    # Expected top-level directories
    expected_dirs = [
        "01-Information-Gathering",
        "02-Vulnerability-Assessment",
        "03-Exploitation",
        "04-Post-Exploitation",
        "05-Active-Directory",
        "06-Password-Cracking",
        "07-Network-Attacks",
        "08-Metasploit",
        "09-Reporting",
        "10-Practice-Labs",
        "resources"
    ]
    
    # Find all top-level directories
    current_dirs = [d.name for d in base_path.iterdir() if d.is_dir()]
    
    # Find unexpected directories
    unexpected_dirs = [d for d in current_dirs if d not in expected_dirs and d != '.git']
    
    # Find files that should be moved to resources
    resource_files = [
        'LICENSE',
        'README.md',
        'cleanup.py',
        'move_files.py',
        'organize_notes.py',
        'identify_remaining.py'
    ]
    
    current_files = [f.name for f in base_path.iterdir() if f.is_file()]
    files_to_move = [f for f in current_files if f in resource_files]
    
    # Print report
    print("=== OSCP Study Notes Organization Status ===\n")
    
    print("1. Unexpected Directories (may need manual review):")
    if unexpected_dirs:
        for d in unexpected_dirs:
            print(f"   - {d}")
    else:
        print("   None found!")
    
    print("\n2. Files to move to resources/:")
    if files_to_move:
        for f in files_to_move:
            print(f"   - {f}")
    else:
        print("   None found!")
    
    print("\n3. Directory Structure Verification:")
    for d in expected_dirs:
        path = base_path / d
        if path.exists():
            print(f"   ✓ {d} (exists)")
        else:
            print(f"   ✗ {d} (missing)")
    
    print("\n4. Next Steps:")
    print("   - Move files listed above to resources/")
    print("   - Review unexpected directories")
    print("   - Verify all expected directories exist")
    print("   - Check for any remaining files that need organization")

if __name__ == "__main__":
    find_remaining_files()
