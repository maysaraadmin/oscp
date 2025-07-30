# Hash Types and Identification

Understanding different hash types and how to identify them is crucial for effective password cracking. This guide covers common hash formats and tools for hash identification.

## 📋 Table of Contents
1. [Common Hash Types](#common-hash-types)
2. [Hash Identification](#hash-identification)
3. [Hash Extraction](#hash-extraction)
4. [Tools](#-tools)
5. [Practice](#-practice)

## Common Hash Types

### Windows Hashes
- **NTLM (NT LAN Manager)**: Used in Windows NT/2000 and later
  - Format: `32-character hexadecimal`
  - Example: `B4B9B02E6F09A9BD760F388B67351E2B`

- **NTLMv2**: More secure version of NTLM
  - Format: `username::domain:challenge:response:response`
  - Example: `admin::N46iSNekpT:08ca45b7d7ea58ee:88dcbe4446168966a153a0064958dac6:5c7830315c7830310000000000000b45c67103d07d7b95acd12ffa11230e0000000052920b85f78d013c31cdb3b92f5d765c783030`

### Linux Hashes
- **MD5 (Unix)**: Used in older Linux systems
  - Format: `$1$salt$hash`
  - Example: `$1$O3JMY.Tw$AdLnLjQ/5jXF9.MTp3gHv/`

- **SHA-512 (Unix)**: Modern Linux default
  - Format: `$6$salt$hash`
  - Example: `$6$zWwwXKjU$ZfoD6Th9K2s9QxJ9.5hMg2nwS4FQNz3bo9Qd5UMRKg7NbvRp3rQ3ZgLrq1BGpNsXpNLoaHXdmN3zB7QGy70Y0.`

### Web Application Hashes
- **MD5**: `8743b52063cd84097a65d1633f5c74f5`
- **SHA1**: `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8`
- **bcrypt**: `$2a$12$K9IuULyB5KyP2mlTf3zUZ.6jVXJN9Qc1JvJv6QwLQ5xY1zqJQxW2`

## Hash Identification

### Using hash-identifier
```bash
hash-identifier
> 5f4dcc3b5aa765d61d8327deb882cf99
```

### Using hashid
```bash
hashid '5f4dcc3b5aa765d61d8327deb882cf99'
# Or analyze a file
hashid hashes.txt
```

### Common Hash Lengths
- **MD5**: 32 characters
- **SHA1**: 40 characters
- **SHA-256**: 64 characters
- **SHA-512**: 128 characters
- **NTLM**: 32 characters

## Hash Extraction

### Windows
```powershell
# Dump SAM hashes with mimikatz
privilege::debug
token::elevate
lsadump::sam

# Or with secretsdump.py
secretsdump.py -hashes :NTLMhash LOCAL/Administrator@TARGET_IP
```

### Linux
```bash
# Dump /etc/shadow
cat /etc/shadow

# Or with unshadow
unshadow /etc/passwd /etc/shadow > hashes.txt
```

## 🛠 Tools

### Hash Identification
- **hash-identifier**: Python tool for hash identification
- **hashid**: Advanced hash identification tool
- **hash-analyzer**: Web-based hash analyzer

### Hash Extraction
- **mimikatz**: Windows credential extraction
- **secretsdump.py**: Part of Impacket
- **pwdump**: Windows password dumper
- **unshadow**: Combines /etc/passwd and /etc/shadow

### Online Resources
- [HashKiller](https://hashkiller.io/)
- [CrackStation](https://crackstation.net/)
- [hashes.com](https://hashes.com/en/decrypt/hash)

## 📚 Resources
- [Hashcat Hash Modes](https://hashcat.net/wiki/doku.php?id=example_hashes)
- [PentestMonkey - Cheat Sheet](http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats)
- [NetSPI - Windows Password Hashes](https://blog.netspi.com/understanding-mimikatz-2/)

## 🎯 Practice
1. Try identifying different hash types using hash-identifier and hashid
2. Extract hashes from a test Windows/Linux machine (with permission)
3. Attempt to crack the hashes using hashcat or John the Ripper

## ⚠️ Legal Note
Only perform hash extraction and cracking on systems you own or have explicit permission to test. Unauthorized testing is illegal.
