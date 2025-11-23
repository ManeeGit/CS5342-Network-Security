# Computer Networking _ A Top Down Approach, 7th (2)-10

## Page 1

destination adapter, the sending adapter inserts the destination adapter’s MAC address into 
the frame and then sends the frame into the LAN. As we will soon see, a switch occasionally 
broadcasts an incoming frame onto all of its interfaces. We’ll see in Chapter 7 that 802.11 also 
broadcasts frames. Thus, an adapter may receive a frame that isn’t addressed to it. Thus, when 
an adapter receives a frame, it will check to see whether the destination MAC address in the 
frame matches its own MAC address. If there is a match, the adapter extracts the enclosed 
datagram and passes the datagram up the protocol stack. If there isn’t a match, the adapter 
discards the frame, without passing the network-layer datagram up. Thus, the destination only 
will be 24 24 interrupted when the frame is received. However, sometimes a sending adapter 
does want all the other adapters on the LAN to receive and process the frame it is about to 
send. In this case, the sending adapter inserts a special MAC broadcast address into the 
destination address field of the frame. For LANs that use 6-byte addresses (such as Ethernet 
and 802.11), the broadcast address is a string of 48 consecutive 1s (that is, FF-FF-FF-FF-FFFF in 
hexadecimal notation). Address Resolution Protocol (ARP) Because there are both network-
layer addresses (for example, Internet IP addresses) and link-layer addresses (that is, MAC 
addresses), there is a need to translate between them. For the Internet, this is the job of the 
Address Resolution Protocol (ARP) [RFC 826]. To understand the need for a protocol such as 
ARP, consider the network shown in Figure 6.17. In this simple example, each host and router 
has a single IP address and single MAC address. As usual, IP addresses are shown in dotted-
decimal PRINCIPLES IN PRACTICE KEEPING THE LAYERS INDEPENDENT There are several 
reasons why hosts and router interfaces have MAC addresses in addition to network-layer 
addresses. First, LANs are designed for arbitrary network-layer protocols, not just for IP and the 
Internet. If adapters were assigned IP addresses rather than “neutral” MAC addresses, then 
adapters would not easily be able to support other network-layer protocols (for example, IPX or 
DECnet). Second, if adapters were to use network-layer addresses instead of MAC addresses, 
the network-layer address would have to be stored in the adapter RAM and reconfigured every 
time the adapter was moved (or powered up). Another option is to not use any addresses in the 
adapters and have each adapter pass the data (typically, an IP datagram) of each frame it 
receives up the protocol stack. The network layer could then check for a matching network-
layer address. One problem with this option is that the host would be interrupted by every frame 
sent on the LAN, including by frames that were destined for other hosts on the same broadcast 
LAN. In summary, in order for the layers to be largely independent building blocks in a network 
architecture, different layers need to have their own addressing scheme. We have now seen 
three types of addresses: host names for the application layer, IP addresses for the network 
layer, and MAC addresses for the link layer. Figure 6.17 Each interface on a LAN has an IP 
address and a MAC address notation and MAC addresses are shown in hexadecimal notation. 
For the purposes of this discussion, we will assume in this section that the switch broadcasts 
all frames; that is, whenever a switch receives a frame on one interface, it forwards the frame 
on all of its other interfaces. In the next section, we will provide a more accurate explanation of 
how switches operate. Now suppose that the host with IP address 222.222.222.220 wants to 
send an IP datagram to host 222.222.222.222. In this example, both the source and destination 
are in the same subnet, in the addressing sense of Section 4.3.3. To send a datagram, the 
source must give its adapter not only the IP datagram but also the MAC address for destination 
222.222.222.222. The sending adapter will then construct a link-layer frame containing the 
destination’s MAC address and send the frame into the LAN. The important question addressed 
in this section is, How does the sending host determine the MAC address for the destination 
host with IP address 222.222.222.222? As you might have guessed, it uses ARP. An ARP module 
in the sending host takes any IP address on the same LAN as input, and returns the 


## Page 2

corresponding MAC address. In the example at hand, sending host 222.222.222.220 provides 
its ARP module the IP address 222.222.222.222, and the ARP module returns the corresponding 
MAC address 49-BD-D2-C7-56-2A. So we see that ARP resolves an IP address to a MAC 
address. In many ways it is analogous to DNS (studied in Section 2.5), which resolves host 
names to IP addresses. However, one important difference between the two resolvers is that 
DNS resolves host names for hosts anywhere in the Internet, whereas ARP resolves IP 
addresses only for hosts and router interfaces on the same subnet. If a node in California were 
to try to use ARP to resolve the IP address for a node in Mississippi, ARP would return with an 
error. Figure 6.18 A possible ARP table in 222.222.222.220 Now that we have explained what 
ARP does, let’s look at how it works. Each host and router has an ARP table in its memory, 
which contains mappings of IP addresses to MAC addresses. Figure 6.18 shows what an ARP 
table in host 222.222.222.220 might look like. The ARP table also contains a timeto-live (TTL) 
value, which indicates when each mapping will be deleted from the table. Note that a table 
does not necessarily contain an entry for every host and router on the subnet; some may have 
never been entered into the table, and others may have expired. A typical expiration time for an 
entry is 20 minutes from when an entry is placed in an ARP table. Now suppose that host 
222.222.222.220 wants to send a datagram that is IP-addressed to another host or router on 
that subnet. The sending host needs to obtain the MAC address of the destination given the IP 
address. This task is easy if the sender’s ARP table has an entry for the destination node. But 
what if the ARP table doesn’t currently have an entry for the destination? In particular, suppose 
222.222.222.220 wants to send a datagram to 222.222.222.222. In this case, the sender uses 
the ARP protocol to resolve the address. First, the sender constructs a special packet called an 
ARP packet. An ARP packet has several fields, including the sending and receiving IP and MAC 
addresses. Both ARP query and response packets have the same format. The purpose of the 
ARP query packet is to query all the other hosts and routers on the subnet to determine the 
MAC address corresponding to the IP address that is being resolved. Returning to our example, 
222.222.222.220 passes an ARP query packet to the adapter along with an indication that the 
adapter should send the packet to the MAC broadcast address, namely, FF-FF-FFFF-FF-FF. The 
adapter encapsulates the ARP packet in a link-layer frame, uses the broadcast address for the 
frame’s destination address, and transmits the frame into the subnet. Recalling our social 
security number/postal address analogy, an ARP query is equivalent to a person shouting out in 
a crowded room of cubicles in some company (say, AnyCorp): “What is the social security 
number of the person whose postal address is Cubicle 13, Room 112, AnyCorp, Palo Alto, 
California?” The frame containing the ARP query is received by all the other adapters on the 
subnet, and (because of the broadcast address) each adapter passes the ARP packet within the 
frame up to its ARP module. Each of these ARP modules checks to see if its IP address matches 
the destination IP address in the ARP packet. The one with a match sends back to the querying 
host a response ARP packet with the desired mapping. The querying host 222.222.222.220 can 
then update its ARP table and send its IP datagram, encapsulated in a link-layer frame whose 
destination MAC is that of the host or router responding to the earlier ARP query. There are a 
couple of interesting things to note about the ARP protocol. First, the query ARP message is 
sent within a broadcast frame, whereas the response ARP message is sent within a standard 
frame. Before reading on you should think about why this is so. Second, ARP is plug-and-play; 
that is, an ARP table gets built automatically—it doesn’t have to be configured by a system 
administrator. And if a host becomes disconnected from the subnet, its entry is eventually 
deleted from the other ARP tables in the subnet. Students often wonder if ARP is a link-layer 
protocol or a network-layer protocol. As we’ve seen, an ARP packet is encapsulated within a 
link-layer frame and thus lies architecturally above the link layer. However, an ARP packet has 


## Page 3

fields containing link-layer addresses and thus is arguably a link-layer protocol, but it also 
contains network-layer addresses and thus is also arguably a network-layer protocol. In the 
end, ARP is probably best considered a protocol that straddles the boundary between the link 
and network layers—not fitting neatly into the simple layered protocol stack we studied in 
Chapter 1. Such are the complexities of real-world protocols! Sending a Datagram off the 
Subnet It should now be clear how ARP operates when a host wants to send a datagram to 
another host on the same subnet. But now let’s look at the more complicated situation when a 
host on a subnet wants to send a network-layer datagram to a host off the subnet (that is, 
across a router onto another subnet). Let’s discuss this issue in the context of Figure 6.19, 
which shows a simple network consisting of two subnets interconnected by a router. There are 
several interesting things to note about Figure 6.19. Each host has exactly one IP address and 
one adapter. But, as discussed in Chapter 4, a router has an IP address for each of its 
interfaces. For each router interface there is also an ARP module (in the router) and an adapter. 
Because the router in Figure 6.19 has two interfaces, it has two IP addresses, two ARP modules, 
and two adapters. Of course, each adapter in the network has its own MAC address. Figure 6.19 
Two subnets interconnected by a router Also note that Subnet 1 has the network address 
111.111.111/24 and that Subnet 2 has the network address 222.222.222/24. Thus all of the 
interfaces connected to Subnet 1 have addresses of the form 111.111.111.xxx and all of the 
interfaces connected to Subnet 2 have addresses of the form 222.222.222.xxx. Now let’s 
examine how a host on Subnet 1 would send a datagram to a host on Subnet 2. Specifically, 
suppose that host 111.111.111.111 wants to send an IP datagram to a host 222.222.222.222. 
The sending host passes the datagram to its adapter, as usual. But the sending host must also 
indicate to its adapter an appropriate destination MAC address. What MAC address should the 
adapter use? One might be tempted to guess that the appropriate MAC address is that of the 
adapter for host 222.222.222.222, namely, 49-BD-D2-C7-56-2A. This guess, however, would be 
wrong! If the sending adapter were to use that MAC address, then none of the adapters on 
Subnet 1 would bother to pass the IP datagram up to its network layer, since the frame’s 
destination address would not match the MAC address of any adapter on Subnet 1. The 
datagram would just die and go to datagram heaven. If we look carefully at Figure 6.19, we see 
that in order for a datagram to go from 111.111.111.111 to a host on Subnet 2, the datagram 
must first be sent to the router interface 111.111.111.110, which is the IP address of the first-
hop router on the path to the final destination. Thus, the appropriate MAC address for the frame 
is the address of the adapter for router interface 111.111.111.110, namely, E6-E9-00-17- BB-4B. 
How does the sending host acquire the MAC address for 111.111.111.110? By using ARP, of 
course! Once the sending adapter has this MAC address, it creates a frame (containing the 
datagram addressed to 222.222.222.222) and sends the frame into Subnet 1. The router 
adapter on Subnet 1 sees that the link-layer frame is addressed to it, and therefore passes the 
frame to the network layer of the router. Hooray—the IP datagram has successfully been moved 
from source host to the router! But we are not finished. We still have to move the datagram from 
the router to the destination. The router now has to determine the correct interface on which 
the datagram is to be forwarded. As discussed in Chapter 4, this is done by consulting a 
forwarding table in the router. The forwarding table tells the router that the datagram is to be 
forwarded via router interface 222.222.222.220. This interface then passes the datagram to its 
adapter, which encapsulates the datagram in a new frame and sends the frame into Subnet 2. 
This time, the destination MAC address of the frame is indeed the MAC address of the ultimate 
destination. And how does the router obtain this destination MAC address? From ARP, of 
course! ARP for Ethernet is defined in RFC 826. A nice introduction to ARP is given in the TCP/IP 
tutorial, RFC 1180. We’ll explore ARP in more detail in the homework problems. 6.4.2 Ethernet 


## Page 4

Ethernet has pretty much taken over the wired LAN market. In the 1980s and the early 1990s, 
Ethernet faced many challenges from other LAN technologies, including token ring, FDDI, and 
ATM. Some of these other technologies succeeded in capturing a part of the LAN market for a 
few years. But since its invention in the mid-1970s, Ethernet has continued to evolve and grow 
and has held on to its dominant position. Today, Ethernet is by far the most prevalent wired LAN 
technology, and it is likely to remain so for the foreseeable future. One might say that Ethernet 
has been to local area networking what the Internet has been to global networking. There are 
many reasons for Ethernet’s success. First, Ethernet was the first widely deployed high-speed 
LAN. Because it was deployed early, network administrators became intimately familiar with 
Ethernet— its wonders and its quirks—and were reluctant to switch over to other LAN 
technologies when they came on the scene. Second, token ring, FDDI, and ATM were more 
complex and expensive than Ethernet, which further discouraged network administrators from 
switching over. Third, the most compelling reason to switch to another LAN technology (such as 
FDDI or ATM) was usually the higher data rate of the new technology; however, Ethernet always 
fought back, producing versions that operated at equal data rates or higher. Switched Ethernet 
was also introduced in the early 1990s, which further increased its effective data rates. Finally, 
because Ethernet has been so popular, Ethernet hardware (in particular, adapters and 
switches) has become a commodity and is remarkably cheap. The original Ethernet LAN was 
invented in the mid-1970s by Bob Metcalfe and David Boggs. The original Ethernet LAN used a 
coaxial bus to interconnect the nodes. Bus topologies for Ethernet actually persisted 
throughout the 1980s and into the mid-1990s. Ethernet with a bus topology is a broadcast LAN 
—all transmitted frames travel to and are processed by all adapters connected to the bus. 
Recall that we covered Ethernet’s CSMA/CD multiple access protocol with binary exponential 
backoff in Section 6.3.2. By the late 1990s, most companies and universities had replaced their 
LANs with Ethernet installations using a hub-based star topology. In such an installation the 
hosts (and routers) are directly connected to a hub with twisted-pair copper wire. A hub is a 
physical-layer device that acts on individual bits rather than frames. When a bit, representing a 
zero or a one, arrives from one interface, the hub simply recreates the bit, boosts its energy 
strength, and transmits the bit onto all the other interfaces. Thus, Ethernet with a hub-based 
star topology is also a broadcast LAN—whenever a hub receives a bit from one of its interfaces, 
it sends a copy out on all of its other interfaces. In particular, if a hub receives frames from two 
different interfaces at the same time, a collision occurs and the nodes that created the frames 
must retransmit. In the early 2000s Ethernet experienced yet another major evolutionary 
change. Ethernet installations continued to use a star topology, but the hub at the center was 
replaced with a switch. We’ll be examining switched Ethernet in depth later in this chapter. For 
now, we only mention that a switch is not only “collision-less” but is also a bona-fide store-and-
forward packet switch; but unlike routers, which operate up through layer 3, a switch operates 
only up through layer 2. Figure 6.20 Ethernet frame structure Ethernet Frame Structure We can 
learn a lot about Ethernet by examining the Ethernet frame, which is shown in Figure 6.20. To 
give this discussion about Ethernet frames a tangible context, let’s consider sending an IP 
datagram from one host to another host, with both hosts on the same Ethernet LAN (for 
example, the Ethernet LAN in Figure 6.17.) (Although the payload of our Ethernet frame is an IP 
datagram, we note that an Ethernet frame can carry other network-layer packets as well.) Let 
the sending adapter, adapter A, have the MAC address AA-AA-AA-AA-AA-AA and the receiving 
adapter, adapter B, have the MAC address BB-BB-BB-BB-BB-BB. The sending adapter 
encapsulates the IP datagram within an Ethernet frame and passes the frame to the physical 
layer. The receiving adapter receives the frame from the physical layer, extracts the IP 
datagram, and passes the IP datagram to the network layer. In this context, let’s now examine 


## Page 5

the six fields of the Ethernet frame, as shown in Figure 6.20. Data field (46 to 1,500 bytes). This 
field carries the IP datagram. The maximum transmission unit (MTU) of Ethernet is 1,500 bytes. 
This means that if the IP datagram exceeds 1,500 bytes, then the host has to fragment the 
datagram, as discussed in Section 4.3.2. The minimum size of the data field is 46 bytes. This 
means that if the IP datagram is less than 46 bytes, the data field has to be “stuffed” to fill it out 
to 46 bytes. When stuffing is used, the data passed to the network layer contains the stuffing as 
well as an IP datagram. The network layer uses the length field in the IP datagram header to 
remove the stuffing. Destination address (6 bytes). This field contains the MAC address of the 
destination adapter, BBBB-BB-BB-BB-BB. When adapter B receives an Ethernet frame whose 
destination address is either BB-BB-BB-BB-BB-BB or the MAC broadcast address, it passes the 
contents of the frame’s data field to the network layer; if it receives a frame with any other MAC 
address, it discards the frame. Source address (6 bytes). This field contains the MAC address of 
the adapter that transmits the frame onto the LAN, in this example, AA-AA-AA-AA-AA-AA. Type 
field (2 bytes). The type field permits Ethernet to multiplex network-layer protocols. To 
understand this, we need to keep in mind that hosts can use other network-layer protocols 
besides IP. In fact, a given host may support multiple network-layer protocols using different 
protocols for different applications. For this reason, when the Ethernet frame arrives at adapter 
B, adapter B needs to know to which network-layer protocol it should pass (that is, demultiplex) 
the contents of the data field. IP and other network-layer protocols (for example, Novell IPX or 
AppleTalk) each have their own, standardized type number. Furthermore, the ARP protocol 
(discussed in the previous section) has its own type number, and if the arriving frame contains 
an ARP packet (i.e., has a type field of 0806 hexadecimal), the ARP packet will be demultiplexed 
up to the ARP protocol. Note that the type field is analogous to the protocol field in the network-
layer datagram and the port-number fields in the transport-layer segment; all of these fields 
serve to glue a protocol at one layer to a protocol at the layer above. Cyclic redundancy check 
(CRC) (4 bytes). As discussed in Section 6.2.3, the purpose of the CRC field is to allow the 
receiving adapter, adapter B, to detect bit errors in the frame. Preamble (8 bytes). The Ethernet 
frame begins with an 8-byte preamble field. Each of the first 7 bytes of the preamble has a value 
of 10101010; the last byte is 10101011. The first 7 bytes of the preamble serve to “wake up” the 
receiving adapters and to synchronize their clocks to that of the sender’s clock. Why should the 
clocks be out of synchronization? Keep in mind that adapter A aims to transmit the frame at 10 
Mbps, 100 Mbps, or 1 Gbps, depending on the type of Ethernet LAN. However, because nothing 
is absolutely perfect, adapter A will not transmit the frame at exactly the target rate; there will 
always be some drift from the target rate, a drift which is not known a priori by the other 
adapters on the LAN. A receiving adapter can lock onto adapter A’s clock simply by locking onto 
the bits in the first 7 bytes of the preamble. The last 2 bits of the eighth byte of the preamble (the 
first two consecutive 1s) alert adapter B that the “important stuff” is about to come. All of the 
Ethernet technologies provide connectionless service to the network layer. That is, when 
adapter A wants to send a datagram to adapter B, adapter A encapsulates the datagram in an 
Ethernet frame and sends the frame into the LAN, without first handshaking with adapter B. This 
layer-2 connectionless service is analogous to IP’s layer-3 datagram service and UDP’s layer-4 
connectionless service. Ethernet technologies provide an unreliable service to the network 
layer. Specifically, when adapter B receives a frame from adapter A, it runs the frame through a 
CRC check, but neither sends an acknowledgment when a frame passes the CRC check nor 
sends a negative acknowledgment when a frame fails the CRC check. When a frame fails the 
CRC check, adapter B simply discards the frame. Thus, adapter A has no idea whether its 
transmitted frame reached adapter B and passed the CRC check. This lack of reliable transport 
(at the link layer) helps to make Ethernet simple and cheap. But it also means that the stream of 


## Page 6

datagrams passed to the network layer can have gaps. CASE HISTORY BOB METCALFE AND 
ETHERNET As a PhD student at Harvard University in the early 1970s, Bob Metcalfe worked on 
the ARPAnet at MIT. During his studies, he also became exposed to Abramson’s work on ALOHA 
and random access protocols. After completing his PhD and just before beginning a job at Xerox 
Palo Alto Research Center (Xerox PARC), he visited Abramson and his University of Hawaii 
colleagues for three months, getting a firsthand look at ALOHAnet. At Xerox PARC, Metcalfe 
became exposed to Alto computers, which in many ways were the forerunners of the personal 
computers of the 1980s. Metcalfe saw the need to network these computers in an inexpensive 
manner. So armed with his knowledge about ARPAnet, ALOHAnet, and random access 
protocols, Metcalfe—along with colleague David Boggs—invented Ethernet. Metcalfe and 
Boggs’s original Ethernet ran at 2.94 Mbps and linked up to 256 hosts separated by up to one 
mile. Metcalfe and Boggs succeeded at getting most of the researchers at Xerox PARC to 
communicate through their Alto computers. Metcalfe then forged an alliance between Xerox, 
Digital, and Intel to establish Ethernet as a 10 Mbps Ethernet standard, ratified by the IEEE. 
Xerox did not show much interest in commercializing Ethernet. In 1979, Metcalfe formed his 
own company, 3Com, which developed and commercialized networking technology, including 
Ethernet technology. In particular, 3Com developed and marketed Ethernet cards in the early 
1980s for the immensely popular IBM PCs. If there are gaps due to discarded Ethernet frames, 
does the application at Host B see gaps as well? As we learned in Chapter 3, this depends on 
whether the application is using UDP or TCP. If the application is using UDP, then the 
application in Host B will indeed see gaps in the data. On the other hand, if the application is 
using TCP, then TCP in Host B will not acknowledge the data contained in discarded frames, 
causing TCP in Host A to retransmit. Note that when TCP retransmits data, the data will 
eventually return to the Ethernet adapter at which it was discarded. Thus, in this sense, 
Ethernet does retransmit data, although Ethernet is unaware of whether it is transmitting a 
brand-new datagram with brand-new data, or a datagram that contains data that has already 
been transmitted at least once. Ethernet Technologies In our discussion above, we’ve referred 
to Ethernet as if it were a single protocol standard. But in fact, Ethernet comes in many different 
flavors, with somewhat bewildering acronyms such as 10BASE-T, 10BASE-2, 100BASE-T, 
1000BASE-LX, 10GBASE-T and 40GBASE-T. These and many other Ethernet technologies have 
been standardized over the years by the IEEE 802.3 CSMA/CD (Ethernet) working group [IEEE 
802.3 2012]. While these acronyms may appear bewildering, there is actually considerable 
order here. The first part of the acronym refers to the speed of the standard: 10, 100, 1000, or 
10G, for 10 Megabit (per second), 100 Megabit, Gigabit, 10 Gigabit and 40 Gigibit Ethernet, 
respectively. “BASE” refers to baseband Ethernet, meaning that the physical media only carries 
Ethernet traffic; almost all of the 802.3 standards are for baseband Ethernet. The final part of 
the acronym refers to the physical media itself; Ethernet is both a link-layer and a physical-layer 
specification and is carried over a variety of physical media including coaxial cable, copper 
wire, and fiber. Generally, a “T” refers to twisted-pair copper wires. Historically, an Ethernet 
was initially conceived of as a segment of coaxial cable. The early 10BASE-2 and 10BASE-5 
standards specify 10 Mbps Ethernet over two types of coaxial cable, each limited in length to 
500 meters. Longer runs could be obtained by using a repeater—a physical-layer device that 
receives a signal on the input side, and regenerates the signal on the output side. A coaxial 
cable corresponds nicely to our view of Ethernet as a broadcast medium—all frames 
transmitted by one interface are received at other interfaces, and Ethernet’s CDMA/CD 
protocol nicely solves the multiple access problem. Nodes simply attach to the cable, and 
voila, we have a local area network! Ethernet has passed through a series of evolutionary steps 
over the years, and today’s Ethernet is very different from the original bus-topology designs 


## Page 7

using coaxial cable. In most installations today, nodes are connected to a switch via point-to-
point segments made of twisted-pair copper wires or fiber-optic cables, as shown in Figures 
6.15–6.17. In the mid-1990s, Ethernet was standardized at 100 Mbps, 10 times faster than 10 
Mbps Ethernet. The original Ethernet MAC protocol and frame format were preserved, but 
higher-speed physical layers were defined for copper wire (100BASE-T) and fiber (100BASE-FX, 
100BASE-SX, 100BASE-BX). Figure 6.21 shows these different standards and the common 
Ethernet MAC protocol and frame format. 100 Mbps Ethernet is limited to a 100-meter distance 
over twisted pair, and to Figure 6.21 100 Mbps Ethernet standards: A common link layer, 
different physical layers several kilometers over fiber, allowing Ethernet switches in different 
buildings to be connected. Gigabit Ethernet is an extension to the highly successful 10 Mbps 
and 100 Mbps Ethernet standards. Offering a raw data rate of 40,000 Mbps, 40 Gigabit Ethernet 
maintains full compatibility with the huge installed base of Ethernet equipment. The standard 
for Gigabit Ethernet, referred to as IEEE 802.3z, does the following: Uses the standard Ethernet 
frame format (Figure 6.20) and is backward compatible with 10BASE-T and 100BASE-T 
technologies. This allows for easy integration of Gigabit Ethernet with the existing installed base 
of Ethernet equipment. Allows for point-to-point links as well as shared broadcast channels. 
Point-to-point links use switches while broadcast channels use hubs, as described earlier. In 
Gigabit Ethernet jargon, hubs are called buffered distributors. Uses CSMA/CD for shared 
broadcast channels. In order to have acceptable efficiency, the maximum distance between 
nodes must be severely restricted. Allows for full-duplex operation at 40 Gbps in both 
directions for point-to-point channels. Initially operating over optical fiber, Gigabit Ethernet is 
now able to run over category 5 UTP cabling. Let’s conclude our discussion of Ethernet 
technology by posing a question that may have begun troubling you. In the days of bus 
topologies and hub-based star topologies, Ethernet was clearly a broadcast link (as defined in 
Section 6.3) in which frame collisions occurred when nodes transmitted at the same time. To 
deal with these collisions, the Ethernet standard included the CSMA/CD protocol, which is 
particularly effective for a wired broadcast LAN spanning a small geographical region. But if the 
prevalent use of Ethernet today is a switch-based star topology, using store-and-forward packet 
switching, is there really a need anymore for an Ethernet MAC protocol? As we’ll see shortly, a 
switch coordinates its transmissions and never forwards more than one frame onto the same 
interface at any time. Furthermore, modern switches are full-duplex, so that a switch and a 
node can each send frames to each other at the same time without interference. In other 
words, in a switch-based Ethernet LAN there are no collisions and, therefore, there is no need 
for a MAC protocol! As we’ve seen, today’s Ethernets are very different from the original 
Ethernet conceived by Metcalfe and Boggs more than 30 years ago—speeds have increased by 
three orders of magnitude, Ethernet frames are carried over a variety of media, switched-
Ethernets have become dominant, and now even the MAC protocol is often unnecessary! Is all 
of this really still Ethernet? The answer, of course, is “yes, by definition.” It is interesting to note, 
however, that through all of these changes, there has indeed been one enduring constant that 
has remained unchanged over 30 years—Ethernet’s frame format. Perhaps this then is the one 
true and timeless centerpiece of the Ethernet standard. 6.4.3 Link-Layer Switches Up until this 
point, we have been purposefully vague about what a switch actually does and how it works. 
The role of the switch is to receive incoming link-layer frames and forward them onto outgoing 
links; we’ll study this forwarding function in detail in this subsection. We’ll see that the switch 
itself is transparent to the hosts and routers in the subnet; that is, a host/router addresses a 
frame to another host/router (rather than addressing the frame to the switch) and happily sends 
the frame into the LAN, unaware that a switch will be receiving the frame and forwarding it. The 
rate at which frames arrive to any one of the switch’s output interfaces may temporarily exceed 


## Page 8

the link capacity of that interface. To accommodate this problem, switch output interfaces have 
buffers, in much the same way that router output interfaces have buffers for datagrams. Let’s 
now take a closer look at how switches operate. Forwarding and Filtering Filtering is the switch 
function that determines whether a frame should be forwarded to some interface or should just 
be dropped. Forwarding is the switch function that determines the interfaces to which a frame 
should be directed, and then moves the frame to those interfaces. Switch filtering and 
forwarding are done with a switch table. The switch table contains entries for some, but not 
necessarily all, of the hosts and routers on a LAN. An entry in the switch table contains (1) a 
MAC address, (2) the switch interface that leads toward that MAC address, and (3) the time at 
which the entry was placed in the table. An example switch table for the uppermost switch in 
Figure 6.15 is shown in Figure 6.22. This description of frame forwarding may sound similar to 
our discussion of datagram forwarding Figure 6.22 Portion of a switch table for the uppermost 
switch in Figure 6.15 in Chapter 4. Indeed, in our discussion of generalized forwarding in 
Section 4.4, we learned that many modern packet switches can be configured to forward on the 
basis of layer-2 destination MAC addresses (i.e., function as a layer-2 switch) or layer-3 IP 
destination addresses (i.e., function as a layer-3 router). Nonetheless, we’ll make the important 
distinction that switches forward packets based on MAC addresses rather than on IP 
addresses. We will also see that a traditional (i.e., in a non-SDN context) switch table is 
constructed in a very different manner from a router’s forwarding table. To understand how 
switch filtering and forwarding work, suppose a frame with destination address DDDD-DD-DD-
DD-DD arrives at the switch on interface x. The switch indexes its table with the MAC address 
DD-DD-DD-DD-DD-DD. There are three possible cases: There is no entry in the table for DD-
DD-DD-DD-DD-DD. In this case, the switch forwards copies of the frame to the output buffers 
preceding all interfaces except for interface x. In other words, if there is no entry for the 
destination address, the switch broadcasts the frame. There is an entry in the table, associating 
DD-DD-DD-DD-DD-DD with interface x. In this case, the frame is coming from a LAN segment 
that contains adapter DD-DD-DD-DD-DD-DD. There being no need to forward the frame to any 
of the other interfaces, the switch performs the filtering function by discarding the frame. There 
is an entry in the table, associating DD-DD-DD-DD-DD-DD with interface In this case, the frame 
needs to be forwarded to the LAN segment attached to interface y. The switch performs its 
forwarding function by putting the frame in an output buffer that precedes interface y. y≠x. Let’s 
walk through these rules for the uppermost switch in Figure 6.15 and its switch table in Figure 
6.22. Suppose that a frame with destination address 62-FE-F7-11-89-A3 arrives at the switch 
from interface 1. The switch examines its table and sees that the destination is on the LAN 
segment connected to interface 1 (that is, Electrical Engineering). This means that the frame 
has already been broadcast on the LAN segment that contains the destination. The switch 
therefore filters (that is, discards) the frame. Now suppose a frame with the same destination 
address arrives from interface 2. The switch again examines its table and sees that the 
destination is in the direction of interface 1; it therefore forwards the frame to the output buffer 
preceding interface 1. It should be clear from this example that as long as the switch table is 
complete and accurate, the switch forwards frames toward destinations without any 
broadcasting. In this sense, a switch is “smarter” than a hub. But how does this switch table get 
configured in the first place? Are there link-layer equivalents to network-layer routing 
protocols? Or must an overworked manager manually configure the switch table? Self-Learning 
A switch has the wonderful property (particularly for the already-overworked network 
administrator) that its table is built automatically, dynamically, and autonomously—without 
any intervention from a network administrator or from a configuration protocol. In other words, 
switches are self-learning. This capability is accomplished as follows: 1. The switch table is 


## Page 9

initially empty. 2. For each incoming frame received on an interface, the switch stores in its 
table (1) the MAC address in the frame’s source address field, (2) the interface from which the 
frame arrived, and (3) the current time. In this manner the switch records in its table the LAN 
segment on which the sender resides. If every host in the LAN eventually sends a frame, then 
every host will eventually get recorded in the table. 3. The switch deletes an address in the table 
if no frames are received with that address as the source address after some period of time (the 
aging time). In this manner, if a PC is replaced by another PC (with a different adapter), the MAC 
address of the original PC will eventually be purged from the switch table. Let’s walk through 
the self-learning property for the uppermost switch in Figure 6.15 and its corresponding switch 
table in Figure 6.22. Suppose at time 9:39 a frame with source address 01-12-23- 34-45-56 
arrives from interface 2. Suppose that this address is not in the switch table. Then the switch 
adds a new entry to the table, as shown in Figure 6.23. Continuing with this same example, 
suppose that the aging time for this switch is 60 minutes, and no frames with source address 
62-FE-F7-11-89-A3 arrive to the switch between 9:32 and 10:32. Then at time 10:32, the switch 
removes this address from its table. Figure 6.23 Switch learns about the location of an adapter 
with address 01-12-23-34-45-56 Switches are plug-and-play devices because they require no 
intervention from a network administrator or user. A network administrator wanting to install a 
switch need do nothing more than connect the LAN segments to the switch interfaces. The 
administrator need not configure the switch tables at the time of installation or when a host is 
removed from one of the LAN segments. Switches are also full-duplex, meaning any switch 
interface can send and receive at the same time. Properties of Link-Layer Switching Having 
described the basic operation of a link-layer switch, let’s now consider their features and 
properties. We can identify several advantages of using switches, rather than broadcast links 
such as buses or hub-based star topologies: Elimination of collisions. In a LAN built from 
switches (and without hubs), there is no wasted bandwidth due to collisions! The switches 
buffer frames and never transmit more than one frame on a segment at any one time. As with a 
router, the maximum aggregate throughput of a switch is the sum of all the switch interface 
rates. Thus, switches provide a significant performance improvement over LANs with broadcast 
links. Heterogeneous links. Because a switch isolates one link from another, the different links 
in the LAN can operate at different speeds and can run over different media. For example, the 
uppermost switch in Figure 6.15 might have three1 Gbps 1000BASE-T copper links, two 100 
Mbps 100BASEFX fiber links, and one 100BASE-T copper link. Thus, a switch is ideal for mixing 
legacy equipment with new equipment. Management. In addition to providing enhanced 
security (see sidebar on Focus on Security), a switch also eases network management. For 
example, if an adapter malfunctions and continually sends Ethernet frames (called a jabbering 
adapter), a switch can detect the problem and internally disconnect the malfunctioning 
adapter. With this feature, the network administrator need not get out of bed and drive back to 
work in order to correct the problem. Similarly, a cable cut disconnects only that host that was 
using the cut cable to connect to the switch. In the days of coaxial cable, many a network 
manager spent hours “walking the line” (or more accurately, “crawling the floor”) to find the 
cable break that brought down the entire network. Switches also gather statistics on bandwidth 
usage, collision rates, and traffic types, and make this information available to the network 
manager. This information can be used to debug and correct problems, and to plan how the 
LAN should evolve in the future. Researchers are exploring adding yet more management 
functionality into Ethernet LANs in prototype deployments [Casado 2007; Koponen 2011]. 
FOCUS ON SECURITY SNIFFING A SWITCHED LAN: SWITCH POISONING When a host is 
connected to a switch, it typically only receives frames that are intended for it. For example, 
consider a switched LAN in Figure 6.17. When host A sends a frame to host B, and there is an 


## Page 10

entry for host B in the switch table, then the switch will forward the frame only to host B. If host 
C happens to be running a sniffer, host C will not be able to sniff this A-to-B frame. Thus, in a 
switched-LAN environment (in contrast to a broadcast link environment such as 802.11 LANs or 
hub–based Ethernet LANs), it is more difficult for an attacker to sniff frames. However, because 
the switch broadcasts frames that have destination addresses that are not in the switch table, 
the sniffer at C can still sniff some frames that are not intended for C. Furthermore, a sniffer will 
be able sniff all Ethernet broadcast frames with broadcast destination address FF–FF–FF–FF–
FF–FF. A well-known attack against a switch, called switch poisoning, is to send tons of packets 
to the switch with many different bogus source MAC addresses, thereby filling the switch table 
with bogus entries and leaving no room for the MAC addresses of the legitimate hosts. This 
causes the switch to broadcast most frames, which can then be picked up by the sniffer 
[Skoudis 2006]. As this attack is rather involved even for a sophisticated attacker, switches are 
significantly less vulnerable to sniffing than are hubs and wireless LANs. Switches Versus 
Routers As we learned in Chapter 4, routers are store-and-forward packet switches that 
forward packets using network-layer addresses. Although a switch is also a store-and-forward 
packet switch, it is fundamentally different from a router in that it forwards packets using MAC 
addresses. Whereas a router is a layer-3 packet switch, a switch is a layer-2 packet switch. 
Recall, however, that we learned in Section 4.4 that modern switches using the “match plus 
action” operation can be used to forward a layer-2 frame based on the frame's destination MAC 
address, as well as a layer-3 datagram using the datagram's destination IP address. Indeed, we 
saw that switches using the OpenFlow standard can perform generalized packet forwarding 
based on any of eleven different frame, datagram, and transportlayer header fields. Even 
though switches and routers are fundamentally different, network administrators must often 
choose between them when installing an interconnection device. For example, for the network 
in Figure 6.15, the network administrator could just as easily have used a router instead of a 
switch to connect the department LANs, servers, and internet gateway router. Indeed, a router 
would permit interdepartmental communication without creating collisions. Given that both 
switches and routers are candidates for interconnection devices, what are the pros and cons of 
the two approaches? Figure 6.24 Packet processing in switches, routers, and hosts First 
consider the pros and cons of switches. As mentioned above, switches are plug-and-play, a 
property that is cherished by all the overworked network administrators of the world. Switches 
can also have relatively high filtering and forwarding rates—as shown in Figure 6.24, switches 
have to process frames only up through layer 2, whereas routers have to process datagrams up 
through layer 3. On the other hand, to prevent the cycling of broadcast frames, the active 
topology of a switched network is restricted to a spanning tree. Also, a large switched network 
would require large ARP tables in the hosts and routers and would generate substantial ARP 
traffic and processing. Furthermore, switches are susceptible to broadcast storms—if one host 
goes haywire and transmits an endless stream of Ethernet broadcast frames, the switches will 
forward all of these frames, causing the entire network to collapse. Now consider the pros and 
cons of routers. Because network addressing is often hierarchical (and not flat, as is MAC 
addressing), packets do not normally cycle through routers even when the network has 
redundant paths. (However, packets can cycle when router tables are misconfigured; but as we 
learned in Chapter 4, IP uses a special datagram header field to limit the cycling.) Thus, packets 
are not restricted to a spanning tree and can use the best path between source and destination. 
Because routers do not have the spanning tree restriction, they have allowed the Internet to be 
built with a rich topology that includes, for example, multiple active links between Europe and 
North America. Another feature of routers is that they provide firewall protection against layer-2 
broadcast storms. Perhaps the most significant drawback of routers, though, is that they are 


## Page 11

not plug-and-play—they and the hosts that connect to them need their IP addresses to be 
configured. Also, routers often have a larger per-packet processing time than switches, 
because they have to process up through the layer-3 fields. Finally, there are two different ways 
to pronounce the word router, either as “rootor” or as “rowter,” and people waste a lot of time 
arguing over the proper pronunciation [Perlman 1999]. Given that both switches and routers 
have their pros and cons (as summarized in Table 6.1), when should an institutional network 
(for example, a university campus Table 6.1 Comparison of the typical features of popular 
interconnection devices Hubs Routers Switches Traffic isolation No Yes Yes Plug and play Yes 
No Yes Optimal routing No Yes No network or a corporate campus network) use switches, and 
when should it use routers? Typically, small networks consisting of a few hundred hosts have a 
few LAN segments. Switches suffice for these small networks, as they localize traffic and 
increase aggregate throughput without requiring any configuration of IP addresses. But larger 
networks consisting of thousands of hosts typically include routers within the network (in 
addition to switches). The routers provide a more robust isolation of traffic, control broadcast 
storms, and use more “intelligent” routes among the hosts in the network. For more discussion 
of the pros and cons of switched versus routed networks, as well as a discussion of how 
switched LAN technology can be extended to accommodate two orders of magnitude more 
hosts than today’s Ethernets, see [Meyers 2004; Kim 2008]. 6.4.4 Virtual Local Area Networks 
(VLANs) In our earlier discussion of Figure 6.15, we noted that modern institutional LANs are 
often configured hierarchically, with each workgroup (department) having its own switched LAN 
connected to the switched LANs of other groups via a switch hierarchy. While such a 
configuration works well in an ideal world, the real world is often far from ideal. Three 
drawbacks can be identified in the configuration in Figure 6.15: Lack of traffic isolation. 
Although the hierarchy localizes group traffic to within a single switch, broadcast traffic (e.g., 
frames carrying ARP and DHCP messages or frames whose destination has not yet been 
learned by a self-learning switch) must still traverse the entire institutional network. Limiting the 
scope of such broadcast traffic would improve LAN performance. Perhaps more importantly, it 
also may be desirable to limit LAN broadcast traffic for security/privacy reasons. For example, if 
one group contains the company’s executive management team and another group contains 
disgruntled employees running Wireshark packet sniffers, the network manager may well prefer 
that the executives’ traffic never even reaches employee hosts. This type of isolation could be 
provided by replacing the center switch in Figure 6.15 with a router. We’ll see shortly that this 
isolation also can be achieved via a switched (layer 2) solution. Inefficient use of switches. If 
instead of three groups, the institution had 10 groups, then 10 firstlevel switches would be 
required. If each group were small, say less than 10 people, then a single 96-port switch would 
likely be large enough to accommodate everyone, but this single switch would not provide 
traffic isolation. Managing users. If an employee moves between groups, the physical cabling 
must be changed to connect the employee to a different switch in Figure 6.15. Employees 
belonging to two groups make the problem even harder. Fortunately, each of these difficulties 
can be handled by a switch that supports virtual local area networks (VLANs). As the name 
suggests, a switch that supports VLANs allows multiple virtual local area networks to be 
defined over a single physical local area network infrastructure. Hosts within a VLAN 
communicate with each other as if they (and no other hosts) were connected to the switch. In a 
port-based VLAN, the switch’s ports (interfaces) are divided into groups by the network 
manager. Each group constitutes a VLAN, with the ports in each VLAN forming a broadcast 
domain (i.e., broadcast traffic from one port can only reach other ports in the group). Figure 
6.25 shows a single switch with 16 ports. Ports 2 to 8 belong to the EE VLAN, while ports 9 to 15 
belong to the CS VLAN (ports 1 and 16 are unassigned). This VLAN solves all of the difficulties 


## Page 12

noted above—EE and CS VLAN frames are isolated from each other, the two switches in Figure 
6.15 have been replaced by a single switch, and if the user at switch port 8 joins the CS 
Department, the network operator simply reconfigures the VLAN software so that port 8 is now 
associated with the CS VLAN. One can easily imagine how the VLAN switch is configured and 
operates—the network manager declares a port to belong Figure 6.25 A single switch with two 
configured VLANs to a given VLAN (with undeclared ports belonging to a default VLAN) using 
switch management software, a table of port-to-VLAN mappings is maintained within the 
switch; and switch hardware only delivers frames between ports belonging to the same VLAN. 
But by completely isolating the two VLANs, we have introduced a new difficulty! How can traffic 
from the EE Department be sent to the CS Department? One way to handle this would be to 
connect a VLAN switch port (e.g., port 1 in Figure 6.25) to an external router and configure that 
port to belong both the EE and CS VLANs. In this case, even though the EE and CS departments 
share the same physical switch, the logical configuration would look as if the EE and CS 
departments had separate switches connected via a router. An IP datagram going from the EE 
to the CS department would first cross the EE VLAN to reach the router and then be forwarded 
by the router back over the CS VLAN to the CS host. Fortunately, switch vendors make such 
configurations easy for the network manager by building a single device that contains both a 
VLAN switch and a router, so a separate external router is not needed. A homework problem at 
the end of the chapter explores this scenario in more detail. Returning again to Figure 6.15, let’s 
now suppose that rather than having a separate Computer Engineering department, some EE 
and CS faculty are housed in a separate building, where (of course!) they need network access, 
and (of course!) they’d like to be part of their department’s VLAN. Figure 6.26 shows a second 8-
port switch, where the switch ports have been defined as belonging to the EE or the CS VLAN, 
as needed. But how should these two switches be interconnected? One easy solution would be 
to define a port belonging to the CS VLAN on each switch (similarly for the EE VLAN) and to 
connect these ports to each other, as shown in Figure 6.26(a). This solution doesn’t scale, 
however, since N VLANS would require N ports on each switch simply to interconnect the two 
switches. A more scalable approach to interconnecting VLAN switches is known as VLAN 
trunking. In the VLAN trunking approach shown in Figure 6.26(b), a special port on each switch 
(port 16 on the left switch and port 1 on the right switch) is configured as a trunk port to 
interconnect the two VLAN switches. The trunk port belongs to all VLANs, and frames sent to 
any VLAN are forwarded over the trunk link to the other switch. But this raises yet another 
question: How does a switch know that a frame arriving on a trunk port belongs to a particular 
VLAN? The IEEE has defined an extended Ethernet frame format, 802.1Q, for frames crossing a 
VLAN trunk. As shown in Figure 6.27, the 802.1Q frame consists of the standard Ethernet frame 
with a four-byte VLAN tag added into the header that carries the identity of the VLAN to which 
the frame belongs. The VLAN tag is added into a frame by the switch at the sending side of a 
VLAN trunk, parsed, and removed by the switch at the receiving side of the trunk. The VLAN tag 
itself consists of a 2-byte Tag Protocol Identifier (TPID) field (with a fixed hexadecimal value of 
81-00), a 2- byte Tag Control Information field that contains a 12-bit VLAN identifier field, and a 
3-bit priority field that is similar in intent to the IP datagram TOS field. Figure 6.26 Connecting 
two VLAN switches with two VLANs: (a) two cables (b) trunked Figure 6.27 Original Ethernet 
frame (top), 802.1Q-tagged Ethernet VLAN frame (below) In this discussion, we’ve only briefly 
touched on VLANs and have focused on port-based VLANs. We should also mention that 
VLANs can be defined in several other ways. In MAC-based VLANs, the network manager 
specifies the set of MAC addresses that belong to each VLAN; whenever a device attaches to a 
port, the port is connected into the appropriate VLAN based on the MAC address of the device. 
VLANs can also be defined based on network-layer protocols (e.g., IPv4, IPv6, or Appletalk) and 


## Page 13

other criteria. It is also possible for VLANs to be extended across IP routers, allowing islands of 
LANs to be connected together to form a single VLAN that could span the globe [Yu 2011]. See 
the 802.1Q standard [IEEE 802.1q 2005] for more details. 6.5 Link Virtualization: A Network as a 
Link Layer Because this chapter concerns link-layer protocols, and given that we’re now nearing 
the chapter’s end, let’s reflect on how our understanding of the term link has evolved. We 
began this chapter by viewing the link as a physical wire connecting two communicating hosts. 
In studying multiple access protocols, we saw that multiple hosts could be connected by a 
shared wire and that the “wire” connecting the hosts could be radio spectra or other media. 
This led us to consider the link a bit more abstractly as a channel, rather than as a wire. In our 
study of Ethernet LANs (Figure 6.15) we saw that the interconnecting media could actually be a 
rather complex switched infrastructure. Throughout this evolution, however, the hosts 
themselves maintained the view that the interconnecting medium was simply a link-layer 
channel connecting two or more hosts. We saw, for example, that an Ethernet host can be 
blissfully unaware of whether it is connected to other LAN hosts by a single short LAN segment 
(Figure 6.17) or by a geographically dispersed switched LAN (Figure 6.15) or by a VLAN (Figure 
6.26). In the case of a dialup modem connection between two hosts, the link connecting the 
two hosts is actually the telephone network—a logically separate, global telecommunications 
network with its own switches, links, and protocol stacks for data transfer and signaling. From 
the Internet link-layer point of view, however, the dial-up connection through the telephone 
network is viewed as a simple “wire.” In this sense, the Internet virtualizes the telephone 
network, viewing the telephone network as a link-layer technology providing link-layer 
connectivity between two Internet hosts. You may recall from our discussion of overlay 
networks in Chapter 2 that an overlay network similarly views the Internet as a means for 
providing connectivity between overlay nodes, seeking to overlay the Internet in the same way 
that the Internet overlays the telephone network. In this section, we’ll consider Multiprotocol 
Label Switching (MPLS) networks. Unlike the circuit-switched telephone network, MPLS is a 
packet-switched, virtual-circuit network in its own right. It has its own packet formats and 
forwarding behaviors. Thus, from a pedagogical viewpoint, a discussion of MPLS fits well into a 
study of either the network layer or the link layer. From an Internet viewpoint, however, we can 
consider MPLS, like the telephone network and switched-Ethernets, as a link-layer technology 
that serves to interconnect IP devices. Thus, we’ll consider MPLS in our discussion of the link 
layer. Framerelay and ATM networks can also be used to interconnect IP devices, though they 
represent a slightly older (but still deployed) technology and will not be covered here; see the 
very readable book [Goralski 1999] for details. Our treatment of MPLS will be necessarily brief, 
as entire books could be (and have been) written on these networks. We recommend [Davie 
2000] for details on MPLS. We’ll focus here primarily on how MPLS servers interconnect to IP 
devices, although we’ll dive a bit deeper into the underlying technologies as well. 6.5.1 
Multiprotocol Label Switching (MPLS) Multiprotocol Label Switching (MPLS) evolved from a 
number of industry efforts in the mid-to-late 1990s to improve the forwarding speed of IP 
routers by adopting a key concept from the world of virtual-circuit networks: a fixed-length 
label. The goal was not to abandon the destination-based IP datagramforwarding infrastructure 
for one based on fixed-length labels and virtual circuits, but to augment it by selectively labeling 
datagrams and allowing routers to forward datagrams based on fixed-length labels (rather than 
destination IP addresses) when possible. Importantly, these techniques work hand-in-hand 
with IP, using IP addressing and routing. The IETF unified these efforts in the MPLS protocol 
[RFC 3031, RFC 3032], effectively blending VC techniques into a routed datagram network. 
Let’s begin our study of MPLS by considering the format of a link-layer frame that is handled by 
an MPLS-capable router. Figure 6.28 shows that a link-layer frame transmitted between MPLS-


## Page 14

capable devices has a small MPLS header added between the layer-2 (e.g., Ethernet) header 
and layer-3 (i.e., IP) header. RFC 3032 defines the format of the MPLS header for such links; 
headers are defined for ATM and frame-relayed networks as well in other RFCs. Among the 
fields in the MPLS Figure 6.28 MPLS header: Located between link- and network-layer headers 
header are the label, 3 bits reserved for experimental use, a single S bit, which is used to 
indicate the end of a series of “stacked” MPLS headers (an advanced topic that we’ll not cover 
here), and a time-tolive field. It’s immediately evident from Figure 6.28 that an MPLS-enhanced 
frame can only be sent between routers that are both MPLS capable (since a non-MPLS-
capable router would be quite confused when it found an MPLS header where it had expected 
to find the IP header!). An MPLS-capable router is often referred to as a label-switched router, 
since it forwards an MPLS frame by looking up the MPLS label in its forwarding table and then 
immediately passing the datagram to the appropriate output interface. Thus, the MPLS-capable 
router need not extract the destination IP address and perform a lookup of the longest prefix 
match in the forwarding table. But how does a router know if its neighbor is indeed MPLS 
capable, and how does a router know what label to associate with the given IP destination? To 
answer these questions, we’ll need to take a look at the interaction among a group of MPLS-
capable routers. In the example in Figure 6.29, routers R1 through R4 are MPLS capable. R5 and 
R6 are standard IP routers. R1 has advertised to R2 and R3 that it (R1) can route to destination 
A, and that a received frame with MPLS label 6 will be forwarded to destination A. Router R3 has 
advertised to router R4 that it can route to destinations A and D, and that incoming frames with 
MPLS labels 10 and 12, respectively, will be switched toward those destinations. Router R2 has 
also advertised to router R4 that it (R2) can reach destination A, and that a received frame with 
MPLS label 8 will be switched toward A. Note that router R4 is now in the interesting position of 
having Figure 6.29 MPLS-enhanced forwarding two MPLS paths to reach A: via interface 0 with 
outbound MPLS label 10, and via interface 1 with an MPLS label of 8. The broad picture painted 
in Figure 6.29 is that IP devices R5, R6, A, and D are connected together via an MPLS 
infrastructure (MPLS-capable routers R1, R2, R3, and R4) in much the same way that a switched 
LAN or an ATM network can connect together IP devices. And like a switched LAN or ATM 
network, the MPLS-capable routers R1 through R4 do so without ever touching the IP header of 
a packet. In our discussion above, we’ve not specified the specific protocol used to distribute 
labels among the MPLS-capable routers, as the details of this signaling are well beyond the 
scope of this book. We note, however, that the IETF working group on MPLS has specified in 
[RFC 3468] that an extension of the RSVP protocol, known as RSVP-TE [RFC 3209], will be the 
focus of its efforts for MPLS signaling. We’ve also not discussed how MPLS actually computes 
the paths for packets among MPLS capable routers, nor how it gathers link-state information 
(e.g., amount of link bandwidth unreserved by MPLS) to use in these path computations. 
Existing link-state routing algorithms (e.g., OSPF) have been extended to flood this information 
to MPLS-capable routers. Interestingly, the actual path computation algorithms are not 
standardized, and are currently vendor-specific. Thus far, the emphasis of our discussion of 
MPLS has been on the fact that MPLS performs switching based on labels, without needing to 
consider the IP address of a packet. The true advantages of MPLS and the reason for current 
interest in MPLS, however, lie not in the potential increases in switching speeds, but rather in 
the new traffic management capabilities that MPLS enables. As noted above, R4 has two MPLS 
paths to A. If forwarding were performed up at the IP layer on the basis of IP address, the IP 
routing protocols we studied in Chapter 5 would specify only a single, least-cost path to A. 
Thus, MPLS provides the ability to forward packets along routes that would not be possible 
using standard IP routing protocols. This is one simple form of traffic engineering using MPLS 
[RFC 3346; RFC 3272; RFC 2702; Xiao 2000], in which a network operator can override normal 


## Page 15

IP routing and force some of the traffic headed toward a given destination along one path, and 
other traffic destined toward the same destination along another path (whether for policy, 
performance, or some other reason). It is also possible to use MPLS for many other purposes as 
well. It can be used to perform fast restoration of MPLS forwarding paths, e.g., to reroute traffic 
over a precomputed failover path in response to link failure [Kar 2000; Huang 2002; RFC 3469]. 
Finally, we note that MPLS can, and has, been used to implement so-called virtual private 
networks (VPNs). In implementing a VPN for a customer, an ISP uses its MPLS-enabled network 
to connect together the customer’s various networks. MPLS can be used to isolate both the 
resources and addressing used by the customer’s VPN from that of other users crossing the 
ISP’s network; see [DeClercq 2002] for details. Our discussion of MPLS has been brief, and we 
encourage you to consult the references we’ve mentioned. We note that with so many possible 
uses for MPLS, it appears that it is rapidly becoming the Swiss Army knife of Internet traffic 
engineering! 6.6 Data Center Networking In recent years, Internet companies such as Google, 
Microsoft, Facebook, and Amazon (as well as their counterparts in Asia and Europe) have built 
massive data centers, each housing tens to hundreds of thousands of hosts, and concurrently 
supporting many distinct cloud applications (e.g., search, e-mail, social networking, and e-
commerce). Each data center has its own data center network that interconnects its hosts with 
each other and interconnects the data center with the Internet. In this section, we provide a 
brief introduction to data center networking for cloud applications. The cost of a large data 
center is huge, exceeding $12 million per month for a 100,000 host data center [Greenberg 
2009a]. Of these costs, about 45 percent can be attributed to the hosts themselves (which 
need to be replaced every 3–4 years); 25 percent to infrastructure, including transformers, 
uninterruptable power supplies (UPS) systems, generators for long-term outages, and cooling 
systems; 15 percent for electric utility costs for the power draw; and 15 percent for networking, 
including network gear (switches, routers and load balancers), external links, and transit traffic 
costs. (In these percentages, costs for equipment are amortized so that a common cost metric 
is applied for one-time purchases and ongoing expenses such as power.) While networking is 
not the largest cost, networking innovation is the key to reducing overall cost and maximizing 
performance [Greenberg 2009a]. The worker bees in a data center are the hosts: They serve 
content (e.g., Web pages and videos), store e-mails and documents, and collectively perform 
massively distributed computations (e.g., distributed index computations for search engines). 
The hosts in data centers, called blades and resembling pizza boxes, are generally commodity 
hosts that include CPU, memory, and disk storage. The hosts are stacked in racks, with each 
rack typically having 20 to 40 blades. At the top of each rack there is a switch, aptly named the 
Top of Rack (TOR) switch, that interconnects the hosts in the rack with each other and with 
other switches in the data center. Specifically, each host in the rack has a network interface 
card that connects to its TOR switch, and each TOR switch has additional ports that can be 
connected to other switches. Today hosts typically have 40 Gbps Ethernet connections to their 
TOR switches [Greenberg 2015]. Each host is also assigned its own data-center-internal IP 
address. The data center network supports two types of traffic: traffic flowing between external 
clients and internal hosts and traffic flowing between internal hosts. To handle flows between 
external clients and internal hosts, the data center network includes one or more border 
routers, connecting the data center network to the public Internet. The data center network 
therefore interconnects the racks with each other and connects the racks to the border routers. 
Figure 6.30 shows an example of a data center network. Data center network design, the art of 
designing the interconnection network and protocols that connect the racks with each other 
and with the border routers, has become an important branch of computer networking research 
in recent years [Al-Fares 2008; Greenberg 2009a; Greenberg 2009b; Mysore 2009; Guo 2009; 


## Page 16

Wang 2010]. Figure 6.30 A data center network with a hierarchical topology Load Balancing A 
cloud data center, such as a Google or Microsoft data center, provides many applications 
concurrently, such as search, e-mail, and video applications. To support requests from external 
clients, each application is associated with a publicly visible IP address to which clients send 
their requests and from which they receive responses. Inside the data center, the external 
requests are first directed to a load balancer whose job it is to distribute requests to the hosts, 
balancing the load across the hosts as a function of their current load. A large data center will 
often have several load balancers, each one devoted to a set of specific cloud applications. 
Such a load balancer is sometimes referred to as a “layer-4 switch” since it makes decisions 
based on the destination port number (layer 4) as well as destination IP address in the packet. 
Upon receiving a request for a particular application, the load balancer forwards it to one of the 
hosts that handles the application. (A host may then invoke the services of other hosts to help 
process the request.) When the host finishes processing the request, it sends its response back 
to the load balancer, which in turn relays the response back to the external client. The load 
balancer not only balances the work load across hosts, but also provides a NAT-like function, 
translating the public external IP address to the internal IP address of the appropriate host, and 
then translating back for packets traveling in the reverse direction back to the clients. This 
prevents clients from contacting hosts directly, which has the security benefit of hiding the 
internal network structure and preventing clients from directly interacting with the hosts. 
Hierarchical Architecture For a small data center housing only a few thousand hosts, a simple 
network consisting of a border router, a load balancer, and a few tens of racks all 
interconnected by a single Ethernet switch could possibly suffice. But to scale to tens to 
hundreds of thousands of hosts, a data center often employs a hierarchy of routers and 
switches, such as the topology shown in Figure 6.30. At the top of the hierarchy, the border 
router connects to access routers (only two are shown in Figure 6.30, but there can be many 
more). Below each access router there are three tiers of switches. Each access router connects 
to a top-tier switch, and each top-tier switch connects to multiple second-tier switches and a 
load balancer. Each second-tier switch in turn connects to multiple racks via the racks’ TOR 
switches (third-tier switches). All links typically use Ethernet for their link-layer and physical-
layer protocols, with a mix of copper and fiber cabling. With such a hierarchical design, it is 
possible to scale a data center to hundreds of thousands of hosts. Because it is critical for a 
cloud application provider to continually provide applications with high availability, data 
centers also include redundant network equipment and redundant links in their designs (not 
shown in Figure 6.30). For example, each TOR switch can connect to two tier-2 switches, and 
each access router, tier-1 switch, and tier-2 switch can be duplicated and integrated into the 
design [Cisco 2012; Greenberg 2009b]. In the hierarchical design in Figure 6.30, observe that 
the hosts below each access router form a single subnet. In order to localize ARP broadcast 
traffic, each of these subnets is further partitioned into smaller VLAN subnets, each comprising 
a few hundred hosts [Greenberg 2009a]. Although the conventional hierarchical architecture 
just described solves the problem of scale, it suffers from limited host-to-host capacity 
[Greenberg 2009b]. To understand this limitation, consider again Figure 6.30, and suppose 
each host connects to its TOR switch with a 1 Gbps link, whereas the links between switches 
are 10 Gbps Ethernet links. Two hosts in the same rack can always communicate at a full 1 
Gbps, limited only by the rate of the hosts’ network interface cards. However, if there are many 
simultaneous flows in the data center network, the maximum rate between two hosts in 
different racks can be much less. To gain insight into this issue, consider a traffic pattern 
consisting of 40 simultaneous flows between 40 pairs of hosts in different racks. Specifically, 
suppose each of 10 hosts in rack 1 in Figure 6.30 sends a flow to a corresponding host in rack 5. 


## Page 17

Similarly, there are ten simultaneous flows between pairs of hosts in racks 2 and 6, ten 
simultaneous flows between racks 3 and 7, and ten simultaneous flows between racks 4 and 8. 
If each flow evenly shares a link’s capacity with other flows traversing that link, then the 40 
flows crossing the 10 Gbps A-to-B link (as well as the 10 Gbps B-to-C link) will each only receive 
10 Gbps/40=250 Mbps, which is significantly less than the 1 Gbps network interface card rate. 
The problem becomes even more acute for flows between hosts that need to travel higher up 
the hierarchy. One possible solution to this limitation is to deploy higher-rate switches and 
routers. But this would significantly increase the cost of the data center, because switches and 
routers with high port speeds are very expensive. Supporting high-bandwidth host-to-host 
communication is important because a key requirement in data centers is flexibility in 
placement of computation and services [Greenberg 2009b; Farrington 2010]. For example, a 
large-scale Internet search engine may run on thousands of hosts spread across multiple racks 
with significant bandwidth requirements between all pairs of hosts. Similarly, a cloud 
computing service such as EC2 may wish to place the multiple virtual machines comprising a 
customer’s service on the physical hosts with the most capacity irrespective of their location in 
the data center. If these physical hosts are spread across multiple racks, network bottlenecks 
as described above may result in poor performance. Trends in Data Center Networking In order 
to reduce the cost of data centers, and at the same time improve their delay and throughput 
performance, Internet cloud giants such as Google, Facebook, Amazon, and Microsoft are 
continually deploying new data center network designs. Although these designs are proprietary, 
many important trends can nevertheless be identified. One such trend is to deploy new 
interconnection architectures and network protocols that overcome the drawbacks of the 
traditional hierarchical designs. One such approach is to replace the hierarchy of switches and 
routers with a fully connected topology [Facebook 2014; Al-Fares 2008; Greenberg 2009b; Guo 
2009], such as the topology shown in Figure 6.31. In this design, each tier-1 switch connects to 
all of the tier-2 switches so that (1) host-to-host traffic never has to rise above the switch tiers, 
and (2) with n tier-1 switches, between any two tier-2 switches there are n disjoint paths. Such a 
design can significantly improve the host-to-host capacity. To see this, consider again our 
example of 40 flows. The topology in Figure 6.31 can handle such a flow pattern since there are 
four distinct paths between the first tier-2 switch and the second tier-2 switch, together 
providing an aggregate capacity of 40 Gbps between the first two tier-2 switches. Such a design 
not only alleviates the host-to-host capacity limitation, but also creates a more flexible 
computation and service environment in which communication between any two racks not 
connected to the same switch is logically equivalent, irrespective of their locations in the data 
center. Another major trend is to employ shipping container–based modular data centers 
(MDCs) [YouTube 2009; Waldrop 2007]. In an MDC, a factory builds, within a Figure 6.31 Highly 
interconnected data network topology standard 12-meter shipping container, a “mini data 
center” and ships the container to the data center location. Each container has up to a few 
thousand hosts, stacked in tens of racks, which are packed closely together. At the data center 
location, multiple containers are interconnected with each other and also with the Internet. 
Once a prefabricated container is deployed at a data center, it is often difficult to service. Thus, 
each container is designed for graceful performance degradation: as components (servers and 
switches) fail over time, the container continues to operate but with degraded performance. 
When many components have failed and performance has dropped below a threshold, the 
entire container is removed and replaced with a fresh one. Building a data center out of 
containers creates new networking challenges. With an MDC, there are two types of networks: 
the container-internal networks within each of the containers and the core network connecting 
each container [Guo 2009; Farrington 2010]. Within each container, at the scale of up to a few 


## Page 18

thousand hosts, it is possible to build a fully connected network (as described above) using 
inexpensive commodity Gigabit Ethernet switches. However, the design of the core network, 
interconnecting hundreds to thousands of containers while providing high host-to-host 
bandwidth across containers for typical workloads, remains a challenging problem. A hybrid 
electrical/optical switch architecture for interconnecting the containers is proposed in 
[Farrington 2010]. When using highly interconnected topologies, one of the major issues is 
designing routing algorithms among the switches. One possibility [Greenberg 2009b] is to use a 
form of random routing. Another possibility [Guo 2009] is to deploy multiple network interface 
cards in each host, connect each host to multiple low-cost commodity switches, and allow the 
hosts themselves to intelligently route traffic among the switches. Variations and extensions of 
these approaches are currently being deployed in contemporary data centers. Another 
important trend is that large cloud providers are increasingly building or customizing just about 
everything that is in their data centers, including network adapters, switches routers, TORs, 
software, and networking protocols [Greenberg 2015, Singh 2015]. Another trend, pioneered by 
Amazon, is to improve reliability with “availability zones,” which essentially replicate distinct 
data centers in different nearby buildings. By having the buildings nearby (a few kilometers 
apart), transactional data can be synchronized across the data centers in the same availability 
zone while providing fault tolerance [Amazon 2014]. Many more innovations in data center 
design are likely to continue to come; interested readers are encouraged to see the recent 
papers and videos on data center network design. 6.7 Retrospective: A Day in the Life of a Web 
Page Request Now that we’ve covered the link layer in this chapter, and the network, transport 
and application layers in earlier chapters, our journey down the protocol stack is complete! In 
the very beginning of this book (Section 1.1), we wrote “much of this book is concerned with 
computer network protocols,” and in the first five chapters, we’ve certainly seen that this is 
indeed the case! Before heading into the topical chapters in second part of this book, we’d like 
to wrap up our journey down the protocol stack by taking an integrated, holistic view of the 
protocols we’ve learned about so far. One way then to take this “big picture” view is to identify 
the many (many!) protocols that are involved in satisfying even the simplest request: 
downloading a Web page. Figure 6.32 illustrates our setting: a student, Bob, connects a laptop 
to his school’s Ethernet switch and downloads a Web page (say the home page of 
www.google.com). As we now know, there’s a lot going on “under the hood” to satisfy this 
seemingly simple request. A Wireshark lab at the end of this chapter examines trace files 
containing a number of the packets involved in similar scenarios in more detail. 6.7.1 Getting 
Started: DHCP, UDP, IP, and Ethernet Let’s suppose that Bob boots up his laptop and then 
connects it to an Ethernet cable connected to the school’s Ethernet switch, which in turn is 
connected to the school’s router, as shown in Figure 6.32. The school’s router is connected to 
an ISP, in this example, comcast.net. In this example, comcast.net is providing the DNS service 
for the school; thus, the DNS server resides in the Comcast network rather than the school 
network. We’ll assume that the DHCP server is running within the router, as is often the case. 
When Bob first connects his laptop to the network, he can’t do anything (e.g., download a Web 
page) without an IP address. Thus, the first network-related Figure 6.32 A day in the life of a Web 
page request: Network setting and actions action taken by Bob’s laptop is to run the DHCP 
protocol to obtain an IP address, as well as other information, from the local DHCP server: 1. 
The operating system on Bob’s laptop creates a DHCP request message (Section 4.3.3) and 
puts this message within a UDP segment (Section 3.3) with destination port 67 (DHCP server) 
and source port 68 (DHCP client). The UDP segment is then placed within an IP datagram 
(Section 4.3.1) with a broadcast IP destination address (255.255.255.255) and a source IP 
address of 0.0.0.0, since Bob’s laptop doesn’t yet have an IP address. 2. The IP datagram 


## Page 19

containing the DHCP request message is then placed within an Ethernet frame (Section 6.4.2). 
The Ethernet frame has a destination MAC addresses of FF:FF:FF:FF:FF:FF so that the frame will 
be broadcast to all devices connected to the switch (hopefully including a DHCP server); the 
frame’s source MAC address is that of Bob’s laptop, 00:16:D3:23:68:8A. 3. The broadcast 
Ethernet frame containing the DHCP request is the first frame sent by Bob’s laptop to the 
Ethernet switch. The switch broadcasts the incoming frame on all outgoing ports, including the 
port connected to the router. 4. The router receives the broadcast Ethernet frame containing 
the DHCP request on its interface with MAC address 00:22:6B:45:1F:1B and the IP datagram is 
extracted from the Ethernet frame. The datagram’s broadcast IP destination address indicates 
that this IP datagram should be processed by upper layer protocols at this node, so the 
datagram’s payload (a UDP segment) is thus demultiplexed (Section 3.2) up to UDP, and the 
DHCP request message is extracted from the UDP segment. The DHCP server now has the 
DHCP request message. 5. Let’s suppose that the DHCP server running within the router can 
allocate IP addresses in the CIDR (Section 4.3.3) block 68.85.2.0/24. In this example, all IP 
addresses used within the school are thus within Comcast’s address block. Let’s suppose the 
DHCP server allocates address 68.85.2.101 to Bob’s laptop. The DHCP server creates a DHCP 
ACK message (Section 4.3.3) containing this IP address, as well as the IP address of the DNS 
server (68.87.71.226), the IP address for the default gateway router (68.85.2.1), and the subnet 
block (68.85.2.0/24) (equivalently, the “network mask”). The DHCP message is put inside a UDP 
segment, which is put inside an IP datagram, which is put inside an Ethernet frame. The 
Ethernet frame has a source MAC address of the router’s interface to the home network 
(00:22:6B:45:1F:1B) and a destination MAC address of Bob’s laptop (00:16:D3:23:68:8A). 6. The 
Ethernet frame containing the DHCP ACK is sent (unicast) by the router to the switch. Because 
the switch is self-learning (Section 6.4.3) and previously received an Ethernet frame (containing 
the DHCP request) from Bob’s laptop, the switch knows to forward a frame addressed to 
00:16:D3:23:68:8A only to the output port leading to Bob’s laptop. 7. Bob’s laptop receives the 
Ethernet frame containing the DHCP ACK, extracts the IP datagram from the Ethernet frame, 
extracts the UDP segment from the IP datagram, and extracts the DHCP ACK message from the 
UDP segment. Bob’s DHCP client then records its IP address and the IP address of its DNS 
server. It also installs the address of the default gateway into its IP forwarding table (Section 
4.1). Bob’s laptop will send all datagrams with destination address outside of its subnet 
68.85.2.0/24 to the default gateway. At this point, Bob’s laptop has initialized its networking 
components and is ready to begin processing the Web page fetch. (Note that only the last two 
DHCP steps of the four presented in Chapter 4 are actually necessary.) 6.7.2 Still Getting 
Started: DNS and ARP When Bob types the URL for www.google.com into his Web browser, he 
begins the long chain of events that will eventually result in Google’s home page being 
displayed by his Web browser. Bob’s Web browser begins the process by creating a TCP socket 
(Section 2.7) that will be used to send the HTTP request (Section 2.2) to www.google.com. In 
order to create the socket, Bob’s laptop will need to know the IP address of www.google.com. 
We learned in Section 2.5, that the DNS protocol is used to provide this name-to-IP-address 
translation service. 8. The operating system on Bob’s laptop thus creates a DNS query message 
(Section 2.5.3), putting the string “www.google.com” in the question section of the DNS 
message. This DNS message is then placed within a UDP segment with a destination port of 53 
(DNS server). The UDP segment is then placed within an IP datagram with an IP destination 
address of 68.87.71.226 (the address of the DNS server returned in the DHCP ACK in step 5) 
and a source IP address of 68.85.2.101. 9. Bob’s laptop then places the datagram containing 
the DNS query message in an Ethernet frame. This frame will be sent (addressed, at the link 
layer) to the gateway router in Bob’s school’s network. However, even though Bob’s laptop 


## Page 20

knows the IP address of the school’s gateway router (68.85.2.1) via the DHCP ACK message in 
step 5 above, it doesn’t know the gateway router’s MAC address. In order to obtain the MAC 
address of the gateway router, Bob’s laptop will need to use the ARP protocol (Section 6.4.1). 
10. Bob’s laptop creates an ARP query message with a target IP address of 68.85.2.1 (the 
default gateway), places the ARP message within an Ethernet frame with a broadcast 
destination address (FF:FF:FF:FF:FF:FF) and sends the Ethernet frame to the switch, which 
delivers the frame to all connected devices, including the gateway router. 11. The gateway 
router receives the frame containing the ARP query message on the interface to the school 
network, and finds that the target IP address of 68.85.2.1 in the ARP message matches the IP 
address of its interface. The gateway router thus prepares an ARP reply, indicating that its MAC 
address of 00:22:6B:45:1F:1B corresponds to IP address 68.85.2.1. It places the ARP reply 
message in an Ethernet frame, with a destination address of 00:16:D3:23:68:8A (Bob’s laptop) 
and sends the frame to the switch, which delivers the frame to Bob’s laptop. 12. Bob’s laptop 
receives the frame containing the ARP reply message and extracts the MAC address of the 
gateway router (00:22:6B:45:1F:1B) from the ARP reply message. 13. Bob’s laptop can now 
(finally!) address the Ethernet frame containing the DNS query to the gateway router’s MAC 
address. Note that the IP datagram in this frame has an IP destination address of 68.87.71.226 
(the DNS server), while the frame has a destination address of 00:22:6B:45:1F:1B (the gateway 
router). Bob’s laptop sends this frame to the switch, which delivers the frame to the gateway 
router. 6.7.3 Still Getting Started: Intra-Domain Routing to the DNS Server 14. The gateway 
router receives the frame and extracts the IP datagram containing the DNS query. The router 
looks up the destination address of this datagram (68.87.71.226) and determines from its 
forwarding table that the datagram should be sent to the leftmost router in the Comcast 
network in Figure 6.32. The IP datagram is placed inside a link-layer frame appropriate for the 
link connecting the school’s router to the leftmost Comcast router and the frame is sent over 
this link. 15. The leftmost router in the Comcast network receives the frame, extracts the IP 
datagram, examines the datagram’s destination address (68.87.71.226) and determines the 
outgoing interface on which to forward the datagram toward the DNS server from its forwarding 
table, which has been filled in by Comcast’s intra-domain protocol (such as RIP, OSPF or IS-IS, 
Section 5.3) as well as the Internet’s inter-domain protocol, BGP (Section 5.4). 16. Eventually 
the IP datagram containing the DNS query arrives at the DNS server. The DNS server extracts 
the DNS query message, looks up the name www.google.com in its DNS database (Section 2.5), 
and finds the DNS resource record that contains the IP address (64.233.169.105) for 
www.google.com. (assuming that it is currently cached in the DNS server). Recall that this 
cached data originated in the authoritative DNS server (Section 2.5.2) for googlecom. The DNS 
server forms a DNS reply message containing this hostname-to-IPaddress mapping, and places 
the DNS reply message in a UDP segment, and the segment within an IP datagram addressed to 
Bob’s laptop (68.85.2.101). This datagram will be forwarded back through the Comcast network 
to the school’s router and from there, via the Ethernet switch to Bob’s laptop. 17. Bob’s laptop 
extracts the IP address of the server www.google.com from the DNS message. Finally, after a 
lot of work, Bob’s laptop is now ready to contact the www.google.com server! 6.7.4 Web Client-
Server Interaction: TCP and HTTP 18. Now that Bob’s laptop has the IP address of 
www.google.com, it can create the TCP socket (Section 2.7) that will be used to send the HTTP 
GET message (Section 2.2.3) to www.google.com. When Bob creates the TCP socket, the TCP in 
Bob’s laptop must first perform a three-way handshake (Section 3.5.6) with the TCP in 
www.google.com. Bob’s laptop thus first creates a TCP SYN segment with destination port 80 
(for HTTP), places the TCP segment inside an IP datagram with a destination IP address of 
64.233.169.105 (www.google.com), places the datagram inside a frame with a destination MAC 


