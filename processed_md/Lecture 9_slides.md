# Lecture 9_slides

## Page 1

Combining sources of randomness
• Suppose r1, r2, …, rk are random numbers from different sources. 
E.g.,
r1 = electrical noise from a resistor or semiconductor
r2 = sample of hip-hop music on radio
r3 = clock on computer
b = r1⊕r2⊕…⊕rk
If any one of r1, r2, …, rk is truly random, then so is b
Many poor sources + 1 good source = good entropy


## Page 2

Pseudorandom Number Generators (PRNGs)
• True randomness is expensive
• Pseudorandom number generator (PRNGs): An algorithm that uses a 
little bit of true randomness to generate a lot of random-looking 
output
• Also called deterministic random bit generators (DRBGs)
• PRNGs are deterministic: Output is generated according to a set 
algorithm
• However, for an attacker who can’t see the internal state, the output is 
computationally indistinguishable from true randomness


## Page 3

PRNG: Definition
• A PRNG has two functions:
• PRNG.Seed(randomness): Initializes the internal state using the entropy
• Input: Some truly random bits
• PRNG.Generate(n): Generate n pseudorandom bits
• Input: A number s
• Output: n pseudorandom bits
• Updates the internal state as needed
• Properties
• Correctness: Deterministic
• Efficiency: Efficient to generate pseudorandom bits
• Security: Indistinguishability from random
• Rollback resistance: cannot deduce anything about any previously-generated bit


## Page 4

Example construction of PRNG
• Using block cipher in Counter (CTR) mode:
• If you want m random bits, and a block cipher with Ek has n bits, apply the 
block cipher m/n times and concatenate the result:
• PRNG.Seed(K | IV) = Ek(IV, 1) | Ek(IV, 2) | Ek(IV, 3) … Ek(IV, ceil(m/n)),
• | is concatenation
• Initialization vector (IV) / Nonce – typically is random or pseudorandom
Randomness, 
PRNG output


## Page 5

PRNG: Security
• Can we design a PRNG that is truly random?
• A PRNG cannot be truly random
• The output is deterministic given the initial seed
• A secure PRNG is computationally indistinguishable from random to 
an attacker
• Game: Present an attacker with a truly random sequence and a sequence 
outputted from a secure PRNG
• An attacker should be able to determine which is which with probability ≈0
• Equivalence: An attacker cannot predict future output of the PRNG


## Page 6

Create pseudorandom numbers
• Truly random numbers are impossible with any program!
• However, we can generate seemingly random numbers, called 
pseudorandom numbers
• The function rand() returns a non-negative number between 0 and 
RAND_MAX
• For C, it is defined in stdlib.h
• arc4random() is a function available in some operating systems (primarily 
BSD-based systems like macOS and FreeBSD) that generates random 
numbers. It is part of the C standard library and provides a more secure 
and higher-quality source of random numbers compared to rand()


## Page 7

PRNGs: Summary
• True randomness requires sampling a physical process
• PRNG: An algorithm that uses a little bit of true randomness to 
generate a lot of random-looking output
• Seed(entropy): Initialize internal state
• Generate(n): Generate n bits of pseudorandom output
• Security: computationally indistinguishable from truly random bits


## Page 8

Stream Ciphers


## Page 9

Stream Ciphers
• process the message bit by bit (as a stream) 
• typically have a (pseudo) random stream key
• combined (XOR) with plaintext bit by bit 
• randomness of stream key completely destroys any statistically 
properties in the message 
• Ci = Mi XOR StreamKeyi
• what could be simpler!!!! 
• but must never reuse stream key
• otherwise, can remove effect and recover messages, M⨁K⨁K = M


## Page 10

Stream Cipher Properties
• some design considerations are:
• statistically random 
• depends on large enough key
• large linear complexity
• correlation immunity 
• confusion
• diffusion


## Page 11

How to generate Stream Key?
• How to generate Stream Key?


## Page 12

Stream Ciphers 
• Idea: replace “rand” by “pseudo rand”
• Use Pseudo Random Number Generator 
• A secure PRNG produces output that looks indistinguishable from random
• An attacker who can’t see the internal PRNG state can’t learn any output
• PRNG: {0,1}s ® {0,1}n
• expand a short (e.g., 128-bit) random seed into a long (typically unbounded) 
string that “looks random”
• Secret key is the seed
• Basic encryption method: Ekey[M] = M Å PRNG(key)


## Page 13

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


