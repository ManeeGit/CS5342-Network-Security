# Lecture 22_slides


## Page 1

A Simple Authentication Dialogue
• 1. C —>AS: IDC ||PC ||IDV
• 2. AS —> C : Ticket = E(KV, [IDC ||ADC ||IDV])
• 3. C —> V: IDC || Ticket
• AS – authentication server 
• ID* - identifier
• PC - password of user
• ADC - network address of C
• KV - secret encryption key shared by AS and V
AS
C
V
1
2
3


## Page 2

Advantage
• Client and malicious attacker cannot alter IDC (impersonate), 
ADC(change of address) , IDV
• server V can verify the user is authenticated through IDC , and grants 
service to C
• guarantee the ticket is valid only if it is transmitted from the same 
client that initially requested the ticket


## Page 3

Secure?
• Insecure: password is transmitted openly and frequently
• Solution: no password transmitted by involving ticket-granting server 
(TGS)


## Page 4

A More Secure Authentication Dialogue
• Once per user logon session
• (1) C —>AS:    IDC ||IDtgs
• (2) AS —> C:   E(KC, Tickettgs)
• Once per type of service:
• (3) C —>TGS:   IDC ||IDv|| Tickettgs
• (4) TGS —> C:   TicketV
• Once per service session:
• (5) C —> V:  IDC || TicketV
AS
C
V
1
2
3, Tickettgs
TGS
4
5
TicketV


## Page 5

Advantage
• No password transmitted in plaintext
• Timestamp is added to prevent reuse of ticket by an attacker


## Page 6

Review and Quiz 2
• Time: Nov. 3, 2025 (Monday) in class
• Content: Chapter 3

