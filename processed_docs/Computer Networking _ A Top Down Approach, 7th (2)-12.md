# Computer Networking _ A Top Down Approach, 7th (2)-12


## Page 1

indicating the new IP address. Also, if Bob remains at the same device for an extended period of 
time, the device will send refresh register messages, indicating that the most recently sent IP 
address is still valid. (In the example above, refresh messages need to be sent every 3600 
seconds to maintain the address at the registrar server.) It is worth noting that the registrar is 
analogous to a DNS authoritative name server: The DNS server translates fixed host names to 
fixed IP addresses; the SIP registrar translates fixed human identifiers (for example, 
bob@domain.com) to dynamic IP addresses. Often SIP registrars and SIP proxies are run on the 
same host. Now let’s examine how Alice’s SIP proxy server obtains Bob’s current IP address. 
From the preceding discussion we see that the proxy server simply needs to forward Alice’s 
INVITE message to Bob’s registrar/proxy. The registrar/proxy could then forward the message to 
Bob’s current SIP device. Finally, Bob, having now received Alice’s INVITE message, could send 
an SIP response to Alice. As an example, consider Figure 9.10, in which jim@umass.edu, 
currently working on 217.123.56.89, wants to initiate a Voice-over-IP (VoIP) session with 
keith@upenn.edu, currently working on 197.87.54.21. The following steps are taken: Figure 9.10 
Session initiation, involving SIP proxies and registrars (1) Jim sends an INVITE message to the 
umass SIP proxy. (2) The proxy does a DNS lookup on the SIP registrar upenn.edu (not shown in 
diagram) and then forwards the message to the registrar server. (3) Because keith@upenn.edu 
is no longer registered at the upenn registrar, the upenn registrar sends a redirect response, 
indicating that it should try keith@nyu.edu. (4) The umass proxy sends an INVITE message to 
the NYU SIP registrar. (5) The NYU registrar knows the IP address of keith@upenn.edu and 
forwards the INVITE message to the host 197.87.54.21, which is running Keith’s SIP client. (6–8) 
An SIP response is sent back through registrars/proxies to the SIP client on 217.123.56.89. (9) 
Media is sent directly between the two clients. (There is also an SIP acknowledgment message, 
which is not shown.) Our discussion of SIP has focused on call initiation for voice calls. SIP, 
being a signaling protocol for initiating and ending calls in general, can be used for video 
conference calls as well as for text-based sessions. In fact, SIP has become a fundamental 
component in many instant messaging applications. Readers desiring to learn more about SIP 
are encouraged to visit Henning Schulzrinne’s SIP Web site [Schulzrinne-SIP 2016]. In 
particular, on this site you will find open source software for SIP clients and servers [SIP 
Software 2016]. 9.5 Network Support for Multimedia In Sections 9.2 through 9.4, we learned 
how application-level mechanisms such as client buffering, prefetching, adapting media 
quality to available bandwidth, adaptive playout, and loss mitigation techniques can be used by 
multimedia applications to improve a multimedia application’s performance. We also learned 
how content distribution networks and P2P overlay networks can be used to provide a system-
level approach for delivering multimedia content. These techniques and approaches are all 
designed to be used in today’s best-effort Internet. Indeed, they are in use today precisely 
because the Internet provides only a single, best-effort class of service. But as designers of 
computer networks, we can’t help but ask whether the network (rather than the applications or 
application-level infrastructure alone) might provide mechanisms to support multimedia 
content delivery. As we’ll see shortly, the answer is, of course, “yes”! But we’ll also see that a 
number of these new network-level mechanisms have yet to be widely deployed. This may be 
due to their complexity and to the fact that application-level techniques together with best-
effort service and properly dimensioned network resources (for example, bandwidth) can 
indeed provide a “good-enough” (even if not-always-perfect) end-to-end multimedia delivery 
service. Table 9.4 summarizes three broad approaches towards providing network-level 
support for multimedia applications. Making the best of best-effort service. The application-
level mechanisms and infrastructure that we studied in Sections 9.2 through 9.4 can be 
successfully used in a well-dimensioned network where packet loss and excessive end-to-end 


## Page 2

delay rarely occur. When demand increases are forecasted, the ISPs deploy additional 
bandwidth and switching capacity to continue to ensure satisfactory delay and packet-loss 
performance [Huang 2005]. We’ll discuss such network dimensioning further in Section 9.5.1. 
Differentiated service. Since the early days of the Internet, it’s been envisioned that different 
types of traffic (for example, as indicated in the Type-of-Service field in the IP4v packet header) 
could be provided with different classes of service, rather than a single one-size-fits-all best-
effort service. With differentiated service, one type of traffic might be given strict priority over 
another class of traffic when both types of traffic are queued at a router. For example, packets 
belonging to a realtime conversational application might be given priority over other packets 
due to their stringent delay constraints. Introducing differentiated service into the network will 
require new mechanisms for packet marking (indicating a packet’s class of service), packet 
scheduling, and more. We’ll cover differentiated service, and new network mechanisms 
needed to implement this service, in Sections 9.5.2 and 9.5.3. Table 9.4 Three network-level 
approaches to supporting multimedia applications Approach Granularity Guarantee 
Mechanisms Complexity Deployment to date Making the best of besteffort service all traffic 
treated equally none, or soft application-layer support, CDNs, overlays, networklevel resource 
provisioning minimal everywhere Differentiated service different classes of traffic treated 
differently none, or soft packet marking, policing, scheduling medium some Perconnection 
Quality-ofService (QoS) Guarantees each sourcedestination flows treated differently soft or 
hard, once flow is admitted packet marking, policing, scheduling; call admission and signaling 
light little Per-connection Quality-of-Service (QoS) Guarantees. With per-connection QoS 
guarantees, each instance of an application explicitly reserves end-to-end bandwidth and thus 
has a guaranteed end-to-end performance. A hard guarantee means the application will receive 
its requested quality of service (QoS) with certainty. A soft guarantee means the application will 
receive its requested quality of service with high probability. For example, if a user wants to 
make a VoIP call from Host A to Host B, the user’s VoIP application reserves bandwidth 
explicitly in each link along a route between the two hosts. But permitting applications to make 
reservations and requiring the network to honor the reservations requires some big changes. 
First, we need a protocol that, on behalf of the applications, reserves link bandwidth on the 
paths from the senders to their receivers. Second, we’ll need new scheduling policies in the 
router queues so that per-connection bandwidth reservations can be honored. Finally, in order 
to make a reservation, the applications must give the network a description of the traffic that 
they intend to send into the network and the network will need to police each application’s 
traffic to make sure that it abides by that description. These mechanisms, when combined, 
require new and complex software in hosts and routers. Because per-connection QoS 
guaranteed service has not seen significant deployment, we’ll cover these mechanisms only 
briefly in Section 9.5.4. 9.5.1 Dimensioning Best-Effort Networks Fundamentally, the difficulty 
in supporting multimedia applications arises from their stringent performance requirements—
low end-to-end packet delay, delay jitter, and loss—and the fact that packet delay, delay jitter, 
and loss occur whenever the network becomes congested. A first approach to improving the 
quality of multimedia applications—an approach that can often be used to solve just about any 
problem where resources are constrained—is simply to “throw money at the problem” and thus 
simply avoid resource contention. In the case of networked multimedia, this means providing 
enough link capacity throughout the network so that network congestion, and its consequent 
packet delay and loss, never (or only very rarely) occurs. With enough link capacity, packets 
could zip through today’s Internet without queuing delay or loss. From many perspectives this is 
an ideal situation—multimedia applications would perform perfectly, users would be happy, 
and this could all be achieved with no changes to Internet’s best-effort architecture. The 


## Page 3

question, of course, is how much capacity is “enough” to achieve this nirvana, and whether the 
costs of providing “enough” bandwidth are practical from a business standpoint to the ISPs. 
The question of how much capacity to provide at network links in a given topology to achieve a 
given level of performance is often known as bandwidth provisioning. The even more 
complicated problem of how to design a network topology (where to place routers, how to 
interconnect routers with links, and what capacity to assign to links) to achieve a given level of 
end-to-end performance is a network design problem often referred to as network 
dimensioning. Both bandwidth provisioning and network dimensioning are complex topics, well 
beyond the scope of this textbook. We note here, however, that the following issues must be 
addressed in order to predict application-level performance between two network end points, 
and thus provision enough capacity to meet an application’s performance requirements. 
Models of traffic demand between network end points. Models may need to be specified at 
both the call level (for example, users “arriving” to the network and starting up end-to-end 
applications) and at the packet level (for example, packets being generated by ongoing 
applications). Note that workload may change over time. Well-defined performance 
requirements. For example, a performance requirement for supporting delay-sensitive traffic, 
such as a conversational multimedia application, might be that the probability that the end-to-
end delay of the packet is greater than a maximum tolerable delay be less than some small 
value [Fraleigh 2003]. Models to predict end-to-end performance for a given workload model, 
and techniques to find a minimal cost bandwidth allocation that will result in all user 
requirements being met. Here, researchers are busy developing performance models that can 
quantify performance for a given workload, and optimization techniques to find minimal-cost 
bandwidth allocations meeting performance requirements. Given that today’s best-effort 
Internet could (from a technology standpoint) support multimedia traffic at an appropriate 
performance level if it were dimensioned to do so, the natural question is why today’s Internet 
doesn’t do so. The answers are primarily economic and organizational. From an economic 
standpoint, would users be willing to pay their ISPs enough for the ISPs to install sufficient 
bandwidth to support multimedia applications over a best-effort Internet? The organizational 
issues are perhaps even more daunting. Note that an end-to-end path between two multimedia 
end points will pass through the networks of multiple ISPs. From an organizational standpoint, 
would these ISPs be willing to cooperate (perhaps with revenue sharing) to ensure that the end-
to-end path is properly dimensioned to support multimedia applications? For a perspective on 
these economic and organizational issues, see [Davies 2005]. For a perspective on provisioning 
tier-1 backbone networks to support delay-sensitive traffic, see [Fraleigh 2003]. 9.5.2 Providing 
Multiple Classes of Service Perhaps the simplest enhancement to the one-size-fits-all best-
effort service in today’s Internet is to divide traffic into classes, and provide different levels of 
service to these different classes of traffic. For example, an ISP might well want to provide a 
higher class of service to delay-sensitive Voice-over-IP or teleconferencing traffic (and charge 
more for this service!) than to elastic traffic such as e-mail or HTTP. Alternatively, an ISP may 
simply want to provide a higher quality of service to customers willing to pay more for this 
improved service. A number of residential wired-access ISPs and cellular wireless-access ISPs 
have adopted such tiered levels of service—with platinum-service subscribers receiving better 
performance than gold- or silver-service subscribers. We’re all familiar with different classes of 
service from our everyday lives—first-class airline passengers get better service than business-
class passengers, who in turn get better service than those of us who fly economy class; VIPs 
are provided immediate entry to events while everyone else waits in line; elders are revered in 
some countries and provided seats of honor and the finest food at a table. It’s important to note 
that such differential service is provided among aggregates of traffic, that is, among classes of 


## Page 4

traffic, not among individual connections. For example, all first-class passengers are handled 
the same (with no first-class passenger receiving any better treatment than any other first-class 
passenger), just as all VoIP packets would receive the same treatment within the network, 
independent of the particular end-to-end connection to which they belong. As we will see, by 
dealing with a small number of traffic aggregates, rather than a large number of individual 
connections, the new network mechanisms required to provide better-than-best service can be 
kept relatively simple. The early Internet designers clearly had this notion of multiple classes of 
service in mind. Recall the type-of-service (ToS) field in the IPv4 header discussed in Chapter 4. 
IEN123 [ISI 1979] describes the ToS field also present in an ancestor of the IPv4 datagram as 
follows: “The Type of Service [field] provides an indication of the abstract parameters of the 
quality of service desired. These parameters are to be used to guide the selection of the actual 
service parameters when transmitting a datagram through a particular network. Several 
networks offer service precedence, which somehow treats high precedence traffic as more 
important that other traffic.” More than four decades ago, the vision of providing different levels 
of service to different classes of traffic was clear! However, it’s taken us an equally long period 
of time to realize this vision. Motivating Scenarios Let’s begin our discussion of network 
mechanisms for providing multiple classes of service with a few motivating scenarios. Figure 
9.11 shows a simple network scenario in which two application packet flows originate on Hosts 
H1 and H2 on one LAN and are destined for Hosts H3 and H4 on another LAN. The routers on 
the two LANs are connected by a 1.5 Mbps link. Let’s assume the LAN speeds are significantly 
higher than 1.5 Mbps, and focus on the output queue of router R1; it is here that packet delay 
and packet loss will occur if the aggregate sending rate of H1 and H2 exceeds 1.5 Mbps. Let’s 
further suppose that a 1 Mbps audio application (for example, a CD-quality audio call) shares 
the Figure 9.11 Competing audio and HTTP applications 1.5 Mbps link between R1 and R2 with 
an HTTP Web-browsing application that is downloading a Web page from H2 to H4. In the best-
effort Internet, the audio and HTTP packets are mixed in the output queue at R1 and (typically) 
transmitted in a first-in-first-out (FIFO) order. In this scenario, a burst of packets from the Web 
server could potentially fill up the queue, causing IP audio packets to be excessively delayed or 
lost due to buffer overflow at R1. How should we solve this potential problem? Given that the 
HTTP Webbrowsing application does not have time constraints, our intuition might be to give 
strict priority to audio packets at R1. Under a strict priority scheduling discipline, an audio 
packet in the R1 output buffer would always be transmitted before any HTTP packet in the R1 
output buffer. The link from R1 to R2 would look like a dedicated link of 1.5 Mbps to the audio 
traffic, with HTTP traffic using the R1-to-R2 link only when no audio traffic is queued. In order for 
R1 to distinguish between the audio and HTTP packets in its queue, each packet must be 
marked as belonging to one of these two classes of traffic. This was the original goal of the type-
of-service (ToS) field in IPv4. As obvious as this might seem, this then is our first insight into 
mechanisms needed to provide multiple classes of traffic: Insight 1: Packet marking allows a 
router to distinguish among packets belonging to different classes of traffic. Note that although 
our example considers a competing multimedia and elastic flow, the same insight applies to 
the case that platinum, gold, and silver classes of service are implemented—a packetmarking 
mechanism is still needed to indicate that class of service to which a packet belongs. Now 
suppose that the router is configured to give priority to packets marked as belonging to the 1 
Mbps audio application. Since the outgoing link speed is 1.5 Mbps, even though the HTTP 
packets receive lower priority, they can still, on average, receive 0.5 Mbps of transmission 
service. But what happens if the audio application starts sending packets at a rate of 1.5 Mbps 
or higher (either maliciously or due to an error in the application)? In this case, the HTTP 
packets will starve, that is, they will not receive any service on the R1-to-R2 link. Similar 


## Page 5

problems would occur if multiple applications (for example, multiple audio calls), all with the 
same class of service as the audio application, were sharing the link’s bandwidth; they too 
could collectively starve the FTP session. Ideally, one wants a degree of isolation among 
classes of traffic so that one class of traffic can be protected from the other. This protection 
could be implemented at different places in the network—at each and every router, at first entry 
to the network, or at inter-domain network boundaries. This then is our second insight: Insight 
2: It is desirable to provide a degree of traffic isolation among classes so that one class is not 
adversely affected by another class of traffic that misbehaves. We’ll examine several specific 
mechanisms for providing such isolation among traffic classes. We note here that two broad 
approaches can be taken. First, it is possible to perform traffic policing, as shown in Figure 
9.12. If a traffic class or flow must meet certain criteria (for example, that the audio flow not 
exceed a peak rate of 1 Mbps), then a policing mechanism can be put into place to ensure that 
these criteria are indeed observed. If the policed application misbehaves, the policing 
mechanism will take some action (for example, drop or delay packets that are in violation of the 
criteria) so that the traffic actually entering the network conforms to the criteria. The leaky 
bucket mechanism that we’ll examine shortly is perhaps the most widely used policing 
mechanism. In Figure 9.12, the packet classification and marking mechanism (Insight 1) and 
the policing mechanism (Insight 2) are both implemented together at the network’s edge, either 
in the end system or at an edge router. A complementary approach for providing isolation 
among traffic classes is for the link-level packetscheduling mechanism to explicitly allocate a 
fixed amount of link bandwidth to each class. For example, the audio class could be allocated 1 
Mbps at R1, and the HTTP class could be allocated 0.5 Mbps. In this case, the audio and Figure 
9.12 Policing (and marking) the audio and HTTP traffic classes Figure 9.13 Logical isolation of 
audio and HTTP traffic classes HTTP flows see a logical link with capacity 1.0 and 0.5 Mbps, 
respectively, as shown in Figure 9.13. With strict enforcement of the link-level allocation of 
bandwidth, a class can use only the amount of bandwidth that has been allocated; in 
particular, it cannot utilize bandwidth that is not currently being used by others. For example, if 
the audio flow goes silent (for example, if the speaker pauses and generates no audio packets), 
the HTTP flow would still not be able to transmit more than 0.5 Mbps over the R1-to-R2 link, 
even though the audio flow’s 1 Mbps bandwidth allocation is not being used at that moment. 
Since bandwidth is a “use-it-or-lose-it” resource, there is no reason to prevent HTTP traffic from 
using bandwidth not used by the audio traffic. We’d like to use bandwidth as efficiently as 
possible, never wasting it when it could be otherwise used. This gives rise to our third insight: 
Insight 3: While providing isolation among classes or flows, it is desirable to use resources (for 
example, link bandwidth and buffers) as efficiently as possible. Recall from our discussion in 
Sections 1.3 and 4.2 that packets belonging to various network flows are multiplexed and 
queued for transmission at the output buffers associated with a link. The manner in which 
queued packets are selected for transmission on the link is known as the link-scheduling 
discipline, and was discussed in detail in Section 4.2. Recall that in Section 4.2 three link-
scheduling disciplines were discussed, namely, FIFO, priority queuing, and Weighted Fair 
Queuing (WFQ). We’ll see soon see that WFQ will play a particularly important role for isolating 
the traffic classes. The Leaky Bucket One of our earlier insights was that policing, the regulation 
of the rate at which a class or flow (we will assume the unit of policing is a flow in our discussion 
below) is allowed to inject packets into the network, is an important QoS mechanism. But what 
aspects of a flow’s packet rate should be policed? We can identify three important policing 
criteria, each differing from the other according to the time scale over which the packet flow is 
policed: Average rate. The network may wish to limit the long-term average rate (packets per 
time interval) at which a flow’s packets can be sent into the network. A crucial issue here is the 


## Page 6

interval of time over which the average rate will be policed. A flow whose average rate is limited 
to 100 packets per second is more constrained than a source that is limited to 6,000 packets 
per minute, even though both have the same average rate over a long enough interval of time. 
For example, the latter constraint would allow a flow to send 1,000 packets in a given second-
long interval of time, while the former constraint would disallow this sending behavior. Peak 
rate. While the average-rate constraint limits the amount of traffic that can be sent into the 
network over a relatively long period of time, a peak-rate constraint limits the maximum number 
of packets that can be sent over a shorter period of time. Using our example above, the network 
may police a flow at an average rate of 6,000 packets per minute, while limiting the flow’s peak 
rate to 1,500 packets per second. Burst size. The network may also wish to limit the maximum 
number of packets (the “burst” of packets) that can be sent into the network over an extremely 
short interval of time. In the limit, as the interval length approaches zero, the burst size limits 
the number of packets that can be instantaneously sent into the network. Even though it is 
physically impossible to instantaneously send multiple packets into the network (after all, every 
link has a physical transmission rate that cannot be exceeded!), the abstraction of a maximum 
burst size is a useful one. The leaky bucket mechanism is an abstraction that can be used to 
characterize these policing limits. As shown in Figure 9.14, a leaky bucket consists of a bucket 
that can hold up to b tokens. Tokens are added to this bucket as follows. New tokens, which 
may potentially be added to the bucket, are always being generated at a rate of r tokens per 
second. (We assume here for simplicity that the unit of time is a second.) If the bucket is filled 
with less than b tokens when a token is generated, the newly generated token is added to the 
bucket; otherwise the newly generated token is ignored, and the token bucket remains full with 
b tokens. Let us now consider how the leaky bucket can be used to police a packet flow. 
Suppose that before a packet is transmitted into the network, it must first remove a token from 
the token bucket. If the token bucket is empty, the packet must wait for Figure 9.14 The leaky 
bucket policer a token. (An alternative is for the packet to be dropped, although we will not 
consider that option here.) Let us now consider how this behavior polices a traffic flow. 
Because there can be at most b tokens in the bucket, the maximum burst size for a leaky-
bucket-policed flow is b packets. Furthermore, because the token generation rate is r, the 
maximum number of packets that can enter the network of any interval of time of length t is 
Thus, the token-generation rate, r, serves to limit the long-term average rate at which packets 
can enter the network. It is also possible to use leaky buckets (specifically, two leaky buckets in 
series) to police a flow’s peak rate in addition to the long-term average rate; see the homework 
problems at the end of this chapter. Leaky Bucket Weighted Fair Queuing Provable Maximum 
Delay in a Queue Let’s close our discussion on policing by showing how the leaky bucket and 
WFQ can be combined to provide a bound on the delay through a router’s queue. (Readers who 
have forgotten about WFQ are encouraged to review WFQ, which is covered in Section 4.2.) 
Let’s consider a router’s output link that multiplexes n flows, each policed by a leaky bucket 
with parameters b and using WFQ scheduling. We use the term flow here loosely to refer to the 
set of packets that are not distinguished from each other by the scheduler. In practice, a flow 
might be comprised of traffic from a single end-toend connection or a collection of many such 
connections, see Figure 9.15. Recall from our discussion of WFQ that each flow, i, is 
guaranteed to receive a share of the link bandwidth equal to at least where R is the 
transmission rt+b. + = i ri,i=1,…,n, R⋅wi/(∑ wj), Figure 9.15 n multiplexed leaky bucket flows with 
WFQ scheduling rate of the link in packets/sec. What then is the maximum delay that a packet 
will experience while waiting for service in the WFQ (that is, after passing through the leaky 
bucket)? Let us focus on flow 1. Suppose that flow 1’s token bucket is initially full. A burst of b 
packets then arrives to the leaky bucket policer for flow 1. These packets remove all of the 


## Page 7

tokens (without wait) from the leaky bucket and then join the WFQ waiting area for flow 1. Since 
these b packets are served at a rate of at least packet/sec, the last of these packets will then 
have a maximum delay, d , until its transmission is completed, where The rationale behind this 
formula is that if there are b packets in the queue and packets are being serviced (removed) 
from the queue at a rate of at least packets per second, then the amount of time until the last 
bit of the last packet is transmitted cannot be more than . A homework problem asks you to 
prove that as long as then d is indeed the maximum delay that any packet in flow 1 will ever 
experience in the WFQ queue. 9.5.3 Diffserv Having seen the motivation, insights, and specific 
mechanisms for providing multiple classes of service, let’s wrap up our study of approaches 
toward proving multiple classes of service with an example—the Internet Diffserv architecture 
[RFC 2475; Kilkki 1999]. Diffserv provides service differentiation—that is, the ability to handle 
different classes of traffic in different ways within the Internet in a scalable manner. 1 1 R⋅wi/(∑ 
wj) max dmax=b1R⋅w1/∑ wj 1 R⋅w1/(∑ wj) b1/(R⋅w1/(∑ wj)) r1r. t=tf t=0 t=T. Q=0, Q>0 HT/2≥Q. 
H>2r Q=HT/2. H>2r. H>2r. t=tf rE. i u=0.1. r1−t1 r2−t2 r4−t4, r3−t3, r2−t2, r1−t1. i i n d1=r1−t1. a. 
Suppose that we would like for all n. Give a recursive formula for d in terms of and t . b. Describe 
why for Internet telephony, the delay estimate described in Section 9.3 is more appropriate 
than the delay estimate outlined in part (a). P10. Compare the procedure described in Section 
9.3 for estimating average delay with the procedure in Section 3.5 for estimating round-trip 
time. What do the procedures have in common? How are they different? P11. Consider the 
figure below (which is similar to Figure 9.3 ). A sender begins sending packetized audio 
periodically at The first packet arrives at the receiver at a. What are the delays (from sender to 
receiver, ignoring any playout delays) of packets 2 through 8? Note that each vertical and 
horizontal line segment in the figure has a length of 1, 2, or 3 time units. b. If audio playout 
begins as soon as the first packet arrives at the receiver at which of the first eight packets sent 
will not arrive in time for playout? c. If audio playout begins at which of the first eight packets 
sent will not arrive in time for playout? d. What is the minimum playout delay at the receiver that 
results in all of the first eight packets arriving in time for their playout? P12. Consider again the 
figure in P11, showing packet audio transmission and reception times. a. Compute the 
estimated delay for packets 2 through 8, using the formula for d from Section 9.3.2 . Use a value 
of . dn=(r1−t1+r2−t2+⋯+rn−tn)/n n dn−1, rn, n t=1. t=8. t=8, t=9, i u=0.1 b. Compute the 
estimated deviation of the delay from the estimated average for packets 2 through 8, using the 
formula for v from Section 9.3.2 . Use a value of . P13. Recall the two FEC schemes for VoIP 
described in Section 9.3 . Suppose the first scheme generates a redundant chunk for every four 
original chunks. Suppose the second scheme uses a low-bit rate encoding whose transmission 
rate is 25 percent of the transmission rate of the nominal stream. a. How much additional 
bandwidth does each scheme require? How much playback delay does each scheme add? b. 
How do the two schemes perform if the first packet is lost in every group of five packets? Which 
scheme will have better audio quality? c. How do the two schemes perform if the first packet is 
lost in every group of two packets? Which scheme will have better audio quality? P14. a. 
Consider an audio conference call in Skype with participants. Suppose each participant 
generates a constant stream of rate r bps. How many bits per second will the call initiator need 
to send? How many bits per second will each of the other participants need to send? What is 
the total send rate, aggregated over all participants? b. Repeat part (a) for a Skype video 
conference call using a central server. c. Repeat part (b), but now for when each peer sends a 
copy of its video stream to each of the other peers. P15. a. Suppose we send into the Internet 
two IP datagrams, each carrying a different UDP segment. The first datagram has source IP 
address A1, destination IP address B, source port P1, and destination port T. The second 
datagram has source IP address A2, destination IP address B, source port P2, and destination 


## Page 8

port T. Suppose that A1 is different from A2 and that P1 is different from P2. Assuming that both 
datagrams reach their final destination, will the two UDP datagrams be received by the same 
socket? Why or why not? b. Suppose Alice, Bob, and Claire want to have an audio conference 
call using SIP and RTP. For Alice to send and receive RTP packets to and from Bob and Claire, is 
only one UDP socket sufficient (in addition to the socket needed for the SIP messages)? If yes, 
then how does Alice’s SIP client distinguish between the RTP packets received from Bob and 
Claire? P16. True or false: a. If stored video is streamed directly from a Web server to a media 
player, then the application is using TCP as the underlying transport protocol. i u=0.1 N>2 N−1 
N−1 b. When using RTP, it is possible for a sender to change encoding in the middle of a 
session. c. All applications that use RTP must use port 87. d. If an RTP session has a separate 
audio and video stream for each sender, then the audio and video streams use the same SSRC. 
e. In differentiated services, while per-hop behavior defines differences in performance among 
classes, it does not mandate any particular mechanism for achieving these performances. f. 
Suppose Alice wants to establish an SIP session with Bob. In her INVITE message she includes 
the line: m=audio 48753 RTP/AVP 3 (AVP 3 denotes GSM audio). Alice has therefore indicated in 
this message that she wishes to send GSM audio. g. Referring to the preceding statement, Alice 
has indicated in her INVITE message that she will send audio to port 48753. h. SIP messages are 
typically sent between SIP entities using a default SIP port number. i. In order to maintain 
registration, SIP clients must periodically send REGISTER messages. j. SIP mandates that all 
SIP clients support G.711 audio encoding. P17. Consider the figure below, which shows a leaky 
bucket policer being fed by a stream of packets. The token buffer can hold at most two tokens, 
and is initially full at New tokens arrive at a rate of one token per slot. The output link speed is 
such that if two packets obtain tokens at the beginning of a time slot, they can both go to the 
output link in the same slot. The timing details of the system are as follows: A. Packets (if any) 
arrive at the beginning of the slot. Thus in the figure, packets 1, 2, and 3 arrive in slot 0. If there 
are already packets in the queue, then the arriving packets join the end of the queue. Packets 
proceed towards the front of the queue in a FIFO manner. B. After the arrivals have been added 
to the queue, if there are any queued packets, one or two of those packets (depending on the 
number of available tokens) will each remove a token from the token buffer and go to the output 
link during that slot. Thus, packets 1 and t=0. Programming Assignment In this lab, you will 
implement a streaming video server and client. The client will use the real-time streaming 
protocol (RTSP) to control the actions of the server. The server will use the real-time protocol 
(RTP) to packetize the video for transport over UDP. You will be given Python code that partially 
implements RTSP and RTP at the client and server. Your job will be to complete both the client 
and server code. When you are finished, you will have created a client-server application that 
does the following: 2 each remove a token from the buffer (since there are initially two tokens) 
and go to the output link during slot 0. C. A new token is added to the token buffer if it is not full, 
since the token generation rate is r = 1 token/slot. D. Time then advances to the next time slot, 
and these steps repeat. Answer the following questions: a. For each time slot, identify the 
packets that are in the queue and the number of tokens in the bucket, immediately after the 
arrivals have been processed (step 1 above) but before any of the packets have passed through 
the queue and removed a token. Thus, for the time slot in the example above, packets 1, 2, and 
3 are in the queue, and there are two tokens in the buffer. b. For each time slot indicate which 
packets appear on the output after the token(s) have been removed from the queue. Thus, for 
the time slot in the example above, packets 1 and 2 appear on the output link from the leaky 
buffer during slot 0. P18. Repeat P17 but assume that Assume again that the bucket is initially 
full. P19. Consider P18 and suppose now that and that as before. Will your answer to the 
question above change? P20. Consider the leaky bucket policer that polices the average rate 


## Page 9

and burst size of a packet flow. We now want to police the peak rate, p, as well. Show how the 
output of this leaky bucket policer can be fed into a second leaky bucket policer so that the two 
leaky buckets in series police the average rate, peak rate, and burst size. Be sure to give the 
bucket size and token generation rate for the second policer. P21. A packet flow is said to 
conform to a leaky bucket specification (r, b) with burst size b and average rate r if the number 
of packets that arrive to the leaky bucket is less than packets in every interval of time of length t 
for all t. Will a packet flow that conforms to a leaky bucket specification (r, b) ever have to wait 
at a leaky bucket policer with parameters r and b? Justify your answer. P22. Show that as long 
as then d is indeed the maximum delay that any packet in flow 1 will ever experience in the WFQ 
queue. t=0 t=0 r=2. r=3 b=2 rt+b r1 
Programming Assignment In this lab, you will implement a streaming video server and client. 
The client will use the real-time streaming protocol (RTSP) to control the actions of the server. 
The server will use the real-time protocol (RTP) to packetize the video for transport over UDP. 
You will be given Python code that partially implements RTSP and RTP at the client and server. 
Your job will be to complete both the client and server code. When you are finished, you will 
have created a client-server application that does the following: 
The client sends SETUP, PLAY, PAUSE, and TEARDOWN RTSP commands, and the server 
responds to the commands. When the server is in the playing state, it periodically grabs a 
stored JPEG frame, packetizes the frame with RTP, and sends the RTP packet into a UDP socket. 
The client receives the RTP packets, removes the JPEG frames, decompresses the frames, and 
renders the frames on the client’s monitor. The code you will be given implements the RTSP 
protocol in the server and the RTP depacketization in the client. The code also takes care of 
displaying the transmitted video. You will need to implement RTSP in the client and RTP server. 
This programming assignment will significantly enhance the student’s understanding of RTP, 
RTSP, and streaming video. It is highly recommended. The assignment also suggests a number 
of optional exercises, including implementing the RTSP DESCRIBE command at both client and 
server. You can find full details of the assignment, as well as an overview of the RTSP protocol, 
at the Web site www.pearsonhighered.com/cs-resources. AN INTERVIEW WITH . . . Henning 
Schulzrinne Henning Schulzrinne is a professor, chair of the Department of Computer Science, 
and head of the Internet Real-Time Laboratory at Columbia University. He is the co-author of 
RTP, RTSP, SIP, and GIST—key protocols for audio and video communications over the Internet. 
Henning received his BS in electrical and industrial engineering at TU Darmstadt in Germany, 
his MS in electrical and computer engineering at the University of Cincinnati, and his PhD in 
electrical engineering at the University of Massachusetts, Amherst. What made you decide to 
specialize in multimedia networking? This happened almost by accident. As a PhD student, I 
got involved with DARTnet, an experimental network spanning the United States with T1 lines. 
DARTnet was used as a proving ground for multicast and Internet real-time tools. That led me to 
write my first audio tool, NeVoT. Through some of the DARTnet participants, I became involved 
in the IETF, in the then-nascent Audio Video Transport working group. This group later ended up 
standardizing RTP. What was your first job in the computer industry? What did it entail? My first 
job in the computer industry was soldering together an Altair computer kit when I was a high 
school student in Livermore, California. Back in Germany, I started a little consulting company 
that devised an address management program for a travel agency—storing data on cassette 
tapes for our TRS-80 and using an IBM Selectric typewriter with a home-brew hardware 
interface as a printer. My first real job was with AT&T Bell Laboratories, developing a network 
emulator for constructing experimental networks in a lab environment. What are the goals of 
the Internet Real-Time Lab? Our goal is to provide components and building blocks for the 


## Page 10

Internet as the single future communications infrastructure. This includes developing new 
protocols, such as GIST (for network-layer signaling) and LoST (for finding resources by 
location), or enhancing protocols that we have worked on earlier, such as SIP, through work on 
rich presence, peer-to-peer systems, next-generation emergency calling, and service creation 
tools. Recently, we have also looked extensively at wireless systems for VoIP, as 802.11b and 
802.11n networks and maybe WiMax networks are likely to become important last-mile 
technologies for telephony. We are also trying to greatly improve the ability of users to diagnose 
faults in the complicated tangle of providers and equipment, using a peer-to-peer fault 
diagnosis system called DYSWIS (Do You See What I See). We try to do practically relevant 
work, by building prototypes and open source systems, by measuring performance of real 
systems, and by contributing to IETF standards. What is your vision for the future of multimedia 
networking? We are now in a transition phase; just a few years shy of when IP will be the 
universal platform for multimedia services, from IPTV to VoIP. We expect radio, telephone, and 
TV to be available even during snowstorms and earthquakes, so when the Internet takes over 
the role of these dedicated networks, users will expect the same level of reliability. We will have 
to learn to design network technologies for an ecosystem of competing carriers, service and 
content providers, serving lots of technically untrained users and defending them against a 
small, but destructive, set of malicious and criminal users. Changing protocols is becoming 
increasingly hard. They are also becoming more complex, as they need to take into account 
competing business interests, security, privacy, and the lack of transparency of networks 
caused by firewalls and network address translators. Since multimedia networking is becoming 
the foundation for almost all of consumer entertainment, there will be an emphasis on 
managing very large networks, at low cost. Users will expect ease of use, such as finding the 
same content on all of their devices. Why does SIP have a promising future? As the current 
wireless network upgrade to 3G networks proceeds, there is the hope of a single multimedia 
signaling mechanism spanning all types of networks, from cable modems, to corporate 
telephone networks and public wireless networks. Together with software radios, this will make 
it possible in the future that a single device can be used on a home network, as a cordless 
BlueTooth phone, in a corporate network via 802.11 and in the wide area via 3G networks. Even 
before we have such a single universal wireless device, the personal mobility mechanisms 
make it possible to hide the differences between networks. One identifier becomes the 
universal means of reaching a person, rather than remembering or passing around half a dozen 
technology- or location-specific telephone numbers. SIP also breaks apart the provision of 
voice (bit) transport from voice services. It now becomes technically possible to break apart the 
local telephone monopoly, where one company provides neutral bit transport, while others 
provide IP “dial tone” and the classical telephone services, such as gateways, call forwarding, 
and caller ID. Beyond multimedia signaling, SIP offers a new service that has been missing in 
the Internet: event notification. We have approximated such services with HTTP kludges and e-
mail, but this was never very satisfactory. Since events are a common abstraction for 
distributed systems, this may simplify the construction of new services. Do you have any advice 
for students entering the networking field? Networking bridges disciplines. It draws from 
electrical engineering, all aspects of computer science, operations research, statistics, 
economics, and other disciplines. Thus, networking researchers have to be familiar with 
subjects well beyond protocols and routing algorithms. Given that networks are becoming such 
an important part of everyday life, students wanting to make a difference in the field should 
think of the new resource constraints in networks: human time and effort, rather than just 
bandwidth or storage. Work in networking research can be immensely satisfying since it is 
about allowing people to communicate and exchange ideas, one of the essentials of being 


## Page 11

human. The Internet has become the third major global infrastructure, next to the 
transportation system and energy distribution. Almost no part of the economy can work without 
high-performance networks, so there should be plenty of opportunities for the foreseeable 
future. 
References A note on URLs. In the references below, we have provided URLs for Web pages, 
Web-only documents, and other material that has not been published in a conference or 
journal (when we have been able to locate a URL for such material). We have not provided URLs 
for conference and journal publications, as these documents can usually be located via a 
search engine, from the conference Web site (e.g., papers in all ACM SIGCOMM conferences 
and workshops can be located via http://www.acm.org/ sigcomm), or via a digital library 
subscription. While all URLs provided below were valid (and tested) in Jan. 2016, URLs can 
become out of date. Please consult the online version of this book (www.pearsonhighered 
.com/cs-resources) for an up-to-date bibliography. A note on Internet Request for Comments 
(RFCs): Copies of Internet RFCs are available at many sites. The RFC Editor of the Internet 
Society (the body that oversees the RFCs) maintains the site, http://www.rfc-editor.org. This 
site allows you to search for a specific RFC by title, number, or authors, and will show updates 
to any RFCs listed. Internet RFCs can be updated or obsoleted by later RFCs. Our favorite site 
for getting RFCs is the original source—http://www.rfc-editor.org. [3GPP 2016] Third Generation 
Partnership Project homepage, http://www.3gpp.org/ [Abramson 1970] N. Abramson, “The 
Aloha System—Another Alternative for Computer Communications,” Proc. 1970 Fall Joint 
Computer Conference, AFIPS Conference, p. 37, 1970. [Abramson 1985] N. Abramson, 
“Development of the Alohanet,” IEEE Transactions on Information Theory, Vol. IT-31, No. 3 
(Mar. 1985), pp. 119–123. [Abramson 2009] N. Abramson, “The Alohanet—Surfing for Wireless 
Data,” IEEE Communications Magazine, Vol. 47, No. 12, pp. 21–25. [Adhikari 2011a] V. K. 
Adhikari, S. Jain, Y. Chen, Z. L. Zhang, “Vivisecting YouTube: An Active Measurement Study,” 
Technical Report, University of Minnesota, 2011. [Adhikari 2012] V. K. Adhikari, Y. Gao, F. Hao, 
M. Varvello, V. Hilt, M. Steiner, Z. L. Zhang, “Unreeling Netflix: Understanding and Improving 
Multi-CDN Movie Delivery,” Technical Report, University of Minnesota, 2012. [Afanasyev 2010] 
A. Afanasyev, N. Tilley, P. Reiher, L. Kleinrock, “Host-to-Host Congestion Control for TCP,” IEEE 
Communications Surveys & Tutorials, Vol. 12, No. 3, pp. 304–342. [Agarwal 2009] S. Agarwal, J. 
Lorch, “Matchmaking for Online Games and Other Latency-sensitive P2P Systems,” Proc. 2009 
ACM SIGCOMM. [Ager 2012] B. Ager, N. Chatzis, A. Feldmann, N. Sarrar, S. Uhlig, W. Willinger, 
“Anatomy of a Large European ISP,” Sigcomm, 2012. [Ahn 1995] J. S. Ahn, P. B. Danzig, Z. Liu, 
and Y. Yan, “Experience with TCP Vegas: Emulation and Experiment,” Proc. 1995 ACM 
SIGCOMM (Boston, MA, Aug. 1995), pp. 185–195. [Akamai 2016] Akamai homepage, 
http://www.akamai.com [Akella 2003] A. Akella, S. Seshan, A. Shaikh, “An Empirical Evaluation 
of Wide-Area Internet Bottlenecks,” Proc. 2003 ACM Internet Measurement Conference (Miami, 
FL, Nov. 2003). [Akhshabi 2011] S. Akhshabi, A. C. Begen, C. Dovrolis, “An Experimental 
Evaluation of Rate-Adaptation Algorithms in Adaptive Streaming over HTTP,” Proc. 2011 ACM 
Multimedia Systems Conf. [Akyildiz 2010] I. Akyildiz, D. Gutierrex-Estevez, E. Reyes, “The 
Evolution to 4G Cellular Systems, LTE Advanced,” Physical Communication, Elsevier, 3 (2010), 
217–244. [Albitz 1993] P. Albitz and C. Liu, DNS and BIND, O’Reilly & Associates, Petaluma, CA, 
1993. [Al-Fares 2008] M. Al-Fares, A. Loukissas, A. Vahdat, “A Scalable, Commodity Data 
Center Network Architecture,” Proc. 2008 ACM SIGCOMM. [Amazon 2014] J. Hamilton, “AWS: 
Innovation at Scale, YouTube video, https://www.youtube.com/watch?v=JIQETrFC_SQ 
[Anderson 1995] J. B. Andersen, T. S. Rappaport, S. Yoshida, “Propagation Measurements and 
Models for Wireless Communications Channels,” IEEE Communications Magazine, (Jan. 1995), 


## Page 12

pp. 42–49. [Alizadeh 2010] M. Alizadeh, A. Greenberg, D. Maltz, J. Padhye, P. Patel, B. 
Prabhakar, S. Sengupta, M. Sridharan. “Data center TCP (DCTCP),” ACM SIGCOMM 2010 
Conference, ACM, New York, NY, USA, pp. 63–74. [Allman 2011] E. Allman, “The Robustness 
Principle Reconsidered: Seeking a Middle Ground,” Communications of the ACM, Vol. 54, No. 8 
(Aug. 2011), pp. 40–45. [Appenzeller 2004] G. Appenzeller, I. Keslassy, N. McKeown, “Sizing 
Router Buffers,” Proc. 2004 ACM SIGCOMM (Portland, OR, Aug. 2004). [ASO-ICANN 2016] The 
Address Supporting Organization homepage, http://www.aso.icann.org [AT&T 2013] “AT&T 
Vision Alignment Challenge Technology Survey,” AT&T Domain 2.0 Vision White Paper, 
November 13, 2013. [Atheros 2016] Atheros Communications Inc., “Atheros AR5006 WLAN 
Chipset Product Bulletins,” http://www.atheros.com/pt/AR5006Bulletins.htm [Ayanoglu 1995] 
E. Ayanoglu, S. Paul, T. F. La Porta, K. K. Sabnani, R. D. Gitlin, “AIRMAIL: A Link-Layer Protocol 
for Wireless Networks,” ACM ACM/Baltzer Wireless Networks Journal, 1: 47–60, Feb. 1995. 
[Bakre 1995] A. Bakre, B. R. Badrinath, “I-TCP: Indirect TCP for Mobile Hosts,” Proc. 1995 Int. 
Conf. on Distributed Computing Systems (ICDCS) (May 1995), pp. 136–143. [Balakrishnan 
1997] H. Balakrishnan, V. Padmanabhan, S. Seshan, R. Katz, “A Comparison of Mechanisms for 
Improving TCP Performance Over Wireless Links,” IEEE/ACM Transactions on Networking Vol. 
5, No. 6 (Dec. 1997). [Balakrishnan 2003] H. Balakrishnan, F. Kaashoek, D. Karger, R. Morris, I. 
Stoica, “Looking Up Data in P2P Systems,” Communications of the ACM, Vol. 46, No. 2 (Feb. 
2003), pp. 43–48. [Baldauf 2007] M. Baldauf, S. Dustdar, F. Rosenberg, “A Survey on Context-
Aware Systems,” Int. J. Ad Hoc and Ubiquitous Computing, Vol. 2, No. 4 (2007), pp. 263–277. 
[Baran 1964] P. Baran, “On Distributed Communication Networks,” IEEE Transactions on 
Communication Systems, Mar. 1964. Rand Corporation Technical report with the same title 
(Memorandum RM-3420-PR, 1964). http://www.rand.org/publications/RM/RM3420/ [Bardwell 
2004] J. Bardwell, “You Believe You Understand What You Think I Said . . . The Truth About 
802.11 Signal and Noise Metrics: A Discussion Clarifying OftenMisused 802.11 WLAN 
Terminologies,” 
http://www.connect802.com/download/techpubs/2004/you_believe_D100201.pdf [Barford 
2009] P. Barford, N. Duffield, A. Ron, J. Sommers, “Network Performance Anomaly Detection 
and Localization,” Proc. 2009 IEEE INFOCOM (Apr. 2009). [Baronti 2007] P. Baronti, P. Pillai, V. 
Chook, S. Chessa, A. Gotta, Y. Hu, “Wireless Sensor Networks: A Survey on the State of the Art 
and the 802.15.4 and ZigBee Standards,” Computer Communications, Vol. 30, No. 7 (2007), pp. 
1655–1695. [Baset 2006] S. A. Basset and H. Schulzrinne, “An Analysis of the Skype Peer-to-
Peer Internet Telephony Protocol,” Proc. 2006 IEEE INFOCOM (Barcelona, Spain, Apr. 2006). 
[BBC 2001] BBC news online “A Small Slice of Design,” Apr. 2001, 
http://news.bbc.co.uk/2/hi/science/nature/1264205.stm [Beheshti 2008] N. Beheshti, Y. 
Ganjali, M. Ghobadi, N. McKeown, G. Salmon, “Experimental Study of Router Buffer Sizing,” 
Proc. ACM Internet Measurement Conference (Oct. 2008, Vouliagmeni, Greece). [Bender 2000] 
P. Bender, P. Black, M. Grob, R. Padovani, N. Sindhushayana, A. Viterbi, “CDMA/HDR: A 
Bandwidth-Efficient High-Speed Wireless Data Service for Nomadic Users,” IEEE Commun. 
Mag., Vol. 38, No. 7 (July 2000), pp. 70–77. [Berners-Lee 1989] T. Berners-Lee, CERN, 
“Information Management: A Proposal,” Mar. 1989, May 1990. 
http://www.w3.org/History/1989/proposal .html [Berners-Lee 1994] T. Berners-Lee, R. Cailliau, 
A. Luotonen, H. Frystyk Nielsen, A. Secret, “The World-Wide Web,” Communications of the 
ACM, Vol. 37, No. 8 (Aug. 1994), pp. 76–82. [Bertsekas 1991] D. Bertsekas, R. Gallagher, Data 
Networks, 2nd Ed., Prentice Hall, Englewood Cliffs, NJ, 1991. [Biersack 1992] E. W. Biersack, 
“Performance Evaluation of Forward Error Correction in ATM Networks,” Proc. 1999 ACM 
SIGCOMM (Baltimore, MD, Aug. 1992), pp. 248–257. [BIND 2016] Internet Software Consortium 
page on BIND, http://www.isc.org/bind.html [Bisdikian 2001] C. Bisdikian, “An Overview of the 


## Page 13

Bluetooth Wireless Technology,” IEEE Communications Magazine, No. 12 (Dec. 2001), pp. 86–
94. [Bishop 2003] M. Bishop, Computer Security: Art and Science, Boston: Addison Wesley, 
Boston MA, 2003. [Black 1995] U. Black, ATM Volume I: Foundation for Broadband Networks, 
Prentice Hall, 1995. [Black 1997] U. Black, ATM Volume II: Signaling in Broadband Networks, 
Prentice Hall, 1997. [Blumenthal 2001] M. Blumenthal, D. Clark, “Rethinking the Design of the 
Internet: The End-to-end Arguments vs. the Brave New World,” ACM Transactions on Internet 
Technology, Vol. 1, No. 1 (Aug. 2001), pp. 70–109. [Bochman 1984] G. V. Bochmann, C. A. 
Sunshine, “Formal Methods in Communication Protocol Design,” IEEE Transactions on 
Communications, Vol. 28, No. 4 (Apr. 1980) pp. 624–631. [Bolot 1996] J-C. Bolot, A. Vega-
Garcia, “Control Mechanisms for Packet Audio in the Internet,” Proc. 1996 IEEE INFOCOM, pp. 
232–239. [Bosshart 2013] P. Bosshart, G. Gibb, H. Kim, G. Varghese, N. McKeown, M. Izzard, F. 
Mujica, M. Horowitz, “Forwarding Metamorphosis: Fast Programmable Match-Action 
Processing in Hardware for SDN,” ACM SIGCOMM Comput. Commun. Rev. 43, 4 (Aug. 2013), 
99–110. [Bosshart 2014] P. Bosshart, D. Daly, G. Gibb, M. Izzard, N. McKeown, J. Rexford, C. 
Schlesinger, D. Talayco, A. Vahdat, G. Varghese, D. Walker, “P4: Programming Protocol-
Independent Packet Processors,” ACM SIGCOMM Comput. Commun. Rev. 44, 3 (July 2014), 
pp. 87–95. [Brakmo 1995] L. Brakmo, L. Peterson, “TCP Vegas: End to End Congestion 
Avoidance on a Global Internet,” IEEE Journal of Selected Areas in Communications, Vol. 13, 
No. 8 (Oct. 1995), pp. 1465–1480. [Bryant 1988] B. Bryant, “Designing an Authentication 
System: A Dialogue in Four Scenes,” http://web.mit.edu/kerberos/www/dialogue.html [Bush 
1945] V. Bush, “As We May Think,” The Atlantic Monthly, July 1945. 
http://www.theatlantic.com/unbound/flashbks/computer/bushf.htm [Byers 1998] J. Byers, M. 
Luby, M. Mitzenmacher, A. Rege, “A Digital Fountain Approach to Reliable Distribution of Bulk 
Data,” Proc. 1998 ACM SIGCOMM (Vancouver, Canada, Aug. 1998), pp. 56–67. [Caesar 2005a] 
M. Caesar, D. Caldwell, N. Feamster, J. Rexford, A. Shaikh, J. van der Merwe, “Design and 
implementation of a Routing Control Platform,” Proc. Networked Systems Design and 
Implementation (May 2005). [Caesar 2005b] M. Caesar, J. Rexford, “BGP Routing Policies in ISP 
Networks,” IEEE Network Magazine, Vol. 19, No. 6 (Nov. 2005). [Caldwell 2012] C. Caldwell, 
“The Prime Pages,” http://www.utm.edu/research/primes/prove [Cardwell 2000] N. Cardwell, 
S. Savage, T. Anderson, “Modeling TCP Latency,” Proc. 2000 IEEE INFOCOM (Tel-Aviv, Israel, 
Mar. 2000). [Casado 2007] M. Casado, M. Freedman, J. Pettit, J. Luo, N. McKeown, S. Shenker, 
“Ethane: Taking Control of the Enterprise,” Proc. ACM SIGCOMM ’07, New York, pp. 1–12. See 
also IEEE/ACM Trans. Networking, 17, 4 (Aug. 2007), pp. 270–1283. [Casado 2009] M. Casado, 
M. Freedman, J. Pettit, J. Luo, N. Gude, N. McKeown, S. Shenker, “Rethinking Enterprise 
Network Control,” IEEE/ACM Transactions on Networking (ToN), Vol. 17, No. 4 (Aug. 2009), pp. 
1270–1283. [Casado 2014] M. Casado, N. Foster, A. Guha, “Abstractions for Software-Defined 
Networks,” Communications of the ACM, Vol. 57 No. 10, (Oct. 2014), pp. 86–95. [Cerf 1974] V. 
Cerf, R. Kahn, “A Protocol for Packet Network Interconnection,” IEEE Transactions on 
Communications Technology, Vol. COM-22, No. 5, pp. 627–641. [CERT 2001–09] CERT, 
“Advisory 2001–09: Statistical Weaknesses in TCP/IP Initial Sequence Numbers,” 
http://www.cert.org/advisories/CA-2001-09.html [CERT 2003–04] CERT, “CERT Advisory CA-
2003-04 MS-SQL Server Worm,” http://www.cert.org/advisories/CA-2003-04.html [CERT 2016] 
CERT, http://www.cert.org [CERT Filtering 2012] CERT, “Packet Filtering for Firewall Systems,” 
http://www.cert.org/tech_tips/packet_filtering.html [Cert SYN 1996] CERT, “Advisory CA-96.21: 
TCP SYN Flooding and IP Spoofing Attacks,” http://www.cert.org/advisories/CA-1998-01.html 
[Chandra 2007] T. Chandra, R. Greisemer, J. Redstone, “Paxos Made Live: an Engineering 
Perspective,” Proc. of 2007 ACM Symposium on Principles of Distributed Computing (PODC), 
pp. 398–407. [Chao 2001] H. J. Chao, C. Lam, E. Oki, Broadband Packet Switching 


## Page 14

Technologies—A Practical Guide to ATM Switches and IP Routers, John Wiley & Sons, 2001. 
[Chao 2011] C. Zhang, P. Dunghel, D. Wu, K. W. Ross, “Unraveling the BitTorrent Ecosystem,” 
IEEE Transactions on Parallel and Distributed Systems, Vol. 22, No. 7 (July 2011). [Chen 2000] 
G. Chen, D. Kotz, “A Survey of Context-Aware Mobile Computing Research,” Technical Report 
TR2000-381, Dept. of Computer Science, Dartmouth College, Nov. 2000. 
http://www.cs.dartmouth.edu/reports/TR2000-381.pdf [Chen 2006] K.-T. Chen, C.-Y. Huang, P. 
Huang, C.-L. Lei, “Quantifying Skype User Satisfaction,” Proc. 2006 ACM SIGCOMM (Pisa, Italy, 
Sept. 2006). [Chen 2011] Y. Chen, S. Jain, V. K. Adhikari, Z. Zhang, “Characterizing Roles of 
Front-End Servers in End-to-End Performance of Dynamic Content Distribution,” Proc. 2011 
ACM Internet Measurement Conference (Berlin, Germany, Nov. 2011). [Cheswick 2000] B. 
Cheswick, H. Burch, S. Branigan, “Mapping and Visualizing the Internet,” Proc. 2000 Usenix 
Conference (San Diego, CA, June 2000). [Cheswick 2000] B. Cheswick, H. Burch, S. Branigan, 
“Mapping and Visualizing the Internet,” Proc. 2000 Usenix Conference (San Diego, CA, June 
2000). [Chiu 1989] D. Chiu, R. Jain, “Analysis of the Increase and Decrease Algorithms for 
Congestion Avoidance in Computer Networks,” Computer Networks and ISDN Systems, Vol. 
17, No. 1, pp. 1–14. http://www.cs.wustl.edu/~jain/papers/cong_av.htm [Christiansen 2001] M. 
Christiansen, K. Jeffay, D. Ott, F. D. Smith, “Tuning Red for Web Traffic,” IEEE/ACM Transactions 
on Networking, Vol. 9, No. 3 (June 2001), pp. 249–264. [Chuang 2005] S. Chuang, S. Iyer, N. 
McKeown, “Practical Algorithms for Performance Guarantees in Buffered Crossbars,” Proc. 
2005 IEEE INFOCOM. [Cisco 802.11ac 2014] Cisco Systems, “802.11ac: The Fifth Generation of 
Wi-Fi,” Technical White Paper, Mar. 2014. [Cisco 7600 2016] Cisco Systems, “Cisco 7600 
Series Solution and Design Guide,” 
http://www.cisco.com/en/US/products/hw/routers/ps368/prod_technical_ 
reference09186a0080092246.html [Cisco 8500 2012] Cisco Systems Inc., “Catalyst 8500 
Campus Switch Router Architecture,” 
http://www.cisco.com/univercd/cc/td/doc/product/l3sw/8540/rel_12_0/w5_6f/softcnfg/1cfg85
00.pdf [Cisco 12000 2016] Cisco Systems Inc., “Cisco XR 12000 Series and Cisco 12000 Series 
Routers,” http://www.cisco.com/en/US/products/ps6342/index.html [Cisco 2012] Cisco 2012, 
Data Centers, http://www.cisco.com/go/dce [Cisco 2015] Cisco Visual Networking Index: 
Forecast and Methodology, 2014–2019, White Paper, 2015. Cisco 6500 2016] Cisco Systems, 
“Cisco Catalyst 6500 Architecture White Paper,” 
http://www.cisco.com/c/en/us/products/collateral/switches/ catalyst-6500-
seriesswitches/prod_white_paper0900aecd80673385.html [Cisco NAT 2016] Cisco Systems 
Inc., “How NAT Works,” 
http://www.cisco.com/en/US/tech/tk648/tk361/technologies_tech_note09186a0080094831.s
html [Cisco QoS 2016] Cisco Systems Inc., “Advanced QoS Services for the Intelligent 
Internet,” http://www.cisco.com/warp/public/cc/pd/iosw/ioft/ioqo/tech/qos_wp.htm [Cisco 
Queue 2016] Cisco Systems Inc., “Congestion Management Overview,” 
http://www.cisco.com/en/US/docs/ios/12_2/qos/configuration/guide/qcfconmg.html [Cisco 
SYN 2016] Cisco Systems Inc., “Defining Strategies to Protect Against TCP SYN Denial of 
Service Attacks,” http://www.cisco.com/en/US/tech/tk828/ 
technologies_tech_note09186a00800f67d5.shtml [Cisco TCAM 2014] Cisco Systems Inc., “CAT 
6500 and 7600 Series Routers and Switches TCAM Allocation Adjustment Procedures,” 
http://www.cisco.com/c/en/us/ support/docs/switches/catalyst-6500-series-
switches/117712-problemsolution-cat6500-00.html [Cisco VNI 2015] Cisco Systems Inc., 
“Visual Networking Index,” 
http://www.cisco.com/web/solutions/sp/vni/vni_forecast_highlights/index.html [Clark 1988] D. 
Clark, “The Design Philosophy of the DARPA Internet Protocols,” Proc. 1988 ACM SIGCOMM 


## Page 15

(Stanford, CA, Aug. 1988) [Cohen 1977] D. Cohen, “Issues in Transnet Packetized Voice 
Communication,” Proc. Fifth Data Communications Symposium (Snowbird, UT, Sept. 1977), 
pp. 6–13. [Cookie Central 2016] Cookie Central homepage, http://www.cookiecentral.com/ 
n_cookie_faq.htm [Cormen 2001] T. H. Cormen, Introduction to Algorithms, 2nd Ed., MIT Press, 
Cambridge, MA, 2001. [Crow 1997] B. Crow, I. Widjaja, J. Kim, P. Sakai, “IEEE 802.11 Wireless 
Local Area Networks,” IEEE Communications Magazine (Sept. 1997), pp. 116–126. [Cusumano 
1998] M. A. Cusumano, D. B. Yoffie, Competing on Internet Time: Lessons from Netscape and 
Its Battle with Microsoft, Free Press, New York, NY, 1998. [Czyz 2014] J. Czyz, M. Allman, J. 
Zhang, S. Iekel-Johnson, E. Osterweil, M. Bailey, “Measuring IPv6 Adoption,” Proc. ACM 
SIGCOMM 2014, ACM, New York, NY, USA, pp. 87–98. [Dahlman 1998] E. Dahlman, B. 
Gudmundson, M. Nilsson, J. Sköld, “UMTS/IMT-2000 Based on Wideband CDMA,” IEEE 
Communications Magazine (Sept. 1998), pp. 70–80. [Daigle 1991] J. N. Daigle, Queuing Theory 
for Telecommunications, Addison-Wesley, Reading, MA, 1991. [DAM 2016] Digital Attack Map, 
http://www.digitalattackmap.com [Davie 2000] B. Davie and Y. Rekhter, MPLS: Technology and 
Applications, Morgan Kaufmann Series in Networking, 2000. [Davies 2005] G. Davies, F. Kelly, 
“Network Dimensioning, Service Costing, and Pricing in a Packet-Switched Environment,” 
Telecommunications Policy, Vol. 28, No. 4, pp. 391–412. [DEC 1990] Digital Equipment 
Corporation, “In Memoriam: J. C. R. Licklider 1915–1990,” SRC Research Report 61, Aug. 1990. 
http://www.memex.org/ licklider.pdf [DeClercq 2002] J. DeClercq, O. Paridaens, “Scalability 
Implications of Virtual Private Networks,” IEEE Communications Magazine, Vol. 40, No. 5 (May 
2002), pp. 151–157. [Demers 1990] A. Demers, S. Keshav, S. Shenker, “Analysis and Simulation 
of a Fair Queuing Algorithm,” Internetworking: Research and Experience, Vol. 1, No. 1 (1990), 
pp. 3–26. [dhc 2016] IETF Dynamic Host Configuration working group homepage, 
http://www.ietf.org/html.charters/dhc-charter.html [Dhungel 2012] P. Dhungel, K. W. Ross, M. 
Steiner., Y. Tian, X. Hei, “Xunlei: Peer-Assisted Download Acceleration on a Massive Scale,” 
Passive and Active Measurement Conference (PAM) 2012, Vienna, 2012. [Diffie 1976] W. Diffie, 
M. E. Hellman, “New Directions in Cryptography,” IEEE Transactions on Information Theory, Vol 
IT-22 (1976), pp. 644–654. [Diggavi 2004] S. N. Diggavi, N. Al-Dhahir, A. Stamoulis, R. 
Calderbank, “Great Expectations: The Value of Spatial Diversity in Wireless Networks,” 
Proceedings of the IEEE, Vol. 92, No. 2 (Feb. 2004). [Dilley 2002] J. Dilley, B. Maggs, J. Parikh, H. 
Prokop, R. Sitaraman, B. Weihl, “Globally Distributed Content Delivert,” IEEE Internet 
Computing (Sept.–Oct. 2002). [Diot 2000] C. Diot, B. N. Levine, B. Lyles, H. Kassem, D. 
Balensiefen, “Deployment Issues for the IP Multicast Service and Architecture,” IEEE Network, 
Vol. 14, No. 1 (Jan./Feb. 2000) pp. 78–88. [Dischinger 2007] M. Dischinger, A. Haeberlen, K. 
Gummadi, S. Saroiu, “Characterizing residential broadband networks,” Proc. 2007 ACM 
Internet Measurement Conference, pp. 24–26. [Dmitiropoulos 2007] X. Dmitiropoulos, D. 
Krioukov, M. Fomenkov, B. Huffaker, Y. Hyun, K. C. Claffy, G. Riley, “AS Relationships: Inference 
and Validation,” ACM Computer Communication Review (Jan. 2007). [DOCSIS 2011] Data-
Over-Cable Service Interface Specifications, DOCSIS 3.0: MAC and Upper Layer Protocols 
Interface Specification, CM-SP-MULPIv3.0-I16-110623 2011.  
[Dodge 2016] M. Dodge, “An Atlas of Cyberspaces,” 
http://www.cybergeography.org/atlas/isp_maps.html [Donahoo 2001] M. Donahoo, K. Calvert, 
TCP/IP Sockets in C: Practical Guide for Programmers, Morgan Kaufman, 2001. [DSL 2016] DSL 
Forum homepage, http://www.dslforum.org/ [Dhunghel 2008] P. Dhungel, D. Wu, B. 
Schonhorst, K.W. Ross, “A Measurement Study of Attacks on BitTorrent Leechers,” 7th 
International Workshop on Peer-to-Peer Systems (IPTPS 2008) (Tampa Bay, FL, Feb. 2008). 
[Droms 2002] R. Droms, T. Lemon, The DHCP Handbook (2nd Edition), SAMS Publishing, 2002. 


## Page 16

[Edney 2003] J. Edney and W. A. Arbaugh, Real 802.11 Security: Wi-Fi Protected Access and 
802.11i, Addison-Wesley Professional, 2003. [Edwards 2011] W. K. Edwards, R. Grinter, R. 
Mahajan, D. Wetherall, “Advancing the State of Home Networking,” Communications of the 
ACM, Vol. 54, No. 6 (June 2011), pp. 62–71. [Ellis 1987] H. Ellis, “The Story of Non-Secret 
Encryption,” http://jya.com/ellisdoc.htm [Erickson 2013] D. Erickson, “ The Beacon Openflow 
Controller,” 2nd ACM SIGCOMM Workshop on Hot Topics in Software Defined Networking 
(HotSDN ’13). ACM, New York, NY, USA, pp. 13–18. [Ericsson 2012] Ericsson, “The Evolution of 
Edge,” 
http://www.ericsson.com/technology/whitepapers/broadband/evolution_of_EDGE.shtml 
[Facebook 2014] A. Andreyev, “Introducing Data Center Fabric, the Next-Generation Facebook 
Data Center Network,” https://code.facebook.com/posts/360346274145943/introducing-data-
center-fabric-the-next-generation-facebook-data-center-network [Faloutsos 1999] C. 
Faloutsos, M. Faloutsos, P. Faloutsos, “What Does the Internet Look Like? Empirical Laws of 
the Internet Topology,” Proc. 1999 ACM SIGCOMM (Boston, MA, Aug. 1999). [Farrington 2010] 
N. Farrington, G. Porter, S. Radhakrishnan, H. Bazzaz, V. Subramanya, Y. Fainman, G. Papen, A. 
Vahdat, “Helios: A Hybrid Electrical/Optical Switch Architecture for Modular Data Centers,” 
Proc. 2010 ACM SIGCOMM. [Feamster 2004] N. Feamster, H. Balakrishnan, J. Rexford, A. 
Shaikh, K. van der Merwe, “The Case for Separating Routing from Routers,” ACM SIGCOMM 
Workshop on Future Directions in Network Architecture, Sept. 2004. [Feamster 2004] N. 
Feamster, J. Winick, J. Rexford, “A Model for BGP Routing for Network Engineering,” Proc. 2004 
ACM SIGMETRICS (New York, NY, June 2004). [Feamster 2005] N. Feamster, H. Balakrishnan, 
“Detecting BGP Configuration Faults with Static Analysis,” NSDI (May 2005). [Feamster 2013] 
N. Feamster, J. Rexford, E. Zegura, “The Road to SDN,” ACM Queue, Volume 11, Issue 12, (Dec. 
2013). [Feldmeier 1995] D. Feldmeier, “Fast Software Implementation of Error Detection 
Codes,” IEEE/ACM Transactions on Networking, Vol. 3, No. 6 (Dec. 1995), pp. 640–652. 
[Ferguson 2013] A. Ferguson, A. Guha, C. Liang, R. Fonseca, S. Krishnamurthi, “Participatory 
Networking: An API for Application Control of SDNs,” Proceedings ACM SIGCOMM 2013, pp. 
327–338. [Fielding 2000] R. Fielding, “Architectural Styles and the Design of Network-based 
Software Architectures,” 2000. PhD Thesis, UC Irvine, 2000. [FIPS 1995] Federal Information 
Processing Standard, “Secure Hash Standard,” FIPS Publication 180-1. 
http://www.itl.nist.gov/fipspubs/fip180-1.htm [Floyd 1999] S. Floyd, K. Fall, “Promoting the Use 
of End-to-End Congestion Control in the Internet,” IEEE/ACM Transactions on Networking, Vol. 
6, No. 5 (Oct. 1998), pp. 458–472. [Floyd 2000] S. Floyd, M. Handley, J. Padhye, J. Widmer, 
“Equation-Based Congestion Control for Unicast Applications,” Proc. 2000 ACM SIGCOMM 
(Stockholm, Sweden, Aug. 2000). [Floyd 2001] S. Floyd, “A Report on Some Recent 
Developments in TCP Congestion Control,” IEEE Communications Magazine (Apr. 2001). [Floyd 
2016] S. Floyd, “References on RED (Random Early Detection) Queue Management,” 
http://www.icir.org/floyd/red.html [Floyd Synchronization 1994] S. Floyd, V. Jacobson, 
“Synchronization of Periodic Routing Messages,” IEEE/ACM Transactions on Networking, Vol. 2, 
No. 2 (Apr. 1997) pp. 122–136. [Floyd TCP 1994] S. Floyd, “TCP and Explicit Congestion 
Notification,” ACM SIGCOMM Computer Communications Review, Vol. 24, No. 5 (Oct. 1994), 
pp. 10–23. [Fluhrer 2001] S. Fluhrer, I. Mantin, A. Shamir, “Weaknesses in the Key Scheduling 
Algorithm of RC4,” Eighth Annual Workshop on Selected Areas in Cryptography (Toronto, 
Canada, Aug. 2002). [Fortz 2000] B. Fortz, M. Thorup, “Internet Traffic Engineering by Optimizing 
OSPF Weights,” Proc. 2000 IEEE INFOCOM (Tel Aviv, Israel, Apr. 2000). [Fortz 2002] B. Fortz, J. 
Rexford, M. Thorup, “Traffic Engineering with Traditional IP Routing Protocols,” IEEE 
Communication Magazine (Oct. 2002). [Fraleigh 2003] C. Fraleigh, F. Tobagi, C. Diot, 
“Provisioning IP Backbone Networks to Support Latency Sensitive Traffic,” Proc. 2003 IEEE 


## Page 17

INFOCOM (San Francisco, CA, Mar. 2003). [Frost 1994] J. Frost, “BSD Sockets: A Quick and 
Dirty Primer,” http://world.std .com/~jimf/papers/sockets/sockets.html [FTC 2015] Internet of 
Things: Privacy and Security in a Connected World, Federal Trade Commission, 2015, 
https://www.ftc.gov/system/files/documents/reports/ federal-trade-commission-staff-report-
november-2013-workshop-entitled-internet-things-privacy/150127iotrpt.pdf [FTTH 2016] Fiber 
to the Home Council, http://www.ftthcouncil.org/ [Gao 2001] L. Gao, J. Rexford, “Stable 
Internet Routing Without Global Coordination,” IEEE/ACM Transactions on Networking, Vol. 9, 
No. 6 (Dec. 2001), pp. 681–692. [Gartner 2014] Gartner report on Internet of Things, 
http://www.gartner.com/ technology/research/internet-of-things [Gauthier 1999] L. Gauthier, 
C. Diot, and J. Kurose, “End-to-End Transmission Control Mechanisms for Multiparty Interactive 
Applications on the Internet,” Proc. 1999 IEEE INFOCOM (New York, NY, Apr. 1999). [Gember-
Jacobson 2014] A. Gember-Jacobson, R. Viswanathan, C. Prakash, R. Grandl, J. Khalid, S. Das, 
A. Akella, “OpenNF: Enabling Innovation in Network Function Control,” Proc. ACM SIGCOMM 
2014, pp. 163–174. [Goodman 1997] David J. Goodman, Wireless Personal Communications 
Systems, Prentice-Hall, 1997. [Google IPv6 2015] Google Inc. “IPv6 Statistics,” 
https://www.google.com/intl/en/ipv6/statistics.html [Google Locations 2016] Google data 
centers. http://www.google.com/corporate/datacenter/locations.html [Goralski 1999] W. 
Goralski, Frame Relay for High-Speed Networks, John Wiley, New York, 1999. [Greenberg 
2009a] A. Greenberg, J. Hamilton, D. Maltz, P. Patel, “The Cost of a Cloud: Research Problems 
in Data Center Networks,” ACM Computer Communications Review (Jan. 2009). [Greenberg 
2009b] A. Greenberg, N. Jain, S. Kandula, C. Kim, P. Lahiri, D. Maltz, P. Patel, S. Sengupta, “VL2: 
A Scalable and Flexible Data Center Network,” Proc. 2009 ACM SIGCOMM. [Greenberg 2011] A. 
Greenberg, J. Hamilton, N. Jain, S. Kandula, C. Kim, P. Lahiri, D. Maltz, P. Patel, S. Sengupta, 
“VL2: A Scalable and Flexible Data Center Network,” Communications of the ACM, Vol. 54, No. 
3 (Mar. 2011), pp. 95–104. [Greenberg 2015] A. Greenberg, “SDN for the Cloud,” Sigcomm 2015 
Keynote Address, http://conferences.sigcomm.org/sigcomm/2015/pdf/papers/keynote.pdf 
[Griffin 2012] T. Griffin, “Interdomain Routing Links,” 
http://www.cl.cam.ac.uk/~tgg22/interdomain/ [Gude 2008] N. Gude, T. Koponen, J. Pettit, B. 
Pfaff, M. Casado, N. McKeown, and S. Shenker, “NOX: Towards an Operating System for 
Networks,” ACM SIGCOMM Computer Communication Review, July 2008. [Guha 2006] S. 
Guha, N. Daswani, R. Jain, “An Experimental Study of the Skype Peer-to-Peer VoIP System,” 
Proc. Fifth Int. Workshop on P2P Systems (Santa Barbara, CA, 2006). [Guo 2005] L. Guo, S. 
Chen, Z. Xiao, E. Tan, X. Ding, X. Zhang, “Measurement, Analysis, and Modeling of BitTorrent-
Like Systems,” Proc. 2005 ACM Internet Measurement Conference. [Guo 2009] C. Guo, G. Lu, 
D. Li, H. Wu, X. Zhang, Y. Shi, C. Tian, Y. Zhang, S. Lu, “BCube: A High Performance, Server-
centric Network Architecture for Modular Data Centers,” Proc. 2009 ACM SIGCOMM. [Gupta 
2001] P. Gupta, N. McKeown, “Algorithms for Packet Classification,” IEEE Network Magazine, 
Vol. 15, No. 2 (Mar./Apr. 2001), pp. 24–32. [Gupta 2014] A. Gupta, L. Vanbever, M. Shahbaz, S. 
Donovan, B. Schlinker, N. Feamster, J. Rexford, S. Shenker, R. Clark, E. Katz-Bassett, “SDX: A 
Software Defined Internet Exchange, “ Proc. ACM SIGCOMM 2014 (Aug. 2014), pp. 551–562. 
[Ha 2008] S. Ha, I. Rhee, L. Xu, “CUBIC: A New TCP-Friendly High-Speed TCP Variant,” ACM 
SIGOPS Operating System Review, 2008. [Halabi 2000] S. Halabi, Internet Routing 
Architectures, 2nd Ed., Cisco Press, 2000. [Hanabali 2005] A. A. Hanbali, E. Altman, P. Nain, “A 
Survey of TCP over Ad Hoc Networks,” IEEE Commun. Surveys and Tutorials, Vol. 7, No. 3 
(2005), pp. 22–36. [Hei 2007] X. Hei, C. Liang, J. Liang, Y. Liu, K. W. Ross, “A Measurement Study 
of a Large-scale P2P IPTV System,” IEEE Trans. on Multimedia (Dec. 2007). [Heidemann 1997] J. 
Heidemann, K. Obraczka, J. Touch, “Modeling the Performance of HTTP over Several Transport 
Protocols,” IEEE/ACM Transactions on Networking, Vol. 5, No. 5 (Oct. 1997), pp. 616–630. [Held 


## Page 18

2001] G. Held, Data Over Wireless Networks: Bluetooth, WAP, and Wireless LANs, McGraw-
Hill, 2001. [Holland 2001] G. Holland, N. Vaidya, V. Bahl, “A Rate-Adaptive MAC Protocol for 
Multi-Hop Wireless Networks,” Proc. 2001 ACM Int. Conference of Mobile Computing and 
Networking (Mobicom01) (Rome, Italy, July 2001). [Hollot 2002] C.V. Hollot, V. Misra, D. 
Towsley, W. Gong, “Analysis and Design of Controllers for AQM Routers Supporting TCP Flows,” 
IEEE Transactions on Automatic Control, Vol. 47, No. 6 (June 2002), pp. 945–959. [Hong 2013] 
C. Hong, S, Kandula, R. Mahajan, M.Zhang, V. Gill, M. Nanduri, R. Wattenhofer, “Achieving High 
Utilization with Software-driven WAN,” ACM SIGCOMM Conference (Aug. 2013), pp.15–26. 
[Huang 2002] C. Haung, V. Sharma, K. Owens, V. Makam, “Building Reliable MPLS Networks 
Using a Path Protection Mechanism,” IEEE Communications Magazine, Vol. 40, No. 3 (Mar. 
2002), pp. 156–162. [Huang 2005] Y. Huang, R. Guerin, “Does Over-Provisioning Become More 
or Less Efficient as Networks Grow Larger?,” Proc. IEEE Int. Conf. Network Protocols (ICNP) 
(Boston MA, Nov. 2005). [Huang 2008] C. Huang, J. Li, A. Wang, K. W. Ross, “Understanding 
Hybrid CDN-P2P: Why Limelight Needs Its Own Red Swoosh,” Proc. 2008 NOSSDAV, 
Braunschweig, Germany. [Huitema 1998] C. Huitema, IPv6: The New Internet Protocol, 2nd Ed., 
Prentice Hall, Englewood Cliffs, NJ, 1998. [Huston 1999a] G. Huston, “Interconnection, Peering, 
and Settlements—Part I,” The Internet Protocol Journal, Vol. 2, No. 1 (Mar. 1999). [Huston 2004] 
G. Huston, “NAT Anatomy: A Look Inside Network Address Translators,” The Internet Protocol 
Journal, Vol. 7, No. 3 (Sept. 2004). [Huston 2008a] G. Huston, “Confronting IPv4 Address 
Exhaustion,” http://www.potaroo.net/ispcol/2008-10/v4depletion.html [Huston 2008b] G. 
Huston, G. Michaelson, “IPv6 Deployment: Just where are we?” 
http://www.potaroo.net/ispcol/2008-04/ipv6.html [Huston 2011a] G. Huston, “A Rough Guide 
to Address Exhaustion,” The Internet Protocol Journal, Vol. 14, No. 1 (Mar. 2011). [Huston 
2011b] G. Huston, “Transitioning Protocols,” The Internet Protocol Journal, Vol. 14, No. 1 (Mar. 
2011). [IAB 2016] Internet Architecture Board homepage, http://www.iab.org/ [IANA Protocol 
Numbers 2016] Internet Assigned Numbers Authority, Protocol Numbers, 
http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml [IBM 1997] IBM 
Corp., IBM Inside APPN - The Essential Guide to the Next-Generation SNA, SG24-3669-03, June 
1997. [ICANN 2016] The Internet Corporation for Assigned Names and Numbers homepage, 
http://www.icann.org [IEEE 802 2016] IEEE 802 LAN/MAN Standards Committee homepage, 
http://www.ieee802.org/ [IEEE 802.11 1999] IEEE 802.11, “1999 Edition (ISO/IEC 8802-11: 1999) 
IEEE Standards for Information Technology—Telecommunications and Information Exchange 
Between Systems—Local and Metropolitan Area Network—Specific Requirements—Part 11: 
Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specification,” 
http://standards.ieee.org/getieee802/download/802.11-1999.pdf [IEEE 802.11ac 2013] IEEE, 
“802.11ac-2013—IEEE Standard for Information technology—Telecommunications and 
Information Exchange Between Systems—Local and Metropolitan Area Networks—Specific 
Requirements—Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) 
Specifications—Amendment 4: Enhancements for Very High Throughput for Operation in Bands 
Below 6 GHz.” [IEEE 802.11n 2012] IEEE, “IEEE P802.11—Task Group N—Meeting Update: 
Status of 802.11n,” http://grouper.ieee.org/groups/802/11/Reports/tgn_update .htm [IEEE 
802.15 2012] IEEE 802.15 Working Group for WPAN homepage, 
http://grouper.ieee.org/groups/802/15/. [IEEE 802.15.4 2012] IEEE 802.15 WPAN Task Group 4, 
http://www.ieee802.org/15/pub/TG4.html [IEEE 802.16d 2004] IEEE, “IEEE Standard for Local 
and Metropolitan Area Networks, Part 16: Air Interface for Fixed Broadband Wireless Access 
Systems,” http:// standards.ieee.org/getieee802/download/802.16-2004.pdf [IEEE 802.16e 
2005] IEEE, “IEEE Standard for Local and Metropolitan Area Networks, Part 16: Air Interface for 
Fixed and Mobile Broadband Wireless Access Systems, Amendment 2: Physical and Medium 


## Page 19

Access Control Layers for Combined Fixed and Mobile Operation in Licensed Bands and 
Corrigendum 1,” http:// standards.ieee.org/getieee802/download/802.16e-2005.pdf [IEEE 
802.1q 2005] IEEE, “IEEE Standard for Local and Metropolitan Area Networks: Virtual Bridged 
Local Area Networks,” http://standards.ieee.org/ getieee802/ download/802.1Q-2005.pdf [IEEE 
802.1X] IEEE Std 802.1X-2001 Port-Based Network Access Control, 
http://standards.ieee.org/reading/ieee/std_public/description/lanman/ 802.1x-2001_desc.html 
[IEEE 802.3 2012] IEEE, “IEEE 802.3 CSMA/CD (Ethernet),” 
http://grouper.ieee.org/groups/802/3/ [IEEE 802.5 2012] IEEE, IEEE 802.5 homepage, 
http://www.ieee802.org/5/ www8025org/ [IETF 2016] Internet Engineering Task Force 
homepage, http://www.ietf.org [Ihm 2011] S. Ihm, V. S. Pai, “Towards Understanding Modern 
Web Traffic,” Proc. 2011 ACM Internet Measurement Conference (Berlin). [IMAP 2012] The IMAP 
Connection, http://www.imap.org/ [Intel 2016] Intel Corp., “Intel 710 Ethernet Adapter,” 
http://www.intel.com/ content/www/us/en/ethernet-products/converged-network-
adapters/ethernet-xl710 .html [Internet2 Multicast 2012] Internet2 Multicast Working Group 
homepage, http://www.internet2.edu/multicast/ [ISC 2016] Internet Systems Consortium 
homepage, http://www.isc.org [ISI 1979] Information Sciences Institute, “DoD Standard 
Internet Protocol,” Internet Engineering Note 123 (Dec. 1979), http://www.isi.edu/in-notes/ien/ 
ien123.txt [ISO 2016] International Organization for Standardization homepage, International 
Organization for Standardization, http://www.iso.org/ [ISO X.680 2002] International 
Organization for Standardization, “X.680: ITU-T Recommendation X.680 (2002) Information 
Technology—Abstract Syntax Notation One (ASN.1): Specification of Basic Notation,” 
http://www.itu.int/ITU-T/studygroups/com17/languages/X.680-0207.pdf [ITU 1999] Asymmetric 
Digital Subscriber Line (ADSL) Transceivers. ITU-T G.992.1, 1999. [ITU 2003] Asymmetric Digital 
Subscriber Line (ADSL) Transceivers—Extended Bandwidth ADSL2 (ADSL2Plus). ITU-T G.992.5, 
2003. [ITU 2005a] International Telecommunication Union, “ITU-T X.509, The Directory: Public-
key and attribute certificate frameworks” (Aug. 2005). [ITU 2006] ITU, “G.993.1: Very High Speed 
Digital Subscriber Line Transceivers (VDSL),” https://www.itu.int/rec/T-REC-G.993.1-200406-
I/en, 2006. [ITU 2015] “Measuring the Information Society Report,” 2015, 
http://www.itu.int/en/ITU-D/Statistics/Pages/publications/mis2015.aspx [ITU 2012] The ITU 
homepage, http://www.itu.int/ [ITU-T Q.2931 1995] International Telecommunication Union, 
“Recommendation Q.2931 (02/95)—Broadband Integrated Services Digital Network (B-ISDN)— 
Digital Subscriber Signalling System No. 2 (DSS 2)—User-Network Interface (UNI)—Layer 3 
Specification for Basic Call/Connection Control.” [IXP List 2016] List of IXPs, Wikipedia, 
https://en.wikipedia.org/wiki/List_of_ Internet_exchange_points [Iyengar 2015] J. Iyengar, I. 
Swett, “QUIC: A UDP-Based Secure and Reliable Transport for HTTP/2,” Internet Draft draft-
tsvwg-quic-protocol-00, June 2015. [Iyer 2008] S. Iyer, R. R. Kompella, N. McKeown, “Designing 
Packet Buffers for Router Line Cards,” IEEE Transactions on Networking, Vol. 16, No. 3 (June 
2008), pp. 705–717. [Jacobson 1988] V. Jacobson, “Congestion Avoidance and Control,” Proc. 
1988 ACM SIGCOMM (Stanford, CA, Aug. 1988), pp. 314–329. [Jain 1986] R. Jain, “A Timeout-
Based Congestion Control Scheme for Window Flow-Controlled Networks,” IEEE Journal on 
Selected Areas in Communications SAC-4, 7 (Oct. 1986). [Jain 1989] R. Jain, “A Delay-Based 
Approach for Congestion Avoidance in Interconnected Heterogeneous Computer Networks,” 
ACM SIGCOMM Computer Communications Review, Vol. 19, No. 5 (1989), pp. 56–71. [Jain 
1994] R. Jain, FDDI Handbook: High-Speed Networking Using Fiber and Other Media, Addison-
Wesley, Reading, MA, 1994. [Jain 1996] R. Jain. S. Kalyanaraman, S. Fahmy, R. Goyal, S. Kim, 
“Tutorial Paper on ABR Source Behavior,” ATM Forum/96-1270, Oct. 1996. 
http://www.cse.wustl.edu/ ~jain/atmf/ftp/atm96-1270.pdf [Jain 2013] S. Jain, A. Kumar, S. 
Mandal, J. Ong, L. Poutievski, A. Singh, S.Venkata, J. Wanderer, J. Zhou, M. Zhu, J. Zolla, U. 


## Page 20

Hölzle, S. Stuart, A, Vahdat, “B4: Experience with a Globally Deployed Software Defined Wan,” 
ACM SIGCOMM 2013, pp. 3–14. [Jaiswal 2003] S. Jaiswal, G. Iannaccone, C. Diot, J. Kurose, D. 
Towsley, “Measurement and Classification of Out-of-Sequence Packets in a Tier-1 IP 
backbone,” Proc. 2003 IEEE INFOCOM. [Ji 2003] P. Ji, Z. Ge, J. Kurose, D. Towsley, “A 
Comparison of Hard-State and Soft-State Signaling Protocols,” Proc. 2003 ACM SIGCOMM 
(Karlsruhe, Germany, Aug. 2003). [Jimenez 1997] D. Jimenez, “Outside Hackers Infiltrate MIT 
Network, Compromise Security,” The Tech, Vol. 117, No 49 (Oct. 1997), p. 1, http://www-
tech.mit.edu/V117/ N49/hackers.49n.html [Jin 2004] C. Jin, D. X. We, S. Low, “FAST TCP: 
Motivation, Architecture, Algorithms, Performance,” Proc. 2004 IEEE INFOCOM (Hong Kong, 
Mar. 2004). [Juniper Contrail 2016] Juniper Networks, “Contrail,” 
http://www.juniper.net/us/en/products-services/sdn/contrail/ [Juniper MX2020 2015] Juniper 
Networks, “MX2020 and MX2010 3D Universal Edge Routers,” 
www.juniper.net/us/en/local/pdf/.../1000417-en.pdf [Kaaranen 2001] H. Kaaranen, S. Naghian, 
L. Laitinen, A. Ahtiainen, V. Niemi, Networks: Architecture, Mobility and Services, New York: 
John Wiley & Sons, 2001. [Kahn 1967] D. Kahn, The Codebreakers: The Story of Secret Writing, 
The Macmillan Company, 1967. [Kahn 1978] R. E. Kahn, S. Gronemeyer, J. Burchfiel, R. 
Kunzelman, “Advances in Packet Radio Technology,” Proc. 1978 IEEE INFOCOM, 66, 11 (Nov. 
1978). [Kamerman 1997] A. Kamerman, L. Monteban, “WaveLAN-II: A High– Performance 
Wireless LAN for the Unlicensed Band,” Bell Labs Technical Journal (Summer 1997), pp. 118–
133. [Kar 2000] K. Kar, M. Kodialam, T. V. Lakshman, “Minimum Interference Routing of 
Bandwidth Guaranteed Tunnels with MPLS Traffic Engineering Applications,” IEEE J. Selected 
Areas in Communications (Dec. 2000). [Karn 1987] P. Karn, C. Partridge, “Improving Round-Trip 
Time Estimates in Reliable Transport Protocols,” Proc. 1987 ACM SIGCOMM. [Karol 1987] M. 
Karol, M. Hluchyj, A. Morgan, “Input Versus Output Queuing on a Space-Division Packet 
Switch,” IEEE Transactions on Communications, Vol. 35, No. 12 (Dec.1987), pp. 1347–1356. 
[Kaufman 1995] C. Kaufman, R. Perlman, M. Speciner, Network Security, Private 
Communication in a Public World, Prentice Hall, Englewood Cliffs, NJ, 1995. [Kelly 1998] F. P. 
Kelly, A. Maulloo, D. Tan, “Rate Control for Communication Networks: Shadow Prices, 
Proportional Fairness and Stability,” J. Operations Res. Soc., Vol. 49, No. 3 (Mar. 1998), pp. 
237–252. [Kelly 2003] T. Kelly, “Scalable TCP: Improving Performance in High Speed Wide Area 
Networks,” ACM SIGCOMM Computer Communications Review, Volume 33, No. 2 (Apr. 2003), 
pp.83–91. [Kilkki 1999] K. Kilkki, Differentiated Services for the Internet, Macmillan Technical 
Publishing, Indianapolis, IN, 1999. [Kim 2005] H. Kim, S. Rixner, V. Pai, “Network Interface Data 
Caching,” IEEE Transactions on Computers, Vol. 54, No. 11 (Nov. 2005), pp. 1394–1408. [Kim 
2008] C. Kim, M. Caesar, J. Rexford, “Floodless in SEATTLE: A Scalable Ethernet Architecture for 
Large Enterprises,” Proc. 2008 ACM SIGCOMM (Seattle, WA, Aug. 2008). [Kleinrock 1961] L. 
Kleinrock, “Information Flow in Large Communication Networks,” RLE Quarterly Progress 
Report, July 1961. [Kleinrock 1964] L. Kleinrock, 1964 Communication Nets: Stochastic 
Message Flow and Delay, McGraw-Hill, New York, NY, 1964. [Kleinrock 1975] L. Kleinrock, 
Queuing Systems, Vol. 1, John Wiley, New York, 1975. [Kleinrock 1975b] L. Kleinrock, F. A. 
Tobagi, “Packet Switching in Radio Channels: Part I—Carrier Sense Multiple-Access Modes and 
Their Throughput-Delay Characteristics,” IEEE Transactions on Communications, Vol. 23, No. 
12 (Dec. 1975), pp. 1400–1416. [Kleinrock 1976] L. Kleinrock, Queuing Systems, Vol. 2, John 
Wiley, New York, 1976. [Kleinrock 2004] L. Kleinrock, “The Birth of the Internet,” 
http://www.lk.cs.ucla.edu/LK/Inet/birth.html [Kohler 2006] E. Kohler, M. Handley, S. Floyd, 
“DDCP: Designing DCCP: Congestion Control Without Reliability,” Proc. 2006 ACM SIGCOMM 
(Pisa, Italy, Sept. 2006). [Kolding 2003] T. Kolding, K. Pedersen, J. Wigard, F. Frederiksen, P. 
Mogensen, “High Speed Downlink Packet Access: WCDMA Evolution,” IEEE Vehicular 

