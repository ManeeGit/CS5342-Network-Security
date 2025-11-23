# Computer Networking _ A Top Down Approach, 7th (2)-5

## Page 1

need for the receiver to ask the sender to slow down! Reliable Data Transfer over a Channel 
with Bit Errors: rdt2.0 A more realistic model of the underlying channel is one in which bits in a 
packet may be corrupted. Such bit errors typically occur in the physical components of a 
network as a packet is transmitted, propagates, or is buffered. We’ll continue to assume for the 
moment that all transmitted packets are received (although their bits may be corrupted) in the 
order in which they were sent. Before developing a protocol for reliably communicating over 
such a channel, first consider how people might deal with such a situation. Consider how you 
yourself might dictate a long message over the phone. In a typical scenario, the message taker 
might say “OK” after each sentence has been heard, understood, and recorded. If the message 
taker hears a garbled sentence, you’re asked to repeat the garbled sentence. This message-
dictation protocol uses both positive acknowledgments (“OK”) and negative acknowledgments 
(“Please repeat that.”). These control messages allow the receiver to let the sender know what 
has been received correctly, and what has been received in error and thus requires repeating. In 
a computer network setting, reliable data transfer protocols based on such retransmission are 
known as ARQ (Automatic Repeat reQuest) protocols. Fundamentally, three additional protocol 
capabilities are required in ARQ protocols to handle the presence of bit errors: Error detection. 
First, a mechanism is needed to allow the receiver to detect when bit errors have occurred. 
Recall from the previous section that UDP uses the Internet checksum field for exactly this 
purpose. In Chapter 6 we’ll examine error-detection and -correction techniques in greater 
detail; these techniques allow the receiver to detect and possibly correct packet bit errors. For 
now, we need only know that these techniques require that extra bits (beyond the bits of original 
data to be transferred) be sent from the sender to the receiver; these bits will be gathered into 
the packet checksum field of the rdt2.0 data packet. Receiver feedback. Since the sender and 
receiver are typically executing on different end systems, possibly separated by thousands of 
miles, the only way for the sender to learn of the receiver’s view of the world (in this case, 
whether or not a packet was received correctly) is for the receiver to provide explicit feedback 
to the sender. The positive (ACK) and negative (NAK) acknowledgment replies in the message-
dictation scenario are examples of such feedback. Our rdt2.0 protocol will similarly send ACK 
and NAK packets back from the receiver to the sender. In principle, these packets need only be 
one bit long; for example, a 0 value could indicate a NAK and a value of 1 could indicate an ACK. 
Retransmission. A packet that is received in error at the receiver will be retransmitted by the 
sender. Figure 3.10 shows the FSM representation of rdt2.0 , a data transfer protocol employing 
error detection, positive acknowledgments, and negative acknowledgments. The send side of 
rdt2.0 has two states. In the leftmost state, the send-side protocol is waiting for data to be 
passed down from the upper layer. When the rdt_send(data) event occurs, the sender will 
create a packet ( sndpkt ) containing the data to be sent, along with a packet checksum (for 
example, as discussed in Section 3.3.2 for the case of a UDP segment), and then send the 
packet via the udt_send(sndpkt) operation. In the rightmost state, the sender protocol is waiting 
for an ACK or a NAK packet from the receiver. If an ACK packet is received Figure 3.10 rdt2.0 – A 
protocol for a channel with bit errors (the notation rdt_rcv(rcvpkt) && isACK (rcvpkt) in Figure 
3.10 corresponds to this event), the sender knows that the most recently transmitted packet 
has been received correctly and thus the protocol returns to the state of waiting for data from 
the upper layer. If a NAK is received, the protocol retransmits the last packet and waits for an 
ACK or NAK to be returned by the receiver in response to the retransmitted data packet. It is 
important to note that when the sender is in the wait-for-ACK-or-NAK state, it cannot get more 
data from the upper layer; that is, the rdt_send() event can not occur; that will happen only after 
the sender receives an ACK and leaves this state. Thus, the sender will not send a new piece of 
data until it is sure that the receiver has correctly received the current packet. Because of this 


## Page 2

behavior, protocols such as rdt2.0 are known as stop-and-wait protocols. The receiver-side 
FSM for rdt2.0 still has a single state. On packet arrival, the receiver replies with either an ACK 
or a NAK, depending on whether or not the received packet is corrupted. In Figure 3.10, the 
notation rdt_rcv(rcvpkt) && corrupt(rcvpkt) corresponds to the event in which a packet is 
received and is found to be in error. Protocol rdt2.0 may look as if it works but, unfortunately, it 
has a fatal flaw. In particular, we haven’t accounted for the possibility that the ACK or NAK 
packet could be corrupted! (Before proceeding on, you should think about how this problem 
may be fixed.) Unfortunately, our slight oversight is not as innocuous as it may seem. Minimally, 
we will need to add checksum bits to ACK/NAK packets in order to detect such errors. The more 
difficult question is how the protocol should recover from errors in ACK or NAK packets. The 
difficulty here is that if an ACK or NAK is corrupted, the sender has no way of knowing whether 
or not the receiver has correctly received the last piece of transmitted data. Consider three 
possibilities for handling corrupted ACKs or NAKs: For the first possibility, consider what a 
human might do in the message-dictation scenario. If the speaker didn’t understand the “OK” 
or “Please repeat that” reply from the receiver, the speaker would probably ask, “What did you 
say?” (thus introducing a new type of sender-to-receiver packet to our protocol). The receiver 
would then repeat the reply. But what if the speaker’s “What did you say?” is corrupted? The 
receiver, having no idea whether the garbled sentence was part of the dictation or a request to 
repeat the last reply, would probably then respond with “What did you say?” And then, of 
course, that response might be garbled. Clearly, we’re heading down a difficult path. A second 
alternative is to add enough checksum bits to allow the sender not only to detect, but also to 
recover from, bit errors. This solves the immediate problem for a channel that can corrupt 
packets but not lose them. A third approach is for the sender simply to resend the current data 
packet when it receives a garbled ACK or NAK packet. This approach, however, introduces 
duplicate packets into the sender-to-receiver channel. The fundamental difficulty with 
duplicate packets is that the receiver doesn’t know whether the ACK or NAK it last sent was 
received correctly at the sender. Thus, it cannot know a priori whether an arriving packet 
contains new data or is a retransmission! A simple solution to this new problem (and one 
adopted in almost all existing data transfer protocols, including TCP) is to add a new field to the 
data packet and have the sender number its data packets by putting a sequence number into 
this field. The receiver then need only check this sequence number to determine whether or not 
the received packet is a retransmission. For this simple case of a stop-andwait protocol, a 1-bit 
sequence number will suffice, since it will allow the receiver to know whether the sender is 
resending the previously transmitted packet (the sequence number of the received packet has 
the same sequence number as the most recently received packet) or a new packet (the 
sequence number changes, moving “forward” in modulo-2 arithmetic). Since we are currently 
assuming a channel that does not lose packets, ACK and NAK packets do not themselves need 
to indicate the sequence number of the packet they are acknowledging. The sender knows that 
a received ACK or NAK packet (whether garbled or not) was generated in response to its most 
recently transmitted data packet. Figures 3.11 and 3.12 show the FSM description for rdt2.1 , 
our fixed version of rdt2.0 . The rdt2.1 sender and receiver FSMs each now have twice as many 
states as before. This is because the protocol state must now reflect whether the packet 
currently being sent (by the sender) or expected (at the receiver) should have a sequence 
number of 0 or 1. Note that the actions in those states where a 0- numbered packet is being 
sent or expected are mirror images of those where a 1-numbered packet is being sent or 
expected; the only differences have to do with the handling of the sequence number. Protocol 
rdt2.1 uses both positive and negative acknowledgments from the receiver to the sender. When 
an out-of-order packet is received, the receiver sends a positive acknowledgment for the 


## Page 3

packet it has received. When a corrupted packet Figure 3.11 rdt2.1 sender Figure 3.12 rdt2.1 
receiver is received, the receiver sends a negative acknowledgment. We can accomplish the 
same effect as a NAK if, instead of sending a NAK, we send an ACK for the last correctly 
received packet. A sender that receives two ACKs for the same packet (that is, receives 
duplicate ACKs) knows that the receiver did not correctly receive the packet following the 
packet that is being ACKed twice. Our NAK-free reliable data transfer protocol for a channel 
with bit errors is rdt2.2 , shown in Figures 3.13 and 3.14. One subtle change between rtdt2.1 
and rdt2.2 is that the receiver must now include the sequence number of the packet being 
acknowledged by an ACK message (this is done by including the ACK , 0 or ACK , 1 argument in 
make_pkt() in the receiver FSM), and the sender must now check the sequence number of the 
packet being acknowledged by a received ACK message (this is done by including the 0 or 1 
argument in isACK() in the sender FSM). Reliable Data Transfer over a Lossy Channel with Bit 
Errors: rdt3.0 Suppose now that in addition to corrupting bits, the underlying channel can lose 
packets as well, a notuncommon event in today’s computer networks (including the Internet). 
Two additional concerns must now be addressed by the protocol: how to detect packet loss 
and what to do when packet loss occurs. The use of checksumming, sequence numbers, ACK 
packets, and retransmissions—the techniques Figure 3.13 rdt2.2 sender already developed in 
rdt2.2 —will allow us to answer the latter concern. Handling the first concern will require adding 
a new protocol mechanism. There are many possible approaches toward dealing with packet 
loss (several more of which are explored in the exercises at the end of the chapter). Here, we’ll 
put the burden of detecting and recovering from lost packets on the sender. Suppose that the 
sender transmits a data packet and either that packet, or the receiver’s ACK of that packet, gets 
lost. In either case, no reply is forthcoming at the sender from the receiver. If the sender is 
willing to wait long enough so that it is certain that a packet has been lost, it can simply 
retransmit the data packet. You should convince yourself that this protocol does indeed work. 
But how long must the sender wait to be certain that something has been lost? The sender must 
clearly wait at least as long as a round-trip delay between the sender and receiver (which may 
include buffering at intermediate routers) plus whatever amount of time is needed to process a 
packet at the receiver. In many networks, this worst-case maximum delay is very difficult even 
to estimate, much less know with certainty. Moreover, the protocol should ideally recover from 
packet loss as soon as possible; waiting for a worst-case delay could mean a long wait until 
error recovery Figure 3.14 rdt2.2 receiver is initiated. The approach thus adopted in practice is 
for the sender to judiciously choose a time value such that packet loss is likely, although not 
guaranteed, to have happened. If an ACK is not received within this time, the packet is 
retransmitted. Note that if a packet experiences a particularly large delay, the sender may 
retransmit the packet even though neither the data packet nor its ACK have been lost. This 
introduces the possibility of duplicate data packets in the sender-to-receiver channel. Happily, 
protocol rdt2.2 already has enough functionality (that is, sequence numbers) to handle the 
case of duplicate packets. From the sender’s viewpoint, retransmission is a panacea. The 
sender does not know whether a data packet was lost, an ACK was lost, or if the packet or ACK 
was simply overly delayed. In all cases, the action is the same: retransmit. Implementing a 
time-based retransmission mechanism requires a countdown timer that can interrupt the 
sender after a given amount of time has expired. The sender will thus need to be able to (1) start 
the timer each time a packet (either a first-time packet or a retransmission) is sent, (2) respond 
to a timer interrupt (taking appropriate actions), and (3) stop the timer. Figure 3.15 shows the 
sender FSM for rdt3.0 , a protocol that reliably transfers data over a channel that can corrupt or 
lose packets; in the homework problems, you’ll be asked to provide the receiver FSM for rdt3.0 . 
Figure 3.16 shows how the protocol operates with no lost or delayed packets and how it 


## Page 4

handles lost data packets. In Figure 3.16, time moves forward from the top of the diagram 
toward the bottom of the Figure 3.15 rdt3.0 sender diagram; note that a receive time for a 
packet is necessarily later than the send time for a packet as a result of transmission and 
propagation delays. In Figures 3.16(b)–(d), the send-side brackets indicate the times at which a 
timer is set and later times out. Several of the more subtle aspects of this protocol are explored 
in the exercises at the end of this chapter. Because packet sequence numbers alternate 
between 0 and 1, protocol rdt3.0 is sometimes known as the alternating-bit protocol. We have 
now assembled the key elements of a data transfer protocol. Checksums, sequence numbers, 
timers, and positive and negative acknowledgment packets each play a crucial and necessary 
role in the operation of the protocol. We now have a working reliable data transfer protocol! 
Developing a protocol and FSM representation for a simple application-layer protocol 3.4.2 
Pipelined Reliable Data Transfer Protocols Protocol rdt3.0 is a functionally correct protocol, but 
it is unlikely that anyone would be happy with its performance, particularly in today’s high-
speed networks. At the heart of rdt3.0 ’s performance problem is the fact that it is a stop-and-
wait protocol. Figure 3.16 Operation of rdt3.0 , the alternating-bit protocol Figure 3.17 Stop-
and-wait versus pipelined protocol To appreciate the performance impact of this stop-and-wait 
behavior, consider an idealized case of two hosts, one located on the West Coast of the United 
States and the other located on the East Coast, as shown in Figure 3.17. The speed-of-light 
round-trip propagation delay between these two end systems, RTT, is approximately 30 
milliseconds. Suppose that they are connected by a channel with a transmission rate, R, of 1 
Gbps (10 bits per second). With a packet size, L, of 1,000 bytes (8,000 bits) per packet, 
including both header fields and data, the time needed to actually transmit the packet into the 1 
Gbps link is Figure 3.18(a) shows that with our stop-and-wait protocol, if the sender begins 
sending the packet at then at microseconds, the last bit enters the channel at the sender side. 
The packet then makes its 15-msec cross-country journey, with the last bit of the packet 
emerging at the receiver at 15.008 msec. Assuming for simplicity that ACK packets are 
extremely small (so that we can ignore their transmission time) and that the receiver can send 
an ACK as soon as the last bit of a data packet is received, the ACK emerges back at the sender 
at At this point, the sender can now transmit the next message. Thus, in 30.008 msec, the 
sender was sending for only 0.008 msec. If we define the utilization of the sender (or the 
channel) as the fraction of time the sender is actually busy sending bits into the channel, the 
analysis in Figure 3.18(a) shows that the stop-andwait protocol has a rather dismal sender 
utilization, U , of 9 dtrans=LR=8000 bits/packet109 bits/sec=8 microseconds t=0, t=L/R=8 
t=RTT/2+L/R= t=RTT+L/R=30.008 msec. sender Usender=L/RRTT+L/R =.00830.008=0.00027 
Figure 3.18 Stop-and-wait and pipelined sending That is, the sender was busy only 2.7 
hundredths of one percent of the time! Viewed another way, the sender was able to send only 
1,000 bytes in 30.008 milliseconds, an effective throughput of only 267 kbps—even though a 1 
Gbps link was available! Imagine the unhappy network manager who just paid a fortune for a 
gigabit capacity link but manages to get a throughput of only 267 kilobits per second! This is a 
graphic example of how network protocols can limit the capabilities provided by the underlying 
network hardware. Also, we have neglected lower-layer protocol-processing times at the 
sender and receiver, as well as the processing and queuing delays that would occur at any 
intermediate routers between the sender and receiver. Including these effects would serve only 
to further increase the delay and further accentuate the poor performance. The solution to this 
particular performance problem is simple: Rather than operate in a stop-and-wait manner, the 
sender is allowed to send multiple packets without waiting for acknowledgments, as illustrated 
in Figure 3.17(b). Figure 3.18(b) shows that if the sender is allowed to transmit three packets 
before having to wait for acknowledgments, the utilization of the sender is essentially tripled. 


## Page 5

Since the many in-transit sender-to-receiver packets can be visualized as filling a pipeline, this 
technique is known as pipelining. Pipelining has the following consequences for reliable data 
transfer protocols: The range of sequence numbers must be increased, since each in-transit 
packet (not counting retransmissions) must have a unique sequence number and there may be 
multiple, in-transit, unacknowledged packets. The sender and receiver sides of the protocols 
may have to buffer more than one packet. Minimally, the sender will have to buffer packets that 
have been transmitted but not yet acknowledged. Buffering of correctly received packets may 
also be needed at the receiver, as discussed below. The range of sequence numbers needed 
and the buffering requirements will depend on the manner in which a data transfer protocol 
responds to lost, corrupted, and overly delayed packets. Two basic approaches toward 
pipelined error recovery can be identified: Go-Back-N and selective repeat. 3.4.3 Go-Back-N 
(GBN) In a Go-Back-N (GBN) protocol, the sender is allowed to transmit multiple packets (when 
available) without waiting for an acknowledgment, but is constrained to have no more than 
some maximum allowable number, N, of unacknowledged packets in the pipeline. We describe 
the GBN protocol in some detail in this section. But before reading on, you are encouraged to 
play with the GBN applet (an awesome applet!) at the companion Web site. Figure 3.19 shows 
the sender’s view of the range of sequence numbers in a GBN protocol. If we define base to be 
the sequence number of the oldest unacknowledged Figure 3.19 Sender’s view of sequence 
numbers in Go-Back-N packet and nextseqnum to be the smallest unused sequence number 
(that is, the sequence number of the next packet to be sent), then four intervals in the range of 
sequence numbers can be identified. Sequence numbers in the interval [ 0, base-1 ] correspond 
to packets that have already been transmitted and acknowledged. The interval [base, 
nextseqnum-1] corresponds to packets that have been sent but not yet acknowledged. 
Sequence numbers in the interval [nextseqnum, base+N-1] can be used for packets that can be 
sent immediately, should data arrive from the upper layer. Finally, sequence numbers greater 
than or equal to base+N cannot be used until an unacknowledged packet currently in the 
pipeline (specifically, the packet with sequence number base ) has been acknowledged. As 
suggested by Figure 3.19, the range of permissible sequence numbers for transmitted but not 
yet acknowledged packets can be viewed as a window of size N over the range of sequence 
numbers. As the protocol operates, this window slides forward over the sequence number 
space. For this reason, N is often referred to as the window size and the GBN protocol itself as a 
sliding-window protocol. You might be wondering why we would even limit the number of 
outstanding, unacknowledged packets to a value of N in the first place. Why not allow an 
unlimited number of such packets? We’ll see in Section 3.5 that flow control is one reason to 
impose a limit on the sender. We’ll examine another reason to do so in Section 3.7, when we 
study TCP congestion control. In practice, a packet’s sequence number is carried in a fixed-
length field in the packet header. If k is the number of bits in the packet sequence number field, 
the range of sequence numbers is thus With a finite range of sequence numbers, all arithmetic 
involving sequence numbers must then be done using modulo 2 arithmetic. (That is, the 
sequence number space can be thought of as a ring of size 2 , where sequence number is 
immediately followed by sequence number 0.) Recall that rdt3.0 had a 1-bit sequence number 
and a range of sequence numbers of [0,1]. Several of the problems at the end of this chapter 
explore the consequences of a finite range of sequence numbers. We will see in Section 3.5 
that TCP has a 32-bit sequence number field, where TCP sequence numbers count bytes in the 
byte stream rather than packets. Figures 3.20 and 3.21 give an extended FSM description of the 
sender and receiver sides of an ACKbased, NAK-free, GBN protocol. We refer to this FSM 
[0,2k−1]. k k 2k−1 Figure 3.20 Extended FSM description of the GBN sender Figure 3.21 
Extended FSM description of the GBN receiver description as an extended FSM because we 


## Page 6

have added variables (similar to programming-language variables) for base and nextseqnum , 
and added operations on these variables and conditional actions involving these variables. 
Note that the extended FSM specification is now beginning to look somewhat like a 
programming-language specification. [Bochman 1984] provides an excellent survey of 
additional extensions to FSM techniques as well as other programming-language-based 
techniques for specifying protocols. The GBN sender must respond to three types of events: 
Invocation from above. When rdt_send() is called from above, the sender first checks to see if 
the window is full, that is, whether there are N outstanding, unacknowledged packets. If the 
window is not full, a packet is created and sent, and variables are appropriately updated. If the 
window is full, the sender simply returns the data back to the upper layer, an implicit indication 
that the window is full. The upper layer would presumably then have to try again later. In a real 
implementation, the sender would more likely have either buffered (but not immediately sent) 
this data, or would have a synchronization mechanism (for example, a semaphore or a flag) that 
would allow the upper layer to call rdt_send() only when the window is not full. Receipt of an 
ACK. In our GBN protocol, an acknowledgment for a packet with sequence number n will be 
taken to be a cumulative acknowledgment, indicating that all packets with a sequence number 
up to and including n have been correctly received at the receiver. We’ll come back to this issue 
shortly when we examine the receiver side of GBN. A timeout event. The protocol’s name, “Go-
Back-N,” is derived from the sender’s behavior in the presence of lost or overly delayed 
packets. As in the stop-and-wait protocol, a timer will again be used to recover from lost data or 
acknowledgment packets. If a timeout occurs, the sender resends all packets that have been 
previously sent but that have not yet been acknowledged. Our sender in Figure 3.20 uses only a 
single timer, which can be thought of as a timer for the oldest transmitted but not yet 
acknowledged packet. If an ACK is received but there are still additional transmitted but not yet 
acknowledged packets, the timer is restarted. If there are no outstanding, unacknowledged 
packets, the timer is stopped. The receiver’s actions in GBN are also simple. If a packet with 
sequence number n is received correctly and is in order (that is, the data last delivered to the 
upper layer came from a packet with sequence number ), the receiver sends an ACK for packet 
n and delivers the data portion of the packet to the upper layer. In all other cases, the receiver 
discards the packet and resends an ACK for the most recently received in-order packet. Note 
that since packets are delivered one at a time to the upper layer, if packet k has been received 
and delivered, then all packets with a sequence number lower than k have also been delivered. 
Thus, the use of cumulative acknowledgments is a natural choice for GBN. In our GBN protocol, 
the receiver discards out-of-order packets. Although it may seem silly and wasteful to discard a 
correctly received (but out-of-order) packet, there is some justification for doing so. Recall that 
the receiver must deliver data in order to the upper layer. Suppose now that packet n is 
expected, but packet arrives. Because data must be delivered in order, the receiver could buffer 
(save) packet and then deliver this packet to the upper layer after it had later received and 
delivered packet n. However, if packet n is lost, both it and packet will eventually be 
retransmitted as a result of the n−1 n+1 n+1 n+1 GBN retransmission rule at the sender. Thus, 
the receiver can simply discard packet . The advantage of this approach is the simplicity of 
receiver buffering—the receiver need not buffer any outof-order packets. Thus, while the sender 
must maintain the upper and lower bounds of its window and the position of nextseqnum within 
this window, the only piece of information the receiver need maintain is the sequence number 
of the next in-order packet. This value is held in the variable expectedseqnum , shown in the 
receiver FSM in Figure 3.21. Of course, the disadvantage of throwing away a correctly received 
packet is that the subsequent retransmission of that packet might be lost or garbled and thus 
even more retransmissions would be required. Figure 3.22 shows the operation of the GBN 


## Page 7

protocol for the case of a window size of four packets. Because of this window size limitation, 
the sender sends packets 0 through 3 but then must wait for one or more of these packets to be 
acknowledged before proceeding. As each successive ACK (for example, ACK0 and ACK1 ) is 
received, the window slides forward and the sender can transmit one new packet (pkt4 and 
pkt5, respectively). On the receiver side, packet 2 is lost and thus packets 3, 4, and 5 are found 
to be out of order and are discarded. Before closing our discussion of GBN, it is worth noting 
that an implementation of this protocol in a protocol stack would likely have a structure similar 
to that of the extended FSM in Figure 3.20. The implementation would also likely be in the form 
of various procedures that implement the actions to be taken in response to the various events 
that can occur. In such event-based programming, the various procedures are called (invoked) 
either by other procedures in the protocol stack, or as the result of an interrupt. In the sender, 
these events would be (1) a call from the upper-layer entity to invoke rdt_send() , (2) a timer 
interrupt, and (3) a call from the lower layer to invoke rdt_rcv() when a packet arrives. The 
programming exercises at the end of this chapter will give you a chance to actually implement 
these routines in a simulated, but realistic, network setting. We note here that the GBN protocol 
incorporates almost all of the techniques that we will encounter when we study the reliable 
data transfer components of TCP in Section 3.5. These techniques include the use of sequence 
numbers, cumulative acknowledgments, checksums, and a timeout/retransmit operation. n+1 
Figure 3.22 Go-Back-N in operation 3.4.4 Selective Repeat (SR) The GBN protocol allows the 
sender to potentially “fill the pipeline” in Figure 3.17 with packets, thus avoiding the channel 
utilization problems we noted with stop-and-wait protocols. There are, however, scenarios in 
which GBN itself suffers from performance problems. In particular, when the window size and 
bandwidth-delay product are both large, many packets can be in the pipeline. A single packet 
error can thus cause GBN to retransmit a large number of packets, many unnecessarily. As the 
probability of channel errors increases, the pipeline can become filled with these unnecessary 
retransmissions. Imagine, in our message-dictation scenario, that if every time a word was 
garbled, the surrounding 1,000 words (for example, a window size of 1,000 words) had to be 
repeated. The dictation would be slowed by all of the reiterated words. As the name suggests, 
selective-repeat protocols avoid unnecessary retransmissions by having the sender retransmit 
only those packets that it suspects were received in error (that is, were lost or corrupted) at the 
receiver. This individual, as-needed, retransmission will require that the receiver individually 
acknowledge correctly received packets. A window size of N will again be used to limit the 
number of outstanding, unacknowledged packets in the pipeline. However, unlike GBN, the 
sender will have already received ACKs for some of the packets in the window. Figure 3.23 
shows the SR sender’s view of the sequence number space. Figure 3.24 details the various 
actions taken by the SR sender. The SR receiver will acknowledge a correctly received packet 
whether or not it is in order. Out-of-order packets are buffered until any missing packets (that is, 
packets with lower sequence numbers) are received, at which point a batch of packets can be 
delivered in order to the upper layer. Figure 3.25 itemizes the various actions taken by the SR 
receiver. Figure 3.26 shows an example of SR operation in the presence of lost packets. Note 
that in Figure 3.26, the receiver initially buffers packets 3, 4, and 5, and delivers them together 
with packet 2 to the upper layer when packet 2 is finally received. Figure 3.23 Selective-repeat 
(SR) sender and receiver views of sequence-number space Figure 3.24 SR sender events and 
actions Figure 3.25 SR receiver events and actions It is important to note that in Step 2 in Figure 
3.25, the receiver reacknowledges (rather than ignores) already received packets with certain 
sequence numbers below the current window base. You should convince yourself that this 
reacknowledgment is indeed needed. Given the sender and receiver sequence number spaces 
in Figure 3.23, for example, if there is no ACK for packet send_base propagating from the Figure 


## Page 8

3.26 SR operation receiver to the sender, the sender will eventually retransmit packet 
send_base , even though it is clear (to us, not the sender!) that the receiver has already received 
that packet. If the receiver were not to acknowledge this packet, the sender’s window would 
never move forward! This example illustrates an important aspect of SR protocols (and many 
other protocols as well). The sender and receiver will not always have an identical view of what 
has been received correctly and what has not. For SR protocols, this means that the sender and 
receiver windows will not always coincide. The lack of synchronization between sender and 
receiver windows has important consequences when we are faced with the reality of a finite 
range of sequence numbers. Consider what could happen, for example, with a finite range of 
four packet sequence numbers, 0, 1, 2, 3, and a window size of three. Suppose packets 0 
through 2 are transmitted and correctly received and acknowledged at the receiver. At this 
point, the receiver’s window is over the fourth, fifth, and sixth packets, which have sequence 
numbers 3, 0, and 1, respectively. Now consider two scenarios. In the first scenario, shown in 
Figure 3.27(a), the ACKs for the first three packets are lost and the sender retransmits these 
packets. The receiver thus next receives a packet with sequence number 0—a copy of the first 
packet sent. In the second scenario, shown in Figure 3.27(b), the ACKs for the first three 
packets are all delivered correctly. The sender thus moves its window forward and sends the 
fourth, fifth, and sixth packets, with sequence numbers 3, 0, and 1, respectively. The packet 
with sequence number 3 is lost, but the packet with sequence number 0 arrives—a packet 
containing new data. Now consider the receiver’s viewpoint in Figure 3.27, which has a 
figurative curtain between the sender and the receiver, since the receiver cannot “see” the 
actions taken by the sender. All the receiver observes is the sequence of messages it receives 
from the channel and sends into the channel. As far as it is concerned, the two scenarios in 
Figure 3.27 are identical. There is no way of distinguishing the retransmission of the first packet 
from an original transmission of the fifth packet. Clearly, a window size that is 1 less than the 
size of the sequence number space won’t work. But how small must the window size be? A 
problem at the end of the chapter asks you to show that the window size must be less than or 
equal to half the size of the sequence number space for SR protocols. At the companion Web 
site, you will find an applet that animates the operation of the SR protocol. Try performing the 
same experiments that you did with the GBN applet. Do the results agree with what you expect? 
This completes our discussion of reliable data transfer protocols. We’ve covered a lot of ground 
and introduced numerous mechanisms that together provide for reliable data transfer. Table 
3.1 summarizes these mechanisms. Now that we have seen all of these mechanisms in 
operation and can see the “big picture,” we encourage you to review this section again to see 
how these mechanisms were incrementally added to cover increasingly complex (and realistic) 
models of the channel connecting the sender and receiver, or to improve the performance of 
the protocols. Let’s conclude our discussion of reliable data transfer protocols by considering 
one remaining assumption in our underlying channel model. Recall that we have assumed that 
packets cannot be reordered within the channel between the sender and receiver. This is 
generally a reasonable assumption when the sender and receiver are connected by a single 
physical wire. However, when the “channel” connecting the two is a network, packet reordering 
can occur. One manifestation of packet reordering is that old copies of a packet with a 
sequence or acknowledgment Figure 3.27 SR receiver dilemma with too-large windows: A new 
packet or a retransmission? Table 3.1 Summary of reliable data transfer mechanisms and their 
use Mechanism Use, Comments Checksum Used to detect bit errors in a transmitted packet. 
Timer Used to timeout/retransmit a packet, possibly because the packet (or its ACK) was lost 
within the channel. Because timeouts can occur when a packet is delayed but not lost 
(premature timeout), or when a packet has been received by the receiver but the receiver-to-


## Page 9

sender ACK has been lost, duplicate copies of a packet may be received by a receiver. 
Sequence number Used for sequential numbering of packets of data flowing from sender to 
receiver. Gaps in the sequence numbers of received packets allow the receiver to detect a lost 
packet. Packets with duplicate sequence numbers allow the receiver to detect duplicate copies 
of a packet. Acknowledgment Used by the receiver to tell the sender that a packet or set of 
packets has been received correctly. Acknowledgments will typically carry the sequence 
number of the packet or packets being acknowledged. Acknowledgments may be individual or 
cumulative, depending on the protocol. Negative acknowledgment Used by the receiver to tell 
the sender that a packet has not been received correctly. Negative acknowledgments will 
typically carry the sequence number of the packet that was not received correctly. Window, 
pipelining The sender may be restricted to sending only packets with sequence numbers that 
fall within a given range. By allowing multiple packets to be transmitted but not yet 
acknowledged, sender utilization can be increased over a stop-and-wait mode of operation. 
We’ll see shortly that the window size may be set on the basis of the receiver’s ability to receive 
and buffer messages, or the level of congestion in the network, or both. number of x can 
appear, even though neither the sender’s nor the receiver’s window contains x. With packet 
reordering, the channel can be thought of as essentially buffering packets and spontaneously 
emitting these packets at any point in the future. Because sequence numbers may be reused, 
some care must be taken to guard against such duplicate packets. The approach taken in 
practice is to ensure that a sequence number is not reused until the sender is “sure” that any 
previously sent packets with sequence number x are no longer in the network. This is done by 
assuming that a packet cannot “live” in the network for longer than some fixed maximum 
amount of time. A maximum packet lifetime of approximately three minutes is assumed in the 
TCP extensions for high-speed networks [RFC 1323]. [Sunshine 1978] describes a method for 
using sequence numbers such that reordering problems can be completely avoided. 3.5 
Connection-Oriented Transport: TCP Now that we have covered the underlying principles of 
reliable data transfer, let’s turn to TCP—the Internet’s transport-layer, connection-oriented, 
reliable transport protocol. In this section, we’ll see that in order to provide reliable data 
transfer, TCP relies on many of the underlying principles discussed in the previous section, 
including error detection, retransmissions, cumulative acknowledgments, timers, and header 
fields for sequence and acknowledgment numbers. TCP is defined in RFC 793, RFC 1122, RFC 
1323, RFC 2018, and RFC 2581. 3.5.1 The TCP Connection TCP is said to be connection-
oriented because before one application process can begin to send data to another, the two 
processes must first “handshake” with each other—that is, they must send some preliminary 
segments to each other to establish the parameters of the ensuing data transfer. As part of TCP 
connection establishment, both sides of the connection will initialize many TCP state variables 
(many of which will be discussed in this section and in Section 3.7) associated with the TCP 
connection. The TCP “connection” is not an end-to-end TDM or FDM circuit as in a circuit-
switched network. Instead, the “connection” is a logical one, with common state residing only 
in the TCPs in the two communicating end systems. Recall that because the TCP protocol runs 
only in the end systems and not in the intermediate network elements (routers and link-layer 
switches), the intermediate network elements do not maintain TCP connection state. In fact, 
the intermediate routers are completely oblivious to TCP connections; they see datagrams, not 
connections. A TCP connection provides a full-duplex service: If there is a TCP connection 
between Process A on one host and Process B on another host, then application-layer data can 
flow from Process A to Process B at the same time as application-layer data flows from Process 
B to Process A. A TCP connection is also always point-to-point, that is, between a single sender 
and a single receiver. Socalled “multicasting” (see the online supplementary materials for this 


## Page 10

text)—the transfer of data from one sender to many receivers in a single send operation—is not 
possible with TCP. With TCP, two hosts are company and three are a crowd! Let’s now take a 
look at how a TCP connection is established. Suppose a process running in one host wants to 
initiate a connection with another process in another host. Recall that the process that is 
initiating the connection is called the client process, while the other process is called the server 
process. The client application process first informs the client transport layer that it wants to 
establish a connection CASE HISTORY Vinton Cerf, Robert Kahn, and TCP/IP In the early 1970s, 
packet-switched networks began to proliferate, with the ARPAnet—the precursor of the 
Internet—being just one of many networks. Each of these networks had its own protocol. Two 
researchers, Vinton Cerf and Robert Kahn, recognized the importance of interconnecting these 
networks and invented a cross-network protocol called TCP/IP, which stands for Transmission 
Control Protocol/Internet Protocol. Although Cerf and Kahn began by seeing the protocol as a 
single entity, it was later split into its two parts, TCP and IP, which operated separately. Cerf and 
Kahn published a paper on TCP/IP in May 1974 in IEEE Transactions on Communications 
Technology [Cerf 1974]. The TCP/IP protocol, which is the bread and butter of today’s Internet, 
was devised before PCs, workstations, smartphones, and tablets, before the proliferation of 
Ethernet, cable, and DSL, WiFi, and other access network technologies, and before the Web, 
social media, and streaming video. Cerf and Kahn saw the need for a networking protocol that, 
on the one hand, provides broad support for yet-to-be-defined applications and, on the other 
hand, allows arbitrary hosts and link-layer protocols to interoperate. In 2004, Cerf and Kahn 
received the ACM’s Turing Award, considered the “Nobel Prize of Computing” for “pioneering 
work on internetworking, including the design and implementation of the Internet’s basic 
communications protocols, TCP/IP, and for inspired leadership in networking.” to a process in 
the server. Recall from Section 2.7.2, a Python client program does this by issuing the 
command clientSocket.connect((serverName, serverPort)) where serverName is the name of 
the server and serverPort identifies the process on the server. TCP in the client then proceeds to 
establish a TCP connection with TCP in the server. At the end of this section we discuss in some 
detail the connection-establishment procedure. For now it suffices to know that the client first 
sends a special TCP segment; the server responds with a second special TCP segment; and 
finally the client responds again with a third special segment. The first two segments carry no 
payload, that is, no application-layer data; the third of these segments may carry a payload. 
Because three segments are sent between the two hosts, this connection-establishment 
procedure is often referred to as a three-way handshake. Once a TCP connection is 
established, the two application processes can send data to each other. Let’s consider the 
sending of data from the client process to the server process. The client process passes a 
stream of data through the socket (the door of the process), as described in Section 2.7. Once 
the data passes through the door, the data is in the hands of TCP running in the client. As shown 
in Figure 3.28, TCP directs this data to the connection’s send buffer, which is one of the buffers 
that is set aside during the initial three-way handshake. From time to time, TCP will grab chunks 
of data from the send buffer and pass the data to the network layer. Interestingly, the TCP 
specification [RFC 793] is very laid back about specifying when TCP should actually send 
buffered data, stating that TCP should “send that data in segments at its own convenience.” 
The maximum amount of data that can be grabbed and placed in a segment is limited by the 
maximum segment size (MSS). The MSS is typically set by first determining the length of the 
largest link-layer frame that can be sent by the local sending host (the socalled maximum 
transmission unit, MTU), and then setting the MSS to ensure that a TCP segment (when 
encapsulated in an IP datagram) plus the TCP/IP header length (typically 40 bytes) will fit into a 
single link-layer frame. Both Ethernet and PPP link-layer protocols have an MTU of 1,500 bytes. 


## Page 11

Thus a typical value of MSS is 1460 bytes. Approaches have also been proposed for discovering 
the path MTU —the largest link-layer frame that can be sent on all links from source to 
destination [RFC 1191]—and setting the MSS based on the path MTU value. Note that the MSS 
is the maximum amount of application-layer data in the segment, not the maximum size of the 
TCP segment including headers. (This terminology is confusing, but we have to live with it, as it 
is well entrenched.) TCP pairs each chunk of client data with a TCP header, thereby forming TCP 
segments. The segments are passed down to the network layer, where they are separately 
encapsulated within network-layer IP datagrams. The IP datagrams are then sent into the 
network. When TCP receives a segment at the other end, the segment’s data is placed in the 
TCP connection’s receive buffer, as shown in Figure 3.28. The application reads the stream of 
data from this buffer. Each side of the connection has Figure 3.28 TCP send and receive buffers 
its own send buffer and its own receive buffer. (You can see the online flow-control applet at 
http://www.awl.com/kurose-ross, which provides an animation of the send and receive 
buffers.) We see from this discussion that a TCP connection consists of buffers, variables, and 
a socket connection to a process in one host, and another set of buffers, variables, and a 
socket connection to a process in another host. As mentioned earlier, no buffers or variables 
are allocated to the connection in the network elements (routers, switches, and repeaters) 
between the hosts. 3.5.2 TCP Segment Structure Having taken a brief look at the TCP 
connection, let’s examine the TCP segment structure. The TCP segment consists of header 
fields and a data field. The data field contains a chunk of application data. As mentioned above, 
the MSS limits the maximum size of a segment’s data field. When TCP sends a large file, such 
as an image as part of a Web page, it typically breaks the file into chunks of size MSS (except for 
the last chunk, which will often be less than the MSS). Interactive applications, however, often 
transmit data chunks that are smaller than the MSS; for example, with remote login 
applications like Telnet, the data field in the TCP segment is often only one byte. Because the 
TCP header is typically 20 bytes (12 bytes more than the UDP header), segments sent by Telnet 
may be only 21 bytes in length. Figure 3.29 shows the structure of the TCP segment. As with 
UDP, the header includes source and destination port numbers, which are used for 
multiplexing/demultiplexing data from/to upper-layer applications. Also, as with UDP, the 
header includes a checksum field. A TCP segment header also contains the following fields: 
The 32-bit sequence number field and the 32-bit acknowledgment number field are used by the 
TCP sender and receiver in implementing a reliable data transfer service, as discussed below. 
The 16-bit receive window field is used for flow control. We will see shortly that it is used to 
indicate the number of bytes that a receiver is willing to accept. The 4-bit header length field 
specifies the length of the TCP header in 32-bit words. The TCP header can be of variable length 
due to the TCP options field. (Typically, the options field is empty, so that the length of the 
typical TCP header is 20 bytes.) The optional and variable-length options field is used when a 
sender and receiver negotiate the maximum segment size (MSS) or as a window scaling factor 
for use in high-speed networks. A timestamping option is also defined. See RFC 854 and RFC 
1323 for additional details. The flag field contains 6 bits. The ACK bit is used to indicate that the 
value carried in the acknowledgment field is valid; that is, the segment contains an 
acknowledgment for a segment that has been successfully received. The RST, Figure 3.29 TCP 
segment structure SYN, and FIN bits are used for connection setup and teardown, as we will 
discuss at the end of this section. The CWR and ECE bits are used in explicit congestion 
notification, as discussed in Section 3.7.2. Setting the PSH bit indicates that the receiver should 
pass the data to the upper layer immediately. Finally, the URG bit is used to indicate that there 
is data in this segment that the sending-side upper-layer entity has marked as “urgent.” The 
location of the last byte of this urgent data is indicated by the 16-bit urgent data pointer field. 


## Page 12

TCP must inform the receiving-side upperlayer entity when urgent data exists and pass it a 
pointer to the end of the urgent data. (In practice, the PSH, URG, and the urgent data pointer are 
not used. However, we mention these fields for completeness.) Our experience as teachers is 
that our students sometimes find discussion of packet formats rather dry and perhaps a bit 
boring. For a fun and fanciful look at TCP header fields, particularly if you love Legos™ as we do, 
see [Pomeranz 2010]. Sequence Numbers and Acknowledgment Numbers Two of the most 
important fields in the TCP segment header are the sequence number field and the 
acknowledgment number field. These fields are a critical part of TCP’s reliable data transfer 
service. But before discussing how these fields are used to provide reliable data transfer, let us 
first explain what exactly TCP puts in these fields. Figure 3.30 Dividing file data into TCP 
segments TCP views data as an unstructured, but ordered, stream of bytes. TCP’s use of 
sequence numbers reflects this view in that sequence numbers are over the stream of 
transmitted bytes and not over the series of transmitted segments. The sequence number for a 
segment is therefore the byte-stream number of the first byte in the segment. Let’s look at an 
example. Suppose that a process in Host A wants to send a stream of data to a process in Host 
B over a TCP connection. The TCP in Host A will implicitly number each byte in the data stream. 
Suppose that the data stream consists of a file consisting of 500,000 bytes, that the MSS is 
1,000 bytes, and that the first byte of the data stream is numbered 0. As shown in Figure 3.30, 
TCP constructs 500 segments out of the data stream. The first segment gets assigned sequence 
number 0, the second segment gets assigned sequence number 1,000, the third segment gets 
assigned sequence number 2,000, and so on. Each sequence number is inserted in the 
sequence number field in the header of the appropriate TCP segment. Now let’s consider 
acknowledgment numbers. These are a little trickier than sequence numbers. Recall that TCP is 
full-duplex, so that Host A may be receiving data from Host B while it sends data to Host B (as 
part of the same TCP connection). Each of the segments that arrive from Host B has a sequence 
number for the data flowing from B to A. The acknowledgment number that Host A puts in its 
segment is the sequence number of the next byte Host A is expecting from Host B. It is good to 
look at a few examples to understand what is going on here. Suppose that Host A has received 
all bytes numbered 0 through 535 from B and suppose that it is about to send a segment to Host 
B. Host A is waiting for byte 536 and all the subsequent bytes in Host B’s data stream. So Host A 
puts 536 in the acknowledgment number field of the segment it sends to B. As another 
example, suppose that Host A has received one segment from Host B containing bytes 0 
through 535 and another segment containing bytes 900 through 1,000. For some reason Host A 
has not yet received bytes 536 through 899. In this example, Host A is still waiting for byte 536 
(and beyond) in order to re-create B’s data stream. Thus, A’s next segment to B will contain 536 
in the acknowledgment number field. Because TCP only acknowledges bytes up to the first 
missing byte in the stream, TCP is said to provide cumulative acknowledgments. This last 
example also brings up an important but subtle issue. Host A received the third segment (bytes 
900 through 1,000) before receiving the second segment (bytes 536 through 899). Thus, the 
third segment arrived out of order. The subtle issue is: What does a host do when it receives 
out-of-order segments in a TCP connection? Interestingly, the TCP RFCs do not impose any 
rules here and leave the decision up to the programmers implementing a TCP implementation. 
There are basically two choices: either (1) the receiver immediately discards out-of-order 
segments (which, as we discussed earlier, can simplify receiver design), or (2) the receiver 
keeps the out-of-order bytes and waits for the missing bytes to fill in the gaps. Clearly, the latter 
choice is more efficient in terms of network bandwidth, and is the approach taken in practice. In 
Figure 3.30, we assumed that the initial sequence number was zero. In truth, both sides of a 
TCP connection randomly choose an initial sequence number. This is done to minimize the 


## Page 13

possibility that a segment that is still present in the network from an earlier, already-terminated 
connection between two hosts is mistaken for a valid segment in a later connection between 
these same two hosts (which also happen to be using the same port numbers as the old 
connection) [Sunshine 1978]. Telnet: A Case Study for Sequence and Acknowledgment 
Numbers Telnet, defined in RFC 854, is a popular application-layer protocol used for remote 
login. It runs over TCP and is designed to work between any pair of hosts. Unlike the bulk data 
transfer applications discussed in Chapter 2, Telnet is an interactive application. We discuss a 
Telnet example here, as it nicely illustrates TCP sequence and acknowledgment numbers. We 
note that many users now prefer to use the SSH protocol rather than Telnet, since data sent in a 
Telnet connection (including passwords!) are not encrypted, making Telnet vulnerable to 
eavesdropping attacks (as discussed in Section 8.7). Suppose Host A initiates a Telnet session 
with Host B. Because Host A initiates the session, it is labeled the client, and Host B is labeled 
the server. Each character typed by the user (at the client) will be sent to the remote host; the 
remote host will send back a copy of each character, which will be displayed on the Telnet 
user’s screen. This “echo back” is used to ensure that characters seen by the Telnet user have 
already been received and processed at the remote site. Each character thus traverses the 
network twice between the time the user hits the key and the time the character is displayed on 
the user’s monitor. Now suppose the user types a single letter, ‘C,’ and then grabs a coffee. 
Let’s examine the TCP segments that are sent between the client and server. As shown in Figure 
3.31, we suppose the starting sequence numbers are 42 and 79 for the client and server, 
respectively. Recall that the sequence number of a segment is the sequence number of the first 
byte in the data field. Thus, the first segment sent from the client will have sequence number 
42; the first segment sent from the server will have sequence number 79. Recall that the 
acknowledgment number is the sequence Figure 3.31 Sequence and acknowledgment 
numbers for a simple Telnet application over TCP number of the next byte of data that the host 
is waiting for. After the TCP connection is established but before any data is sent, the client is 
waiting for byte 79 and the server is waiting for byte 42. As shown in Figure 3.31, three segments 
are sent. The first segment is sent from the client to the server, containing the 1-byte ASCII 
representation of the letter ‘C’ in its data field. This first segment also has 42 in its sequence 
number field, as we just described. Also, because the client has not yet received any data from 
the server, this first segment will have 79 in its acknowledgment number field. The second 
segment is sent from the server to the client. It serves a dual purpose. First it provides an 
acknowledgment of the data the server has received. By putting 43 in the acknowledgment 
field, the server is telling the client that it has successfully received everything up through byte 
42 and is now waiting for bytes 43 onward. The second purpose of this segment is to echo back 
the letter ‘C.’ Thus, the second segment has the ASCII representation of ‘C’ in its data field. This 
second segment has the sequence number 79, the initial sequence number of the server-to-
client data flow of this TCP connection, as this is the very first byte of data that the server is 
sending. Note that the acknowledgment for client-to-server data is carried in a segment 
carrying server-to-client data; this acknowledgment is said to be piggybacked on the server-to-
client data segment. The third segment is sent from the client to the server. Its sole purpose is 
to acknowledge the data it has received from the server. (Recall that the second segment 
contained data—the letter ‘C’—from the server to the client.) This segment has an empty data 
field (that is, the acknowledgment is not being piggybacked with any client-to-server data). The 
segment has 80 in the acknowledgment number field because the client has received the 
stream of bytes up through byte sequence number 79 and it is now waiting for bytes 80 onward. 
You might think it odd that this segment also has a sequence number since the segment 
contains no data. But because TCP has a sequence number field, the segment needs to have 


## Page 14

some sequence number. 3.5.3 Round-Trip Time Estimation and Timeout TCP, like our rdt 
protocol in Section 3.4, uses a timeout/retransmit mechanism to recover from lost segments. 
Although this is conceptually simple, many subtle issues arise when we implement a 
timeout/retransmit mechanism in an actual protocol such as TCP. Perhaps the most obvious 
question is the length of the timeout intervals. Clearly, the timeout should be larger than the 
connection’s round-trip time (RTT), that is, the time from when a segment is sent until it is 
acknowledged. Otherwise, unnecessary retransmissions would be sent. But how much larger? 
How should the RTT be estimated in the first place? Should a timer be associated with each and 
every unacknowledged segment? So many questions! Our discussion in this section is based 
on the TCP work in [Jacobson 1988] and the current IETF recommendations for managing TCP 
timers [RFC 6298]. Estimating the Round-Trip Time Let’s begin our study of TCP timer 
management by considering how TCP estimates the round-trip time between sender and 
receiver. This is accomplished as follows. The sample RTT, denoted SampleRTT , for a segment 
is the amount of time between when the segment is sent (that is, passed to IP) and when an 
acknowledgment for the segment is received. Instead of measuring a SampleRTT for every 
transmitted segment, most TCP implementations take only one SampleRTT measurement at a 
time. That is, at any point in time, the SampleRTT is being estimated for only one of the 
transmitted but currently unacknowledged segments, leading to a new value of SampleRTT 
approximately once every RTT. Also, TCP never computes a SampleRTT for a segment that has 
been retransmitted; it only measures SampleRTT for segments that have been transmitted once 
[Karn 1987]. (A problem at the end of the chapter asks you to consider why.) Obviously, the 
SampleRTT values will fluctuate from segment to segment due to congestion in the routers and 
to the varying load on the end systems. Because of this fluctuation, any given SampleRTT value 
may be atypical. In order to estimate a typical RTT, it is therefore natural to take some sort of 
average of the SampleRTT values. TCP maintains an average, called EstimatedRTT , of the 
SampleRTT values. Upon obtaining a new SampleRTT , TCP updates EstimatedRTT according to 
the following formula: The formula above is written in the form of a programming-language 
statement—the new value of EstimatedRTT is a weighted combination of the previous value of 
EstimatedRTT and the new value for SampleRTT. The recommended value of α is α = 0.125 (that 
is, 1/8) [RFC 6298], in which case the formula above becomes: Note that EstimatedRTT is a 
weighted average of the SampleRTT values. As discussed in a homework problem at the end of 
this chapter, this weighted average puts more weight on recent samples than on old samples. 
This is natural, as the more recent samples better reflect the current congestion in the network. 
In statistics, such an average is called an exponential weighted moving average (EWMA). The 
word “exponential” appears in EWMA because the weight of a given SampleRTT decays 
exponentially fast as the updates proceed. In the homework problems you will be asked to 
derive the exponential term in EstimatedRTT . Figure 3.32 shows the SampleRTT values and 
EstimatedRTT for a value of α = 1/8 for a TCP connection between gaia.cs.umass.edu (in 
Amherst, Massachusetts) to fantasia.eurecom.fr (in the south of France). Clearly, the variations 
in the SampleRTT are smoothed out in the computation of the EstimatedRTT . In addition to 
having an estimate of the RTT, it is also valuable to have a measure of the variability of the RTT. 
[RFC 6298] defines the RTT variation, DevRTT , as an estimate of how much SampleRTT typically 
deviates from EstimatedRTT : Note that DevRTT is an EWMA of the difference between 
SampleRTT and EstimatedRTT . If the SampleRTT values have little fluctuation, then DevRTT will 
be small; on the other hand, if there is a lot of fluctuation, DevRTT will be large. The 
recommended value of β is 0.25. EstimatedRTT=(1−α)⋅EstimatedRTT+α⋅SampleRTT 
EstimatedRTT=0.875⋅EstimatedRTT+0.125⋅SampleRTT 
DevRTT=(1−β)⋅DevRTT+β⋅|SampleRTT−EstimatedRTT| Setting and Managing the Retransmission 


## Page 15

Timeout Interval Given values of EstimatedRTT and DevRTT , what value should be used for 
TCP’s timeout interval? Clearly, the interval should be greater than or equal to PRINCIPLES IN 
PRACTICE TCP provides reliable data transfer by using positive acknowledgments and timers in 
much the same way that we studied in Section 3.4. TCP acknowledges data that has been 
received correctly, and it then retransmits segments when segments or their corresponding 
acknowledgments are thought to be lost or corrupted. Certain versions of TCP also have an 
implicit NAK mechanism—with TCP’s fast retransmit mechanism, the receipt of three duplicate 
ACKs for a given segment serves as an implicit NAK for the following segment, triggering 
retransmission of that segment before timeout. TCP uses sequences of numbers to allow the 
receiver to identify lost or duplicate segments. Just as in the case of our reliable data transfer 
protocol, rdt3.0 , TCP cannot itself tell for certain if a segment, or its ACK, is lost, corrupted, or 
overly delayed. At the sender, TCP’s response will be the same: retransmit the segment in 
question. TCP also uses pipelining, allowing the sender to have multiple transmitted but yet-to-
beacknowledged segments outstanding at any given time. We saw earlier that pipelining can 
greatly improve a session’s throughput when the ratio of the segment size to round-trip delay is 
small. The specific number of outstanding, unacknowledged segments that a sender can have 
is determined by TCP’s flow-control and congestion-control mechanisms. TCP flow control is 
discussed at the end of this section; TCP congestion control is discussed in Section 3.7. For the 
time being, we must simply be aware that the TCP sender uses pipelining. EstimatedRTT , or 
unnecessary retransmissions would be sent. But the timeout interval should not be too much 
larger than EstimatedRTT ; otherwise, when a segment is lost, TCP would not quickly retransmit 
the segment, leading to large data transfer delays. It is therefore desirable to set the timeout 
equal to the EstimatedRTT plus some margin. The margin should be large when there is a lot of 
fluctuation in the SampleRTT values; it should be small when there is little fluctuation. The 
value of DevRTT should thus come into play here. All of these considerations are taken into 
account in TCP’s method for determining the retransmission timeout interval: An initial 
TimeoutInterval value of 1 second is recommended [RFC 6298]. Also, when a timeout occurs, 
the value of TimeoutInterval is doubled to avoid a premature timeout occurring for a 
TimeoutInterval=EstimatedRTT+4⋅DevRTT subsequent segment that will soon be 
acknowledged. However, as soon as a segment is received and EstimatedRTT is updated, the 
TimeoutInterval is again computed using the formula above. Figure 3.32 RTT samples and RTT 
estimates 3.5.4 Reliable Data Transfer Recall that the Internet’s network-layer service (IP 
service) is unreliable. IP does not guarantee datagram delivery, does not guarantee in-order 
delivery of datagrams, and does not guarantee the integrity of the data in the datagrams. With IP 
service, datagrams can overflow router buffers and never reach their destination, datagrams 
can arrive out of order, and bits in the datagram can get corrupted (flipped from 0 to 1 and vice 
versa). Because transport-layer segments are carried across the network by IP datagrams, 
transport-layer segments can suffer from these problems as well. TCP creates a reliable data 
transfer service on top of IP’s unreliable best-effort service. TCP’s reliable data transfer service 
ensures that the data stream that a process reads out of its TCP receive buffer is uncorrupted, 
without gaps, without duplication, and in sequence; that is, the byte stream is exactly the same 
byte stream that was sent by the end system on the other side of the connection. How TCP 
provides a reliable data transfer involves many of the principles that we studied in Section 3.4. 
In our earlier development of reliable data transfer techniques, it was conceptually easiest to 
assume that an individual timer is associated with each transmitted but not yet acknowledged 
segment. While this is great in theory, timer management can require considerable overhead. 
Thus, the recommended TCP timer management procedures [RFC 6298] use only a single 
retransmission timer, even if there are multiple transmitted but not yet acknowledged 


## Page 16

segments. The TCP protocol described in this section follows this single-timer 
recommendation. We will discuss how TCP provides reliable data transfer in two incremental 
steps. We first present a highly simplified description of a TCP sender that uses only timeouts to 
recover from lost segments; we then present a more complete description that uses duplicate 
acknowledgments in addition to timeouts. In the ensuing discussion, we suppose that data is 
being sent in only one direction, from Host A to Host B, and that Host A is sending a large file. 
Figure 3.33 presents a highly simplified description of a TCP sender. We see that there are three 
major events related to data transmission and retransmission in the TCP sender: data received 
from application above; timer timeout; and ACK Figure 3.33 Simplified TCP sender receipt. 
Upon the occurrence of the first major event, TCP receives data from the application, 
encapsulates the data in a segment, and passes the segment to IP. Note that each segment 
includes a sequence number that is the byte-stream number of the first data byte in the 
segment, as described in Section 3.5.2. Also note that if the timer is already not running for 
some other segment, TCP starts the timer when the segment is passed to IP. (It is helpful to 
think of the timer as being associated with the oldest unacknowledged segment.) The expiration 
interval for this timer is the TimeoutInterval , which is calculated from EstimatedRTT and 
DevRTT , as described in Section 3.5.3. The second major event is the timeout. TCP responds to 
the timeout event by retransmitting the segment that caused the timeout. TCP then restarts the 
timer. The third major event that must be handled by the TCP sender is the arrival of an 
acknowledgment segment (ACK) from the receiver (more specifically, a segment containing a 
valid ACK field value). On the occurrence of this event, TCP compares the ACK value y with its 
variable SendBase . The TCP state variable SendBase is the sequence number of the oldest 
unacknowledged byte. (Thus SendBase–1 is the sequence number of the last byte that is known 
to have been received correctly and in order at the receiver.) As indicated earlier, TCP uses 
cumulative acknowledgments, so that y acknowledges the receipt of all bytes before byte 
number y . If y > SendBase , then the ACK is acknowledging one or more previously 
unacknowledged segments. Thus the sender updates its SendBase variable; it also restarts the 
timer if there currently are any not-yet-acknowledged segments. A Few Interesting Scenarios 
We have just described a highly simplified version of how TCP provides reliable data transfer. 
But even this highly simplified version has many subtleties. To get a good feeling for how this 
protocol works, let’s now walk through a few simple scenarios. Figure 3.34 depicts the first 
scenario, in which Host A sends one segment to Host B. Suppose that this segment has 
sequence number 92 and contains 8 bytes of data. After sending this segment, Host A waits for 
a segment from B with acknowledgment number 100. Although the segment from A is received 
at B, the acknowledgment from B to A gets lost. In this case, the timeout event occurs, and Host 
A retransmits the same segment. Of course, when Host B receives the retransmission, it 
observes from the sequence number that the segment contains data that has already been 
received. Thus, TCP in Host B will discard the bytes in the retransmitted segment. In a second 
scenario, shown in Figure 3.35, Host A sends two segments back to back. The first segment has 
sequence number 92 and 8 bytes of data, and the second segment has sequence number 100 
and 20 bytes of data. Suppose that both segments arrive intact at B, and B sends two separate 
acknowledgments for each of these segments. The first of these acknowledgments has 
acknowledgment number 100; the second has acknowledgment number 120. Suppose now 
that neither of the acknowledgments arrives at Host A before the timeout. When the timeout 
event occurs, Host Figure 3.34 Retransmission due to a lost acknowledgment A resends the 
first segment with sequence number 92 and restarts the timer. As long as the ACK for the 
second segment arrives before the new timeout, the second segment will not be retransmitted. 
In a third and final scenario, suppose Host A sends the two segments, exactly as in the second 


## Page 17

example. The acknowledgment of the first segment is lost in the network, but just before the 
timeout event, Host A receives an acknowledgment with acknowledgment number 120. Host A 
therefore knows that Host B has received everything up through byte 119; so Host A does not 
resend either of the two segments. This scenario is illustrated in Figure 3.36. Doubling the 
Timeout Interval We now discuss a few modifications that most TCP implementations employ. 
The first concerns the length of the timeout interval after a timer expiration. In this modification, 
whenever the timeout event occurs, TCP retransmits the not-yet-acknowledged segment with 
the smallest sequence number, as described above. But each time TCP retransmits, it sets the 
next timeout interval to twice the previous value, Figure 3.35 Segment 100 not retransmitted 
rather than deriving it from the last EstimatedRTT and DevRTT (as described in Section 3.5.3). 
For example, suppose TimeoutInterval associated with the oldest not yet acknowledged 
segment is .75 sec when the timer first expires. TCP will then retransmit this segment and set 
the new expiration time to 1.5 sec. If the timer expires again 1.5 sec later, TCP will again 
retransmit this segment, now setting the expiration time to 3.0 sec. Thus the intervals grow 
exponentially after each retransmission. However, whenever the timer is started after either of 
the two other events (that is, data received from application above, and ACK received), the 
TimeoutInterval is derived from the most recent values of EstimatedRTT and DevRTT . This 
modification provides a limited form of congestion control. (More comprehensive forms of TCP 
congestion control will be studied in Section 3.7.) The timer expiration is most likely caused by 
congestion in the network, that is, too many packets arriving at one (or more) router queues in 
the path between the source and destination, causing packets to be dropped and/or long 
queuing delays. In times of congestion, if the sources continue to retransmit packets 
persistently, the congestion Figure 3.36 A cumulative acknowledgment avoids retransmission 
of the first segment may get worse. Instead, TCP acts more politely, with each sender 
retransmitting after longer and longer intervals. We will see that a similar idea is used by 
Ethernet when we study CSMA/CD in Chapter 6. Fast Retransmit One of the problems with 
timeout-triggered retransmissions is that the timeout period can be relatively long. When a 
segment is lost, this long timeout period forces the sender to delay resending the lost packet, 
thereby increasing the end-to-end delay. Fortunately, the sender can often detect packet loss 
well before the timeout event occurs by noting so-called duplicate ACKs. A duplicate ACK is an 
ACK that reacknowledges a segment for which the sender has already received an earlier 
acknowledgment. To understand the sender’s response to a duplicate ACK, we must look at 
why the receiver sends a duplicate ACK in the first place. Table 3.2 summarizes the TCP 
receiver’s ACK generation policy [RFC 5681]. When a TCP receiver receives Table 3.2 TCP ACK 
Generation Recommendation [RFC 5681] Event TCP Receiver Action Arrival of in-order segment 
with expected sequence number. All data up to expected sequence number already 
acknowledged. Delayed ACK. Wait up to 500 msec for arrival of another in-order segment. If 
next in-order segment does not arrive in this interval, send an ACK. Arrival of in-order segment 
with expected sequence number. One other in-order segment waiting for ACK transmission. 
One Immediately send single cumulative ACK, ACKing both in-order segments. Arrival of out-of-
order segment with higherthan-expected sequence number. Gap detected. Immediately send 
duplicate ACK, indicating sequence number of next expected byte (which is the lower end of the 
gap). Arrival of segment that partially or completely fills in gap in received data. Immediately 
send ACK, provided that segment starts at the lower end of gap. a segment with a sequence 
number that is larger than the next, expected, in-order sequence number, it detects a gap in the 
data stream—that is, a missing segment. This gap could be the result of lost or reordered 
segments within the network. Since TCP does not use negative acknowledgments, the receiver 
cannot send an explicit negative acknowledgment back to the sender. Instead, it simply 


## Page 18

reacknowledges (that is, generates a duplicate ACK for) the last in-order byte of data it has 
received. (Note that Table 3.2 allows for the case that the receiver does not discard out-of-order 
segments.) Because a sender often sends a large number of segments back to back, if one 
segment is lost, there will likely be many back-to-back duplicate ACKs. If the TCP sender 
receives three duplicate ACKs for the same data, it takes this as an indication that the segment 
following the segment that has been ACKed three times has been lost. (In the homework 
problems, we consider the question of why the sender waits for three duplicate ACKs, rather 
than just a single duplicate ACK.) In the case that three duplicate ACKs are received, the TCP 
sender performs a fast retransmit [RFC 5681], retransmitting the missing segment before that 
segment’s timer expires. This is shown in Figure 3.37, where the second segment is lost, then 
retransmitted before its timer expires. For TCP with fast retransmit, the following code snippet 
replaces the ACK received event in Figure 3.33: event: ACK received, with ACK field value of y if 
(y > SendBase) { SendBase=y if (there are currently any not yet acknowledged segments) start 
timer } Figure 3.37 Fast retransmit: retransmitting the missing segment before the segment’s 
timer expires else {/* a duplicate ACK for already ACKed segment */ increment number of 
duplicate ACKs received for y if (number of duplicate ACKS received for y==3) /* TCP fast 
retransmit */ resend segment with sequence number y } break; We noted earlier that many 
subtle issues arise when a timeout/retransmit mechanism is implemented in an actual 
protocol such as TCP. The procedures above, which have evolved as a result of more than 20 
years of experience with TCP timers, should convince you that this is indeed the case! Go-Back-
N or Selective Repeat? Let us close our study of TCP’s error-recovery mechanism by 
considering the following question: Is TCP a GBN or an SR protocol? Recall that TCP 
acknowledgments are cumulative and correctly received but out-of-order segments are not 
individually ACKed by the receiver. Consequently, as shown in Figure 3.33 (see also Figure 
3.19), the TCP sender need only maintain the smallest sequence number of a transmitted but 
unacknowledged byte ( SendBase ) and the sequence number of the next byte to be sent ( 
NextSeqNum ). In this sense, TCP looks a lot like a GBN-style protocol. But there are some 
striking differences between TCP and Go-Back-N. Many TCP implementations will buffer 
correctly received but out-of-order segments [Stevens 1994]. Consider also what happens 
when the sender sends a sequence of segments 1, 2, . . ., N, and all of the segments arrive in 
order without error at the receiver. Further suppose that the acknowledgment for packet gets 
lost, but the remaining acknowledgments arrive at the sender before their respective timeouts. 
In this example, GBN would retransmit not only packet n, but also all of the subsequent packets 
TCP, on the other hand, would retransmit at most one segment, namely, segment n. Moreover, 
TCP would not even retransmit segment n if the acknowledgment for segment arrived before 
the timeout for segment n. A proposed modification to TCP, the so-called selective 
acknowledgment [RFC 2018], allows a TCP receiver to acknowledge out-of-order segments 
selectively rather than just cumulatively acknowledging the last correctly received, in-order 
segment. When combined with selective retransmission—skipping the retransmission of 
segments that have already been selectively acknowledged by the receiver—TCP looks a lot like 
our generic SR protocol. Thus, TCP’s error-recovery mechanism is probably best categorized as 
a hybrid of GBN and SR protocols. 3.5.5 Flow Control Recall that the hosts on each side of a 
TCP connection set aside a receive buffer for the connection. When the TCP connection 
receives bytes that are correct and in sequence, it places the data in the receive buffer. The 
associated application process will read data from this buffer, but not necessarily at the instant 
the data arrives. Indeed, the receiving application may be busy with some other task and may 
not even attempt to read the data until long after it has arrived. If the application is relatively 
slow at reading the data, the sender can very easily overflow the connection’s receive buffer by 


## Page 19

sending too much data too quickly. n<aS/R+RTT>2S/R S/R+RTT>4 S/R S/R>RTT In this lab, you’ll 
use your Web browser to access a file from a Web server. As in earlier Wireshark labs, you’ll use 
Wireshark to capture the packets arriving at your computer. Unlike earlier labs, you’ll also be 
able to download a Wireshark-readable packet trace from the Web server from which you 
downloaded the file. In this server trace, you’ll find the packets that were generated by your own 
access of the Web server. You’ll analyze the client- and server-side traces to explore aspects of 
TCP. In particular, you’ll evaluate the performance of the TCP connection between your 
computer and the Web server. You’ll trace TCP’s window behavior, and infer packet loss, 
retransmission, flow control and congestion control behavior, and estimated roundtrip time. As 
is the case with all Wireshark labs, the full description of this lab is available at this book’s Web 
site, www.pearsonhighered.com/cs-resources. Wireshark Lab: Exploring UDP In this short lab, 
you’ll do a packet capture and analysis of your favorite application that uses UDP (for example, 
DNS or a multimedia application such as Skype). As we learned in Section 3.3, UDP is a simple, 
no-frills transport protocol. In this lab, you’ll investigate the header fields in the UDP segment 
as well as the checksum calculation. As is the case with all Wireshark labs, the full description 
of this lab is available at this book’s Web site, www.pearsonhighered.com/cs-resources. AN 
INTERVIEW WITH... Van Jacobson Van Jacobson works at Google and was previously a 
Research Fellow at PARC. Prior to that, he was co-founder and Chief Scientist of Packet Design. 
Before that, he was Chief Scientist at Cisco. Before joining Cisco, he was head of the Network 
Research Group at Lawrence Berkeley National Laboratory and taught at UC Berkeley and 
Stanford. Van received the ACM SIGCOMM Award in 2001 for outstanding lifetime contribution 
to the field of communication networks and the IEEE Kobayashi Award in 2002 for “contributing 
to the understanding of network congestion and developing congestion control mechanisms 
that enabled the successful scaling of the Internet”. He was elected to the U.S. National 
Academy of Engineering in 2004. Please describe one or two of the most exciting projects you 
have worked on during your career. What were the biggest challenges? School teaches us lots 
of ways to find answers. In every interesting problem I’ve worked on, the challenge has been 
finding the right question. When Mike Karels and I started looking at TCP congestion, we spent 
months staring at protocol and packet traces asking “Why is it failing?”. One day in Mike’s 
office, one of us said “The reason I can’t figure out why it fails is because I don’t understand 
how it ever worked to begin with.” That turned out to be the right question and it forced us to 
figure out the “ack clocking” that makes TCP work. After that, the rest was easy. More generally, 
where do you see the future of networking and the Internet? For most people, the Web is the 
Internet. Networking geeks smile politely since we know the Web is an application running over 
the Internet but what if they’re right? The Internet is about enabling conversations between 
pairs of hosts. The Web is about distributed information production and consumption. 
“Information propagation” is a very general view of communication of which “pairwise 
conversation” is a tiny subset. We need to move into the larger tent. Networking today deals 
with broadcast media (radios, PONs, etc.) by pretending it’s a point-topoint wire. That’s 
massively inefficient. Terabits-per-second of data are being exchanged all over the World via 
thumb drives or smart phones but we don’t know how to treat that as “networking”. ISPs are 
busily setting up caches and CDNs to scalably distribute video and audio. Caching is a 
necessary part of the solution but there’s no part of today’s networking—from Information, 
Queuing or Traffic Theory down to the Internet protocol specs—that tells us how to engineer 
and deploy it. I think and hope that over the next few years, networking will evolve to embrace 
the much larger vision of communication that underlies the Web. What people inspired you 
professionally? When I was in grad school, Richard Feynman visited and gave a colloquium. He 
talked about a piece of Quantum theory that I’d been struggling with all semester and his 


## Page 20

explanation was so simple and lucid that what had been incomprehensible gibberish to me 
became obvious and inevitable. That ability to see and convey the simplicity that underlies our 
complex world seems to me a rare and wonderful gift. What are your recommendations for 
students who want careers in computer science and networking? It’s a wonderful field—
computers and networking have probably had more impact on society than any invention since 
the book. Networking is fundamentally about connecting stuff, and studying it helps you make 
intellectual connections: Ant foraging & Bee dances demonstrate protocol design better than 
RFCs, traffic jams or people leaving a packed stadium are the essence of congestion, and 
students finding flights back to school in a post-Thanksgiving blizzard are the core of dynamic 
routing. If you’re interested in lots of stuff and want to have an impact, it’s hard to imagine a 
better field. Chapter 4 The Network Layer: Data Plane We learned in the previous chapter that 
the transport layer provides various forms of process-to-process communication by relying on 
the network layer’s host-to-host communication service. We also learned that the transport 
layer does so without any knowledge about how the network layer actually implements this 
service. So perhaps you’re now wondering, what’s under the hood of the host-to-host 
communication service, what makes it tick? In this chapter and the next, we’ll learn exactly how 
the network layer can provide its host-to-host communication service. We’ll see that unlike the 
transport and application layers, there is a piece of the network layer in each and every host and 
router in the network. Because of this, network-layer protocols are among the most challenging 
(and therefore among the most interesting!) in the protocol stack. Since the network layer is 
arguably the most complex layer in the protocol stack, we’ll have a lot of ground to cover here. 
Indeed, there is so much to cover that we cover the network layer in two chapters. We’ll see 
that the network layer can be decomposed into two interacting parts, the data plane and the 
control plane. In Chapter 4, we’ll first cover the data plane functions of the network layer—the 
perrouter functions in the network layer that determine how a datagram (that is, a network-layer 
packet) arriving on one of a router’s input links is forwarded to one of that router’s output links. 
We’ll cover both traditional IP forwarding (where forwarding is based on a datagram’s 
destination address) and generalized forwarding (where forwarding and other functions may be 
performed using values in several different fields in the datagram’s header). We’ll study the IPv4 
and IPv6 protocols and addressing in detail. In Chapter 5, we’ll cover the control plane 
functions of the network layer—the network-wide logic that controls how a datagram is routed 
among routers along an end-to-end path from the source host to the destination host. We’ll 
cover routing algorithms, as well as routing protocols, such as OSPF and BGP, that are in 
widespread use in today’s Internet. Traditionally, these control-plane routing protocols and 
data-plane forwarding functions have been implemented together, monolithically, within a 
router. Software-defined networking (SDN) explicitly separates the data plane and control plane 
by implementing these control plane functions as a separate service, typically in a remote 
“controller.” We’ll also cover SDN controllers in Chapter 5. This distinction between data-plane 
and control-plane functions in the network layer is an important concept to keep in mind as you 
learn about the network layer —it will help structure your thinking about the network layer and 
reflects a modern view of the network layer’s role in computer networking. 4.1 Overview of 
Network Layer Figure 4.1 shows a simple network with two hosts, H1 and H2, and several 
routers on the path between H1 and H2. Let’s suppose that H1 is sending information to H2, 
and consider the role of the network layer in these hosts and in the intervening routers. The 
network layer in H1 takes segments from the transport layer in H1, encapsulates each segment 
into a datagram, and then sends the datagrams to its nearby router, R1. At the receiving host, 
H2, the network layer receives the datagrams from its nearby router R2, extracts the transport-
layer segments, and delivers the segments up to the transport layer at H2. The primary data-


