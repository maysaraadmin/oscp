# Password Attacks

This directory contains notes and techniques for various password attacks, which are essential for gaining unauthorized access to systems and applications.

## Contents

- [Password Attacks Guide](password_attacks.md) - Comprehensive guide to different password attack techniques

## Key Concepts

- **Brute Force Attacks**: Trying all possible combinations
- **Dictionary Attacks**: Using wordlists to guess passwords
- **Credential Stuffing**: Using known username/password pairs
- **Password Spraying**: Trying common passwords across multiple accounts
- **Hash Cracking**: Recovering passwords from hashed values
- **Rainbow Tables**: Precomputed tables for reversing cryptographic hash functions

## Tools

- `John the Ripper`
- `Hashcat`
- `Hydra`
- `Medusa`
- `CeWL` (Custom Word List generator)
- `Crunch` (Wordlist generator)
- `Cewler` (Custom wordlist generator)

## Best Practices

- Always obtain proper authorization before performing password attacks
- Be aware of account lockout policies
- Use wordlists appropriate for the target
- Consider the impact on the target system
- Document all attempts and results
- Be mindful of network traffic and potential detection
- Respect rate limits to avoid service disruption
