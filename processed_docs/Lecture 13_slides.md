# Lecture 13_slides


## Page 1

Public-Key Cryptography Algorithm
(RSA)


## Page 2

RSA Public-key encryption
• by Rivest, Shamir & Adleman of MIT in 1977 
• currently the “work horse” of Internet security
• most public key infrastructure (PKI) products
• SSL/TLS: certificates and key-exchange
• secure e-mail: PGP, Outlook, ….
• based on exponentiation in a finite (Galois) field over integers modulo a 
prime 
• exponentiation takes O((log n)3) operations (easy)
• security due to cost of factoring large integer numbers 
• factorization takes O(e log n log log n) operations (hard)
• uses large integers (eg. 1024 bits)


## Page 3

RSA key setup
• each user generates a public/private key pair by: 
• selecting two large primes at random - p, q
• computing their system modulus n=p!q
• note ø(n)=(p-1)(q-1)
• selecting at random the encryption key e
• where 1<e<ø(n), gcd(e,ø(n))=1 
• solve following equation to find decryption key d
• ed=1 mod ø(n)
• publish their public encryption key: pk={e,n} 
• keep secret private decryption key: sk={d,p,q} 


## Page 5

RSA key generation
• users of RSA must:
• determine two primes at random - p, q
• select either e or d and compute the other
• primes p,q must not be easily derived from modulus n=p.q
• means must be sufficiently large
• typically guess and use probabilistic test
• exponents e, d are inverses, so use Inverse algorithm to compute the 
other


## Page 6

RSA example
1.
Select primes: p=17 & q=11
2.
Compute n = pq =17×11=187
3.
Compute ø(n)=(p–1)(q-1)=16×10=160
4.
Select e : gcd(e,160)=1; choose e=7
5.
Determine d: de=1 mod 160 and d < 160 Value is d=23 since 
23×7=161= 10×160+1
6.
Publish public key pk={7,187}
7.
Keep secret private key sk={23,17,11}


## Page 7

RSA use
• to encrypt a message M the sender:
• obtains public key of recipient pk={e,n}
• computes: C=Me mod n, where 0≤M<n
• to decrypt the ciphertext C the owner:
• uses their private key sk={d,p,q}
• computes: M=Cd mod n
• note that the message M must be smaller than the modulus n (block 
if needed)
Plaintext
Ciphertext
C = 𝑀!
pk={e,n}
sk={d,p,q}


## Page 8

Example of RSA algorithm


## Page 9

Correctness of RSA
• Euler’s theorem: if gcd (M, n) = 1, then 𝑀!(#) = 1 mod n. Here φ(n) 
is Euler’s totient function: the number of integers in {1, 2, . . ., n-1} 
which are relatively prime to n. When n is a prime, this theorem is 
just Fermat’s little theorem
M’ = 𝐶% mod n = 𝑀&% mod n
=  𝑀(! # )* mod n
=  [𝑀!(#)](, 𝑀 mod n
= M  mod n

