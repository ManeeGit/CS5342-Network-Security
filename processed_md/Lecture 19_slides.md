# Lecture 19_slides

## Page 1

Digital Signature


## Page 2

Digital Signatures
• NIST FIPS PUB 186-4 - the result of a cryptographic transformation of 
data that, when properly implemented, provides a mechanism for 
verifying origin authentication, data integrity, and signatory non-
repudiation
• Based on asymmetric keys


## Page 3

Digital Signatures
• Asymmetric cryptography is good because we don’t need to share a 
secret key
• Digital signatures are the asymmetric way of providing 
integrity/authenticity to data
• Assume that Alice and Bob can communicate public keys without 
David interfering


## Page 4

Digital Signatures: Definition
• Three parts:
• KeyGen() → PK, SK: Generate a public/private keypair, where PK is the verify (public) key, and SK
is the signing (secret) key
• Sign(SK, M) → sig: Sign the message M using the signing key SK to produce the signature sig
• Verify(PK, M, sig) → {0, 1}: Verify the signature sig on message M using the verify key PK and 
output 1 if valid and 0 if invalid
• Properties:
• Correctness: Verification should be successful for a signature generated over any message
• Verify(PK, M, Sign(SK, M)) = 1 for all PK, SK ← KeyGen() and M
• Efficiency: Signing/verifying should be fast
• Security: Same as for MACs except that the attacker also receives PK
• Namely, no attacker can forge a signature for a message


## Page 5

RSA Signature
• KeyGen():
• Randomly pick two large primes, p and q
• Compute n = pq
• n is usually between 2048 bits and 4096 bits long
• Choose e
• Requirement: e is relatively prime to (p - 1)(q - 1)
• Requirement: 2 < e < (p - 1)(q - 1)
• Compute d = e-1 mod (p - 1)(q - 1)
• Public key: n and e
• Private key: d


## Page 6

RSA Signatures
• Sign(d, M):
• Compute H(M)d mod n
• Verify(e, n, M, sig)
• Verify that H(M) ≡ sige mod n


## Page 7

RSA Probabilistic Digital 
Signature Scheme (RSA-PSS)
Step1: Generate a hash value, or message digest, 
mHash from the message M to be signed 
Step2: Pad mHash with a constant value padding1 and 
pseudorandom value salt to form M’ 
Step3: Generate hash value H from M’
Step4: Generate a block DB consisting of a constant 
value padding 2 and salt
Step5: Use the mask generating function MGF, which 
produces a randomized out-put from input H of the 
same length as DB
Step 6: Create the encoded message (EM) block by 
padding H with the hexadecimal constant bc and the 
XOR of DB and output of MGF
Step 7: Encrypt EM with RSA using the signer’s private 
key 


## Page 8

RSA Signatures: Correctness
Theorem: sige ≡ H(M) mod N
Proof:
sige = [𝐻𝑀𝑑 ]𝑒 𝑚𝑜𝑑 𝑁
= 𝐻(𝑀)"# mod N


## Page 9

RSA Signatures: Correctness
Theorem: sige ≡ H(M) mod N
Proof:
sige = [𝐻𝑀𝑑 ]𝑒 𝑚𝑜𝑑 𝑁
= 𝐻(𝑀)"# mod N
= 𝐻(𝑀)$% & '(   mod N
=  [𝐻(𝑀)%(&)]$- 𝐻𝑀 mod N
= H(M)    mod N


## Page 10

Homework (Textbook) – no submission
• Review Question: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6
• Problems: 
• prove correctness of RSA digital signature
• 3.14 & 3.15


## Page 11

Homework 2 - individual
• Chapter 3
• Deadline: Friday, October 24 before class
• We will use the RaiderCanvas submission time as your final 
timestamp
• 10% penalty per day for late submission


