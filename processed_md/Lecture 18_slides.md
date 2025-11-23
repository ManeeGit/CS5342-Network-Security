# Lecture 18_slides

## Page 1

MAC-then-Encrypt or Encrypt-then-MAC?
• Method 1: Encrypt-then-MAC
• First compute Enc(K1, M)
• Then MAC the ciphertext: MAC(K2, Enc(K1, M))
• Method 2: MAC-then-encrypt
• First compute MAC(K2, M)
• Then encrypt the message and the MAC together: Enc(k1, M || MAC(K2, M))
• Which is better?
• In theory, both are secure if applied properly
• MAC-then-encrypt has a flaw: You don’t know if tampering has occurred until after 
decrypting
• Attacker can supply arbitrary tampered input, and you always have to decrypt it
• Passing attacker-chosen input through the decryption function can cause side-channel leaks
• Always use encrypt-then-MAC because it’s more robust to mistakes


## Page 2

TLS 1.0 “Lucky 13” Attack
• TLS: A protocol for sending encrypted and authenticated messages over the 
Internet
• TLS 1.0 uses MAC-then-encrypt: Enc(k1, M || MAC(k2, M))
• The encryption algorithm is AES-CBC
• The Lucky 13 attack abuses MAC-then-encrypt to read encrypted messages
• Guess a byte of plaintext and change the ciphertext accordingly
• The MAC will error, but the time it takes to error is different depending on if the 
guess is correct
• Attacker measures how long it takes to error in order to learn information about 
plaintext
• TLS will send the message again if the MAC errors, so the attacker can guess 
repeatedly
• Takeaways
• Side channel attack: The algorithm is proved secure, but poor implementation made 
it vulnerable
• Always encrypt-then-MAC


## Page 4

Authenticated Encryption: Summary
• Authenticated encryption: A scheme that simultaneously guarantees 
confidentiality and integrity (and authenticity) on a message
• Approach: Combine schemes that provide confidentiality with 
schemes that provide integrity and authenticity
• MAC-then-encrypt: Enc(K1, M || MAC(K2, M))
• Encrypt-then-MAC: MAC(K2, Enc(K1, M))
• Always use Encrypt-then-MAC because it's more robust to mistakes


