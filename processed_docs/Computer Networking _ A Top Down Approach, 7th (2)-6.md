# Computer Networking _ A Top Down Approach, 7th (2)-6


## Page 1

plane role of each router is to forward datagrams from its input links to its output links; the 
primary role of the network control plane is to coordinate these local, per-router forwarding 
actions so that datagrams are ultimately transferred end-to-end, along paths of routers 
between source and destination hosts. Note that the routers in Figure 4.1 are shown with a 
truncated protocol stack, that is, with no upper layers above the network layer, because routers 
do not run application- and transportlayer protocols such as those we examined in Chapters 2 
and 3. 4.1.1 Forwarding and Routing: The Data and Control Planes The primary role of the 
network layer is deceptively simple—to move packets from a sending host to a receiving host. 
To do so, two important network-layer functions can be identified: Forwarding. When a packet 
arrives at a router’s input link, the router must move the packet to the appropriate output link. 
For example, a packet arriving from Host H1 to Router R1 in Figure 4.1 must be forwarded to the 
next router on a path to H2. As we will see, forwarding is but one function (albeit the most Figure 
4.1 The network layer common and important one!) implemented in the data plane. In the more 
general case, which we’ll cover in Section 4.4, a packet might also be blocked from exiting a 
router (e.g., if the packet originated at a known malicious sending host, or if the packet were 
destined to a forbidden destination host), or might be duplicated and sent over multiple 
outgoing links. Routing. The network layer must determine the route or path taken by packets as 
they flow from a sender to a receiver. The algorithms that calculate these paths are referred to 
as routing algorithms. A routing algorithm would determine, for example, the path along which 
packets flow from H1 to H2 in Figure 4.1. Routing is implemented in the control plane of the 
network layer. The terms forwarding and routing are often used interchangeably by authors 
discussing the network layer. We’ll use these terms much more precisely in this book. 
Forwarding refers to the router-local action of transferring a packet from an input link interface 
to the appropriate output link interface. Forwarding takes place at very short timescales 
(typically a few nanoseconds), and thus is typically implemented in hardware. Routing refers to 
the network-wide process that determines the end-to-end paths that packets take from source 
to destination. Routing takes place on much longer timescales (typically seconds), and as we 
will see is often implemented in software. Using our driving analogy, consider the trip from 
Pennsylvania to Florida undertaken by our traveler back in Section 1.3.1. During this trip, our 
driver passes through many interchanges en route to Florida. We can think of forwarding as the 
process of getting through a single interchange: A car enters the interchange from one road and 
determines which road it should take to leave the interchange. We can think of routing as the 
process of planning the trip from Pennsylvania to Florida: Before embarking on the trip, the 
driver has consulted a map and chosen one of many paths possible, with each path consisting 
of a series of road segments connected at interchanges. A key element in every network router 
is its forwarding table. A router forwards a packet by examining the value of one or more fields in 
the arriving packet’s header, and then using these header values to index into its forwarding 
table. The value stored in the forwarding table entry for those values indicates the outgoing link 
interface at that router to which that packet is to be forwarded. For example, in Figure 4.2, a 
packet with header field value of 0110 arrives to a router. The router indexes into its forwarding 
table and determines that the output link interface for this packet is interface 2. The router then 
internally forwards the packet to interface 2. In Section 4.2, we’ll look inside a router and 
examine the forwarding function in much greater detail. Forwarding is the key function 
performed by the data-plane functionality of the network layer. Control Plane: The Traditional 
Approach But now you are undoubtedly wondering how a router’s forwarding tables are 
configured in the first place. This is a crucial issue, one that exposes the important interplay 
between forwarding (in data plane) and routing (in control plane). As shown Figure 4.2 Routing 
algorithms determine values in forward tables in Figure 4.2, the routing algorithm determines 


## Page 2

the contents of the routers’ forwarding tables. In this example, a routing algorithm runs in each 
and every router and both forwarding and routing functions are contained within a router. As 
we’ll see in Sections 5.3 and 5.4, the routing algorithm function in one router communicates 
with the routing algorithm function in other routers to compute the values for its forwarding 
table. How is this communication performed? By exchanging routing messages containing 
routing information according to a routing protocol! We’ll cover routing algorithms and 
protocols in Sections 5.2 through 5.4. The distinct and different purposes of the forwarding and 
routing functions can be further illustrated by considering the hypothetical (and unrealistic, but 
technically feasible) case of a network in which all forwarding tables are configured directly by 
human network operators physically present at the routers. In this case, no routing protocols 
would be required! Of course, the human operators would need to interact with each other to 
ensure that the forwarding tables were configured in such a way that packets reached their 
intended destinations. It’s also likely that human configuration would be more error-prone and 
much slower to respond to changes in the network topology than a routing protocol. We’re thus 
fortunate that all networks have both a forwarding and a routing function! Control Plane: The 
SDN Approach The approach to implementing routing functionality shown in Figure 4.2—with 
each router having a routing component that communicates with the routing component of 
other routers—has been the traditional approach adopted by routing vendors in their products, 
at least until recently. Our observation that humans could manually configure forwarding tables 
does suggest, however, that there may be other ways for control-plane functionality to 
determine the contents of the data-plane forwarding tables. Figure 4.3 shows an alternate 
approach in which a physically separate (from the routers), remote controller computes and 
distributes the forwarding tables to be used by each and every router. Note that the data plane 
components of Figures 4.2 and 4.3 are identical. In Figure 4.3, however, control-plane routing 
functionality is separated Figure 4.3 A remote controller determines and distributes values in 
forwarding tables from the physical router—the routing device performs forwarding only, while 
the remote controller computes and distributes forwarding tables. The remote controller might 
be implemented in a remote data center with high reliability and redundancy, and might be 
managed by the ISP or some third party. How might the routers and the remote controller 
communicate? By exchanging messages containing forwarding tables and other pieces of 
routing information. The control-plane approach shown in Figure 4.3 is at the heart of software-
defined networking (SDN), where the network is “software-defined” because the controller that 
computes forwarding tables and interacts with routers is implemented in software. 
Increasingly, these software implementations are also open, i.e., similar to Linux OS code, the 
code is publically available, allowing ISPs (and networking researchers and students!) to 
innovate and propose changes to the software that controls network-layer functionality. We will 
cover the SDN control plane in Section 5.5. 4.1.2 Network Service Model Before delving into the 
network layer’s data plane, let’s wrap up our introduction by taking the broader view and 
consider the different types of service that might be offered by the network layer. When the 
transport layer at a sending host transmits a packet into the network (that is, passes it down to 
the network layer at the sending host), can the transport layer rely on the network layer to 
deliver the packet to the destination? When multiple packets are sent, will they be delivered to 
the transport layer in the receiving host in the order in which they were sent? Will the amount of 
time between the sending of two sequential packet transmissions be the same as the amount 
of time between their reception? Will the network provide any feedback about congestion in the 
network? The answers to these questions and others are determined by the service model 
provided by the network layer. The network service model defines the characteristics of end-to-
end delivery of packets between sending and receiving hosts. Let’s now consider some 


## Page 3

possible services that the network layer could provide. These services could include: 
Guaranteed delivery. This service guarantees that a packet sent by a source host will eventually 
arrive at the destination host. Guaranteed delivery with bounded delay. This service not only 
guarantees delivery of the packet, but delivery within a specified host-to-host delay bound (for 
example, within 100 msec). In-order packet delivery. This service guarantees that packets arrive 
at the destination in the order that they were sent. Guaranteed minimal bandwidth. This 
network-layer service emulates the behavior of a transmission link of a specified bit rate (for 
example, 1 Mbps) between sending and receiving hosts. As long as the sending host transmits 
bits (as part of packets) at a rate below the specified bit rate, then all packets are eventually 
delivered to the destination host. Security. The network layer could encrypt all datagrams at the 
source and decrypt them at the destination, thereby providing confidentiality to all transport-
layer segments. This is only a partial list of services that a network layer could provide—there 
are countless variations possible. The Internet’s network layer provides a single service, known 
as best-effort service. With best-effort service, packets are neither guaranteed to be received in 
the order in which they were sent, nor is their eventual delivery even guaranteed. There is no 
guarantee on the end-to-end delay nor is there a minimal bandwidth guarantee. It might appear 
that best-effort service is a euphemism for no service at all—a network that delivered no 
packets to the destination would satisfy the definition of best-effort delivery service! Other 
network architectures have defined and implemented service models that go beyond the 
Internet’s best-effort service. For example, the ATM network architecture [MFA Forum 2016, 
Black 1995] provides for guaranteed in-order delay, bounded delay, and guaranteed minimal 
bandwidth. There have also been proposed service model extensions to the Internet 
architecture; for example, the Intserv architecture [RFC 1633] aims to provide end-end delay 
guarantees and congestion-free communication. Interestingly, in spite of these well-developed 
alternatives, the Internet’s basic best-effort service model combined with adequate bandwidth 
provisioning have arguably proven to be more than “good enough” to enable an amazing range 
of applications, including streaming video services such as Netflix and voice-and-video-over-IP, 
real-time conferencing applications such as Skype and Facetime. An Overview of Chapter 4 
Having now provided an overview of the network layer, we’ll cover the data-plane component of 
the network layer in the following sections in this chapter. In Section 4.2, we’ll dive down into 
the internal hardware operations of a router, including input and output packet processing, the 
router’s internal switching mechanism, and packet queueing and scheduling. In Section 4.3, 
we’ll take a look at traditional IP forwarding, in which packets are forwarded to output ports 
based on their destination IP addresses. We’ll encounter IP addressing, the celebrated IPv4 and 
IPv6 protocols and more. In Section 4.4, we’ll cover more generalized forwarding, where 
packets may be forwarded to output ports based on a large number of header values (i.e., not 
only based on destination IP address). Packets may be blocked or duplicated at the router, or 
may have certain header field values rewritten—all under software control. This more 
generalized form of packet forwarding is a key component of a modern network data plane, 
including the data plane in software-defined networks (SDN). We mention here in passing that 
the terms forwarding and switching are often used interchangeably by computer-networking 
researchers and practitioners; we’ll use both terms interchangeably in this textbook as well. 
While we’re on the topic of terminology, it’s also worth mentioning two other terms that are 
often used interchangeably, but that we will use more carefully. We’ll reserve the term packet 
switch to mean a general packet-switching device that transfers a packet from input link 
interface to output link interface, according to values in a packet’s header fields. Some packet 
switches, called link-layer switches (examined in Chapter 6), base their forwarding decision on 
values in the fields of the linklayer frame; switches are thus referred to as link-layer (layer 2) 


## Page 4

devices. Other packet switches, called routers, base their forwarding decision on header field 
values in the network-layer datagram. Routers are thus network-layer (layer 3) devices. (To fully 
appreciate this important distinction, you might want to review Section 1.5.2, where we discuss 
network-layer datagrams and link-layer frames and their relationship.) Since our focus in this 
chapter is on the network layer, we’ll mostly use the term router in place of packet switch. 4.2 
What’s Inside a Router? Now that we’ve overviewed the data and control planes within the 
network layer, the important distinction between forwarding and routing, and the services and 
functions of the network layer, let’s turn our attention to its forwarding function—the actual 
transfer of packets from a router’s incoming links to the appropriate outgoing links at that 
router. A high-level view of a generic router architecture is shown in Figure 4.4. Four router 
components can be identified: Figure 4.4 Router architecture Input ports. An input port 
performs several key functions. It performs the physical layer function of terminating an 
incoming physical link at a router; this is shown in the leftmost box of an input port and the 
rightmost box of an output port in Figure 4.4. An input port also performs link-layer functions 
needed to interoperate with the link layer at the other side of the incoming link; this is 
represented by the middle boxes in the input and output ports. Perhaps most crucially, a 
lookup function is also performed at the input port; this will occur in the rightmost box of the 
input port. It is here that the forwarding table is consulted to determine the router output port to 
which an arriving packet will be forwarded via the switching fabric. Control packets (for 
example, packets carrying routing protocol information) are forwarded from an input port to the 
routing processor. Note that the term “port” here —referring to the physical input and output 
router interfaces—is distinctly different from the software ports associated with network 
applications and sockets discussed in Chapters 2 and 3. In practice, the number of ports 
supported by a router can range from a relatively small number in enterprise routers, to 
hundreds of 10 Gbps ports in a router at an ISP’s edge, where the number of incoming lines 
tends to be the greatest. The Juniper MX2020, edge router, for example, supports up to 960 10 
Gbps Ethernet ports, with an overall router system capacity of 80 Tbps [Juniper MX 2020 2016]. 
Switching fabric. The switching fabric connects the router’s input ports to its output ports. This 
switching fabric is completely contained within the router—a network inside of a network 
router! Output ports. An output port stores packets received from the switching fabric and 
transmits these packets on the outgoing link by performing the necessary link-layer and 
physical-layer functions. When a link is bidirectional (that is, carries traffic in both directions), 
an output port will typically be paired with the input port for that link on the same line card. 
Routing processor. The routing processor performs control-plane functions. In traditional 
routers, it executes the routing protocols (which we’ll study in Sections 5.3 and 5.4), maintains 
routing tables and attached link state information, and computes the forwarding table for the 
router. In SDN routers, the routing processor is responsible for communicating with the remote 
controller in order to (among other activities) receive forwarding table entries computed by the 
remote controller, and install these entries in the router’s input ports. The routing processor 
also performs the network management functions that we’ll study in Section 5.7. A router’s 
input ports, output ports, and switching fabric are almost always implemented in hardware, as 
shown in Figure 4.4. To appreciate why a hardware implementation is needed, consider that 
with a 10 Gbps input link and a 64-byte IP datagram, the input port has only 51.2 ns to process 
the datagram before another datagram may arrive. If N ports are combined on a line card (as is 
often done in practice), the datagram-processing pipeline must operate N times faster—far too 
fast for software implementation. Forwarding hardware can be implemented either using a 
router vendor’s own hardware designs, or constructed using purchased merchant-silicon chips 
(e.g., as sold by companies such as Intel and Broadcom). While the data plane operates at the 


## Page 5

nanosecond time scale, a router’s control functions—executing the routing protocols, 
responding to attached links that go up or down, communicating with the remote controller (in 
the SDN case) and performing management functions—operate at the millisecond or second 
timescale. These control plane functions are thus usually implemented in software and execute 
on the routing processor (typically a traditional CPU). Before delving into the details of router 
internals, let’s return to our analogy from the beginning of this chapter, where packet 
forwarding was compared to cars entering and leaving an interchange. Let’s suppose that the 
interchange is a roundabout, and that as a car enters the roundabout, a bit of processing is 
required. Let’s consider what information is required for this processing: Destination-based 
forwarding. Suppose the car stops at an entry station and indicates its final destination (not at 
the local roundabout, but the ultimate destination of its journey). An attendant at the entry 
station looks up the final destination, determines the roundabout exit that leads to that final 
destination, and tells the driver which roundabout exit to take. Generalized forwarding. The 
attendant could also determine the car’s exit ramp on the basis of many other factors besides 
the destination. For example, the selected exit ramp might depend on the car’s origin, for 
example the state that issued the car’s license plate. Cars from a certain set of states might be 
directed to use one exit ramp (that leads to the destination via a slow road), while cars from 
other states might be directed to use a different exit ramp (that leads to the destination via 
superhighway). The same decision might be made based on the model, make and year of the 
car. Or a car not deemed roadworthy might be blocked and not be allowed to pass through the 
roundabout. In the case of generalized forwarding, any number of factors may contribute to the 
attendant’s choice of the exit ramp for a given car. Once the car enters the roundabout (which 
may be filled with other cars entering from other input roads and heading to other roundabout 
exits), it eventually leaves at the prescribed roundabout exit ramp, where it may encounter 
other cars leaving the roundabout at that exit. We can easily recognize the principal router 
components in Figure 4.4 in this analogy—the entry road and entry station correspond to the 
input port (with a lookup function to determine to local outgoing port); the roundabout 
corresponds to the switch fabric; and the roundabout exit road corresponds to the output port. 
With this analogy, it’s instructive to consider where bottlenecks might occur. What happens if 
cars arrive blazingly fast (for example, the roundabout is in Germany or Italy!) but the station 
attendant is slow? How fast must the attendant work to ensure there’s no backup on an entry 
road? Even with a blazingly fast attendant, what happens if cars traverse the roundabout 
slowly—can backups still occur? And what happens if most of the cars entering at all of the 
roundabout’s entrance ramps all want to leave the roundabout at the same exit ramp—can 
backups occur at the exit ramp or elsewhere? How should the roundabout operate if we want to 
assign priorities to different cars, or block certain cars from entering the roundabout in the first 
place? These are all analogous to critical questions faced by router and switch designers. In the 
following subsections, we’ll look at router functions in more detail. [Iyer 2008, Chao 2001; 
Chuang 2005; Turner 1988; McKeown 1997a; Partridge 1998; Sopranos 2011] provide a 
discussion of specific router architectures. For concreteness and simplicity, we’ll initially 
assume in this section that forwarding decisions are based only on the packet’s destination 
address, rather than on a generalized set of packet header fields. We will cover the case of 
more generalized packet forwarding in Section 4.4. 4.2.1 Input Port Processing and Destination-
Based Forwarding A more detailed view of input processing is shown in Figure 4.5. As just 
discussed, the input port’s linetermination function and link-layer processing implement the 
physical and link layers for that individual input link. The lookup performed in the input port is 
central to the router’s operation—it is here that the router uses the forwarding table to look up 
the output port to which an arriving packet will be forwarded via the switching fabric. The 


## Page 6

forwarding table is either computed and updated by the routing processor (using a routing 
protocol to interact with the routing processors in other network routers) or is received from a 
remote SDN controller. The forwarding table is copied from the routing processor to the line 
cards over a separate bus (e.g., a PCI bus) indicated by the dashed line from the routing 
processor to the input line cards in Figure 4.4. With such a shadow copy at each line card, 
forwarding decisions can be made locally, at each input port, without invoking the centralized 
routing processor on a per-packet basis and thus avoiding a centralized processing bottleneck. 
Let’s now consider the “simplest” case that the output port to which an incoming packet is to 
be switched is based on the packet’s destination address. In the case of 32-bit IP addresses, a 
brute-force implementation of the forwarding table would have one entry for every possible 
destination address. Since there are more than 4 billion possible addresses, this option is 
totally out of the question. Figure 4.5 Input port processing As an example of how this issue of 
scale can be handled, let’s suppose that our router has four links, numbered 0 through 3, and 
that packets are to be forwarded to the link interfaces as follows: Destination Address Range 
Link Interface 11001000 00010111 00010000 00000000 through 11001000 00010111 00010111 
11111111 0 11001000 00010111 00011000 00000000 1 through 11001000 00010111 00011000 
11111111 11001000 00010111 00011001 00000000 through 11001000 00010111 00011111 
11111111 2 Otherwise 3 Clearly, for this example, it is not necessary to have 4 billion entries in 
the router’s forwarding table. We could, for example, have the following forwarding table with 
just four entries: Prefix Link Interface 11001000 00010111 00010 0 11001000 00010111 
00011000 1 11001000 00010111 00011 2 Otherwise 3 With this style of forwarding table, the 
router matches a prefix of the packet’s destination address with the entries in the table; if 
there’s a match, the router forwards the packet to a link associated with the match. For 
example, suppose the packet’s destination address is 11001000 00010111 00010110 
10100001 ; because the 21-bit prefix of this address matches the first entry in the table, the 
router forwards the packet to link interface 0. If a prefix doesn’t match any of the first three 
entries, then the router forwards the packet to the default interface 3. Although this sounds 
simple enough, there’s a very important subtlety here. You may have noticed that it is possible 
for a destination address to match more than one entry. For example, the first 24 bits of the 
address 11001000 00010111 00011000 10101010 match the second entry in the table, and the 
first 21 bits of the address match the third entry in the table. When there are multiple matches, 
the router uses the longest prefix matching rule; that is, it finds the longest matching entry in the 
table and forwards the packet to the link interface associated with the longest prefix match. 
We’ll see exactly why this longest prefix-matching rule is used when we study Internet 
addressing in more detail in Section 4.3. Given the existence of a forwarding table, lookup is 
conceptually simple—hardware logic just searches through the forwarding table looking for the 
longest prefix match. But at Gigabit transmission rates, this lookup must be performed in 
nanoseconds (recall our earlier example of a 10 Gbps link and a 64-byte IP datagram). Thus, not 
only must lookup be performed in hardware, but techniques beyond a simple linear search 
through a large table are needed; surveys of fast lookup algorithms can be found in [Gupta 
2001, Ruiz-Sanchez 2001]. Special attention must also be paid to memory access times, 
resulting in designs with embedded on-chip DRAM and faster SRAM (used as a DRAM cache) 
memories. In practice, Ternary Content Addressable Memories (TCAMs) are also often used for 
lookup [Yu 2004]. With a TCAM, a 32-bit IP address is presented to the memory, which returns 
the content of the forwarding table entry for that address in essentially constant time. The Cisco 
Catalyst 6500 and 7600 Series routers and switches can hold upwards of a million TCAM 
forwarding table entries [Cisco TCAM 2014]. Once a packet’s output port has been determined 
via the lookup, the packet can be sent into the switching fabric. In some designs, a packet may 


## Page 7

be temporarily blocked from entering the switching fabric if packets from other input ports are 
currently using the fabric. A blocked packet will be queued at the input port and then scheduled 
to cross the fabric at a later point in time. We’ll take a closer look at the blocking, queuing, and 
scheduling of packets (at both input ports and output ports) shortly. Although “lookup” is 
arguably the most important action in input port processing, many other actions must be taken: 
(1) physical- and link-layer processing must occur, as discussed previously; (2) the packet’s 
version number, checksum and time-to-live field—all of which we’ll study in Section 4.3—must 
be checked and the latter two fields rewritten; and (3) counters used for network management 
(such as the number of IP datagrams received) must be updated. Let’s close our discussion of 
input port processing by noting that the input port steps of looking up a destination IP address 
(“match”) and then sending the packet into the switching fabric to the specified output port 
(“action”) is a specific case of a more general “match plus action” abstraction that is 
performed in many networked devices, not just routers. In link-layer switches (covered in 
Chapter 6), link-layer destination addresses are looked up and several actions may be taken in 
addition to sending the frame into the switching fabric towards the output port. In firewalls 
(covered in Chapter 8)—devices that filter out selected incoming packets—an incoming packet 
whose header matches a given criteria (e.g., a combination of source/destination IP addresses 
and transport-layer port numbers) may be dropped (action). In a network address translator 
(NAT, covered in Section 4.3), an incoming packet whose transport-layer port number matches 
a given value will have its port number rewritten before forwarding (action). Indeed, the “match 
plus action” abstraction is both powerful and prevalent in network devices today, and is central 
to the notion of generalized forwarding that we’ll study in Section 4.4. 4.2.2 Switching The 
switching fabric is at the very heart of a router, as it is through this fabric that the packets are 
actually switched (that is, forwarded) from an input port to an output port. Switching can be 
accomplished in a number of ways, as shown in Figure 4.6: Switching via memory. The 
simplest, earliest routers were traditional computers, with switching between input and output 
ports being done under direct control of the CPU (routing processor). Input and output ports 
functioned as traditional I/O devices in a traditional operating system. An input port with an 
arriving packet first signaled the routing processor via an interrupt. The packet was then copied 
from the input port into processor memory. The routing processor then extracted the 
destination address from the header, looked up the appropriate output port in the forwarding 
table, and copied the packet to the output port’s buffers. In this scenario, if the memory 
bandwidth is such that a maximum of B packets per second can be written into, or read from, 
memory, then the overall forwarding throughput (the total rate at which packets are transferred 
from input ports to output ports) must be less than B/2. Note also that two packets cannot be 
forwarded Figure 4.6 Three switching techniques at the same time, even if they have different 
destination ports, since only one memory read/write can be done at a time over the shared 
system bus. Some modern routers switch via memory. A major difference from early routers, 
however, is that the lookup of the destination address and the storing of the packet into the 
appropriate memory location are performed by processing on the input line cards. In some 
ways, routers that switch via memory look very much like shared-memory multiprocessors, 
with the processing on a line card switching (writing) packets into the memory of the 
appropriate output port. Cisco’s Catalyst 8500 series switches [Cisco 8500 2016] internally 
switches packets via a shared memory. Switching via a bus. In this approach, an input port 
transfers a packet directly to the output port over a shared bus, without intervention by the 
routing processor. This is typically done by having the input port pre-pend a switch-internal 
label (header) to the packet indicating the local output port to which this packet is being 
transferred and transmitting the packet onto the bus. All output ports receive the packet, but 


## Page 8

only the port that matches the label will keep the packet. The label is then removed at the 
output port, as this label is only used within the switch to cross the bus. If multiple packets 
arrive to the router at the same time, each at a different input port, all but one must wait since 
only one packet can cross the bus at a time. Because every packet must cross the single bus, 
the switching speed of the router is limited to the bus speed; in our roundabout analogy, this is 
as if the roundabout could only contain one car at a time. Nonetheless, switching via a bus is 
often sufficient for routers that operate in small local area and enterprise networks. The Cisco 
6500 router [Cisco 6500 2016] internally switches packets over a 32-Gbps-backplane bus. 
Switching via an interconnection network. One way to overcome the bandwidth limitation of a 
single, shared bus is to use a more sophisticated interconnection network, such as those that 
have been used in the past to interconnect processors in a multiprocessor computer 
architecture. A crossbar switch is an interconnection network consisting of 2N buses that 
connect N input ports to N output ports, as shown in Figure 4.6. Each vertical bus intersects 
each horizontal bus at a crosspoint, which can be opened or closed at any time by the switch 
fabric controller (whose logic is part of the switching fabric itself). When a packet arrives from 
port A and needs to be forwarded to port Y, the switch controller closes the crosspoint at the 
intersection of busses A and Y, and port A then sends the packet onto its bus, which is picked 
up (only) by bus Y. Note that a packet from port B can be forwarded to port X at the same time, 
since the A-to-Y and B-to-X packets use different input and output busses. Thus, unlike the 
previous two switching approaches, crossbar switches are capable of forwarding multiple 
packets in parallel. A crossbar switch is non-blocking—a packet being forwarded to an output 
port will not be blocked from reaching that output port as long as no other packet is currently 
being forwarded to that output port. However, if two packets from two different input ports are 
destined to that same output port, then one will have to wait at the input, since only one packet 
can be sent over any given bus at a time. Cisco 12000 series switches [Cisco 12000 2016] use a 
crossbar switching network; the Cisco 7600 series can be configured to use either a bus or 
crossbar switch [Cisco 7600 2016]. More sophisticated interconnection networks use multiple 
stages of switching elements to allow packets from different input ports to proceed towards the 
same output port at the same time through the multi-stage switching fabric. See [Tobagi 1990] 
for a survey of switch architectures. The Cisco CRS employs a three-stage non-blocking 
switching strategy. A router’s switching capacity can also be scaled by running multiple 
switching fabrics in parallel. In this approach, input ports and output ports are connected to N 
switching fabrics that operate in parallel. An input port breaks a packet into K smaller chunks, 
and sends (“sprays”) the chunks through K of these N switching fabrics to the selected output 
port, which reassembles the K chunks back into the original packet. 4.2.3 Output Port 
Processing Output port processing, shown in Figure 4.7, takes packets that have been stored in 
the output port’s memory and transmits them over the output link. This includes selecting and 
de-queueing packets for transmission, and performing the needed link-layer and physical-layer 
transmission functions. 4.2.4 Where Does Queuing Occur? If we consider input and output port 
functionality and the configurations shown in Figure 4.6, it’s clear that packet queues may form 
at both the input ports and the output ports, just as we identified cases where cars may wait at 
the inputs and outputs of the traffic intersection in our roundabout analogy. The location and 
extent of queueing (either at the input port queues or the output port queues) will depend on the 
traffic load, the relative speed of the switching fabric, and the line speed. Let’s now consider 
these queues in a bit more detail, since as these queues grow large, the router’s memory can 
eventually be exhausted and packet loss will occur when no memory is available to store 
arriving packets. Recall that in our earlier discussions, we said that packets were “lost within 
the network” or “dropped at a router.” It is here, at these queues within a router, where such 


## Page 9

packets are actually dropped and lost. Figure 4.7 Output port processing Suppose that the 
input and output line speeds (transmission rates) all have an identical transmission rate of R 
packets per second, and that there are N input ports and N output ports. To further simplify the 
discussion, let’s assume that all packets have the same fixed length, and that packets arrive to 
input ports in a synchronous manner. That is, the time to send a packet on any link is equal to 
the time to receive a packet on any link, and during such an interval of time, either zero or one 
packets can arrive on an input link. Define the switching fabric transfer rate R as the rate at 
which packets can be moved from input port to output port. If R is N times faster than R , then 
only negligible queuing will occur at the input ports. This is because even in the worst case, 
where all N input lines are receiving packets, and all packets are to be forwarded to the same 
output port, each batch of N packets (one packet per input port) can be cleared through the 
switch fabric before the next batch arrives. Input Queueing But what happens if the switch 
fabric is not fast enough (relative to the input line speeds) to transfer all arriving packets 
through the fabric without delay? In this case, packet queuing can also occur at the input ports, 
as packets must join input port queues to wait their turn to be transferred through the switching 
fabric to the output port. To illustrate an important consequence of this queuing, consider a 
crossbar switching fabric and suppose that (1) all link speeds are identical, (2) that one packet 
can be transferred from any one input port to a given output port in the same amount of time it 
takes for a packet to be received on an input link, and (3) packets are moved from a given input 
queue to their desired output queue in an FCFS manner. Multiple packets can be transferred in 
parallel, as long as their output ports are different. However, if two packets at the front of two 
input queues are destined for the same output queue, then one of the packets will be blocked 
and must wait at the input queue—the switching fabric can transfer only one packet to a given 
output port at a time. Figure 4.8 shows an example in which two packets (darkly shaded) at the 
front of their input queues are destined for the same upper-right output port. Suppose that the 
switch fabric chooses to transfer the packet from the front of the upper-left queue. In this case, 
the darkly shaded packet in the lower-left queue must wait. But not only must this darkly 
shaded packet wait, so too must the lightly shaded line switch switch line packet that is queued 
behind that packet in the lower-left queue, even though there is no contention for the middle-
right output port (the destination for the lightly shaded packet). This phenomenon is known as 
head-of-the-line (HOL) blocking in an input-queued switch—a queued packet in an input queue 
must wait for transfer through the fabric (even though its output port is free) because it is 
blocked by another packet at the head of the line. [Karol 1987] shows that due to HOL blocking, 
the input queue will grow to unbounded length (informally, this is equivalent to saying that 
significant packet loss will occur) under certain assumptions as soon as the packet arrival rate 
on the input links reaches only 58 percent of their capacity. A number of solutions to HOL 
blocking are discussed in [McKeown 1997]. Figure 4.8 HOL blocking at and input-queued switch 
Output Queueing Let’s next consider whether queueing can occur at a switch’s output ports. 
Suppose that R is again N times faster than R and that packets arriving at each of the N input 
ports are destined to the same output port. In this case, in the time it takes to send a single 
packet onto the outgoing link, N new packets will arrive at this output port (one from each of the 
N input ports). Since the output port can switch line transmit only a single packet in a unit of 
time (the packet transmission time), the N arriving packets will have to queue (wait) for 
transmission over the outgoing link. Then N more packets can possibly arrive in the time it takes 
to transmit just one of the N packets that had just previously been queued. And so on. Thus, 
packet queues can form at the output ports even when the switching fabric is N times faster 
than the port line speeds. Eventually, the number of queued packets can grow large enough to 
exhaust available memory at the output port. Figure 4.9 Output port queueing When there is not 


## Page 10

enough memory to buffer an incoming packet, a decision must be made to either drop the 
arriving packet (a policy known as drop-tail) or remove one or more already-queued packets to 
make room for the newly arrived packet. In some cases, it may be advantageous to drop (or 
mark the header of) a packet before the buffer is full in order to provide a congestion signal to 
the sender. A number of proactive packet-dropping and -marking policies (which collectively 
have become known as active queue management (AQM) algorithms) have been proposed and 
analyzed [Labrador 1999, Hollot 2002]. One of the most widely studied and implemented AQM 
algorithms is the Random Early Detection (RED) algorithm [Christiansen 2001; Floyd 2016]. 
Output port queuing is illustrated in Figure 4.9. At time t, a packet has arrived at each of the 
incoming input ports, each destined for the uppermost outgoing port. Assuming identical line 
speeds and a switch operating at three times the line speed, one time unit later (that is, in the 
time needed to receive or send a packet), all three original packets have been transferred to the 
outgoing port and are queued awaiting transmission. In the next time unit, one of these three 
packets will have been transmitted over the outgoing link. In our example, two new packets 
have arrived at the incoming side of the switch; one of these packets is destined for this 
uppermost output port. A consequence of such queuing is that a packet scheduler at the 
output port must choose one packet, among those queued, for transmission— a topic we’ll 
cover in the following section. Given that router buffers are needed to absorb the fluctuations in 
traffic load, a natural question to ask is how much buffering is required. For many years, the 
rule of thumb [RFC 3439] for buffer sizing was that the amount of buffering (B) should be equal 
to an average round-trip time (RTT, say 250 msec) times the link capacity (C). This result is 
based on an analysis of the queueing dynamics of a relatively small number of TCP flows 
[Villamizar 1994]. Thus, a 10 Gbps link with an RTT of 250 msec would need an amount of 
buffering equal to B 5 RTT · C 5 2.5 Gbits of buffers. More recent theoretical and experimental 
efforts [Appenzeller 2004], however, suggest that when there are a large number of TCP flows 
(N) passing through a link, the amount of buffering needed is With a large number of flows 
typically passing through large backbone router links (see, e.g., [Fraleigh 2003]), the value of N 
can be large, with the decrease in needed buffer size becoming quite significant. [Appenzeller 
2004; Wischik 2005; Beheshti 2008] provide very readable discussions of the buffer-sizing 
problem from a theoretical, implementation, and operational standpoint. 4.2.5 Packet 
Scheduling Let’s now return to the question of determining the order in which queued packets 
are transmitted over an outgoing link. Since you yourself have undoubtedly had to wait in long 
lines on many occasions and observed how waiting customers are served, you’re no doubt 
familiar with many of the queueing disciplines commonly used in routers. There is first-come-
first-served (FCFS, also known as first-in-firstout, FIFO). The British are famous for patient and 
orderly FCFS queueing at bus stops and in the marketplace (“Oh, are you queueing?”). Other 
countries operate on a priority basis, with one class of waiting customers given priority service 
over other waiting customers. There is also round-robin queueing, where customers are again 
divided into classes (as in priority queueing) but each class of customer is given service in turn. 
First-in-First-Out (FIFO) Figure 4.10 shows the queuing model abstraction for the FIFO link-
scheduling discipline. Packets arriving at the link output queue wait for transmission if the link 
is currently busy transmitting another packet. If there is not sufficient buffering space to hold 
the arriving packet, the queue’s packetdiscarding policy then determines whether the packet 
will be dropped (lost) or whether other packets will be removed from the queue to make space 
for the arriving packet, as discussed above. In our B=RTI⋅C/N. discussion below, we’ll ignore 
packet discard. When a packet is completely transmitted over the outgoing link (that is, 
receives service) it is removed from the queue. The FIFO (also known as first-come-first-served, 
or FCFS) scheduling discipline selects packets for link transmission in the same order in which 


## Page 11

they arrived at the output link queue. We’re all familiar with FIFO queuing from service centers, 
where Figure 4.10 FIFO queueing abstraction arriving customers join the back of the single 
waiting line, remain in order, and are then served when they reach the front of the line. Figure 
4.11 shows the FIFO queue in operation. Packet arrivals are indicated by numbered arrows 
above the upper timeline, with the number indicating the order in which the packet arrived. 
Individual packet departures are shown below the lower timeline. The time that a packet 
spends in service (being transmitted) is indicated by the shaded rectangle between the two 
timelines. In our examples here, let’s assume that each packet takes three units of time to be 
transmitted. Under the FIFO discipline, packets leave in the same order in which they arrived. 
Note that after the departure of packet 4, the link remains idle (since packets 1 through 4 have 
been transmitted and removed from the queue) until the arrival of packet 5. Priority Queuing 
Under priority queuing, packets arriving at the output link are classified into priority classes 
upon arrival at the queue, as shown in Figure 4.12. In practice, a network operator may 
configure a queue so that packets carrying network management information (e.g., as indicated 
by the source or destination TCP/UDP port number) receive priority over user traffic; 
additionally, real-time voice-over-IP packets might receive priority over non-real traffic such as 
SMTP or IMAP e-mail packets. Each Figure 4.11 The FIFO queue in operation Figure 4.12 The 
priority queueing model priority class typically has its own queue. When choosing a packet to 
transmit, the priority queuing discipline will transmit a packet from the highest priority class 
that has a nonempty queue (that is, has packets waiting for transmission). The choice among 
packets in the same priority class is typically done in a FIFO manner. Figure 4.13 illustrates the 
operation of a priority queue with two priority classes. Packets 1, 3, and 4 belong to the high-
priority class, and packets 2 and 5 belong to the low-priority class. Packet 1 arrives and, finding 
the link idle, begins transmission. During the transmission of packet 1, packets 2 and 3 arrive 
and are queued in the low- and high-priority queues, respectively. After the transmission of 
packet 1, packet 3 (a high-priority packet) is selected for transmission over packet 2 (which, 
even though it arrived earlier, is a low-priority packet). At the end of the transmission of packet 
3, packet 2 then begins transmission. Packet 4 (a high-priority packet) arrives during the 
transmission of packet 2 (a low-priority packet). Under a non-preemptive priority queuing 
discipline, the transmission of a packet is not interrupted once it has Figure 4.13 The priority 
queue in operation Figure 4.14 The two-class robin queue in operation begun. In this case, 
packet 4 queues for transmission and begins being transmitted after the transmission of packet 
2 is completed. Round Robin and Weighted Fair Queuing (WFQ) Under the round robin queuing 
discipline, packets are sorted into classes as with priority queuing. However, rather than there 
being a strict service priority among classes, a round robin scheduler alternates service among 
the classes. In the simplest form of round robin scheduling, a class 1 packet is transmitted, 
followed by a class 2 packet, followed by a class 1 packet, followed by a class 2 packet, and so 
on. A so-called work-conserving queuing discipline will never allow the link to remain idle 
whenever there are packets (of any class) queued for transmission. A work-conserving round 
robin discipline that looks for a packet of a given class but finds none will immediately check 
the next class in the round robin sequence. Figure 4.14 illustrates the operation of a two-class 
round robin queue. In this example, packets 1, 2, and 4 belong to class 1, and packets 3 and 5 
belong to the second class. Packet 1 begins transmission immediately upon arrival at the 
output queue. Packets 2 and 3 arrive during the transmission of packet 1 and thus queue for 
transmission. After the transmission of packet 1, the link scheduler looks for a class 2 packet 
and thus transmits packet 3. After the transmission of packet 3, the scheduler looks for a class 
1 packet and thus transmits packet 2. After the transmission of packet 2, packet 4 is the only 
queued packet; it is thus transmitted immediately after packet 2. A generalized form of round 


## Page 12

robin queuing that has been widely implemented in routers is the so-called weighted fair 
queuing (WFQ) discipline [Demers 1990; Parekh 1993; Cisco QoS 2016]. WFQ is illustrated in 
Figure 4.15. Here, arriving packets are classified and queued in the appropriate per-class 
waiting area. As in round robin scheduling, a WFQ scheduler will serve classes in a circular 
manner— first serving class 1, then serving class 2, then serving class 3, and then (assuming 
there are three classes) repeating the service pattern. WFQ is also a work-conserving Figure 
4.15 Weighted fair queueing queuing discipline and thus will immediately move on to the next 
class in the service sequence when it finds an empty class queue. WFQ differs from round robin 
in that each class may receive a differential amount of service in any interval of time. 
Specifically, each class, i, is assigned a weight, w. Under WFQ, during any interval of time 
during which there are class i packets to send, class i will then be guaranteed to receive a 
fraction of service equal to where the sum in the denominator is taken over all classes that also 
have packets queued for transmission. In the worst case, even if all classes have queued 
packets, class i will still be guaranteed to receive a fraction of the bandwidth, where in this 
worst case the sum in the denominator is over all classes. Thus, for a link with transmission 
rate R, class i will always achieve a throughput of at least Our description of WFQ has been 
idealized, as we have not considered the fact that packets are discrete and a packet’s 
transmission will not be interrupted to begin transmission of another packet; [Demers 1990; 
Parekh 1993] discuss this packetization issue. i wi/(∑wj), wi/(∑wj) R⋅wi/(∑wj). 4.3 The Internet 
Protocol (IP): IPv4, Addressing, IPv6, and More Our study of the network layer thus far in 
Chapter 4—the notion of the data and control plane component of the network layer, our 
distinction between forwarding and routing, the identification of various network service 
models, and our look inside a router—have often been without reference to any specific 
computer network architecture or protocol. In this section we’ll focus on key aspects of the 
network layer on today’s Internet and the celebrated Internet Protocol (IP). There are two 
versions of IP in use today. We’ll first examine the widely deployed IP protocol version 4, which 
is usually referred to simply as IPv4 [RFC 791] Figure 4.16 IPv4 datagram format in Section 
4.3.1. We’ll examine IP version 6 [RFC 2460; RFC 4291], which has been proposed to replace 
IPv4, in Section 4.3.5. In between, we’ll primarily cover Internet addressing—a topic that might 
seem rather dry and detail-oriented but we’ll see is crucial to understanding how the Internet’s 
network layer works. To master IP addressing is to master the Internet’s network layer itself! 
4.3.1 IPv4 Datagram Format Recall that the Internet’s network-layer packet is referred to as a 
datagram. We begin our study of IP with an overview of the syntax and semantics of the IPv4 
datagram. You might be thinking that nothing could be drier than the syntax and semantics of a 
packet’s bits. Nevertheless, the datagram plays a central role in the Internet—every networking 
student and professional needs to see it, absorb it, and master it. (And just to see that protocol 
headers can indeed be fun to study, check out [Pomeranz 2010]). The IPv4 datagram format is 
shown in Figure 4.16. The key fields in the IPv4 datagram are the following: Version number. 
These 4 bits specify the IP protocol version of the datagram. By looking at the version number, 
the router can determine how to interpret the remainder of the IP datagram. Different versions 
of IP use different datagram formats. The datagram format for IPv4 is shown in Figure 4.16. The 
datagram format for the new version of IP (IPv6) is discussed in Section 4.3.5. Header length. 
Because an IPv4 datagram can contain a variable number of options (which are included in the 
IPv4 datagram header), these 4 bits are needed to determine where in the IP datagram the 
payload (e.g., the transport-layer segment being encapsulated in this datagram) actually 
begins. Most IP datagrams do not contain options, so the typical IP datagram has a 20-byte 
header. Type of service. The type of service (TOS) bits were included in the IPv4 header to allow 
different types of IP datagrams to be distinguished from each other. For example, it might be 


## Page 13

useful to distinguish real-time datagrams (such as those used by an IP telephony application) 
from non-realtime traffic (for example, FTP). The specific level of service to be provided is a 
policy issue determined and configured by the network administrator for that router. We also 
learned in Section 3.7.2 that two of the TOS bits are used for Explicit Congestion Notification. 
Datagram length. This is the total length of the IP datagram (header plus data), measured in 
bytes. Since this field is 16 bits long, the theoretical maximum size of the IP datagram is 65,535 
bytes. However, datagrams are rarely larger than 1,500 bytes, which allows an IP datagram to fit 
in the payload field of a maximally sized Ethernet frame. Identifier, flags, fragmentation offset. 
These three fields have to do with so-called IP fragmentation, a topic we will consider shortly. 
Interestingly, the new version of IP, IPv6, does not allow for fragmentation. Time-to-live. The 
time-to-live (TTL) field is included to ensure that datagrams do not circulate forever (due to, for 
example, a long-lived routing loop) in the network. This field is decremented by one each time 
the datagram is processed by a router. If the TTL field reaches 0, a router must drop that 
datagram. Protocol. This field is typically used only when an IP datagram reaches its final 
destination. The value of this field indicates the specific transport-layer protocol to which the 
data portion of this IP datagram should be passed. For example, a value of 6 indicates that the 
data portion is passed to TCP, while a value of 17 indicates that the data is passed to UDP. For a 
list of all possible values, see [IANA Protocol Numbers 2016]. Note that the protocol number in 
the IP datagram has a role that is analogous to the role of the port number field in the transport-
layer segment. The protocol number is the glue that binds the network and transport layers 
together, whereas the port number is the glue that binds the transport and application layers 
together. We’ll see in Chapter 6 that the linklayer frame also has a special field that binds the 
link layer to the network layer. Header checksum. The header checksum aids a router in 
detecting bit errors in a received IP datagram. The header checksum is computed by treating 
each 2 bytes in the header as a number and summing these numbers using 1s complement 
arithmetic. As discussed in Section 3.3, the 1s complement of this sum, known as the Internet 
checksum, is stored in the checksum field. A router computes the header checksum for each 
received IP datagram and detects an error condition if the checksum carried in the datagram 
header does not equal the computed checksum. Routers typically discard datagrams for which 
an error has been detected. Note that the checksum must be recomputed and stored again at 
each router, since the TTL field, and possibly the options field as well, will change. An 
interesting discussion of fast algorithms for computing the Internet checksum is [RFC 1071]. A 
question often asked at this point is, why does TCP/IP perform error checking at both the 
transport and network layers? There are several reasons for this repetition. First, note that only 
the IP header is checksummed at the IP layer, while the TCP/UDP checksum is computed over 
the entire TCP/UDP segment. Second, TCP/UDP and IP do not necessarily both have to belong 
to the same protocol stack. TCP can, in principle, run over a different network-layer protocol 
(for example, ATM) [Black 1995]) and IP can carry data that will not be passed to TCP/UDP. 
Source and destination IP addresses. When a source creates a datagram, it inserts its IP 
address into the source IP address field and inserts the address of the ultimate destination into 
the destination IP address field. Often the source host determines the destination address via a 
DNS lookup, as discussed in Chapter 2. We’ll discuss IP addressing in detail in Section 4.3.3. 
Options. The options fields allow an IP header to be extended. Header options were meant to be 
used rarely—hence the decision to save overhead by not including the information in options 
fields in every datagram header. However, the mere existence of options does complicate 
matters—since datagram headers can be of variable length, one cannot determine a priori 
where the data field will start. Also, since some datagrams may require options processing and 
others may not, the amount of time needed to process an IP datagram at a router can vary 


## Page 14

greatly. These considerations become particularly important for IP processing in high-
performance routers and hosts. For these reasons and others, IP options were not included in 
the IPv6 header, as discussed in Section 4.3.5. Data (payload). Finally, we come to the last and 
most important field—the raison d’etre for the datagram in the first place! In most 
circumstances, the data field of the IP datagram contains the transport-layer segment (TCP or 
UDP) to be delivered to the destination. However, the data field can carry other types of data, 
such as ICMP messages (discussed in Section 5.6). Note that an IP datagram has a total of 20 
bytes of header (assuming no options). If the datagram carries a TCP segment, then each (non-
fragmented) datagram carries a total of 40 bytes of header (20 bytes of IP header plus 20 bytes 
of TCP header) along with the application-layer message. 4.3.2 IPv4 Datagram Fragmentation 
We’ll see in Chapter 6 that not all link-layer protocols can carry network-layer packets of the 
same size. Some protocols can carry big datagrams, whereas other protocols can carry only 
little datagrams. For example, Ethernet frames can carry up to 1,500 bytes of data, whereas 
frames for some wide-area links can carry no more than 576 bytes. The maximum amount of 
data that a link-layer frame can carry is called the maximum transmission unit (MTU). Because 
each IP datagram is encapsulated within the link-layer frame for transport from one router to 
the next router, the MTU of the link-layer protocol places a hard limit on the length of an IP 
datagram. Having a hard limit on the size of an IP datagram is not much of a problem. What is a 
problem is that each of the links along the route between sender and destination can use 
different link-layer protocols, and each of these protocols can have different MTUs. To 
understand the forwarding issue better, imagine that you are a router that interconnects several 
links, each running different link-layer protocols with different MTUs. Suppose you receive an IP 
datagram from one link. You check your forwarding table to determine the outgoing link, and 
this outgoing link has an MTU that is smaller than the length of the IP datagram. Time to panic—
how are you going to squeeze this oversized IP datagram into the payload field of the link-layer 
frame? The solution is to fragment the payload in the IP datagram into two or more smaller IP 
datagrams, encapsulate each of these smaller IP datagrams in a separate link-layer frame; and 
send these frames over the outgoing link. Each of these smaller datagrams is referred to as a 
fragment. Fragments need to be reassembled before they reach the transport layer at the 
destination. Indeed, both TCP and UDP are expecting to receive complete, unfragmented 
segments from the network layer. The designers of IPv4 felt that reassembling datagrams in the 
routers would introduce significant complication into the protocol and put a damper on router 
performance. (If you were a router, would you want to be reassembling fragments on top of 
everything else you had to do?) Sticking to the principle of keeping the network core simple, the 
designers of IPv4 decided to put the job of datagram reassembly in the end systems rather than 
in network routers. When a destination host receives a series of datagrams from the same 
source, it needs to determine whether any of these datagrams are fragments of some original, 
larger datagram. If some datagrams are fragments, it must further determine when it has 
received the last fragment and how the fragments it has received should be pieced back 
together to form the original datagram. To allow the destination host to perform these 
reassembly tasks, the designers of IP (version 4) put identification, flag, and fragmentation 
offset fields in the IP datagram header. When a datagram is created, the sending host stamps 
the datagram with an identification number as well as source and destination addresses. 
Typically, the sending host increments the identification number for each datagram it sends. 
When a router needs to fragment a datagram, each resulting datagram (that is, fragment) is 
stamped with the source address, destination address, and identification number of the 
original datagram. When the destination receives a series of datagrams from the same sending 
host, it can examine the identification numbers of the datagrams to determine which of the 


## Page 15

datagrams are actually fragments of the same larger datagram. Because IP is an unreliable 
service, one or more of the fragments may never arrive at the destination. For this reason, in 
order for the destination host to be absolutely sure it has received the last fragment of Figure 
4.17 IP fragmentation and reassembly the original datagram, the last fragment has a flag bit set 
to 0, whereas all the other fragments have this flag bit set to 1. Also, in order for the destination 
host to determine whether a fragment is missing (and also to be able to reassemble the 
fragments in their proper order), the offset field is used to specify where the fragment fits within 
the original IP datagram. Figure 4.17 illustrates an example. A datagram of 4,000 bytes (20 bytes 
of IP header plus 3,980 bytes of IP payload) arrives at a router and must be forwarded to a link 
with an MTU of 1,500 bytes. This implies that the 3,980 data bytes in the original datagram must 
be allocated to three separate fragments (each of which is also an IP datagram). The online 
material for this book, and the problems at the end of this chapter will allow you to explore 
fragmentation in more detail. Also, on this book’s Web site, we provide a Java applet that 
generates fragments. You provide the incoming datagram size, the MTU, and the incoming 
datagram identification. The applet automatically generates the fragments for you. See 
http://www.pearsonhighered.com/csresources/. 4.3.3 IPv4 Addressing We now turn our 
attention to IPv4 addressing. Although you may be thinking that addressing must be a 
straightforward topic, hopefully by the end of this section you’ll be convinced that Internet 
addressing is not only a juicy, subtle, and interesting topic but also one that is of central 
importance to the Internet. An excellent treatment of IPv4 addressing can be found in the first 
chapter in [Stewart 1999]. Before discussing IP addressing, however, we’ll need to say a few 
words about how hosts and routers are connected into the Internet. A host typically has only a 
single link into the network; when IP in the host wants to send a datagram, it does so over this 
link. The boundary between the host and the physical link is called an interface. Now consider a 
router and its interfaces. Because a router’s job is to receive a datagram on one link and 
forward the datagram on some other link, a router necessarily has two or more links to which it 
is connected. The boundary between the router and any one of its links is also called an 
interface. A router thus has multiple interfaces, one for each of its links. Because every host 
and router is capable of sending and receiving IP datagrams, IP requires each host and router 
interface to have its own IP address. Thus, an IP address is technically associated with an 
interface, rather than with the host or router containing that interface. Each IP address is 32 bits 
long (equivalently, 4 bytes), and there are thus a total of 2 (or approximately 4 billion) possible 
IP addresses. These addresses are typically written in so-called dotted-decimal notation, in 
which each byte of the address is written in its decimal form and is separated by a period (dot) 
from other bytes in the address. For example, consider the IP address 193.32.216.9. The 193 is 
the decimal equivalent of the first 8 bits of the address; the 32 is the decimal equivalent of the 
second 8 bits of the address, and so on. Thus, the address 193.32.216.9 in binary notation is 
11000001 00100000 11011000 00001001 Each interface on every host and router in the global 
Internet must have an IP address that is globally unique (except for interfaces behind NATs, as 
discussed in Section 4.3.4). These addresses cannot be chosen in a willy-nilly manner, 
however. A portion of an interface’s IP address will be determined by the subnet to which it is 
connected. Figure 4.18 provides an example of IP addressing and interfaces. In this figure, one 
router (with three interfaces) is used to interconnect seven hosts. Take a close look at the IP 
addresses assigned to the host and router interfaces, as there are several things to notice. The 
three hosts in the upper-left portion of Figure 4.18, and the router interface to which they are 
connected, all have an IP address of the form 32 223.1.1.xxx. That is, they all have the same 
leftmost 24 bits in their IP address. These four interfaces are also interconnected to each other 
by a network that contains no routers. This network could be interconnected by an Ethernet 


## Page 16

LAN, in which case the interfaces would be interconnected by an Ethernet switch (as we’ll 
discuss in Chapter 6), or by a wireless access point (as we’ll discuss in Chapter 7). We’ll 
represent this routerless network connecting these hosts as a cloud for now, and dive into the 
internals of such networks in Chapters 6 and 7. In IP terms, this network interconnecting three 
host interfaces and one router interface forms a subnet [RFC 950]. (A subnet is also called an IP 
network or simply Figure 4.18 Interface addresses and subnets a network in the Internet 
literature.) IP addressing assigns an address to this subnet: 223.1.1.0/24, where the /24 (“slash-
24”) notation, sometimes known as a subnet mask, indicates that the leftmost 24 bits of the 32-
bit quantity define the subnet address. The 223.1.1.0/24 subnet thus consists of the three host 
interfaces (223.1.1.1, 223.1.1.2, and 223.1.1.3) and one router interface (223.1.1.4). Any 
additional hosts attached to the 223.1.1.0/24 subnet would be required to have an address of 
the form 223.1.1.xxx. There are two additional subnets shown in Figure 4.18: the 223.1.2.0/24 
network and the 223.1.3.0/24 subnet. Figure 4.19 illustrates the three IP subnets present in 
Figure 4.18. The IP definition of a subnet is not restricted to Ethernet segments that connect 
multiple hosts to a router interface. To get some insight here, consider Figure 4.20, which 
shows three routers that are interconnected with each other by point-to-point links. Each router 
has three interfaces, one for each point-to-point link and one for the broadcast link that directly 
connects the router to a pair of hosts. What subnets are present here? Three subnets, 
223.1.1.0/24, 223.1.2.0/24, and 223.1.3.0/24, are similar to the subnets we encountered in 
Figure 4.18. But note that there are three additional subnets in this example as well: one 
subnet, 223.1.9.0/24, for the interfaces that connect routers R1 and R2; another subnet, 
223.1.8.0/24, for the interfaces that connect routers R2 and R3; and a third subnet, 
223.1.7.0/24, for the interfaces that connect routers R3 and R1. For a general interconnected 
system of routers and hosts, we can use the following recipe to define the subnets in the 
system: Figure 4.19 Subnet addresses To determine the subnets, detach each interface from its 
host or router, creating islands of isolated networks, with interfaces terminating the end points 
of the isolated networks. Each of these isolated networks is called a subnet. If we apply this 
procedure to the interconnected system in Figure 4.20, we get six islands or subnets. From the 
discussion above, it’s clear that an organization (such as a company or academic institution) 
with multiple Ethernet segments and point-to-point links will have multiple subnets, with all of 
the devices on a given subnet having the same subnet address. In principle, the different 
subnets could have quite different subnet addresses. In practice, however, their subnet 
addresses often have much in common. To understand why, let’s next turn our attention to how 
addressing is handled in the global Internet. The Internet’s address assignment strategy is 
known as Classless Interdomain Routing (CIDR— pronounced cider) [RFC 4632]. CIDR 
generalizes the notion of subnet addressing. As with subnet addressing, the 32-bit IP address is 
divided into two parts and again has the dotted-decimal form a.b.c.d/x, where x indicates the 
number of bits in the first part of the address. The x most significant bits of an address of the 
form a.b.c.d/x constitute the network portion of the IP address, and are often referred to as the 
prefix (or network prefix) of the address. An organization is typically assigned a block of 
contiguous addresses, that is, a range of addresses with a common prefix (see the Principles in 
Practice feature). In this case, the IP addresses of devices within the organization will share the 
common prefix. When we cover the Internet’s BGP routing protocol in Figure 4.20 Three routers 
interconnecting six subnets Section 5.4, we’ll see that only these x leading prefix bits are 
considered by routers outside the organization’s network. That is, when a router outside the 
organization forwards a datagram whose destination address is inside the organization, only the 
leading x bits of the address need be considered. This considerably reduces the size of the 
forwarding table in these routers, since a single entry of the form a.b.c.d/x will be sufficient to 


## Page 17

forward packets to any destination within the organization. The remaining 32-x bits of an 
address can be thought of as distinguishing among the devices within the organization, all of 
which have the same network prefix. These are the bits that will be considered when forwarding 
packets at routers within the organization. These lower-order bits may (or may not) have an 
additional subnetting structure, such as that discussed above. For example, suppose the first 
21 bits of the CIDRized address a.b.c.d/21 specify the organization’s network prefix and are 
common to the IP addresses of all devices in that organization. The remaining 11 bits then 
identify the specific hosts in the organization. The organization’s internal structure might be 
such that these 11 rightmost bits are used for subnetting within the organization, as discussed 
above. For example, a.b.c.d/24 might refer to a specific subnet within the organization. Before 
CIDR was adopted, the network portions of an IP address were constrained to be 8, 16, or 24 
bits in length, an addressing scheme known as classful addressing, since subnets with 8-, 16-, 
and 24-bit subnet addresses were known as class A, B, and C networks, respectively. The 
requirement that the subnet portion of an IP address be exactly 1, 2, or 3 bytes long turned out 
to be problematic for supporting the rapidly growing number of organizations with small and 
medium-sized subnets. A class C (/24) subnet could accommodate only up to 2 − 2 = 254 hosts 
(two of the 2 = 256 addresses are reserved for special use)—too small for many organizations. 
However, a class B (/16) subnet, which supports up to 65,634 hosts, was too large. Under 
classful addressing, an organization with, say, 2,000 hosts was typically allocated a class B 
(/16) subnet address. This led to a rapid depletion of the class B address space and poor 
utilization of the assigned address space. For example, the organization that used a class B 
address for its 2,000 hosts was allocated enough of the address space for up to 65,534 
interfaces—leaving more than 63,000 addresses that could not be used by other organizations. 
PRINCIPLES IN PRACTICE This example of an ISP that connects eight organizations to the 
Internet nicely illustrates how carefully allocated CIDRized addresses facilitate routing. 
Suppose, as shown in Figure 4.21, that the ISP (which we’ll call Fly-By-Night-ISP) advertises to 
the outside world that it should be sent any datagrams whose first 20 address bits match 
200.23.16.0/20. The rest of the world need not know that within the address block 
200.23.16.0/20 there are in fact eight other organizations, each with its own subnets. This ability 
to use a single prefix to advertise multiple networks is often referred to as address aggregation 
(also route aggregation or route summarization). Address aggregation works extremely well 
when addresses are allocated in blocks to ISPs and then from ISPs to client organizations. But 
what happens when addresses are not allocated in such a hierarchical manner? What would 
happen, for example, if Fly-By-Night-ISP acquires ISPs-R-Us and then has Organization 1 
connect to the Internet through its subsidiary ISPs-RUs? As shown in Figure 4.21, the subsidiary 
ISPs-R-Us owns the address block 199.31.0.0/16, but Organization 1’s IP addresses are 
unfortunately outside of this address block. What should be done here? Certainly, Organization 
1 could renumber all of its routers and hosts to have addresses within the ISPs-R-Us address 
block. But this is a costly solution, and Organization 1 might well be reassigned to another 
subsidiary in the future. The solution typically adopted is for Organization 1 to keep its IP 
addresses in 200.23.18.0/23. In this case, as shown in Figure 4.22, 8 8 Fly-By-Night-ISP 
continues to advertise the address block 200.23.16.0/20 and ISPs-R-Us continues to advertise 
199.31.0.0/16. However, ISPs-R-Us now also advertises the block of addresses for Organization 
1, 200.23.18.0/23. When other routers in the larger Internet see the address blocks 
200.23.16.0/20 (from Fly-By-Night-ISP) and 200.23.18.0/23 (from ISPs-R-Us) and want to route 
to an address in the block 200.23.18.0/23, they will use longest prefix matching (see Section 
4.2.1), and route toward ISPs-R-Us, as it advertises the longest (i.e., most-specific) address 
prefix that matches the destination address. Figure 4.21 Hierarchical addressing and route 


## Page 18

aggregation Figure 4.22 ISPs-R-Us has a more specific route to Organization 1 We would be 
remiss if we did not mention yet another type of IP address, the IP broadcast address 
255.255.255.255. When a host sends a datagram with destination address 255.255.255.255, 
the message is delivered to all hosts on the same subnet. Routers optionally forward the 
message into neighboring subnets as well (although they usually don’t). Having now studied IP 
addressing in detail, we need to know how hosts and subnets get their addresses in the first 
place. Let’s begin by looking at how an organization gets a block of addresses for its devices, 
and then look at how a device (such as a host) is assigned an address from within the 
organization’s block of addresses. Obtaining a Block of Addresses In order to obtain a block of 
IP addresses for use within an organization’s subnet, a network administrator might first 
contact its ISP, which would provide addresses from a larger block of addresses that had 
already been allocated to the ISP. For example, the ISP may itself have been allocated the 
address block 200.23.16.0/20. The ISP, in turn, could divide its address block into eight equal-
sized contiguous address blocks and give one of these address blocks out to each of up to eight 
organizations that are supported by this ISP, as shown below. (We have underlined the subnet 
part of these addresses for your convenience.) ISP’s block:     200.23.16.0/20     11001000 
00010111 00010000 00000000 Organization 0   200.23.16.0/23     11001000 00010111 
00010000 00000000 Organization 1   200.23.18.0/23     11001000 00010111 00010010 
00000000 Organization 2   200.23.20.0/23     11001000 00010111 00010100 00000000 … …        
… Organization 7   200.23.30.0/23     11001000 00010111 00011110 00000000 While 
obtaining a set of addresses from an ISP is one way to get a block of addresses, it is not the only 
way. Clearly, there must also be a way for the ISP itself to get a block of addresses. Is there a 
global authority that has ultimate responsibility for managing the IP address space and 
allocating address blocks to ISPs and other organizations? Indeed there is! IP addresses are 
managed under the authority of the Internet Corporation for Assigned Names and Numbers 
(ICANN) [ICANN 2016], based on guidelines set forth in [RFC 7020]. The role of the nonprofit 
ICANN organization [NTIA 1998] is not only to allocate IP addresses, but also to manage the 
DNS root servers. It also has the very contentious job of assigning domain names and resolving 
domain name disputes. The ICANN allocates addresses to regional Internet registries (for 
example, ARIN, RIPE, APNIC, and LACNIC, which together form the Address Supporting 
Organization of ICANN [ASO-ICANN 2016]), and handle the allocation/management of 
addresses within their regions. Obtaining a Host Address: The Dynamic Host Configuration 
Protocol Once an organization has obtained a block of addresses, it can assign individual IP 
addresses to the host and router interfaces in its organization. A system administrator will 
typically manually configure the IP addresses into the router (often remotely, with a network 
management tool). Host addresses can also be configured manually, but typically this is done 
using the Dynamic Host Configuration Protocol (DHCP) [RFC 2131]. DHCP allows a host to 
obtain (be allocated) an IP address automatically. A network administrator can configure DHCP 
so that a given host receives the same IP address each time it connects to the network, or a 
host may be assigned a temporary IP address that will be different each time the host connects 
to the network. In addition to host IP address assignment, DHCP also allows a host to learn 
additional information, such as its subnet mask, the address of its first-hop router (often called 
the default gateway), and the address of its local DNS server. Because of DHCP’s ability to 
automate the network-related aspects of connecting a host into a network, it is often referred to 
as a plug-and-play or zeroconf (zero-configuration) protocol. This capability makes it very 
attractive to the network administrator who would otherwise have to perform these tasks 
manually! DHCP is also enjoying widespread use in residential Internet access networks, 
enterprise networks, and in wireless LANs, where hosts join and leave the network frequently. 


## Page 19

Consider, for example, the student who carries a laptop from a dormitory room to a library to a 
classroom. It is likely that in each location, the student will be connecting into a new subnet 
and hence will need a new IP address at each location. DHCP is ideally suited to this situation, 
as there are many users coming and going, and addresses are needed for only a limited amount 
of time. The value of DHCP’s plug-and-play capability is clear, since it’s unimaginable that a 
system administrator would be able to reconfigure laptops at each location, and few students 
(except those taking a computer networking class!) would have the expertise to configure their 
laptops manually. DHCP is a client-server protocol. A client is typically a newly arriving host 
wanting to obtain network configuration information, including an IP address for itself. In the 
simplest case, each subnet (in the addressing sense of Figure 4.20) will have a DHCP server. If 
no server is present on the subnet, a DHCP relay agent (typically a router) that knows the 
address of a DHCP server for that network is needed. Figure 4.23 shows a DHCP server 
attached to subnet 223.1.2/24, with the router serving as the relay agent for arriving clients 
attached to subnets 223.1.1/24 and 223.1.3/24. In our discussion below, we’ll assume that a 
DHCP server is available on the subnet. For a newly arriving host, the DHCP protocol is a four-
step process, as shown in Figure 4.24 for the network setting shown in Figure 4.23. In this figure, 
yiaddr (as in “your Internet address”) indicates the address being allocated to the newly arriving 
client. The four steps are: Figure 4.23 DHCP client and server DHCP server discovery. The first 
task of a newly arriving host is to find a DHCP server with which to interact. This is done using a 
DHCP discover message, which a client sends within a UDP packet to port 67. The UDP packet 
is encapsulated in an IP datagram. But to whom should this datagram be sent? The host 
doesn’t even know the IP address of the network to which it is attaching, much less the address 
of a DHCP server for this network. Given this, the DHCP client creates an IP datagram 
containing its DHCP discover message along with the broadcast destination IP address of 
255.255.255.255 and a “this host” source IP address of 0.0.0.0. The DHCP client passes the IP 
datagram to the link layer, which then broadcasts this frame to all nodes attached to the subnet 
(we will cover the details of link-layer broadcasting in Section 6.4). DHCP server offer(s). A 
DHCP server receiving a DHCP discover message responds to the client with a DHCP offer 
message that is broadcast to all nodes on the subnet, again using the IP broadcast address of 
255.255.255.255. (You might want to think about why this server reply must also be broadcast). 
Since several DHCP servers can be present on the subnet, the client may find itself in the 
enviable position of being able to choose from among several offers. Each Figure 4.24 DHCP 
client-server interaction server offer message contains the transaction ID of the received 
discover message, the proposed IP address for the client, the network mask, and an IP address 
lease time—the amount of time for which the IP address will be valid. It is common for the 
server to set the lease time to several hours or days [Droms 2002]. DHCP request. The newly 
arriving client will choose from among one or more server offers and respond to its selected 
offer with a DHCP request message, echoing back the configuration parameters. DHCP ACK. 
The server responds to the DHCP request message with a DHCP ACK message, confirming the 
requested parameters. Once the client receives the DHCP ACK, the interaction is complete and 
the client can use the DHCPallocated IP address for the lease duration. Since a client may want 
to use its address beyond the lease’s expiration, DHCP also provides a mechanism that allows 
a client to renew its lease on an IP address. From a mobility aspect, DHCP does have one very 
significant shortcoming. Since a new IP address is obtained from DHCP each time a node 
connects to a new subnet, a TCP connection to a remote application cannot be maintained as a 
mobile node moves between subnets. In Chapter 6, we will examine mobile IP—an extension to 
the IP infrastructure that allows a mobile node to use a single permanent address as it moves 
between subnets. Additional details about DHCP can be found in [Droms 2002] and [dhc 2016]. 


## Page 20

An open source reference implementation of DHCP is available from the Internet Systems 
Consortium [ISC 2016]. 4.3.4 Network Address Translation (NAT) Given our discussion about 
Internet addresses and the IPv4 datagram format, we’re now well aware that every IP-capable 
device needs an IP address. With the proliferation of small office, home office (SOHO) subnets, 
this would seem to imply that whenever a SOHO wants to install a LAN to connect multiple 
machines, a range of addresses would need to be allocated by the ISP to cover all of the 
SOHO’s IP devices (including phones, tablets, gaming devices, IP TVs, printers and more). If the 
subnet grew bigger, a larger block of addresses would have to be allocated. But what if the ISP 
had already allocated the contiguous portions of the SOHO network’s current address range? 
And what typical homeowner wants (or should need) to know how to manage IP addresses in 
the first place? Fortunately, there is a simpler approach to address allocation that has found 
increasingly widespread use in such scenarios: network address translation (NAT) [RFC 2663; 
RFC 3022; Huston 2004, Zhang 2007; Cisco NAT 2016]. Figure 4.25 shows the operation of a 
NAT-enabled router. The NAT-enabled router, residing in the home, has an interface that is part 
of the home network on the right of Figure 4.25. Addressing within the home network is exactly 
as we have seen above—all four interfaces in the home network have the same subnet address 
of 10.0.0/24. The address space 10.0.0.0/8 is one of three portions of the IP address space that 
is reserved in [RFC 1918] for a private network or a realm with private addresses, such as the 
home network in Figure 4.25. A realm with private addresses refers to a network whose 
addresses only have meaning to devices within that network. To see why this is important, 
consider the fact that there are hundreds of thousands of home networks, many using the same 
address space, 10.0.0.0/24. Devices within a given home network can send packets to each 
other using 10.0.0.0/24 addressing. However, packets forwarded beyond the home network 
into the larger global Internet clearly cannot use these addresses (as either a source or a 
destination address) because there are hundreds of thousands of networks using this block of 
addresses. That is, the 10.0.0.0/24 addresses can only have meaning within the Figure 4.25 
Network address translation given home network. But if private addresses only have meaning 
within a given network, how is addressing handled when packets are sent to or received from 
the global Internet, where addresses are necessarily unique? The answer lies in understanding 
NAT. The NAT-enabled router does not look like a router to the outside world. Instead the NAT 
router behaves to the outside world as a single device with a single IP address. In Figure 4.25, all 
traffic leaving the home router for the larger Internet has a source IP address of 138.76.29.7, 
and all traffic entering the home router must have a destination address of 138.76.29.7. In 
essence, the NAT-enabled router is hiding the details of the home network from the outside 
world. (As an aside, you might wonder where the home network computers get their addresses 
and where the router gets its single IP address. Often, the answer is the same—DHCP! The 
router gets its address from the ISP’s DHCP server, and the router runs a DHCP server to 
provide addresses to computers within the NAT-DHCP-routercontrolled home network’s 
address space.) If all datagrams arriving at the NAT router from the WAN have the same 
destination IP address (specifically, that of the WAN-side interface of the NAT router), then how 
does the router know the internal host to which it should forward a given datagram? The trick is 
to use a NAT translation table at the NAT router, and to include port numbers as well as IP 
addresses in the table entries. Consider the example in Figure 4.25. Suppose a user sitting in a 
home network behind host 10.0.0.1 requests a Web page on some Web server (port 80) with IP 
address 128.119.40.186. The host 10.0.0.1 assigns the (arbitrary) source port number 3345 and 
sends the datagram into the LAN. The NAT router receives the datagram, generates a new 
source port number 5001 for the datagram, replaces the source IP address with its WAN-side IP 
address 138.76.29.7, and replaces the original source port number 3345 with the new source 

