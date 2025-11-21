# Lecture 25_slides


## Page 1

Diffie-Hellman: issues
• Diffie-Hellman is not secure against a MITM adversary
• Diffie-Hellman does not provide authentication
• You exchanged keys with someone, but Diffie-Hellman makes no guarantees 
about who you exchanged keys with; it could be David!
• DHE is an active protocol: Alice and Bob need to be online at the 
same time to exchange keys
• What if Bob wants to encrypt something and send it to Alice for her to read 
later?


## Page 2

Diffie-Hellman Key Exchange: Summary
• Algorithm:
• Alice chooses 𝑋! and sends 𝛼"! 𝑚𝑜𝑑𝑞to Bob
• Bob chooses 𝑋# and sends 𝛼"" 𝑚𝑜𝑑𝑞to Alice
• Their shared secret is (𝛼"!)""= (𝛼"")"!= 𝛼"!"" 𝑚𝑜𝑑𝑞
• Diffie-Hellman provides forwards secrecy: Nothing is saved or can be 
recorded that can ever recover the key
• Diffie-Hellman can be performed over other mathematical groups, 
such as elliptic-curve Diffie-Hellman (ECDH)
• Issues
• Not secure against MITM
• Does not provide authenticity
• Both parties must be online


## Page 3

DHKE in Python Cryptography Library
• https://cryptography.io/en/latest/hazmat/primitives/asymmetric/


## Page 4

Take home exercises
• SW, “Network Security Essentials”, 6th Edition, 2017 
• Problems – 3.21
Consider a Diffie-Hellman scheme with a common prime 𝑞= 11 and a primitive 
root 𝛼= 2.
a. if user A has public key 𝑌! = 9, what is A’s private key 𝑋!?
b. If user B has public key 𝑌# = 3, what is the shared secret key 𝐾?


## Page 5

Elliptic Curve Cryptography (ECC)
• Originally independently proposed by Neal Koblitz (University of 
Washington) and Victor Miller (IBM) in 1985. 
• ECC was proposed as an alternative to other public key encryption 
algorithms, for example RSA. 
• All ECC schemes are public key 
CPSC 467: Cryptography and Computer Security , Michael J. Fischer, 2017, 
https://zoo.cs.yale.edu/classes/cs467/2017f/lectures/ln13.pdf
 


## Page 6

The Elliptic Curve Equation
An elliptic curve over real numbers:
where:
•
(to avoid singularities) 
Example curve: 


## Page 8

Why ECC? 
• In case of ECC, we are able to use smaller primes, or smaller finite fields, and 
achieve a level of security comparable to that of RSA
• ECC has lower computational requirements. For this reason, ECC algorithms can 
be easily implemented on smart cards, pagers, or mobile devices. Some smart 
cards can only work with ECC. 


## Page 9

ECC Key Generation
• Let k be an integer and G a point on E. k×G is defined as adding G to 
itself k times. 
• Once we calculate Q = k × G, it is extremely difficult to recover k from 
Q. The only way to recover k from Q is to try every possible repeated 
addition of G. 
• Q: Does it sound familiar? 


## Page 10

Elliptic Curve Discrete Logarithm Problem 
(ECDLP)
• Let G be a point on E. Compute Q = k × G. Then, ECDLP: given G and Q 
compute k. 
• This allows us to translate crypto schemes based on DLP to EC-based 
schemes. 
• Q is a public key. k is a private key. G is a generator point on E. 


## Page 12

TLS Key Agreement with ECDH 
RFC  8446: The Transport Layer Security (TLS) Protocol Version 1.3,  https://datatracker.ietf.org/doc/html/rfc8446 


## Page 13

Summary
• ECC achieves strong security with small keys.
• Based on the hardness of ECDLP.
• Powers many modern systems (TLS, blockchain, mobile apps). 

