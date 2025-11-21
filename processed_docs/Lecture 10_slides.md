# Lecture 10_slides


## Page 1

Stream Ciphers
• Protocol: Alice and Bob both seed a secure PRNG with their 
symmetric secret key, and then use the output as the key for stream 
key
Alice
Bob
Seed(k)
Seed(k)
Generate(n)
Generate(n)
Plaintext
Plaintext
Ciphertext
⊕
⊕


## Page 2

Stream Ciphers: Encrypting Multiple Messages
• How do we encrypt multiple messages without key reuses?
Alice
Bob
Seed(k)
Seed(k)
Generate(n)
Generate(n)
Plaintext
Plaintext
Ciphertext
⊕
⊕


## Page 3

Stream Ciphers: Encrypting Multiple Messages
• Solution: For each message, seed the PRNG with the key and a 
random IV, concatenated(“|”). Send the IV with the ciphertext
Alice
Bob
Seed(k | IV)
Seed(k | IV)
Generate(n)
Generate(n)
Plaintext
Plaintext
Ciphertext
⊕
⊕
IV
IV


## Page 4

Real-world example: RC4
• a proprietary cipher designed in 1987 
• Extremely simple but effective!
• Very fast - especially in software
• Easily adapts to any key length, byte-oriented stream cipher 
• widely used (web SSL/TLS, wireless WEP, WAP) 
• A trade secret by RSA Security
• uses that permutation to scramble input info processed a byte at a 
time 


## Page 5

RC4 Stream Cipher
K
RC4 (K|IV)
011010010111
⊕
M
C
key
(seed)
key stream
(pseudo random sequence)
message
ciphertext


## Page 6

RC4 Key Schedule
• starts with an array S of 
numbers: 0…255
• S forms internal state of 
the cipher
• given a key k of length I 
bytes
• use key to well and truly 
shuffle
Throw away T & K, retain S


## Page 8

RC4 Encryption
• encryption continues 
shuffling array values
• sum of shuffled pair 
selects "stream key" 
value
• XOR with next byte of 
message to en/decrypt


## Page 9

RC4


## Page 10

RC4 Security
• claimed secure against known attacks
• since RC4 is a stream cipher, must never reuse a key
• have a concern with WEP, but due to key handling rather than RC4 
itself 
• RC4 is widely used, in SSL for secure web transactions amongst other 
uses. Currently it’s regarded as secure, if used correctly.
• Extensively studied, not a completely secure PRNG, first part of output biased, when used as 
stream cipher, should use RC4-Drop[n]
• Which drops first n bytes before using the output
• Conservatively, set n=3072


## Page 11

Summary – Chapter 2
• Symmetric block cipher
• DES, 3DES
• AES
• Random number
• true random number
• pseudorandom number
• Stream cipher 
• The security of symmetric encryption depends on the secrecy of the 
key
• Symmetric encryption: pros and cons 


## Page 12

Reading material
• Encryption: Strengths and Weaknesses of Public-key Cryptography


## Page 13

Homework 1 - individual
• Chapter 1 & 2
• Deadline: Thursday, October 2, 11:59 PM
• We will use the Canvas submission time as your final timestamp
• 10% penalty per day for late submission


## Page 14

Modular Arithmetic
• Definition (congruent modulo): 
• given b – a = km for some k 𝜖𝑍, then a ≡𝑏(mod m)
• Given a ≡𝑏(mod m) and c ≡𝑑(mod m), then
• a + b ≡c + d (mod m)
• a - b ≡c - d (mod m)
• a + c ≡b + d (mod m)
• a × c ≡b × d (mod m)
• ak ≡bk (mod m)
• ka = kb (mod m)
• p(a) ≡p(b) (mod m), any polynomial p(x) with integer coefficients
• A ⨁𝐵⨁𝐵= A


## Page 15

Thank you!

