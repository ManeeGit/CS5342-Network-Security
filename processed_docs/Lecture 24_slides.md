# Lecture 24_slides


## Page 1

Key Distribution Using Asymmetric Encryption


## Page 2

Diffie-Hellman Key Exchange
Section 3.5


## Page 3

Recall: ways to achieve symmetric key 
distribution
• A key could be selected by A and physically delivered to B
• A third party could select the key and physically deliver it to A and B 
• If A and B have previously and recently used a key, one party could 
transmit the new key to the other, using the old key to encrypt the 
new key 
• If A and B each have an encrypted connection to a third-party C, C 
could deliver a key on the encrypted links to A and B 


## Page 4

Diffie-Hellman Key Exchange
• Solve the problem of distributing a symmetric key between A and B 
over unsecure channel without the assistance of third party
• There is no pre-shared secret either. 


## Page 5

Diffie-Hellman Key Exchange
• Invented by Whitfield Diffie and Martin Hellman in 1976
• Allows Alice and Bob to exchange a key even with Eve learning it
• No third party involved
• After DHKE, a common shared key, 𝛼!!!" is established, it can be 
used to encrypt message
• A common shared key is symmetric


## Page 6

The Diffie-Hellman Key Exchange
• From A’s view
• 𝐾= 𝑌!
"! 𝑚𝑜𝑑𝑞
= (𝛼"" 𝑚𝑜𝑑𝑞)"! 𝑚𝑜𝑑𝑞
= 𝛼"""! 𝑚𝑜𝑑𝑞


## Page 7

Example of the Diffie -Hellman algorithm
Alice
q=11, 𝜶=7
Bob
XA=3
XB=6
YA = 73 mod 11
    = 2              
YB = 76 mod 11
    = 4              
YB = 4    
YA = 2    
K1 = 43 mod 11
    = 9              
K2 = 26 mod 11
    = 9              
K1 = K2 = K    
Large Random
Number
Large Random
Number
Large Prime Number
Note: XA, XB, K1, K2 are Private


## Page 8

Analysis of DHKE - Attack
• Adversary gets 𝑞, 𝛼, 𝑌,, 𝑌-.
• She needs to compute either 𝑋, or 𝑋- = 𝑑𝑙𝑜𝑔.,0𝑌-
• Secure?


## Page 9

Discrete Log Problem
Cryptographic assumptions:
• Discrete logarithm problem (discrete log problem): Given 
𝛼, 𝑞, 𝛼!! 𝑚𝑜𝑑𝑞for random 𝑋,, it is computationally hard to find 𝑋,
• Diffie-Hellman assumption: Given 𝛼, 𝑞, 𝛼!! 𝑚𝑜𝑑𝑞, and 
𝛼!" 𝑚𝑜𝑑𝑞for random 𝑋,, 𝑋-, no polynomial time attacker can 
distinguish between a random value R and 𝛼!!!" 𝑚𝑜𝑑𝑞.
• Intuition: The best known algorithm is to first calculate 𝑋" and then compute 
(𝛼#!)#" 𝑚𝑜𝑑𝑞, but this requires solving the discrete log problem, which is 
hard!
• Note: Multiplying the values doesn’t work, since you get 
𝛼!!1!" 𝑚𝑜𝑑𝑝≠𝛼!!!" 𝑚𝑜𝑑𝑝


## Page 10

Ephemerality of Diffie-Hellman
• Diffie-Hellman can be used ephemerally (called Diffie-Hellman 
ephemeral, or DHE)
• Ephemeral: Short-term and temporary, not permanent
• Alice and Bob discard 𝑋", 𝑋$ and 𝐾= 𝛼#"#! 𝑚𝑜𝑑𝑞when they’re done
• Because you need 𝑋" and 𝑋$ to derive 𝐾, you can never derive 𝐾again!
• Sometimes 𝐾is called a session key, because it’s only used for an ephemeral 
session
• Eve can’t decrypt any messages she recorded: Nobody saved 𝑋,, 𝑋-
or 𝐾, and her recording only has 𝛼!! 𝑚𝑜𝑑𝑞and 𝛼!" 𝑚𝑜𝑑𝑞!     


## Page 11

Diffie-Hellman is susceptible to man-in-the-
middle attacks
• David can alter messages, block messages, and send her own 
messages
• DH is not secure against a MITM attacker: David can just do a DH with 
both sides!


## Page 12

Diffie-Hellman: Security

