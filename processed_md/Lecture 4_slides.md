# Lecture 4_slides

## Page 1

Requirements
• Two requirements for secure use of symmetric encryption:
• a strong encryption algorithm
• a secret key known only to sender / receiver
Y = EK(X)
X = DK(Y)
• assume encryption algorithm is known
• the security of symmetric encryption depends on the secrecy of the 
key
• implies a secure channel to distribute key


## Page 2

A strong encryption algorithm
attacker
encryption algorithm
plaintext / enquiry
cyphertext / response


## Page 3

Secure Encryption Scheme
• Unconditional security
• no matter how much computer power is available, the cipher cannot be 
broken since the ciphertext provides insufficient information to uniquely 
determine the corresponding plaintext
• Computational security
• the cost of breaking the cipher exceeds the value of the encrypted 
information;
• or the time required to break the cipher exceeds the useful lifetime of the 
information


## Page 4

Desired characteristics
• Cipher needs to completely obscure statistical properties of original 
message
• more practically Shannon suggested combining elements to obtain:
• Confusion – how does changing a bit of the key affect the ciphertext?
• Diffusion – how does changing one bit of the plaintext affect the ciphertext?
confusion
ciphertext
plaintext
diffusion


## Page 5

Ways to achieve
• Symmetric Encryption: 
• substitution / transposition / hybrid
• Asymmetric Encryption: 
• Mathematical hardness - problems that are efficient to compute in one 
direction, but inefficient to reverse by the attacker
• Examples: Modular arithmetic, factoring, discrete logarithm problem, Elliptic Logs over 
Elliptic Curves


## Page 6

Two basic types
• Block Ciphers 
• Typically 64, 128 bit blocks
• A k-bit plaintext block maps to a k-bit ciphertext block 
• Usually employ Feistel structure 
• Stream Ciphers
• A key is used to generate a stream of pseudo-random bits – key stream
• Just XOR plaintext bits with the key stream for encryption 
• For decryption generate the key stream and XOR with the ciphertext! 


