# Lecture 12_slides


## Page 1

Public-Key Encryption: Definition
• Three parts:
• KeyGen() → PK, SK: Generate a public/private keypair, where PK is the public 
key, and SK is the private (secret) key
• Enc(PK, M) → C: Encrypt a plaintext M using public key PK to produce 
ciphertext C
• Dec(SK, C) → M: Decrypt a ciphertext C using secret key SK
• Properties
• Correctness: Decrypting a ciphertext should result in the message that was 
originally encrypted
• Dec(SK, Enc(PK, M)) = M for all PK, SK ← KeyGen() and M
• Efficiency: Encryption/decryption should be fast
• Security: 1. Alice (the challenger) just gives Eve (the adversary) the public key, 
and Eve doesn’t request encryptions. Eve cannot guess out anything; 2. 
computationally infeasible to recover M with PK and ciphertext


## Page 2

Public-Key Cryptography - Signature


## Page 4

Review
Private Key
Public Key
Signature
Encryption


## Page 5

Public-Key application
• can classify uses into 3 categories:
• encryption/decryption (provide secrecy)
• digital signatures (provide authentication)
• key exchange (of session keys)
• some algorithms are suitable for all uses; others are specific to one
• Either of the two related keys can be used for encryption, with the 
other used for decryption


## Page 6

TLS 1.2 – Use Public Key for Session Key Exchange
RFC 5246: The Transport Layer Security (TLS) Protocol - Version 1.2


## Page 7

Security of Public Key Schemes
• Keys used are very large (>512bits) 
• like private key schemes brute force exhaustive search attack is always 
theoretically possible 
• Security relies on a large enough difference in difficulty between easy 
(en/decrypt) and hard (cryptanalyze) problems
• more generally the hard problem is known, it’s just made too hard to do in 
practice 
• Requires the use of very large numbers, hence is slow compared to 
private/symmetric key schemes

