# Lecture 14_slides

## Page 1

Attack approaches
• Mathematical attacks: several approaches, all equivalent in effort to 
factoring the product of two primes. The defense against 
mathematical attacks is to use a large key size. 
• Timing attacks: These depend on the running time of the decryption 
algorithm
• Chosen ciphertext attacks: this type of attacks exploits properties of 
the RSA algorithm by selecting blocks of data. These attacks can be 
thwarted by suitable padding of the plaintext, such as PKCS1 V1.5 in 
SSL


## Page 2

RSA Decryption With Message Blinding
1.Choose random blinding factor
Pick random r with gcd(r,n)=1
2.Blind the ciphertext
Compute     cʹ=c⋅re mod n            where e is the public exponent.
3.Decrypt the blinded ciphertext
Compute     mʹ=(cʹ)d mod n
4.Unblind the result
Compute     m=mʹ⋅r−1 mod n        where r−1 is the modular inverse of r.
• The output m is the correct plaintext.


## Page 4

A simple attack on textbook RSA
• Session-key  K is 64 bits.     View   K Î {0,…,264}
• Eavesdropper sees:    C = Ke (mod N) .
• Suppose   K = K1×K2 where   K1, K2 < 234 .   
• Then:    C/K1
e = K2
e (mod N)
• Build table:   C/1e, C/2e, C/3e, …, C/234e .   time:  234
For  K2 = 0,…, 234 test if  K2
e is in table.   time: 234×34
• Attack time:   »240  << 264
Web 
Browser
Web
Server
Random session key K
d
Client Hello
Server Hello (e, N)
C = RSA (K)


## Page 5

Take-home exercise – no need to submit 
• SW textbook (6th edition) problems: 3.14 & 3.15


## Page 6

RSA reading materials
• A Method for Obtaining Digital Signatures and Public-Key 
Cryptosystems


## Page 7

Homomorphic encryption 
• Encryption scheme that allows computation on ciphertexts 
• an extension of public-key encryption scheme that allows anyone in 
possession of the public key to perform operations on encrypted data without 
access to the decryption key
• Partially Homomorphic Encryption: Initial public-key systems that 
allow this for either addition or multiplication, but not both.
• i.e. RSA
• Fully homomorphic encryption (FHE)


## Page 8

Application of homomorphic encryption 
• One Use case: cloud computing 
• A weak computational device Alice (e.g., a mobile phone or a laptop) wishes 
to perform a computationally heavy task, beyond her computational means. 
She can delegate it to a much stronger (but still feasible) machine Bob (the 
cloud, or a supercomputer) who offers the service of doing so. The problem is 
that Alice does not trust Bob.
E (Pk, data)
E (Pk, f(data))


