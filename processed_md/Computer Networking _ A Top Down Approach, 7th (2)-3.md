# Computer Networking _ A Top Down Approach, 7th (2)-3

## Page 1

and querying hosts communicate. A simple design for DNS would have one DNS server that 
contains all the mappings. In this centralized design, clients simply direct all queries to the 
single DNS server, and the DNS server responds directly to the querying clients. Although the 
simplicity of this design is attractive, it is inappropriate for today’s Internet, with its vast (and 
growing) number of hosts. The problems with a centralized design include: A single point of 
failure. If the DNS server crashes, so does the entire Internet! Traffic volume. A single DNS 
server would have to handle all DNS queries (for all the HTTP requests and e-mail messages 
generated from hundreds of millions of hosts). Distant centralized database. A single DNS 
server cannot be “close to” all the querying clients. If we put the single DNS server in New York 
City, then all queries from Australia must travel to the other side of the globe, perhaps over slow 
and congested links. This can lead to significant delays. Maintenance. The single DNS server 
would have to keep records for all Internet hosts. Not only would this centralized database be 
huge, but it would have to be updated frequently to account for every new host. In summary, a 
centralized database in a single DNS server simply doesn’t scale. Consequently, the DNS is 
distributed by design. In fact, the DNS is a wonderful example of how a distributed database 
can be implemented in the Internet. A Distributed, Hierarchical Database In order to deal with 
the issue of scale, the DNS uses a large number of servers, organized in a hierarchical fashion 
and distributed around the world. No single DNS server has all of the mappings for all of the 
hosts in the Internet. Instead, the mappings are distributed across the DNS servers. To a first 
approximation, there are three classes of DNS servers—root DNS servers, top-level domain 
(TLD) DNS servers, and authoritative DNS servers—organized in a hierarchy as shown in Figure 
2.17. To understand how these three classes of servers interact, suppose a DNS client wants to 
determine the IP address for the hostname www.amazon.com . To a first Figure 2.17 Portion of 
the hierarchy of DNS servers approximation, the following events will take place. The client first 
contacts one of the root servers, which returns IP addresses for TLD servers for the top-level 
domain com . The client then contacts one of these TLD servers, which returns the IP address of 
an authoritative server for amazon.com . Finally, the client contacts one of the authoritative 
servers for amazon.com , which returns the IP address for the hostname www.amazon.com . 
We’ll soon examine this DNS lookup process in more detail. But let’s first take a closer look at 
these three classes of DNS servers: Root DNS servers. There are over 400 root name servers 
scattered all over the world. Figure 2.18 shows the countries that have root names servers, with 
countries having more than ten darkly shaded. These root name servers are managed by 13 
different organizations. The full list of root name servers, along with the organizations that 
manage them and their IP addresses can be found at [Root Servers 2016]. Root name servers 
provide the IP addresses of the TLD servers. Top-level domain (TLD) servers. For each of the 
top-level domains — top-level domains such as com, org, net, edu, and gov, and all of the 
country top-level domains such as uk, fr, ca, and jp — there is TLD server (or server cluster). The 
company Verisign Global Registry Services maintains the TLD servers for the com top-level 
domain, and the company Educause maintains the TLD servers for the edu top-level domain. 
The network infrastructure supporting a TLD can be large and complex; see [Osterweil 2012] for 
a nice overview of the Verisign network. See [TLD list 2016] for a list of all top-level domains. 
TLD servers provide the IP addresses for authoritative DNS servers. Figure 2.18 DNS root 
servers in 2016 Authoritative DNS servers. Every organization with publicly accessible hosts 
(such as Web servers and mail servers) on the Internet must provide publicly accessible DNS 
records that map the names of those hosts to IP addresses. An organization’s authoritative 
DNS server houses these DNS records. An organization can choose to implement its own 
authoritative DNS server to hold these records; alternatively, the organization can pay to have 
these records stored in an authoritative DNS server of some service provider. Most universities 


## Page 2

and large companies implement and maintain their own primary and secondary (backup) 
authoritative DNS server. The root, TLD, and authoritative DNS servers all belong to the 
hierarchy of DNS servers, as shown in Figure 2.17. There is another important type of DNS 
server called the local DNS server. A local DNS server does not strictly belong to the hierarchy 
of servers but is nevertheless central to the DNS architecture. Each ISP—such as a residential 
ISP or an institutional ISP—has a local DNS server (also called a default name server). When a 
host connects to an ISP, the ISP provides the host with the IP addresses of one or more of its 
local DNS servers (typically through DHCP, which is discussed in Chapter 4). You can easily 
determine the IP address of your local DNS server by accessing network status windows in 
Windows or UNIX. A host’s local DNS server is typically “close to” the host. For an institutional 
ISP, the local DNS server may be on the same LAN as the host; for a residential ISP, it is typically 
separated from the host by no more than a few routers. When a host makes a DNS query, the 
query is sent to the local DNS server, which acts a proxy, forwarding the query into the DNS 
server hierarchy, as we’ll discuss in more detail below. Let’s take a look at a simple example. 
Suppose the host cse.nyu.edu desires the IP address of gaia.cs.umass.edu . Also suppose that 
NYU’s ocal DNS server for cse.nyu.edu is called dns.nyu.edu and that an authoritative DNS 
server for gaia.cs.umass.edu is called dns.umass.edu . As shown in Figure 2.19, the host 
cse.nyu.edu first sends a DNS query message to its local DNS server, dns.nyu.edu . The query 
message contains the hostname to be translated, namely, gaia.cs.umass.edu . The local DNS 
server forwards the query message to a root DNS server. The root DNS server takes note of the 
edu suffix and returns to the local DNS server a list of IP addresses for TLD servers responsible 
for edu . The local DNS server then resends the query message to one of these TLD servers. The 
TLD server takes note of the umass.edu suffix and responds with the IP address of the 
authoritative DNS server for the University of Massachusetts, namely, dns.umass.edu . Finally, 
the local DNS server resends the query message directly to dns.umass.edu , which responds 
with the IP address of gaia.cs.umass.edu . Note that in this example, in order to obtain the 
mapping for one hostname, eight DNS messages were sent: four query messages and four reply 
messages! We’ll soon see how DNS caching reduces this query traffic. Our previous example 
assumed that the TLD server knows the authoritative DNS server for the hostname. In general 
this not always true. Instead, the TLD server Figure 2.19 Interaction of the various DNS servers 
may know only of an intermediate DNS server, which in turn knows the authoritative DNS server 
for the hostname. For example, suppose again that the University of Massachusetts has a DNS 
server for the university, called dns.umass.edu . Also suppose that each of the departments at 
the University of Massachusetts has its own DNS server, and that each departmental DNS 
server is authoritative for all hosts in the department. In this case, when the intermediate DNS 
server, dns.umass.edu , receives a query for a host with a hostname ending with cs.umass.edu 
, it returns to dns.nyu.edu the IP address of dns.cs.umass.edu , which is authoritative for all 
hostnames ending with cs.umass.edu . The local DNS server dns.nyu.edu then sends the query 
to the authoritative DNS server, which returns the desired mapping to the local DNS server, 
which in turn returns the mapping to the requesting host. In this case, a total of 10 DNS 
messages are sent! The example shown in Figure 2.19 makes use of both recursive queries and 
iterative queries. The query sent from cse.nyu.edu to dns.nyu.edu is a recursive query, since 
the query asks dns.nyu.edu to obtain the mapping on its behalf. But the subsequent three 
queries are iterative since all of the replies are directly returned to dns.nyu.edu . In theory, any 
DNS query can be iterative or recursive. For example, Figure 2.20 shows a DNS query chain for 
which all of the queries are recursive. In practice, the queries typically follow the pattern in 
Figure 2.19: The query from the requesting host to the local DNS server is recursive, and the 
remaining queries are iterative. DNS Caching Our discussion thus far has ignored DNS caching, 


## Page 3

a critically important feature of the DNS system. In truth, DNS extensively exploits DNS caching 
in order to improve the delay performance and to reduce the number of DNS messages Figure 
2.20 Recursive queries in DNS ricocheting around the Internet. The idea behind DNS caching is 
very simple. In a query chain, when a DNS server receives a DNS reply (containing, for example, 
a mapping from a hostname to an IP address), it can cache the mapping in its local memory. For 
example, in Figure 2.19, each time the local DNS server dns.nyu.edu receives a reply from some 
DNS server, it can cache any of the information contained in the reply. If a hostname/IP address 
pair is cached in a DNS server and another query arrives to the DNS server for the same 
hostname, the DNS server can provide the desired IP address, even if it is not authoritative for 
the hostname. Because hosts and mappings between hostnames and IP addresses are by no 
means permanent, DNS servers discard cached information after a period of time (often set to 
two days). As an example, suppose that a host apricot.nyu.edu queries dns.nyu.edu for the IP 
address for the hostname cnn.com . Furthermore, suppose that a few hours later, another NYU 
host, say, kiwi.nyu.edu , also queries dns.nyu.edu with the same hostname. Because of 
caching, the local DNS server will be able to immediately return the IP address of cnn.com to 
this second requesting host without having to query any other DNS servers. A local DNS server 
can also cache the IP addresses of TLD servers, thereby allowing the local DNS server to bypass 
the root DNS servers in a query chain. In fact, because of caching, root servers are bypassed for 
all but a very small fraction of DNS queries. 2.4.3 DNS Records and Messages The DNS servers 
that together implement the DNS distributed database store resource records (RRs), including 
RRs that provide hostname-to-IP address mappings. Each DNS reply message carries one or 
more resource records. In this and the following subsection, we provide a brief overview of DNS 
resource records and messages; more details can be found in [Albitz 1993] or in the DNS RFCs 
[RFC 1034; RFC 1035]. A resource record is a four-tuple that contains the following fields: 
(Name, Value, Type, TTL) TTL is the time to live of the resource record; it determines when a 
resource should be removed from a cache. In the example records given below, we ignore the 
TTL field. The meaning of Name and Value depend on Type : If Type=A , then Name is a 
hostname and Value is the IP address for the hostname. Thus, a Type A record provides the 
standard hostname-to-IP address mapping. As an example, (relay1.bar.foo.com, 
145.37.93.126, A) is a Type A record. If Type=NS , then Name is a domain (such as foo.com ) and 
Value is the hostname of an authoritative DNS server that knows how to obtain the IP addresses 
for hosts in the domain. This record is used to route DNS queries further along in the query 
chain. As an example, (foo.com, dns.foo.com, NS) is a Type NS record. If Type=CNAME , then 
Value is a canonical hostname for the alias hostname Name . This record can provide querying 
hosts the canonical name for a hostname. As an example, (foo.com, relay1.bar.foo.com, 
CNAME) is a CNAME record. If Type=MX , then Value is the canonical name of a mail server that 
has an alias hostname Name . As an example, (foo.com, mail.bar.foo.com, MX) is an MX 
record. MX records allow the hostnames of mail servers to have simple aliases. Note that by 
using the MX record, a company can have the same aliased name for its mail server and for one 
of its other servers (such as its Web server). To obtain the canonical name for the mail server, a 
DNS client would query for an MX record; to obtain the canonical name for the other server, the 
DNS client would query for the CNAME record. If a DNS server is authoritative for a particular 
hostname, then the DNS server will contain a Type A record for the hostname. (Even if the DNS 
server is not authoritative, it may contain a Type A record in its cache.) If a server is not 
authoritative for a hostname, then the server will contain a Type NS record for the domain that 
includes the hostname; it will also contain a Type A record that provides the IP address of the 
DNS server in the Value field of the NS record. As an example, suppose an edu TLD server is not 
authoritative for the host gaia.cs.umass.edu . Then this server will contain a record for a domain 


## Page 4

that includes the host gaia.cs.umass.edu , for example, (umass.edu, dns.umass.edu, NS) . The 
edu TLD server would also contain a Type A record, which maps the DNS server dns.umass.edu 
to an IP address, for example, (dns.umass.edu, 128.119.40.111, A) . DNS Messages Earlier in 
this section, we referred to DNS query and reply messages. These are the only two kinds of DNS 
messages. Furthermore, both query and reply messages have the same format, as shown in 
Figure 2.21.The semantics of the various fields in a DNS message are as follows: The first 12 
bytes is the header section, which has a number of fields. The first field is a 16-bit number that 
identifies the query. This identifier is copied into the reply message to a query, allowing the 
client to match received replies with sent queries. There are a number of flags in the flag field. A 
1-bit query/reply flag indicates whether the message is a query (0) or a reply (1). A 1-bit 
authoritative flag is Figure 2.21 DNS message format set in a reply message when a DNS server 
is an authoritative server for a queried name. A 1-bit recursion-desired flag is set when a client 
(host or DNS server) desires that the DNS server perform recursion when it doesn’t have the 
record. A 1-bit recursion-available field is set in a reply if the DNS server supports recursion. In 
the header, there are also four number-of fields. These fields indicate the number of 
occurrences of the four types of data sections that follow the header. The question section 
contains information about the query that is being made. This section includes (1) a name field 
that contains the name that is being queried, and (2) a type field that indicates the type of 
question being asked about the name—for example, a host address associated with a name 
(Type A) or the mail server for a name (Type MX). In a reply from a DNS server, the answer 
section contains the resource records for the name that was originally queried. Recall that in 
each resource record there is the Type (for example, A, NS, CNAME, and MX), the Value , and 
the TTL . A reply can return multiple RRs in the answer, since a hostname can have multiple IP 
addresses (for example, for replicated Web servers, as discussed earlier in this section). The 
authority section contains records of other authoritative servers. The additional section 
contains other helpful records. For example, the answer field in a reply to an MX query contains 
a resource record providing the canonical hostname of a mail server. The additional section 
contains a Type A record providing the IP address for the canonical hostname of the mail server. 
How would you like to send a DNS query message directly from the host you’re working on to 
some DNS server? This can easily be done with the nslookup program, which is available from 
most Windows and UNIX platforms. For example, from a Windows host, open the Command 
Prompt and invoke the nslookup program by simply typing “nslookup.” After invoking nslookup, 
you can send a DNS query to any DNS server (root, TLD, or authoritative). After receiving the 
reply message from the DNS server, nslookup will display the records included in the reply (in a 
human-readable format). As an alternative to running nslookup from your own host, you can 
visit one of many Web sites that allow you to remotely employ nslookup. (Just type “nslookup” 
into a search engine and you’ll be brought to one of these sites.) The DNS Wireshark lab at the 
end of this chapter will allow you to explore the DNS in much more detail. Inserting Records into 
the DNS Database The discussion above focused on how records are retrieved from the DNS 
database. You might be wondering how records get into the database in the first place. Let’s 
look at how this is done in the context of a specific example. Suppose you have just created an 
exciting new startup company called Network Utopia. The first thing you’ll surely want to do is 
register the domain name networkutopia.com at a registrar. A registrar is a commercial entity 
that verifies the uniqueness of the domain name, enters the domain name into the DNS 
database (as discussed below), and collects a small fee from you for its services. Prior to 1999, 
a single registrar, Network Solutions, had a monopoly on domain name registration for com , 
net , and org domains. But now there are many registrars competing for customers, and the 
Internet Corporation for Assigned Names and Numbers (ICANN) accredits the various 


## Page 5

registrars. A complete list of accredited registrars is available at http:// www.internic.net . 
When you register the domain name networkutopia.com with some registrar, you also need to 
provide the registrar with the names and IP addresses of your primary and secondary 
authoritative DNS servers. Suppose the names and IP addresses are dns1.networkutopia.com , 
dns2.networkutopia.com , 212.2.212.1, and 212.212.212.2. For each of these two authoritative 
DNS servers, the registrar would then make sure that a Type NS and a Type A record are entered 
into the TLD com servers. Specifically, for the primary authoritative server for 
networkutopia.com , the registrar would insert the following two resource records into the DNS 
system: (networkutopia.com, dns1.networkutopia.com, NS) (dns1.networkutopia.com, 
212.212.212.1, A) You’ll also have to make sure that the Type A resource record for your Web 
server www.networkutopia.com and the Type MX resource record for your mail server 
mail.networkutopia.com are entered into your authoritative DNS FOCUS ON SECURITY DNS 
VULNERABILITIES We have seen that DNS is a critical component of the Internet infrastructure, 
with many important services—including the Web and e-mail—simply incapable of functioning 
without it. We therefore naturally ask, how can DNS be attacked? Is DNS a sitting duck, waiting 
to be knocked out of service, while taking most Internet applications down with it? The first type 
of attack that comes to mind is a DDoS bandwidth-flooding attack (see Section 1.6) against 
DNS servers. For example, an attacker could attempt to send to each DNS root server a deluge 
of packets, so many that the majority of legitimate DNS queries never get answered. Such a 
large-scale DDoS attack against DNS root servers actually took place on October 21, 2002. In 
this attack, the attackers leveraged a botnet to send truck loads of ICMP ping messages to each 
of the 13 DNS root IP addresses. (ICMP messages are discussed in Section 5.6. For now, it 
suffices to know that ICMP packets are special types of IP datagrams.) Fortunately, this large-
scale attack caused minimal damage, having little or no impact on users’ Internet experience. 
The attackers did succeed at directing a deluge of packets at the root servers. But many of the 
DNS root servers were protected by packet filters, configured to always block all ICMP ping 
messages directed at the root servers. These protected servers were thus spared and 
functioned as normal. Furthermore, most local DNS servers cache the IP addresses of top-
level-domain servers, allowing the query process to often bypass the DNS root servers. A 
potentially more effective DDoS attack against DNS would be send a deluge of DNS queries to 
top-level-domain servers, for example, to all the top-level-domain servers that handle the .com 
domain. It would be harder to filter DNS queries directed to DNS servers; and top-level-domain 
servers are not as easily bypassed as are root servers. But the severity of such an attack would 
be partially mitigated by caching in local DNS servers. DNS could potentially be attacked in 
other ways. In a man-in-the-middle attack, the attacker intercepts queries from hosts and 
returns bogus replies. In the DNS poisoning attack, the attacker sends bogus replies to a DNS 
server, tricking the server into accepting bogus records into its cache. Either of these attacks 
could be used, for example, to redirect an unsuspecting Web user to the attacker’s Web site. 
These attacks, however, are difficult to implement, as they require intercepting packets or 
throttling servers [Skoudis 2006]. In summary, DNS has demonstrated itself to be surprisingly 
robust against attacks. To date, there hasn’t been an attack that has successfully impeded the 
DNS service. servers. (Until recently, the contents of each DNS server were configured 
statically, for example, from a configuration file created by a system manager. More recently, 
an UPDATE option has been added to the DNS protocol to allow data to be dynamically added 
or deleted from the database via DNS messages. [RFC 2136] and [RFC 3007] specify DNS 
dynamic updates.) Once all of these steps are completed, people will be able to visit your Web 
site and send e-mail to the employees at your company. Let’s conclude our discussion of DNS 
by verifying that this statement is true. This verification also helps to solidify what we have 


## Page 6

learned about DNS. Suppose Alice in Australia wants to view the Web page 
www.networkutopia.com . As discussed earlier, her host will first send a DNS query to her local 
DNS server. The local DNS server will then contact a TLD com server. (The local DNS server will 
also have to contact a root DNS server if the address of a TLD com server is not cached.) This 
TLD server contains the Type NS and Type A resource records listed above, because the 
registrar had these resource records inserted into all of the TLD com servers. The TLD com 
server sends a reply to Alice’s local DNS server, with the reply containing the two resource 
records. The local DNS server then sends a DNS query to 212.212.212.1 , asking for the Type A 
record corresponding to www.networkutopia.com . This record provides the IP address of the 
desired Web server, say, 212.212.71.4 , which the local DNS server passes back to Alice’s host. 
Alice’s browser can now initiate a TCP connection to the host 212.212.71.4 and send an HTTP 
request over the connection. Whew! There’s a lot more going on than what meets the eye when 
one surfs the Web! 2.5 Peer-to-Peer File Distribution The applications described in this chapter 
thus far—including the Web, e-mail, and DNS—all employ client-server architectures with 
significant reliance on always-on infrastructure servers. Recall from Section 2.1.1 that with a 
P2P architecture, there is minimal (or no) reliance on always-on infrastructure servers. Instead, 
pairs of intermittently connected hosts, called peers, communicate directly with each other. 
The peers are not owned by a service provider, but are instead desktops and laptops controlled 
by users. In this section we consider a very natural P2P application, namely, distributing a large 
file from a single server to a large number of hosts (called peers). The file might be a new version 
of the Linux operating system, a software patch for an existing operating system or application, 
an MP3 music file, or an MPEG video file. In client-server file distribution, the server must send a 
copy of the file to each of the peers—placing an enormous burden on the server and consuming 
a large amount of server bandwidth. In P2P file distribution, each peer can redistribute any 
portion of the file it has received to any other peers, thereby assisting the server in the 
distribution process. As of 2016, the most popular P2P file distribution protocol is BitTorrent. 
Originally developed by Bram Cohen, there are now many different independent BitTorrent 
clients conforming to the BitTorrent protocol, just as there are a number of Web browser clients 
that conform to the HTTP protocol. In this subsection, we first examine the selfscalability of P2P 
architectures in the context of file distribution. We then describe BitTorrent in some detail, 
highlighting its most important characteristics and features. Scalability of P2P Architectures To 
compare client-server architectures with peer-to-peer architectures, and illustrate the inherent 
selfscalability of P2P, we now consider a simple quantitative model for distributing a file to a 
fixed set of peers for both architecture types. As shown in Figure 2.22, the server and the peers 
are connected to the Internet with access links. Denote the upload rate of the server’s access 
link by u , the upload rate of the ith peer’s access link by u, and the download rate of the ith 
peer’s access link by d. Also denote the size of the file to be distributed (in bits) by F and the 
number of peers that want to obtain a copy of the file by N. The distribution time is the time it 
takes to get s i i Figure 2.22 An illustrative file distribution problem a copy of the file to all N 
peers. In our analysis of the distribution time below, for both client-server and P2P 
architectures, we make the simplifying (and generally accurate [Akella 2003]) assumption that 
the Internet core has abundant bandwidth, implying that all of the bottlenecks are in access 
networks. We also suppose that the server and clients are not participating in any other network 
applications, so that all of their upload and download access bandwidth can be fully devoted to 
distributing this file. Let’s first determine the distribution time for the client-server architecture, 
which we denote by D . In the client-server architecture, none of the peers aids in distributing 
the file. We make the following observations: The server must transmit one copy of the file to 
each of the N peers. Thus the server must transmit NF bits. Since the server’s upload rate is u , 


## Page 7

the time to distribute the file must be at least NF/u . Let d denote the download rate of the peer 
with the lowest download rate, that is, The peer with the lowest download rate cannot obtain all 
F bits of the file in less than F/d seconds. Thus the minimum distribution time is at least F/d . 
Putting these two observations together, we obtain cs s s min dmin=min{d1,dp,. . .,dN}. min min 
Dcs≥max{NFus,Fdmin}. This provides a lower bound on the minimum distribution time for the 
client-server architecture. In the homework problems you will be asked to show that the server 
can schedule its transmissions so that the lower bound is actually achieved. So let’s take this 
lower bound provided above as the actual distribution time, that is, We see from Equation 2.1 
that for N large enough, the client-server distribution time is given by NF/u . Thus, the 
distribution time increases linearly with the number of peers N. So, for example, if the number 
of peers from one week to the next increases a thousand-fold from a thousand to a million, the 
time required to distribute the file to all peers increases by 1,000. Let’s now go through a similar 
analysis for the P2P architecture, where each peer can assist the server in distributing the file. 
In particular, when a peer receives some file data, it can use its own upload capacity to 
redistribute the data to other peers. Calculating the distribution time for the P2P architecture is 
somewhat more complicated than for the client-server architecture, since the distribution time 
depends on how each peer distributes portions of the file to the other peers. Nevertheless, a 
simple expression for the minimal distribution time can be obtained [Kumar 2006]. To this end, 
we first make the following observations: At the beginning of the distribution, only the server 
has the file. To get this file into the community of peers, the server must send each bit of the file 
at least once into its access link. Thus, the minimum distribution time is at least F/u . (Unlike 
the client-server scheme, a bit sent once by the server may not have to be sent by the server 
again, as the peers may redistribute the bit among themselves.) As with the client-server 
architecture, the peer with the lowest download rate cannot obtain all F bits of the file in less 
than F/d seconds. Thus the minimum distribution time is at least F/d . Finally, observe that the 
total upload capacity of the system as a whole is equal to the upload rate of the server plus the 
upload rates of each of the individual peers, that is, The system must deliver (upload) F bits to 
each of the N peers, thus delivering a total of NF bits. This cannot be done at a rate faster than u 
. Thus, the minimum distribution time is also at least Putting these three observations together, 
we obtain the minimum distribution time for P2P, denoted by D . Equation 2.2 provides a lower 
bound for the minimum distribution time for the P2P architecture. It turns out that if we imagine 
that each peer can redistribute a bit as soon as it receives the bit, then there is a 
Dcs=max{NFus,Fdmin} (2.1) s s min min utotal=us+u1+⋯+uN. total NF/(us+u1+⋯+uN). P2P 
DP2P≥max{Fus,Fdmin,NFus+∑i=1Nui} (2.2) redistribution scheme that actually achieves this 
lower bound [Kumar 2006]. (We will prove a special case of this result in the homework.) In 
reality, where chunks of the file are redistributed rather than individual bits, Equation 2.2 serves 
as a good approximation of the actual minimum distribution time. Thus, let’s take the lower 
bound provided by Equation 2.2 as the actual minimum distribution time, that is, Figure 2.23 
compares the minimum distribution time for the client-server and P2P architectures assuming 
that all peers have the same upload rate u. In Figure 2.23, we have set and Thus, a peer can 
transmit the entire file in one hour, the server transmission rate is 10 times the peer upload 
rate, Figure 2.23 Distribution time for P2P and client-server architectures and (for simplicity) the 
peer download rates are set large enough so as not to have an effect. We see from Figure 2.23 
that for the client-server architecture, the distribution time increases linearly and without 
bound as the number of peers increases. However, for the P2P architecture, the minimal 
distribution time is not only always less than the distribution time of the client-server 
architecture; it is also less than one hour for any number of peers N. Thus, applications with the 
P2P architecture can be self-scaling. This scalability is a direct consequence of peers being 


## Page 8

redistributors as well as consumers of bits. BitTorrent BitTorrent is a popular P2P protocol for 
file distribution [Chao 2011]. In BitTorrent lingo, the collection of 
DP2P=max{Fus,Fdmin,NFus+∑i=1Nui} (2.3) F/u=1 hour, us=10u, dmin≥us. all peers 
participating in the distribution of a particular file is called a torrent. Peers in a torrent download 
equal-size chunks of the file from one another, with a typical chunk size of 256 KBytes. When a 
peer first joins a torrent, it has no chunks. Over time it accumulates more and more chunks. 
While it downloads chunks it also uploads chunks to other peers. Once a peer has acquired the 
entire file, it may (selfishly) leave the torrent, or (altruistically) remain in the torrent and 
continue to upload chunks to other peers. Also, any peer may leave the torrent at any time with 
only a subset of chunks, and later rejoin the torrent. Let’s now take a closer look at how 
BitTorrent operates. Since BitTorrent is a rather complicated protocol and system, we’ll only 
describe its most important mechanisms, sweeping some of the details under the rug; this will 
allow us to see the forest through the trees. Each torrent has an infrastructure node called a 
tracker. Figure 2.24 File distribution with BitTorrent When a peer joins a torrent, it registers itself 
with the tracker and periodically informs the tracker that it is still in the torrent. In this manner, 
the tracker keeps track of the peers that are participating in the torrent. A given torrent may 
have fewer than ten or more than a thousand peers participating at any instant of time. As 
shown in Figure 2.24, when a new peer, Alice, joins the torrent, the tracker randomly selects a 
subset of peers (for concreteness, say 50) from the set of participating peers, and sends the IP 
addresses of these 50 peers to Alice. Possessing this list of peers, Alice attempts to establish 
concurrent TCP connections with all the peers on this list. Let’s call all the peers with which 
Alice succeeds in establishing a TCP connection “neighboring peers.” (In Figure 2.24, Alice is 
shown to have only three neighboring peers. Normally, she would have many more.) As time 
evolves, some of these peers may leave and other peers (outside the initial 50) may attempt to 
establish TCP connections with Alice. So a peer’s neighboring peers will fluctuate over time. At 
any given time, each peer will have a subset of chunks from the file, with different peers having 
different subsets. Periodically, Alice will ask each of her neighboring peers (over the TCP 
connections) for the list of the chunks they have. If Alice has L different neighbors, she will 
obtain L lists of chunks. With this knowledge, Alice will issue requests (again over the TCP 
connections) for chunks she currently does not have. So at any given instant of time, Alice will 
have a subset of chunks and will know which chunks her neighbors have. With this information, 
Alice will have two important decisions to make. First, which chunks should she request first 
from her neighbors? And second, to which of her neighbors should she send requested chunks? 
In deciding which chunks to request, Alice uses a technique called rarest first. The idea is to 
determine, from among the chunks she does not have, the chunks that are the rarest among her 
neighbors (that is, the chunks that have the fewest repeated copies among her neighbors) and 
then request those rarest chunks first. In this manner, the rarest chunks get more quickly 
redistributed, aiming to (roughly) equalize the numbers of copies of each chunk in the torrent. 
To determine which requests she responds to, BitTorrent uses a clever trading algorithm. The 
basic idea is that Alice gives priority to the neighbors that are currently supplying her data at the 
highest rate. Specifically, for each of her neighbors, Alice continually measures the rate at 
which she receives bits and determines the four peers that are feeding her bits at the highest 
rate. She then reciprocates by sending chunks to these same four peers. Every 10 seconds, she 
recalculates the rates and possibly modifies the set of four peers. In BitTorrent lingo, these four 
peers are said to be unchoked. Importantly, every 30 seconds, she also picks one additional 
neighbor at random and sends it chunks. Let’s call the randomly chosen peer Bob. In BitTorrent 
lingo, Bob is said to be optimistically unchoked. Because Alice is sending data to Bob, she may 
become one of Bob’s top four uploaders, in which case Bob would start to send data to Alice. If 


## Page 9

the rate at which Bob sends data to Alice is high enough, Bob could then, in turn, become one 
of Alice’s top four uploaders. In other words, every 30 seconds, Alice will randomly choose a 
new trading partner and initiate trading with that partner. If the two peers are satisfied with the 
trading, they will put each other in their top four lists and continue trading with each other until 
one of the peers finds a better partner. The effect is that peers capable of uploading at 
compatible rates tend to find each other. The random neighbor selection also allows new peers 
to get chunks, so that they can have something to trade. All other neighboring peers besides 
these five peers (four “top” peers and one probing peer) are “choked,” that is, they do not 
receive any chunks from Alice. BitTorrent has a number of interesting mechanisms that are not 
discussed here, including pieces (minichunks), pipelining, random first selection, endgame 
mode, and anti-snubbing [Cohen 2003]. The incentive mechanism for trading just described is 
often referred to as tit-for-tat [Cohen 2003]. It has been shown that this incentive scheme can 
be circumvented [Liogkas 2006; Locher 2006; Piatek 2007]. Nevertheless, the BitTorrent 
ecosystem is wildly successful, with millions of simultaneous peers actively sharing files in 
hundreds of thousands of torrents. If BitTorrent had been designed without tit-fortat (or a 
variant), but otherwise exactly the same, BitTorrent would likely not even exist now, as the 
majority of the users would have been freeriders [Saroiu 2002]. We close our discussion on P2P 
by briefly mentioning another application of P2P, namely, Distributed Hast Table (DHT). A 
distributed hash table is a simple database, with the database records being distributed over 
the peers in a P2P system. DHTs have been widely implemented (e.g., in BitTorrent) and have 
been the subject of extensive research. An overview is provided in a Video Note in the 
companion website. Walking though distributed hash tables 2.6 Video Streaming and Content 
Distribution Networks Streaming prerecorded video now accounts for the majority of the traffic 
in residential ISPs in North America. In particular, the Netflix and YouTube services alone 
consumed a whopping 37% and 16%, respectively, of residential ISP traffic in 2015 [Sandvine 
2015]. In this section we will provide an overview of how popular video streaming services are 
implemented in today’s Internet. We will see they are implemented using application-level 
protocols and servers that function in some ways like a cache. In Chapter 9, devoted to 
multimedia networking, we will further examine Internet video as well as other Internet 
multimedia services. 2.6.1 Internet Video In streaming stored video applications, the underlying 
medium is prerecorded video, such as a movie, a television show, a prerecorded sporting 
event, or a prerecorded user-generated video (such as those commonly seen on YouTube). 
These prerecorded videos are placed on servers, and users send requests to the servers to view 
the videos on demand. Many Internet companies today provide streaming video, including, 
Netflix, YouTube (Google), Amazon, and Youku. But before launching into a discussion of video 
streaming, we should first get a quick feel for the video medium itself. A video is a sequence of 
images, typically being displayed at a constant rate, for example, at 24 or 30 images per 
second. An uncompressed, digitally encoded image consists of an array of pixels, with each 
pixel encoded into a number of bits to represent luminance and color. An important 
characteristic of video is that it can be compressed, thereby trading off video quality with bit 
rate. Today’s off-the-shelf compression algorithms can compress a video to essentially any bit 
rate desired. Of course, the higher the bit rate, the better the image quality and the better the 
overall user viewing experience. From a networking perspective, perhaps the most salient 
characteristic of video is its high bit rate. Compressed Internet video typically ranges from 100 
kbps for low-quality video to over 3 Mbps for streaming high-definition movies; 4K streaming 
envisions a bitrate of more than 10 Mbps. This can translate to huge amount of traffic and 
storage, particularly for high-end video. For example, a single 2 Mbps video with a duration of 67 
minutes will consume 1 gigabyte of storage and traffic. By far, the most important performance 


## Page 10

measure for streaming video is average end-to-end throughput. In order to provide continuous 
playout, the network must provide an average throughput to the streaming application that is at 
least as large as the bit rate of the compressed video. We can also use compression to create 
multiple versions of the same video, each at a different quality level. For example, we can use 
compression to create, say, three versions of the same video, at rates of 300 kbps, 1 Mbps, and 
3 Mbps. Users can then decide which version they want to watch as a function of their current 
available bandwidth. Users with high-speed Internet connections might choose the 3 Mbps 
version; users watching the video over 3G with a smartphone might choose the 300 kbps 
version. 2.6.2 HTTP Streaming and DASH In HTTP streaming, the video is simply stored at an 
HTTP server as an ordinary file with a specific URL. When a user wants to see the video, the 
client establishes a TCP connection with the server and issues an HTTP GET request for that 
URL. The server then sends the video file, within an HTTP response message, as quickly as the 
underlying network protocols and traffic conditions will allow. On the client side, the bytes are 
collected in a client application buffer. Once the number of bytes in this buffer exceeds a 
predetermined threshold, the client application begins playback—specifically, the streaming 
video application periodically grabs video frames from the client application buffer, 
decompresses the frames, and displays them on the user’s screen. Thus, the video streaming 
application is displaying video as it is receiving and buffering frames corresponding to latter 
parts of the video. Although HTTP streaming, as described in the previous paragraph, has been 
extensively deployed in practice (for example, by YouTube since its inception), it has a major 
shortcoming: All clients receive the same encoding of the video, despite the large variations in 
the amount of bandwidth available to a client, both across different clients and also over time 
for the same client. This has led to the development of a new type of HTTP-based streaming, 
often referred to as Dynamic Adaptive Streaming over HTTP (DASH). In DASH, the video is 
encoded into several different versions, with each version having a different bit rate and, 
correspondingly, a different quality level. The client dynamically requests chunks of video 
segments of a few seconds in length. When the amount of available bandwidth is high, the 
client naturally selects chunks from a high-rate version; and when the available bandwidth is 
low, it naturally selects from a low-rate version. The client selects different chunks one at a 
time with HTTP GET request messages [Akhshabi 2011]. DASH allows clients with different 
Internet access rates to stream in video at different encoding rates. Clients with low-speed 3G 
connections can receive a low bit-rate (and low-quality) version, and clients with fiber 
connections can receive a high-quality version. DASH also allows a client to adapt to the 
available bandwidth if the available end-to-end bandwidth changes during the session. This 
feature is particularly important for mobile users, who typically see their bandwidth availability 
fluctuate as they move with respect to the base stations. With DASH, each video version is 
stored in the HTTP server, each with a different URL. The HTTP server also has a manifest file, 
which provides a URL for each version along with its bit rate. The client first requests the 
manifest file and learns about the various versions. The client then selects one chunk at a time 
by specifying a URL and a byte range in an HTTP GET request message for each chunk. While 
downloading chunks, the client also measures the received bandwidth and runs a rate 
determination algorithm to select the chunk to request next. Naturally, if the client has a lot of 
video buffered and if the measured receive bandwidth is high, it will choose a chunk from a 
high-bitrate version. And naturally if the client has little video buffered and the measured 
received bandwidth is low, it will choose a chunk from a low-bitrate version. DASH therefore 
allows the client to freely switch among different quality levels. 2.6.3 Content Distribution 
Networks Today, many Internet video companies are distributing on-demand multi-Mbps 
streams to millions of users on a daily basis. YouTube, for example, with a library of hundreds of 


## Page 11

millions of videos, distributes hundreds of millions of video streams to users around the world 
every day. Streaming all this traffic to locations all over the world while providing continuous 
playout and high interactivity is clearly a challenging task. For an Internet video company, 
perhaps the most straightforward approach to providing streaming video service is to build a 
single massive data center, store all of its videos in the data center, and stream the videos 
directly from the data center to clients worldwide. But there are three major problems with this 
approach. First, if the client is far from the data center, server-to-client packets will cross many 
communication links and likely pass through many ISPs, with some of the ISPs possibly located 
on different continents. If one of these links provides a throughput that is less than the video 
consumption rate, the end-to-end throughput will also be below the consumption rate, 
resulting in annoying freezing delays for the user. (Recall from Chapter 1 that the end-to-end 
throughput of a stream is governed by the throughput at the bottleneck link.) The likelihood of 
this happening increases as the number of links in the end-to-end path increases. A second 
drawback is that a popular video will likely be sent many times over the same communication 
links. Not only does this waste network bandwidth, but the Internet video company itself will be 
paying its provider ISP (connected to the data center) for sending the same bytes into the 
Internet over and over again. A third problem with this solution is that a single data center 
represents a single point of failure—if the data center or its links to the Internet goes down, it 
would not be able to distribute any video streams. In order to meet the challenge of distributing 
massive amounts of video data to users distributed around the world, almost all major video-
streaming companies make use of Content Distribution Networks (CDNs). A CDN manages 
servers in multiple geographically distributed locations, stores copies of the videos (and other 
types of Web content, including documents, images, and audio) in its servers, and attempts to 
direct each user request to a CDN location that will provide the best user experience. The CDN 
may be a private CDN, that is, owned by the content provider itself; for example, Google’s CDN 
distributes YouTube videos and other types of content. The CDN may alternatively be a third-
party CDN that distributes content on behalf of multiple content providers; Akamai, Limelight 
and Level-3 all operate third-party CDNs. A very readable overview of modern CDNs is [Leighton 
2009; Nygren 2010]. CDNs typically adopt one of two different server placement philosophies 
[Huang 2008]: Enter Deep. One philosophy, pioneered by Akamai, is to enter deep into the 
access networks of Internet Service Providers, by deploying server clusters in access ISPs all 
over the world. (Access networks are described in Section 1.3.) Akamai takes this approach 
with clusters in approximately 1,700 locations. The goal is to get close to end users, thereby 
improving user-perceived delay and throughput by decreasing the number of links and routers 
between the end user and the CDN server from which it receives content. Because of this highly 
distributed design, the task of maintaining and managing the clusters becomes challenging. 
Bring Home. A second design philosophy, taken by Limelight and many other CDN companies, 
is to bring the ISPs home by building large clusters at a smaller number (for example, tens) of 
sites. Instead of getting inside the access ISPs, these CDNs typically place their clusters in 
Internet Exchange Points (IXPs) (see Section 1.3). Compared with the enter-deep design 
philosophy, the bring-home design typically results in lower maintenance and management 
overhead, possibly at the expense of higher delay and lower throughput to end users. Once its 
clusters are in place, the CDN replicates content across its clusters. The CDN may not want to 
place a copy of every video in each cluster, since some videos are rarely viewed or are only 
popular in some countries. In fact, many CDNs do not push videos to their clusters but instead 
use a simple pull strategy: If a client requests a video from a cluster that is not storing the video, 
then the cluster retrieves the video (from a central repository or from another cluster) and 
stores a copy locally while streaming the video to the client at the same time. Similar Web 


## Page 12

caching (see Section 2.2.5), when a cluster’s storage becomes full, it removes videos that are 
not frequently requested. CDN Operation Having identified the two major approaches toward 
deploying a CDN, let’s now dive down into the nuts and bolts of how a CDN operates. When a 
browser in a user’s CASE STUDY GOOGLE’S NETWORK INFRASTRUCTURE To support its vast 
array of cloud services—including search, Gmail, calendar, YouTube video, maps, documents, 
and social networks—Google has deployed an extensive private network and CDN 
infrastructure. Google’s CDN infrastructure has three tiers of server clusters: Fourteen “mega 
data centers,” with eight in North America, four in Europe, and two in Asia [Google Locations 
2016], with each data center having on the order of 100,000 servers. These mega data centers 
are responsible for serving dynamic (and often personalized) content, including search results 
and Gmail messages. An estimated 50 clusters in IXPs scattered throughout the world, with 
each cluster consisting on the order of 100–500 servers [Adhikari 2011a]. These clusters are 
responsible for serving static content, including YouTube videos [Adhikari 2011a]. Many 
hundreds of “enter-deep” clusters located within an access ISP. Here a cluster typically 
consists of tens of servers within a single rack. These enter-deep servers perform TCP splitting 
(see Section 3.7) and serve static content [Chen 2011], including the static portions of Web 
pages that embody search results. All of these data centers and cluster locations are 
networked together with Google’s own private network. When a user makes a search query, 
often the query is first sent over the local ISP to a nearby enter-deep cache, from where the 
static content is retrieved; while providing the static content to the client, the nearby cache also 
forwards the query over Google’s private network to one of the mega data centers, from where 
the personalized search results are retrieved. For a YouTube video, the video itself may come 
from one of the bring-home caches, whereas portions of the Web page surrounding the video 
may come from the nearby enter-deep cache, and the advertisements surrounding the video 
come from the data centers. In summary, except for the local ISPs, the Google cloud services 
are largely provided by a network infrastructure that is independent of the public Internet. host 
is instructed to retrieve a specific video (identified by a URL), the CDN must intercept the 
request so that it can (1) determine a suitable CDN server cluster for that client at that time, 
and (2) redirect the client’s request to a server in that cluster. We’ll shortly discuss how a CDN 
can determine a suitable cluster. But first let’s examine the mechanics behind intercepting and 
redirecting a request. Most CDNs take advantage of DNS to intercept and redirect requests; an 
interesting discussion of such a use of the DNS is [Vixie 2009]. Let’s consider a simple example 
to illustrate how the DNS is typically involved. Suppose a content provider, NetCinema, 
employs the third-party CDN company, KingCDN, to distribute its videos to its customers. On 
the NetCinema Web pages, each of its videos is assigned a URL that includes the string “video” 
and a unique identifier for the video itself; for example, Transformers 7 might be assigned 
http://video.netcinema.com/6Y7B23V. Six steps then occur, as shown in Figure 2.25: 1. The 
user visits the Web page at NetCinema. 2. When the user clicks on the link 
http://video.netcinema.com/6Y7B23V, the user’s host sends a DNS query for 
video.netcinema.com. 3. The user’s Local DNS Server (LDNS) relays the DNS query to an 
authoritative DNS server for NetCinema, which observes the string “video” in the hostname 
video.netcinema.com. To “hand over” the DNS query to KingCDN, instead of returning an IP 
address, the NetCinema authoritative DNS server returns to the LDNS a hostname in the 
KingCDN’s domain, for example, a1105.kingcdn.com. 4. From this point on, the DNS query 
enters into KingCDN’s private DNS infrastructure. The user’s LDNS then sends a second query, 
now for a1105.kingcdn.com, and KingCDN’s DNS system eventually returns the IP addresses of 
a KingCDN content server to the LDNS. It is thus here, within the KingCDN’s DNS system, that 
the CDN server from which the client will receive its content is specified. Figure 2.25 DNS 


## Page 13

redirects a user’s request to a CDN server 5. The LDNS forwards the IP address of the content-
serving CDN node to the user’s host. 6. Once the client receives the IP address for a KingCDN 
content server, it establishes a direct TCP connection with the server at that IP address and 
issues an HTTP GET request for the video. If DASH is used, the server will first send to the client 
a manifest file with a list of URLs, one for each version of the video, and the client will 
dynamically select chunks from the different versions. Cluster Selection Strategies At the core 
of any CDN deployment is a cluster selection strategy, that is, a mechanism for dynamically 
directing clients to a server cluster or a data center within the CDN. As we just saw, the CDN 
learns the IP address of the client’s LDNS server via the client’s DNS lookup. After learning this 
IP address, the CDN needs to select an appropriate cluster based on this IP address. CDNs 
generally employ proprietary cluster selection strategies. We now briefly survey a few 
approaches, each of which has its own advantages and disadvantages. One simple strategy is 
to assign the client to the cluster that is geographically closest. Using commercial geo-location 
databases (such as Quova [Quova 2016] and Max-Mind [MaxMind 2016]), each LDNS IP address 
is mapped to a geographic location. When a DNS request is received from a particular LDNS, 
the CDN chooses the geographically closest cluster, that is, the cluster that is the fewest 
kilometers from the LDNS “as the bird flies.” Such a solution can work reasonably well for a 
large fraction of the clients [Agarwal 2009]. However, for some clients, the solution may 
perform poorly, since the geographically closest cluster may not be the closest cluster in terms 
of the length or number of hops of the network path. Furthermore, a problem inherent with all 
DNS-based approaches is that some end-users are configured to use remotely located LDNSs 
[Shaikh 2001; Mao 2002], in which case the LDNS location may be far from the client’s location. 
Moreover, this simple strategy ignores the variation in delay and available bandwidth over time 
of Internet paths, always assigning the same cluster to a particular client. In order to determine 
the best cluster for a client based on the current traffic conditions, CDNs can instead perform 
periodic real-time measurements of delay and loss performance between their clusters and 
clients. For instance, a CDN can have each of its clusters periodically send probes (for 
example, ping messages or DNS queries) to all of the LDNSs around the world. One drawback 
of this approach is that many LDNSs are configured to not respond to such probes. 2.6.4 Case 
Studies: Netflix, YouTube, and Kankan We conclude our discussion of streaming stored video 
by taking a look at three highly successful largescale deployments: Netflix, YouTube, and 
Kankan. We’ll see that each of these systems take a very different approach, yet employ many 
of the underlying principles discussed in this section. Netflix Generating 37% of the 
downstream traffic in residential ISPs in North America in 2015, Netflix has become the leading 
service provider for online movies and TV series in the United States [Sandvine 2015]. As we 
discuss below, Netflix video distribution has two major components: the Amazon cloud and its 
own private CDN infrastructure. Netflix has a Web site that handles numerous functions, 
including user registration and login, billing, movie catalogue for browsing and searching, and a 
movie recommendation system. As shown in Figure 2.26, this Web site (and its associated 
backend databases) run entirely on Amazon servers in the Amazon cloud. Additionally, the 
Amazon cloud handles the following critical functions: Content ingestion. Before Netflix can 
distribute a movie to its customers, it must first ingest and process the movie. Netflix receives 
studio master versions of movies and uploads them to hosts in the Amazon cloud. Content 
processing. The machines in the Amazon cloud create many different formats for each movie, 
suitable for a diverse array of client video players running on desktop computers, smartphones, 
and game consoles connected to televisions. A different version is created for each of these 
formats and at multiple bit rates, allowing for adaptive streaming over HTTP using DASH. 
Uploading versions to its CDN. Once all of the versions of a movie have been created, the hosts 


## Page 14

in the Amazon cloud upload the versions to its CDN. Figure 2.26 Netflix video streaming 
platform When Netflix first rolled out its video streaming service in 2007, it employed three 
third-party CDN companies to distribute its video content. Netflix has since created its own 
private CDN, from which it now streams all of its videos. (Netflix still uses Akamai to distribute 
its Web pages, however.) To create its own CDN, Netflix has installed server racks both in IXPs 
and within residential ISPs themselves. Netflix currently has server racks in over 50 IXP 
locations; see [Netflix Open Connect 2016] for a current list of IXPs housing Netflix racks. There 
are also hundreds of ISP locations housing Netflix racks; also see [Netflix Open Connect 2016], 
where Netflix provides to potential ISP partners instructions about installing a (free) Netflix rack 
for their networks. Each server in the rack has several 10 Gbps Ethernet ports and over 100 
terabytes of storage. The number of servers in a rack varies: IXP installations often have tens of 
servers and contain the entire Netflix streaming video library, including multiple versions of the 
videos to support DASH; local IXPs may only have one server and contain only the most popular 
videos. Netflix does not use pull-caching (Section 2.2.5) to populate its CDN servers in the IXPs 
and ISPs. Instead, Netflix distributes by pushing the videos to its CDN servers during offpeak 
hours. For those locations that cannot hold the entire library, Netflix pushes only the most 
popular videos, which are determined on a day-to-day basis. The Netflix CDN design is 
described in some detail in the YouTube videos [Netflix Video 1] and [Netflix Video 2]. Having 
described the components of the Netflix architecture, let’s take a closer look at the interaction 
between the client and the various servers that are involved in movie delivery. As indicated 
earlier, the Web pages for browsing the Netflix video library are served from servers in the 
Amazon cloud. When a user selects a movie to play, the Netflix software, running in the Amazon 
cloud, first determines which of its CDN servers have copies of the movie. Among the servers 
that have the movie, the software then determines the “best” server for that client request. If 
the client is using a residential ISP that has a Netflix CDN server rack installed in that ISP, and 
this rack has a copy of the requested movie, then a server in this rack is typically selected. If 
not, a server at a nearby IXP is typically selected. Once Netflix determines the CDN server that 
is to deliver the content, it sends the client the IP address of the specific server as well as a 
manifest file, which has the URLs for the different versions of the requested movie. The client 
and that CDN server then directly interact using a proprietary version of DASH. Specifically, as 
described in Section 2.6.2, the client uses the byte-range header in HTTP GET request 
messages, to request chunks from the different versions of the movie. Netflix uses chunks that 
are approximately four-seconds long [Adhikari 2012]. While the chunks are being downloaded, 
the client measures the received throughput and runs a rate-determination algorithm to 
determine the quality of the next chunk to request. Netflix embodies many of the key principles 
discussed earlier in this section, including adaptive streaming and CDN distribution. However, 
because Netflix uses its own private CDN, which distributes only video (and not Web pages), 
Netflix has been able to simplify and tailor its CDN design. In particular, Netflix does not need to 
employ DNS redirect, as discussed in Section 2.6.3, to connect a particular client to a CDN 
server; instead, the Netflix software (running in the Amazon cloud) directly tells the client to use 
a particular CDN server. Furthermore, the Netflix CDN uses push caching rather than pull 
caching (Section 2.2.5): content is pushed into the servers at scheduled times at off-peak 
hours, rather than dynamically during cache misses. YouTube With 300 hours of video 
uploaded to YouTube every minute and several billion video views per day [YouTube 2016], 
YouTube is indisputably the world’s largest video-sharing site. YouTube began its service in 
April 2005 and was acquired by Google in November 2006. Although the Google/YouTube 
design and protocols are proprietary, through several independent measurement efforts we can 
gain a basic understanding about how YouTube operates [Zink 2009; Torres 2011; Adhikari 


## Page 15

2011a]. As with Netflix, YouTube makes extensive use of CDN technology to distribute its videos 
[Torres 2011]. Similar to Netflix, Google uses its own private CDN to distribute YouTube videos, 
and has installed server clusters in many hundreds of different IXP and ISP locations. From 
these locations and directly from its huge data centers, Google distributes YouTube videos 
[Adhikari 2011a]. Unlike Netflix, however, Google uses pull caching, as described in Section 
2.2.5, and DNS redirect, as described in Section 2.6.3. Most of the time, Google’s cluster-
selection strategy directs the client to the cluster for which the RTT between client and cluster 
is the lowest; however, in order to balance the load across clusters, sometimes the client is 
directed (via DNS) to a more distant cluster [Torres 2011]. YouTube employs HTTP streaming, 
often making a small number of different versions available for a video, each with a different bit 
rate and corresponding quality level. YouTube does not employ adaptive streaming (such as 
DASH), but instead requires the user to manually select a version. In order to save bandwidth 
and server resources that would be wasted by repositioning or early termination, YouTube uses 
the HTTP byte range request to limit the flow of transmitted data after a target amount of video 
is prefetched. Several million videos are uploaded to YouTube every day. Not only are YouTube 
videos streamed from server to client over HTTP, but YouTube uploaders also upload their 
videos from client to server over HTTP. YouTube processes each video it receives, converting it 
to a YouTube video format and creating multiple versions at different bit rates. This processing 
takes place entirely within Google data centers. (See the case study on Google’s network 
infrastructure in Section 2.6.3.) Kankan We just saw that dedicated servers, operated by private 
CDNs, stream Netflix and YouTube videos to clients. Netflix and YouTube have to pay not only 
for the server hardware but also for the bandwidth the servers use to distribute the videos. 
Given the scale of these services and the amount of bandwidth they are consuming, such a 
CDN deployment can be costly. We conclude this section by describing an entirely different 
approach for providing video on demand over the Internet at a large scale—one that allows the 
service provider to significantly reduce its infrastructure and bandwidth costs. As you might 
suspect, this approach uses P2P delivery instead of (or along with) client-server delivery. Since 
2011, Kankan (owned and operated by Xunlei) has been deploying P2P video delivery with great 
success, with tens of millions of users every month [Zhang 2015]. At a high level, P2P video 
streaming is very similar to BitTorrent file downloading. When a peer wants to see a video, it 
contacts a tracker to discover other peers in the system that have a copy of that video. This 
requesting peer then requests chunks of the video in parallel from the other peers that have the 
video. Different from downloading with BitTorrent, however, requests are preferentially made 
for chunks that are to be played back in the near future in order to ensure continuous playback 
[Dhungel 2012]. Recently, Kankan has migrated to a hybrid CDN-P2P streaming system [Zhang 
2015]. Specifically, Kankan now deploys a few hundred servers within China and pushes video 
content to these servers. This Kankan CDN plays a major role in the start-up stage of video 
streaming. In most cases, the client requests the beginning of the content from CDN servers, 
and in parallel requests content from peers. When the total P2P traffic is sufficient for video 
playback, the client will cease streaming from the CDN and only stream from peers. But if the 
P2P streaming traffic becomes insufficient, the client will restart CDN connections and return 
to the mode of hybrid CDN-P2P streaming. In this manner, Kankan can ensure short initial start-
up delays while minimally relying on costly infrastructure servers and bandwidth. 2.7 Socket 
Programming: Creating Network Applications Now that we’ve looked at a number of important 
network applications, let’s explore how network application programs are actually created. 
Recall from Section 2.1 that a typical network application consists of a pair of programs—a 
client program and a server program—residing in two different end systems. When these two 
programs are executed, a client process and a server process are created, and these processes 


## Page 16

communicate with each other by reading from, and writing to, sockets. When creating a 
network application, the developer’s main task is therefore to write the code for both the client 
and server programs. There are two types of network applications. One type is an 
implementation whose operation is specified in a protocol standard, such as an RFC or some 
other standards document; such an application is sometimes referred to as “open,” since the 
rules specifying its operation are known to all. For such an implementation, the client and 
server programs must conform to the rules dictated by the RFC. For example, the client 
program could be an implementation of the client side of the HTTP protocol, described in 
Section 2.2 and precisely defined in RFC 2616; similarly, the server program could be an 
implementation of the HTTP server protocol, also precisely defined in RFC 2616. If one 
developer writes code for the client program and another developer writes code for the server 
program, and both developers carefully follow the rules of the RFC, then the two programs will 
be able to interoperate. Indeed, many of today’s network applications involve communication 
between client and server programs that have been created by independent developers—for 
example, a Google Chrome browser communicating with an Apache Web server, or a BitTorrent 
client communicating with BitTorrent tracker. The other type of network application is a 
proprietary network application. In this case the client and server programs employ an 
application-layer protocol that has not been openly published in an RFC or elsewhere. A single 
developer (or development team) creates both the client and server programs, and the 
developer has complete control over what goes in the code. But because the code does not 
implement an open protocol, other independent developers will not be able to develop code 
that interoperates with the application. In this section, we’ll examine the key issues in 
developing a client-server application, and we’ll “get our hands dirty” by looking at code that 
implements a very simple client-server application. During the development phase, one of the 
first decisions the developer must make is whether the application is to run over TCP or over 
UDP. Recall that TCP is connection oriented and provides a reliable byte-stream channel 
through which data flows between two end systems. UDP is connectionless and sends 
independent packets of data from one end system to the other, without any guarantees about 
delivery. Recall also that when a client or server program implements a protocol defined by an 
RFC, it should use the well-known port number associated with the protocol; conversely, when 
developing a proprietary application, the developer must be careful to avoid using such well-
known port numbers. (Port numbers were briefly discussed in Section 2.1. They are covered in 
more detail in Chapter 3.) We introduce UDP and TCP socket programming by way of a simple 
UDP application and a simple TCP application. We present the simple UDP and TCP 
applications in Python 3. We could have written the code in Java, C, or C++, but we chose 
Python mostly because Python clearly exposes the key socket concepts. With Python there are 
fewer lines of code, and each line can be explained to the novice programmer without difficulty. 
But there’s no need to be frightened if you are not familiar with Python. You should be able to 
easily follow the code if you have experience programming in Java, C, or C++. If you are 
interested in client-server programming with Java, you are encouraged to see the Companion 
Website for this textbook; in fact, you can find there all the examples in this section (and 
associated labs) in Java. For readers who are interested in client-server programming in C, there 
are several good references available [Donahoo 2001; Stevens 1997; Frost 1994; Kurose 1996]; 
our Python examples below have a similar look and feel to C. 2.7.1 Socket Programming with 
UDP In this subsection, we’ll write simple client-server programs that use UDP; in the following 
section, we’ll write similar programs that use TCP. Recall from Section 2.1 that processes 
running on different machines communicate with each other by sending messages into 
sockets. We said that each process is analogous to a house and the process’s socket is 


## Page 17

analogous to a door. The application resides on one side of the door in the house; the transport-
layer protocol resides on the other side of the door in the outside world. The application 
developer has control of everything on the application-layer side of the socket; however, it has 
little control of the transport-layer side. Now let’s take a closer look at the interaction between 
two communicating processes that use UDP sockets. Before the sending process can push a 
packet of data out the socket door, when using UDP, it must first attach a destination address 
to the packet. After the packet passes through the sender’s socket, the Internet will use this 
destination address to route the packet through the Internet to the socket in the receiving 
process. When the packet arrives at the receiving socket, the receiving process will retrieve the 
packet through the socket, and then inspect the packet’s contents and take appropriate action. 
So you may be now wondering, what goes into the destination address that is attached to the 
packet? As you might expect, the destination host’s IP address is part of the destination 
address. By including the destination IP address in the packet, the routers in the Internet will be 
able to route the packet through the Internet to the destination host. But because a host may be 
running many network application processes, each with one or more sockets, it is also 
necessary to identify the particular socket in the destination host. When a socket is created, an 
identifier, called a port number, is assigned to it. So, as you might expect, the packet’s 
destination address also includes the socket’s port number. In summary, the sending process 
attaches to the packet a destination address, which consists of the destination host’s IP 
address and the destination socket’s port number. Moreover, as we shall soon see, the 
sender’s source address—consisting of the IP address of the source host and the port number 
of the source socket—are also attached to the packet. However, attaching the source address 
to the packet is typically not done by the UDP application code; instead it is automatically done 
by the underlying operating system. We’ll use the following simple client-server application to 
demonstrate socket programming for both UDP and TCP: 1. The client reads a line of characters 
(data) from its keyboard and sends the data to the server. 2. The server receives the data and 
converts the characters to uppercase. 3. The server sends the modified data to the client. 4. 
The client receives the modified data and displays the line on its screen. Figure 2.27 highlights 
the main socket-related activity of the client and server that communicate over the UDP 
transport service. Now let’s get our hands dirty and take a look at the client-server program pair 
for a UDP implementation of this simple application. We also provide a detailed, line-by-line 
analysis after each program. We’ll begin with the UDP client, which will send a simple 
application-level message to the server. In order for Figure 2.27 The client-server application 
using UDP the server to be able to receive and reply to the client’s message, it must be ready 
and running—that is, it must be running as a process before the client sends its message. The 
client program is called UDPClient.py, and the server program is called UDPServer.py. In order 
to emphasize the key issues, we intentionally provide code that is minimal. “Good code” would 
certainly have a few more auxiliary lines, in particular for handling error cases. For this 
application, we have arbitrarily chosen 12000 for the server port number. UDPClient.py Here is 
the code for the client side of the application: from socket import * serverName = ’hostname’ 
serverPort = 12000 clientSocket = socket(AF_INET, SOCK_DGRAM) message = raw_input(’Input 
lowercase sentence:’) clientSocket.sendto(message.encode(),(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print(modifiedMessage.decode()) clientSocket.close() Now let’s take a look at the various lines 
of code in UDPClient.py. from socket import * The socket module forms the basis of all network 
communications in Python. By including this line, we will be able to create sockets within our 
program. serverName = ’hostname’ serverPort = 12000 The first line sets the variable 
serverName to the string ‘hostname’. Here, we provide a string containing either the IP address 


## Page 18

of the server (e.g., “128.138.32.126”) or the hostname of the server (e.g., “cis.poly.edu”). If we 
use the hostname, then a DNS lookup will automatically be performed to get the IP address.) 
The second line sets the integer variable serverPort to 12000. clientSocket = socket(AF_INET, 
SOCK_DGRAM) This line creates the client’s socket, called clientSocket . The first parameter 
indicates the address family; in particular, AF_INET indicates that the underlying network is 
using IPv4. (Do not worry about this now—we will discuss IPv4 in Chapter 4.) The second 
parameter indicates that the socket is of type SOCK_DGRAM , which means it is a UDP socket 
(rather than a TCP socket). Note that we are not specifying the port number of the client socket 
when we create it; we are instead letting the operating system do this for us. Now that the client 
process’s door has been created, we will want to create a message to send through the door. 
message = raw_input(’Input lowercase sentence:’) raw_input() is a built-in function in Python. 
When this command is executed, the user at the client is prompted with the words “Input 
lowercase sentence:” The user then uses her keyboard to input a line, which is put into the 
variable message . Now that we have a socket and a message, we will want to send the 
message through the socket to the destination host. 
clientSocket.sendto(message.encode(),(serverName, serverPort)) In the above line, we first 
convert the message from string type to byte type, as we need to send bytes into a socket; this 
is done with the encode() method. The method sendto() attaches the destination address ( 
serverName, serverPort ) to the message and sends the resulting packet into the process’s 
socket, clientSocket . (As mentioned earlier, the source address is also attached to the packet, 
although this is done automatically rather than explicitly by the code.) Sending a client-to-
server message via a UDP socket is that simple! After sending the packet, the client waits to 
receive data from the server. modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
With the above line, when a packet arrives from the Internet at the client’s socket, the packet’s 
data is put into the variable modifiedMessage and the packet’s source address is put into the 
variable serverAddress . The variable serverAddress contains both the server’s IP address and 
the server’s port number. The program UDPClient doesn’t actually need this server address 
information, since it already knows the server address from the outset; but this line of Python 
provides the server address nevertheless. The method recvfrom also takes the buffer size 2048 
as input. (This buffer size works for most purposes.) print(modifiedMessage.decode()) This line 
prints out modifiedMessage on the user’s display, after converting the message from bytes to 
string. It should be the original line that the user typed, but now capitalized. clientSocket.close() 
This line closes the socket. The process then terminates. UDPServer.py Let’s now take a look at 
the server side of the application: from socket import * serverPort = 12000 serverSocket = 
socket(AF_INET, SOCK_DGRAM) serverSocket.bind((’’, serverPort)) print(”The server is ready to 
receive”) while True: message, clientAddress = serverSocket.recvfrom(2048) modifiedMessage 
= message.decode().upper() serverSocket.sendto(modifiedMessage.encode(), clientAddress) 
Note that the beginning of UDPServer is similar to UDPClient. It also imports the socket 
module, also sets the integer variable serverPort to 12000, and also creates a socket of type 
SOCK_DGRAM (a UDP socket). The first line of code that is significantly different from 
UDPClient is: serverSocket.bind((’’, serverPort)) The above line binds (that is, assigns) the port 
number 12000 to the server’s socket. Thus in UDPServer, the code (written by the application 
developer) is explicitly assigning a port number to the socket. In this manner, when anyone 
sends a packet to port 12000 at the IP address of the server, that packet will be directed to this 
socket. UDPServer then enters a while loop; the while loop will allow UDPServer to receive and 
process packets from clients indefinitely. In the while loop, UDPServer waits for a packet to 
arrive. message, clientAddress = serverSocket.recvfrom(2048) This line of code is similar to 
what we saw in UDPClient. When a packet arrives at the server’s socket, the packet’s data is 


## Page 19

put into the variable message and the packet’s source address is put into the variable 
clientAddress . The variable clientAddress contains both the client’s IP address and the client’s 
port number. Here, UDPServer will make use of this address information, as it provides a return 
address, similar to the return address with ordinary postal mail. With this source address 
information, the server now knows to where it should direct its reply. modifiedMessage = 
message.decode().upper() This line is the heart of our simple application. It takes the line sent 
by the client and, after converting the message to a string, uses the method upper() to capitalize 
it. serverSocket.sendto(modifiedMessage.encode(), clientAddress) This last line attaches the 
client’s address (IP address and port number) to the capitalized message (after converting the 
string to bytes), and sends the resulting packet into the server’s socket. (As mentioned earlier, 
the server address is also attached to the packet, although this is done automatically rather 
than explicitly by the code.) The Internet will then deliver the packet to this client address. After 
the server sends the packet, it remains in the while loop, waiting for another UDP packet to 
arrive (from any client running on any host). To test the pair of programs, you run UDPClient.py 
on one host and UDPServer.py on another host. Be sure to include the proper hostname or IP 
address of the server in UDPClient.py. Next, you execute UDPServer.py, the compiled server 
program, in the server host. This creates a process in the server that idles until it is contacted by 
some client. Then you execute UDPClient.py, the compiled client program, in the client. This 
creates a process in the client. Finally, to use the application at the client, you type a sentence 
followed by a carriage return. To develop your own UDP client-server application, you can begin 
by slightly modifying the client or server programs. For example, instead of converting all the 
letters to uppercase, the server could count the number of times the letter s appears and return 
this number. Or you can modify the client so that after receiving a capitalized sentence, the 
user can continue to send more sentences to the server. 2.7.2 Socket Programming with TCP 
Unlike UDP, TCP is a connection-oriented protocol. This means that before the client and server 
can start to send data to each other, they first need to handshake and establish a TCP 
connection. One end of the TCP connection is attached to the client socket and the other end is 
attached to a server socket. When creating the TCP connection, we associate with it the client 
socket address (IP address and port number) and the server socket address (IP address and 
port number). With the TCP connection established, when one side wants to send data to the 
other side, it just drops the data into the TCP connection via its socket. This is different from 
UDP, for which the server must attach a destination address to the packet before dropping it 
into the socket. Now let’s take a closer look at the interaction of client and server programs in 
TCP. The client has the job of initiating contact with the server. In order for the server to be able 
to react to the client’s initial contact, the server has to be ready. This implies two things. First, 
as in the case of UDP, the TCP server must be running as a process before the client attempts 
to initiate contact. Second, the server program must have a special door—more precisely, a 
special socket—that welcomes some initial contact from a client process running on an 
arbitrary host. Using our house/door analogy for a process/socket, we will sometimes refer to 
the client’s initial contact as “knocking on the welcoming door.” With the server process 
running, the client process can initiate a TCP connection to the server. This is done in the client 
program by creating a TCP socket. When the client creates its TCP socket, it specifies the 
address of the welcoming socket in the server, namely, the IP address of the server host and the 
port number of the socket. After creating its socket, the client initiates a three-way handshake 
and establishes a TCP connection with the server. The three-way handshake, which takes place 
within the transport layer, is completely invisible to the client and server programs. During the 
three-way handshake, the client process knocks on the welcoming door of the server process. 
When the server “hears” the knocking, it creates a new door—more precisely, a new socket that 


## Page 20

is dedicated to that particular client. In our example below, the welcoming door is a TCP socket 
object that we call serverSocket ; the newly created socket dedicated to the client making the 
connection is called connectionSocket . Students who are encountering TCP sockets for the 
first time sometimes confuse the welcoming socket (which is the initial point of contact for all 
clients wanting to communicate with the server), and each newly created server-side 
connection socket that is subsequently created for communicating with each client. From the 
application’s perspective, the client’s socket and the server’s connection socket are directly 
connected by a pipe. As shown in Figure 2.28, the client process can send arbitrary bytes into 
its socket, and TCP guarantees that the server process will receive (through the connection 
socket) each byte in the order sent. TCP thus provides a reliable service between the client and 
server processes. Furthermore, just as people can go in and out the same door, the client 
process not only sends bytes into but also receives bytes from its socket; similarly, the server 
process not only receives bytes from but also sends bytes into its connection socket. We use 
the same simple client-server application to demonstrate socket programming with TCP: The 
client sends one line of data to the server, the server capitalizes the line and sends it back to the 
client. Figure 2.29 highlights the main socket-related activity of the client and server that 
communicate over the TCP transport service. Figure 2.28 The TCPServer process has two 
sockets TCPClient.py Here is the code for the client side of the application: from socket import 
* serverName = ’servername’ serverPort = 12000 clientSocket = socket(AF_INET, 
SOCK_STREAM) clientSocket.connect((serverName, serverPort)) sentence = raw_input(’Input 
lowercase sentence:’) clientSocket.send(sentence.encode()) modifiedSentence = 
clientSocket.recv(1024) print(’From Server: ’, modifiedSentence.decode()) clientSocket.close() 
Let’s now take a look at the various lines in the code that differ significantly from the UDP 
implementation. The first such line is the creation of the client socket. clientSocket = 
socket(AF_INET, SOCK_STREAM) This line creates the client’s socket, called clientSocket . The 
first parameter again indicates that the underlying network is using IPv4. The second parameter 
Figure 2.29 The client-server application using TCP indicates that the socket is of type 
SOCK_STREAM , which means it is a TCP socket (rather than a UDP socket). Note that we are 
again not specifying the port number of the client socket when we create it; we are instead 
letting the operating system do this for us. Now the next line of code is very different from what 
we saw in UDPClient: clientSocket.connect((serverName, serverPort)) Recall that before the 
client can send data to the server (or vice versa) using a TCP socket, a TCP connection must 
first be established between the client and server. The above line initiates the TCP connection 
between the client and server. The parameter of the connect() method is the address of the 
server side of the connection. After this line of code is executed, the three-way handshake is 
performed and a TCP connection is established between the client and server. sentence = 
raw_input(’Input lowercase sentence:’) As with UDPClient, the above obtains a sentence from 
the user. The string sentence continues to gather characters until the user ends the line by 
typing a carriage return. The next line of code is also very different from UDPClient: 
clientSocket.send(sentence.encode()) The above line sends the sentence through the client’s 
socket and into the TCP connection. Note that the program does not explicitly create a packet 
and attach the destination address to the packet, as was the case with UDP sockets. Instead 
the client program simply drops the bytes in the string sentence into the TCP connection. The 
client then waits to receive bytes from the server. modifiedSentence = clientSocket.recv(2048) 
When characters arrive from the server, they get placed into the string modifiedSentence . 
Characters continue to accumulate in modifiedSentence until the line ends with a carriage 
return character. After printing the capitalized sentence, we close the client’s socket: 
clientSocket.close() This last line closes the socket and, hence, closes the TCP connection 


