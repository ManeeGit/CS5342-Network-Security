# Lecture 6_slides


## Page 1

Feistel Encryption and Decryption 


## Page 3

DES encryption
•
64 bits plaintext
•
56 bits effective key length


## Page 4

DES Weakness
• short length key (56 bits) is not secure enough. Brutal force search 
takes short time. 


## Page 5

Triple DES (3DES)
Decrypting with the wrong key will further convolute the output


## Page 6

3DES
• Triple DES with three different keys – brute-force complexity 2168
• 3DES is the FIPS-approved symmetric encryption algorithm
• Weakness: slow speed for encryption
FIPS – Federal Information Processing Standards. The United States' Federal Information Processing Standards are publicly announced 
standards developed by the National Institute of Standards and Technology for use in computer systems by non-military American government 
agencies and government contractors


## Page 7

AES
• clearly a replacement for DES was needed
• have theoretical attacks that can break it
• have demonstrated exhaustive key search attacks
• can use Triple-DES – but slow with small blocks
• US NIST issued call for ciphers in 1997
• 15 candidates accepted in Jun 98 
• 5 were short-listed in Aug-99 
• Rijndael was selected as the AES in Oct-2000
• issued as FIPS PUB 197 standard in Nov-2001 


## Page 8

Criteria to evaluate AES
• General security
• Software implementations
• Restricted-space environments
• Hardware implementations
• Attacks on implementations
• Encryption versus decryption
• Key agility
• Other versatility and flexibility
• Potential for instruction-level parallelism
Cryptographic Standards and Guidelines | CSRC (nist.gov)


## Page 9

AES Specification
• symmetric block cipher 
• 128-bit data, 128/192/256-bit keys 
• stronger & faster than Triple-DES 
• provide full specification & design details 
• both C & Java implementations
• NIST have released all submissions & unclassified analyses
https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Standards-
and-Guidelines/documents/aes-development/Rijndael-ammended.pdf


## Page 10

The AES Cipher - Rijndael 
• an iterative rather than feistel cipher
• treats data in 4 groups of 4 bytes
• operates an entire block in every round
• designed to be:
• resistant against known-plaintext attacks
• speed and code compactness on many CPUs
• design simplicity


## Page 11

Rijndael
• processes data as 4 groups of 4 bytes (state) = 128 bits
• has 10/12/14 rounds in which state undergoes: 
• byte substitution (1 S-box used on every byte) 
• shift rows (permute bytes row by row) 
• mix columns (alter each byte in a column as a function of all of the bytes in 
the column) 
• add round key (XOR state with key material) 
• 128-bit keys – 10 rounds, 192-bit keys – 12 rounds, 256-bit keys – 14 
rounds


## Page 12

AES Encryption and Decryption


## Page 13

AES encryption round

