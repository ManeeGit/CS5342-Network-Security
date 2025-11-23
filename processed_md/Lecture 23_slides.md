# Lecture 23_slides

## Page 1

Secure?
• Ticket hijacking 
• Malicious user may steal the service ticket of another user on the same workstation 
and try to use it 
• Network address verification does not help
• Servers must verify that the user who is presenting the ticket is the same user to 
whom the ticket was issued 
• No server authentication
• Attacker may misconfigure the network so that he receives messages addressed to a 
legitimate user – man in the middle attack
• Cause a denial of service
• Servers must prove their identity to users
• Solution: session key
no user authentication


## Page 2

Kerberos v4.  - once per user logon session
C
password
Program
AS
client will use this unforgeable ticket to get
other tickets without re-authenticating
Decrypts with 
Kc and obtains
Kc,tgs and Tickettgs
Implicit authentication:
only someone who knows Kc can decrypt
Client only needs to obtain Tickettgs once (say, every morning)
Ticket is encrypted; client cannot forge it or tamper with it 
All users must
pre-register their
passwords with AS
Kc,tgs


## Page 3

Kerberos v4.  - once per type of service
C
System command
e.g. “lpr – Pprint”
Program
TGS
client will use this unforgeable ticket to
get access to service V
Client uses Tickettgs to obtain a service ticket, Ticketv and a short-term session
key for each network service (printer, email, etc.)
Knows Kv
Proves that client knows key Kc,tgs 
contained in encrypted TGS ticket
Kc,v


## Page 4

Kerberos v4.  - once per service session
C
System command
e.g. “lpr – Pprint”
Program
Authenticates server to client
Chain of Reasoning:
Server can produce this message only if he knows Kc,v 
Server can learn key Kc,v only if he can decrypt service ticket
Server can decrypt service ticket only if he knows correct key KV 
If server knows correct key KV, then he is the right server 
For each service request, client uses the short-term key, Kc,v , for that service and 
the ticket he received from TGS 
Proves that client knows key Kc,v 
contained in encrypted ticket
V


## Page 5

Overview of Kerberos


## Page 6

Important Ideas in Kerberos
• Short-term session keys 
• Long-term secrets used only to derive short-term keys 
• Separate session key for each user-server pair
• Re-used by multiple sessions between same user and server 
• Proofs of identity based on authenticators 
• Client encrypts his identity, addr, time with session key; knowledge of key 
proves client has authenticated to KDC/AS 
• Also prevents replays (if clocks are globally synchronized)
• Server learns this key separately (via encrypted ticket that client can’t 
decrypt), then verifies client’s authenticator 
• Symmetric cryptography only 


## Page 7

Kerberos in Large Networks
• One KDC isn’t enough for large networks 
• Network is divided into realms 
• KDCs in different realms have different key databases 
• To access a service in another realm, users must... 
• Get ticket for home-realm TGS from home-realm KDC 
• Get ticket for remote-realm TGS from home-realm TGS 
• As if remote-realm TGS were just another network service 
• Get ticket for remote service from that realm’s TGS
• Use remote-realm ticket to access service
home-realm KDC
home-realm TGS
Ticket_hTGS
remote-realm TGS
Ticket_rTGS
remote service
Ticket_rS


## Page 8

Practical Uses of Kerberos
• Microsoft Windows – Active Directory
• Email, FTP, network file systems, many other applications have been 
kerberized
• Use of Kerberos is transparent for the end user 
• Transparency is important for usability! 
• Authentication for network protocols 
• rsh
• Local authentication
• login and su in OpenBSD 
• Secure windowing systems 


## Page 9

Readings
• Kerberos: The Network Authentication Protocol 
https://web.mit.edu/kerberos/


## Page 10

Practice – no submission 
• William Stallings, “Network Security Essentials”, 6 Edition, 2017
• Chapter 4’s problems: 4.8, 4.9, 4.10


