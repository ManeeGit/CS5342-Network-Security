# Computer Networking _ A Top Down Approach, 7th (2)-1


## Page 1

Computer Networking A Top-Down Approach Seventh Edition James F. Kurose University of 
Massachusetts, Amherst Keith W. Ross NYU and NYU Shanghai Boston Columbus Indianapolis 
New York San Francisco Hoboken Amsterdam Cape Town Dubai London Madrid Milan Munich 
Paris Montréal Toronto Delhi Mexico City São Paulo Sydney Hong Kong Seoul Singapore Taipei 
Tokyo Vice President, Editorial Director, ECS: Marcia Horton Acquisitions Editor: Matt Goldstein 
Editorial Assistant: Kristy Alaura Vice President of Marketing: Christy Lesko Director of Field 
Marketing: Tim Galligan Product Marketing Manager: Bram Van Kempen Field Marketing 
Manager: Demetrius Hall Marketing Assistant: Jon Bryant Director of Product Management: Erin 
Gregg Team Lead, Program and Project Management: Scott Disanno Program Manager: Joanne 
Manning and Carole Snyder Project Manager: Katrina Ostler, Ostler Editorial, Inc. Senior 
Specialist, Program Planning and Support: Maura Zaldivar-Garcia Cover Designer: Joyce Wells 
Manager, Rights and Permissions: Ben Ferrini Project Manager, Rights and Permissions: Jenny 
Hoffman, Aptara Corporation Inventory Manager: Ann Lam Cover Image: Marc Gutierrez/Getty 
Images Media Project Manager: Steve Wright Composition: Cenveo Publishing Services 
Printer/Binder: Edwards Brothers Malloy Cover and Insert Printer: Phoenix Color/ Hagerstown 
Credits and acknowledgments borrowed from other sources and reproduced, with permission, 
in this textbook appear on appropriate page within text. Copyright © 2017, 2013, 2010 Pearson 
Education, Inc. All rights reserved. Manufactured in the United States of America. This 
publication is protected by Copyright, and permission should be obtained from the publisher 
prior to any prohibited reproduction, storage in a retrieval system, or transmission in any form 
or by any means, electronic, mechanical, photocopying, recording, or likewise. For information 
regarding permissions, request forms and the appropriate contacts within the Pearson 
Education Global Rights & Permissions Department, please visit 
www.pearsoned.com/permissions/. Many of the designations by manufacturers and seller to 
distinguish their products are claimed as trademarks. Where those designations appear in this 
book, and the publisher was aware of a trademark claim, the designations have been printed in 
initial caps or all caps. Library of Congress Cataloging-in-Publication Data Names: Kurose, 
James F. | Ross, Keith W., 1956- Title: Computer networking: a top-down approach / James F. 
Kurose, University of Massachusetts, Amherst, Keith W. Ross, NYU and NYU Shanghai. 
Description: Seventh edition. | Hoboken, New Jersey: Pearson, [2017] | Includes bibliographical 
references and index. Identifiers: LCCN 2016004976 | ISBN 9780133594140 | ISBN 0133594149 
Subjects: LCSH: Internet. | Computer networks. Classification: LCC TK5105.875.I57 K88 2017 | 
DDC 004.6-dc23 LC record available at http://lccn.loc.gov/2016004976 ISBN-10:     0-13-
359414-9 ISBN-13: 978-0-13-359414-0 About the Authors Jim Kurose Jim Kurose is a 
Distinguished University Professor of Computer Science at the University of Massachusetts, 
Amherst. He is currently on leave from the University of Massachusetts, serving as an Assistant 
Director at the US National Science Foundation, where he leads the Directorate of Computer 
and Information Science and Engineering. Dr. Kurose has received a number of recognitions for 
his educational activities including Outstanding Teacher Awards from the National 
Technological University (eight times), the University of Massachusetts, and the Northeast 
Association of Graduate Schools. He received the IEEE Taylor Booth Education Medal and was 
recognized for his leadership of Massachusetts’ Commonwealth Information Technology 
Initiative. He has won several conference best paper awards and received the IEEE Infocom 
Achievement Award and the ACM Sigcomm Test of Time Award. Dr. Kurose is a former Editor-in-
Chief of IEEE Transactions on Communications and of IEEE/ACM Transactions on Networking. 
He has served as Technical Program co-Chair for IEEE Infocom, ACM SIGCOMM, ACM Internet 
Measurement Conference, and ACM SIGMETRICS. He is a Fellow of the IEEE and the ACM. His 
research interests include network protocols and architecture, network measurement, 


## Page 2

multimedia communication, and modeling and performance evaluation. He holds a PhD in 
Computer Science from Columbia University. Keith Ross Keith Ross is the Dean of Engineering 
and Computer Science at NYU Shanghai and the Leonard J. Shustek Chair Professor in the 
Computer Science and Engineering Department at NYU. Previously he was at University of 
Pennsylvania (13 years), Eurecom Institute (5 years) and Polytechnic University (10 years). He 
received a B.S.E.E from Tufts University, a M.S.E.E. from Columbia University, and a Ph.D. in 
Computer and Control Engineering from The University of Michigan. Keith Ross is also the co-
founder and original CEO of Wimba, which develops online multimedia applications for e-
learning and was acquired by Blackboard in 2010. Professor Ross’s research interests are in 
privacy, social networks, peer-to-peer networking, Internet measurement, content distribution 
networks, and stochastic modeling. He is an ACM Fellow, an IEEE Fellow, recipient of the 
Infocom 2009 Best Paper Award, and recipient of 2011 and 2008 Best Paper Awards for 
Multimedia Communications (awarded by IEEE Communications Society). He has served on 
numerous journal editorial boards and conference program committees, including IEEE/ACM 
Transactions on Networking, ACM SIGCOMM, ACM CoNext, and ACM Internet Measurement 
Conference. He also has served as an advisor to the Federal Trade Commission on P2P file 
sharing. To Julie and our three precious ones—Chris, Charlie, and Nina JFK A big THANKS to my 
professors, colleagues, and students all over the world. KWR Preface Welcome to the seventh 
edition of Computer Networking: A Top-Down Approach. Since the publication of the first 
edition 16 years ago, our book has been adopted for use at many hundreds of colleges and 
universities, translated into 14 languages, and used by over one hundred thousand students 
and practitioners worldwide. We’ve heard from many of these readers and have been 
overwhelmed by the positive response. What’s New in the Seventh Edition? We think one 
important reason for this success has been that our book continues to offer a fresh and timely 
approach to computer networking instruction. We’ve made changes in this seventh edition, but 
we’ve also kept unchanged what we believe (and the instructors and students who have used 
our book have confirmed) to be the most important aspects of this book: its top-down 
approach, its focus on the Internet and a modern treatment of computer networking, its 
attention to both principles and practice, and its accessible style and approach toward learning 
about computer networking. Nevertheless, the seventh edition has been revised and updated 
substantially. Long-time readers of our book will notice that for the first time since this text was 
published, we’ve changed the organization of the chapters themselves. The network layer, 
which had been previously covered in a single chapter, is now covered in Chapter 4 (which 
focuses on the so-called “data plane” component of the network layer) and Chapter 5 (which 
focuses on the network layer’s “control plane”). This expanded coverage of the network layer 
reflects the swift rise in importance of software-defined networking (SDN), arguably the most 
important and exciting advance in networking in decades. Although a relatively recent 
innovation, SDN has been rapidly adopted in practice—so much so that it’s already hard to 
imagine an introduction to modern computer networking that doesn’t cover SDN. The topic of 
network management, previously covered in Chapter 9, has now been folded into the new 
Chapter 5. As always, we’ve also updated many other sections of the text to reflect recent 
changes in the dynamic field of networking since the sixth edition. As always, material that has 
been retired from the printed text can always be found on this book’s Companion Website. The 
most important updates are the following: Chapter 1 has been updated to reflect the ever-
growing reach and use of the Internet. Chapter 2, which covers the application layer, has been 
significantly updated. We’ve removed the material on the FTP protocol and distributed hash 
tables to make room for a new section on application-level video streaming and content 
distribution networks, together with Netflix and YouTube case studies. The socket programming 


## Page 3

sections have been updated from Python 2 to Python 3. Chapter 3, which covers the transport 
layer, has been modestly updated. The material on asynchronous transport mode (ATM) 
networks has been replaced by more modern material on the Internet’s explicit congestion 
notification (ECN), which teaches the same principles. Chapter 4 covers the “data plane” 
component of the network layer—the per-router forwarding function that determine how a 
packet arriving on one of a router’s input links is forwarded to one of that router’s output links. 
We updated the material on traditional Internet forwarding found in all previous editions, and 
added material on packet scheduling. We’ve also added a new section on generalized 
forwarding, as practiced in SDN. There are also numerous updates throughout the chapter. 
Material on multicast and broadcast communication has been removed to make way for the 
new material. In Chapter 5, we cover the control plane functions of the network layer—the 
network-wide logic that controls how a datagram is routed along an end-to-end path of routers 
from the source host to the destination host. As in previous editions, we cover routing 
algorithms, as well as routing protocols (with an updated treatment of BGP) used in today’s 
Internet. We’ve added a significant new section on the SDN control plane, where routing and 
other functions are implemented in so-called SDN controllers. Chapter 6, which now covers the 
link layer, has an updated treatment of Ethernet, and of data center networking. Chapter 7, 
which covers wireless and mobile networking, contains updated material on 802.11 (so-called 
“WiFi) networks and cellular networks, including 4G and LTE. Chapter 8, which covers network 
security and was extensively updated in the sixth edition, has only modest updates in this 
seventh edition. Chapter 9, on multimedia networking, is now slightly “thinner” than in the sixth 
edition, as material on video streaming and content distribution networks has been moved to 
Chapter 2, and material on packet scheduling has been incorporated into Chapter 4. Significant 
new material involving end-of-chapter problems has been added. As with all previous editions, 
homework problems have been revised, added, and removed. As always, our aim in creating 
this new edition of our book is to continue to provide a focused and modern treatment of 
computer networking, emphasizing both principles and practice. Audience This textbook is for a 
first course on computer networking. It can be used in both computer science and electrical 
engineering departments. In terms of programming languages, the book assumes only that the 
student has experience with C, C++, Java, or Python (and even then only in a few places). 
Although this book is more precise and analytical than many other introductory computer 
networking texts, it rarely uses any mathematical concepts that are not taught in high school. 
We have made a deliberate effort to avoid using any advanced calculus, probability, or 
stochastic process concepts (although we’ve included some homework problems for students 
with this advanced background). The book is therefore appropriate for undergraduate courses 
and for first-year graduate courses. It should also be useful to practitioners in the 
telecommunications industry. What Is Unique About This Textbook? The subject of computer 
networking is enormously complex, involving many concepts, protocols, and technologies that 
are woven together in an intricate manner. To cope with this scope and complexity, many 
computer networking texts are often organized around the “layers” of a network architecture. 
With a layered organization, students can see through the complexity of computer networking—
they learn about the distinct concepts and protocols in one part of the architecture while seeing 
the big picture of how all parts fit together. From a pedagogical perspective, our personal 
experience has been that such a layered approach indeed works well. Nevertheless, we have 
found that the traditional approach of teaching—bottom up; that is, from the physical layer 
towards the application layer—is not the best approach for a modern course on computer 
networking. A Top-Down Approach Our book broke new ground 16 years ago by treating 
networking in a top-down manner—that is, by beginning at the application layer and working its 


## Page 4

way down toward the physical layer. The feedback we received from teachers and students 
alike have confirmed that this top-down approach has many advantages and does indeed work 
well pedagogically. First, it places emphasis on the application layer (a “high growth area” in 
networking). Indeed, many of the recent revolutions in computer networking—including the 
Web, peer-to-peer file sharing, and media streaming—have taken place at the application layer. 
An early emphasis on application-layer issues differs from the approaches taken in most other 
texts, which have only a small amount of material on network applications, their requirements, 
application-layer paradigms (e.g., client-server and peer-to-peer), and application 
programming interfaces. Second, our experience as instructors (and that of many instructors 
who have used this text) has been that teaching networking applications near the beginning of 
the course is a powerful motivational tool. Students are thrilled to learn about how networking 
applications work—applications such as e-mail and the Web, which most students use on a 
daily basis. Once a student understands the applications, the student can then understand the 
network services needed to support these applications. The student can then, in turn, examine 
the various ways in which such services might be provided and implemented in the lower 
layers. Covering applications early thus provides motivation for the remainder of the text. Third, 
a top-down approach enables instructors to introduce network application development at an 
early stage. Students not only see how popular applications and protocols work, but also learn 
how easy it is to create their own network applications and application-level protocols. With the 
top-down approach, students get early exposure to the notions of socket programming, service 
models, and protocols—important concepts that resurface in all subsequent layers. By 
providing socket programming examples in Python, we highlight the central ideas without 
confusing students with complex code. Undergraduates in electrical engineering and computer 
science should not have difficulty following the Python code. An Internet Focus Although we 
dropped the phrase “Featuring the Internet” from the title of this book with the fourth edition, 
this doesn’t mean that we dropped our focus on the Internet. Indeed, nothing could be further 
from the case! Instead, since the Internet has become so pervasive, we felt that any networking 
textbook must have a significant focus on the Internet, and thus this phrase was somewhat 
unnecessary. We continue to use the Internet’s architecture and protocols as primary vehicles 
for studying fundamental computer networking concepts. Of course, we also include concepts 
and protocols from other network architectures. But the spotlight is clearly on the Internet, a 
fact reflected in our organizing the book around the Internet’s five-layer architecture: the 
application, transport, network, link, and physical layers. Another benefit of spotlighting the 
Internet is that most computer science and electrical engineering students are eager to learn 
about the Internet and its protocols. They know that the Internet has been a revolutionary and 
disruptive technology and can see that it is profoundly changing our world. Given the enormous 
relevance of the Internet, students are naturally curious about what is “under the hood.” Thus, 
it is easy for an instructor to get students excited about basic principles when using the Internet 
as the guiding focus. Teaching Networking Principles Two of the unique features of the book—
its top-down approach and its focus on the Internet—have appeared in the titles of our book. If 
we could have squeezed a third phrase into the subtitle, it would have contained the word 
principles. The field of networking is now mature enough that a number of fundamentally 
important issues can be identified. For example, in the transport layer, the fundamental issues 
include reliable communication over an unreliable network layer, connection establishment/ 
teardown and handshaking, congestion and flow control, and multiplexing. Three 
fundamentally important network-layer issues are determining “good” paths between two 
routers, interconnecting a large number of heterogeneous networks, and managing the 
complexity of a modern network. In the link layer, a fundamental problem is sharing a multiple 


## Page 5

access channel. In network security, techniques for providing confidentiality, authentication, 
and message integrity are all based on cryptographic fundamentals. This text identifies 
fundamental networking issues and studies approaches towards addressing these issues. The 
student learning these principles will gain knowledge with a long “shelf life”—long after today’s 
network standards and protocols have become obsolete, the principles they embody will 
remain important and relevant. We believe that the combination of using the Internet to get the 
student’s foot in the door and then emphasizing fundamental issues and solution approaches 
will allow the student to quickly understand just about any networking technology. The Website 
Each new copy of this textbook includes twelve months of access to a Companion Website for 
all book readers at http://www.pearsonhighered.com/cs-resources/, which includes: 
Interactive learning material. The book’s Companion Website contains VideoNotes—video 
presentations of important topics throughout the book done by the authors, as well as 
walkthroughs of solutions to problems similar to those at the end of the chapter. We’ve seeded 
the Web site with VideoNotes and online problems for Chapters 1 through 5 and will continue to 
actively add and update this material over time. As in earlier editions, the Web site contains the 
interactive Java applets that animate many key networking concepts. The site also has 
interactive quizzes that permit students to check their basic understanding of the subject 
matter. Professors can integrate these interactive features into their lectures or use them as 
mini labs. Additional technical material. As we have added new material in each edition of our 
book, we’ve had to remove coverage of some existing topics to keep the book at manageable 
length. For example, to make room for the new material in this edition, we’ve removed material 
on FTP, distributed hash tables, and multicasting, Material that appeared in earlier editions of 
the text is still of interest, and thus can be found on the book’s Web site. Programming 
assignments. The Web site also provides a number of detailed programming assignments, 
which include building a multithreaded Web server, building an e-mail client with a GUI 
interface, programming the sender and receiver sides of a reliable data transport protocol, 
programming a distributed routing algorithm, and more. Wireshark labs. One’s understanding 
of network protocols can be greatly deepened by seeing them in action. The Web site provides 
numerous Wireshark assignments that enable students to actually observe the sequence of 
messages exchanged between two protocol entities. The Web site includes separate Wireshark 
labs on HTTP, DNS, TCP, UDP, IP, ICMP, Ethernet, ARP, WiFi, SSL, and on tracing all protocols 
involved in satisfying a request to fetch a Web page. We’ll continue to add new labs over time. 
In addition to the Companion Website, the authors maintain a public Web site, 
http://gaia.cs.umass.edu/kurose_ross/interactive, containing interactive exercises that create 
(and present solutions for) problems similar to selected end-of-chapter problems. Since 
students can generate (and view solutions for) an unlimited number of similar problem 
instances, they can work until the material is truly mastered. Pedagogical Features We have 
each been teaching computer networking for more than 30 years. Together, we bring more than 
60 years of teaching experience to this text, during which time we have taught many thousands 
of students. We have also been active researchers in computer networking during this time. (In 
fact, Jim and Keith first met each other as master’s students in a computer networking course 
taught by Mischa Schwartz in 1979 at Columbia University.) We think all this gives us a good 
perspective on where networking has been and where it is likely to go in the future. 
Nevertheless, we have resisted temptations to bias the material in this book towards our own 
pet research projects. We figure you can visit our personal Web sites if you are interested in our 
research. Thus, this book is about modern computer networking—it is about contemporary 
protocols and technologies as well as the underlying principles behind these protocols and 
technologies. We also believe that learning (and teaching!) about networking can be fun. A 


## Page 6

sense of humor, use of analogies, and real-world examples in this book will hopefully make this 
material more fun. Supplements for Instructors We provide a complete supplements package 
to aid instructors in teaching this course. This material can be accessed from Pearson’s 
Instructor Resource Center (http://www.pearsonhighered.com/irc). Visit the Instructor 
Resource Center for information about accessing these instructor’s supplements. PowerPoint 
slides. We provide PowerPoint slides for all nine chapters. The slides have been completely 
updated with this seventh edition. The slides cover each chapter in detail. They use graphics 
and animations (rather than relying only on monotonous text bullets) to make the slides 
interesting and visually appealing. We provide the original PowerPoint slides so you can 
customize them to best suit your own teaching needs. Some of these slides have been 
contributed by other instructors who have taught from our book. Homework solutions. We 
provide a solutions manual for the homework problems in the text, programming assignments, 
and Wireshark labs. As noted earlier, we’ve introduced many new homework problems in the 
first six chapters of the book. Chapter Dependencies The first chapter of this text presents a 
self-contained overview of computer networking. Introducing many key concepts and 
terminology, this chapter sets the stage for the rest of the book. All of the other chapters 
directly depend on this first chapter. After completing Chapter 1, we recommend instructors 
cover Chapters 2 through 6 in sequence, following our top-down philosophy. Each of these five 
chapters leverages material from the preceding chapters. After completing the first six 
chapters, the instructor has quite a bit of flexibility. There are no interdependencies among the 
last three chapters, so they can be taught in any order. However, each of the last three chapters 
depends on the material in the first six chapters. Many instructors first teach the first six 
chapters and then teach one of the last three chapters for “dessert.” One Final Note: We’d Love 
to Hear from You We encourage students and instructors to e-mail us with any comments they 
might have about our book. It’s been wonderful for us to hear from so many instructors and 
students from around the world about our first five editions. We’ve incorporated many of these 
suggestions into later editions of the book. We also encourage instructors to send us new 
homework problems (and solutions) that would complement the current homework problems. 
We’ll post these on the instructor-only portion of the Web site. We also encourage instructors 
and students to create new Java applets that illustrate the concepts and protocols in this book. 
If you have an applet that you think would be appropriate for this text, please submit it to us. If 
the applet (including notation and terminology) is appropriate, we’ll be happy to include it on 
the text’s Web site, with an appropriate reference to the applet’s authors. So, as the saying 
goes, “Keep those cards and letters coming!” Seriously, please do continue to send us 
interesting URLs, point out typos, disagree with any of our claims, and tell us what works and 
what doesn’t work. Tell us what you think should or shouldn’t be included in the next edition. 
Send your e-mail to kurose@cs.umass.edu and keithwross@nyu.edu. ® Acknowledgments 
Since we began writing this book in 1996, many people have given us invaluable help and have 
been influential in shaping our thoughts on how to best organize and teach a networking 
course. We want to say A BIG THANKS to everyone who has helped us from the earliest first 
drafts of this book, up to this seventh edition. We are also very thankful to the many hundreds of 
readers from around the world—students, faculty, practitioners—who have sent us thoughts 
and comments on earlier editions of the book and suggestions for future editions of the book. 
Special thanks go out to: Al Aho (Columbia University) Hisham Al-Mubaid (University of 
Houston-Clear Lake) Pratima Akkunoor (Arizona State University) Paul Amer (University of 
Delaware) Shamiul Azom (Arizona State University) Lichun Bao (University of California at Irvine) 
Paul Barford (University of Wisconsin) Bobby Bhattacharjee (University of Maryland) Steven 
Bellovin (Columbia University) Pravin Bhagwat (Wibhu) Supratik Bhattacharyya (previously at 


## Page 7

Sprint) Ernst Biersack (Eurécom Institute) Shahid Bokhari (University of Engineering & 
Technology, Lahore) Jean Bolot (Technicolor Research) Daniel Brushteyn (former University of 
Pennsylvania student) Ken Calvert (University of Kentucky) Evandro Cantu (Federal University of 
Santa Catarina) Jeff Case (SNMP Research International) Jeff Chaltas (Sprint) Vinton Cerf 
(Google) Byung Kyu Choi (Michigan Technological University) Bram Cohen (BitTorrent, Inc.) 
Constantine Coutras (Pace University) John Daigle (University of Mississippi) Edmundo A. de 
Souza e Silva (Federal University of Rio de Janeiro) Philippe Decuetos (Eurécom Institute) 
Christophe Diot (Technicolor Research) Prithula Dhunghel (Akamai) Deborah Estrin (University 
of California, Los Angeles) Michalis Faloutsos (University of California at Riverside) Wu-chi Feng 
(Oregon Graduate Institute) Sally Floyd (ICIR, University of California at Berkeley) Paul Francis 
(Max Planck Institute) David Fullager (Netflix) Lixin Gao (University of Massachusetts) JJ Garcia-
Luna-Aceves (University of California at Santa Cruz) Mario Gerla (University of California at Los 
Angeles) David Goodman (NYU-Poly) Yang Guo (Alcatel/Lucent Bell Labs) Tim Griffin 
(Cambridge University) Max Hailperin (Gustavus Adolphus College) Bruce Harvey (Florida A&M 
University, Florida State University) Carl Hauser (Washington State University) Rachelle Heller 
(George Washington University) Phillipp Hoschka (INRIA/W3C) Wen Hsin (Park University) 
Albert Huang (former University of Pennsylvania student) Cheng Huang (Microsoft Research) 
Esther A. Hughes (Virginia Commonwealth University) Van Jacobson (Xerox PARC) Pinak Jain 
(former NYU-Poly student) Jobin James (University of California at Riverside) Sugih Jamin 
(University of Michigan) Shivkumar Kalyanaraman (IBM Research, India) Jussi Kangasharju 
(University of Helsinki) Sneha Kasera (University of Utah) Parviz Kermani (formerly of IBM 
Research) Hyojin Kim (former University of Pennsylvania student) Leonard Kleinrock (University 
of California at Los Angeles) David Kotz (Dartmouth College) Beshan Kulapala (Arizona State 
University) Rakesh Kumar (Bloomberg) Miguel A. Labrador (University of South Florida) Simon 
Lam (University of Texas) Steve Lai (Ohio State University) Tom LaPorta (Penn State University) 
Tim-Berners Lee (World Wide Web Consortium) Arnaud Legout (INRIA) Lee Leitner (Drexel 
University) Brian Levine (University of Massachusetts) Chunchun Li (former NYU-Poly student) 
Yong Liu (NYU-Poly) William Liang (former University of Pennsylvania student) Willis Marti 
(Texas A&M University) Nick McKeown (Stanford University) Josh McKinzie (Park University) 
Deep Medhi (University of Missouri, Kansas City) Bob Metcalfe (International Data Group) Sue 
Moon (KAIST) Jenni Moyer (Comcast) Erich Nahum (IBM Research) Christos Papadopoulos 
(Colorado Sate University) Craig Partridge (BBN Technologies) Radia Perlman (Intel) Jitendra 
Padhye (Microsoft Research) Vern Paxson (University of California at Berkeley) Kevin Phillips 
(Sprint) George Polyzos (Athens University of Economics and Business) Sriram Rajagopalan 
(Arizona State University) Ramachandran Ramjee (Microsoft Research) Ken Reek (Rochester 
Institute of Technology) Martin Reisslein (Arizona State University) Jennifer Rexford (Princeton 
University) Leon Reznik (Rochester Institute of Technology) Pablo Rodrigez (Telefonica) Sumit 
Roy (University of Washington) Dan Rubenstein (Columbia University) Avi Rubin (Johns Hopkins 
University) Douglas Salane (John Jay College) Despina Saparilla (Cisco Systems) John Schanz 
(Comcast) Henning Schulzrinne (Columbia University) Mischa Schwartz (Columbia University) 
Ardash Sethi (University of Delaware) Harish Sethu (Drexel University) K. Sam Shanmugan 
(University of Kansas) Prashant Shenoy (University of Massachusetts) Clay Shields (Georgetown 
University) Subin Shrestra (University of Pennsylvania) Bojie Shu (former NYU-Poly student) 
Mihail L. Sichitiu (NC State University) Peter Steenkiste (Carnegie Mellon University) Tatsuya 
Suda (University of California at Irvine) Kin Sun Tam (State University of New York at Albany) Don 
Towsley (University of Massachusetts) David Turner (California State University, San 
Bernardino) Nitin Vaidya (University of Illinois) Michele Weigle (Clemson University) David 
Wetherall (University of Washington) Ira Winston (University of Pennsylvania) Di Wu (Sun Yat-


## Page 8

sen University) Shirley Wynn (NYU-Poly) Raj Yavatkar (Intel) Yechiam Yemini (Columbia 
University) Dian Yu (NYU Shanghai) Ming Yu (State University of New York at Binghamton) Ellen 
Zegura (Georgia Institute of Technology) Honggang Zhang (Suffolk University) Hui Zhang 
(Carnegie Mellon University) Lixia Zhang (University of California at Los Angeles) Meng Zhang 
(former NYU-Poly student) Shuchun Zhang (former University of Pennsylvania student) 
Xiaodong Zhang (Ohio State University) ZhiLi Zhang (University of Minnesota) Phil Zimmermann 
(independent consultant) Mike Zink (University of Massachusetts) Cliff C. Zou (University of 
Central Florida) We also want to thank the entire Pearson team—in particular, Matt Goldstein 
and Joanne Manning—who have done an absolutely outstanding job on this seventh edition 
(and who have put up with two very finicky authors who seem congenitally unable to meet 
deadlines!). Thanks also to our artists, Janet Theurer and Patrice Rossi Calkin, for their work on 
the beautiful figures in this and earlier editions of our book, and to Katie Ostler and her team at 
Cenveo for their wonderful production work on this edition. Finally, a most special thanks go to 
our previous two editors at Addison-Wesley—Michael Hirsch and Susan Hartman. This book 
would not be what it is (and may well not have been at all) without their graceful management, 
constant encouragement, nearly infinite patience, good humor, and perseverance. Table of 
Contents Chapter 1 Computer Networks and the Internet 1 1.1 What Is the Internet? 2 1.1.1 A 
Nuts-and-Bolts Description 2 1.1.2 A Services Description 5 1.1.3 What Is a Protocol? 7 1.2 The 
Network Edge 9 1.2.1 Access Networks 12 1.2.2 Physical Media 18 1.3 The Network Core 21 
1.3.1 Packet Switching 23 1.3.2 Circuit Switching 27 1.3.3 A Network of Networks 31 1.4 Delay, 
Loss, and Throughput in Packet-Switched Networks 35 1.4.1 Overview of Delay in Packet-
Switched Networks 35 1.4.2 Queuing Delay and Packet Loss 39 1.4.3 End-to-End Delay 41 1.4.4 
Throughput in Computer Networks 43 1.5 Protocol Layers and Their Service Models 47 1.5.1 
Layered Architecture 47 1.5.2 Encapsulation 53 1.6 Networks Under Attack 55 1.7 History of 
Computer Networking and the Internet 59 1.7.1 The Development of Packet Switching: 1961–
1972 59 1.7.2 Proprietary Networks and Internetworking: 1972–1980 60 1.7.3 A Proliferation of 
Networks: 1980–1990 62 1.7.4 The Internet Explosion: The 1990s 63 1.7.5 The New Millennium 
64 1.8 Summary 65 Homework Problems and Questions 67 Wireshark Lab 77 Interview: 
Leonard Kleinrock 79 Chapter 2 Application Layer 83 2.1 Principles of Network Applications 84 
2.1.1 Network Application Architectures 86 2.1.2 Processes Communicating 88 2.1.3 Transport 
Services Available to Applications 90 2.1.4 Transport Services Provided by the Internet 93 2.1.5 
Application-Layer Protocols 96 2.1.6 Network Applications Covered in This Book 97 2.2 The 
Web and HTTP 98 2.2.1 Overview of HTTP 98 2.2.2 Non-Persistent and Persistent Connections 
100 2.2.3 HTTP Message Format 103 2.2.4 User-Server Interaction: Cookies 108 2.2.5 Web 
Caching 110 2.3 Electronic Mail in the Internet 116 2.3.1 SMTP 118 2.3.2 Comparison with HTTP 
121 2.3.3 Mail Message Formats 121 2.3.4 Mail Access Protocols 122 2.4 DNS—The Internet’s 
Directory Service 126 2.4.1 Services Provided by DNS 127 2.4.2 Overview of How DNS Works 
129 2.4.3 DNS Records and Messages 135 2.5 Peer-to-Peer Applications 140 2.5.1 P2P File 
Distribution 140 2.6 Video Streaming and Content Distribution Networks 147 2.6.1 Internet 
Video 148 2.6.2 HTTP Streaming and DASH 148 2.6.3 Content Distribution Networks 149 2.6.4 
Case Studies: Netflix, YouTube, and Kankan 153 2.7 Socket Programming: Creating Network 
Applications 157 2.7.1 Socket Programming with UDP 159 2.7.2 Socket Programming with TCP 
164 2.8 Summary 170 Homework Problems and Questions 171 Socket Programming 
Assignments 180 Wireshark Labs: HTTP, DNS 182 Interview: Marc Andreessen 184 Chapter 3 
Transport Layer 187 3.1 Introduction and Transport-Layer Services 188 3.1.1 Relationship 
Between Transport and Network Layers 188 3.1.2 Overview of the Transport Layer in the Internet 
191 3.2 Multiplexing and Demultiplexing 193 3.3 Connectionless Transport: UDP 200 3.3.1 UDP 
Segment Structure 204 3.3.2 UDP Checksum 204 3.4 Principles of Reliable Data Transfer 206 


## Page 9

3.4.1 Building a Reliable Data Transfer Protocol 208 3.4.2 Pipelined Reliable Data Transfer 
Protocols 217 3.4.3 Go-Back-N (GBN) 221 3.4.4 Selective Repeat (SR) 226 3.5 Connection-
Oriented Transport: TCP 233 3.5.1 The TCP Connection 233 3.5.2 TCP Segment Structure 236 
3.5.3 Round-Trip Time Estimation and Timeout 241 3.5.4 Reliable Data Transfer 244 3.5.5 Flow 
Control 252 3.5.6 TCP Connection Management 255 3.6 Principles of Congestion Control 261 
3.6.1 The Causes and the Costs of Congestion 261 3.6.2 Approaches to Congestion Control 268 
3.7 TCP Congestion Control 269 3.7.1 Fairness 279 3.7.2 Explicit Congestion Notification (ECN): 
Network-assisted Congestion Control 282 3.8 Summary 284 Homework Problems and 
Questions 286 Programming Assignments 301 Wireshark Labs: Exploring TCP, UDP 302 
Interview: Van Jacobson 303 Chapter 4 The Network Layer: Data Plane 305 4.1 Overview of 
Network Layer 306 4.1.1 Forwarding and Routing: The Network Data and Control Planes 306 
4.1.2 Network Service Models 311 4.2 What’s Inside a Router? 313 4.2.1 Input Port Processing 
and Destination-Based Forwarding 316 4.2.2 Switching 319 4.2.3 Output Port Processing 321 
4.2.4 Where Does Queuing Occur? 321 4.2.5 Packet Scheduling 325 4.3 The Internet Protocol 
(IP): IPv4, Addressing, IPv6, and More 329 4.3.1 IPv4 Datagram Format 330 4.3.2 IPv4 Datagram 
Fragmentation 332 4.3.3 IPv4 Addressing 334 4.3.4 Network Address Translation (NAT) 345 
4.3.5 IPv6 348 4.4 Generalized Forwarding and SDN 354 4.4.1 Match 356 4.4.2 Action 358 4.4.3 
OpenFlow Examples of Match-plus-action in Action 358 4.5 Summary 361 Homework Problems 
and Questions 361 Wireshark Lab 370 Interview: Vinton G. Cerf 371 Chapter 5 The Network 
Layer: Control Plane 373 5.1 Introduction 374 5.2 Routing Algorithms 376 5.2.1 The Link-State 
(LS) Routing Algorithm 379 5.2.2 The Distance-Vector (DV) Routing Algorithm 384 5.3 Intra-AS 
Routing in the Internet: OSPF 391 5.4 Routing Among the ISPs: BGP 395 5.4.1 The Role of BGP 
395 5.4.2 Advertising BGP Route Information 396 5.4.3 Determining the Best Routes 398 5.4.4 
IP-Anycast 402 5.4.5 Routing Policy 403 5.4.6 Putting the Pieces Together: Obtaining Internet 
Presence 406 5.5 The SDN Control Plane 407 5.5.1 The SDN Control Plane: SDN Controller and 
SDN Control Applications 410 5.5.2 OpenFlow Protocol 412 5.5.3 Data and Control Plane 
Interaction: An Example 414 5.5.4 SDN: Past and Future 415 5.6 ICMP: The Internet Control 
Message Protocol 419 5.7 Network Management and SNMP 421 5.7.1 The Network 
Management Framework 422 5.7.2 The Simple Network Management Protocol (SNMP) 424 5.8 
Summary 426 Homework Problems and Questions 427 Socket Programming Assignment 433 
Programming Assignment 434 Wireshark Lab 435 Interview: Jennifer Rexford 436 Chapter 6 The 
Link Layer and LANs 439 6.1 Introduction to the Link Layer 440 6.1.1 The Services Provided by 
the Link Layer 442 6.1.2 Where Is the Link Layer Implemented? 443 6.2 Error-Detection and -
Correction Techniques 444 6.2.1 Parity Checks 446 6.2.2 Checksumming Methods 448 6.2.3 
Cyclic Redundancy Check (CRC) 449 6.3 Multiple Access Links and Protocols 451 6.3.1 
Channel Partitioning Protocols 453 6.3.2 Random Access Protocols 455 6.3.3 Taking-Turns 
Protocols 464 6.3.4 DOCSIS: The Link-Layer Protocol for Cable Internet Access 465 6.4 
Switched Local Area Networks 467 6.4.1 Link-Layer Addressing and ARP 468 6.4.2 Ethernet 474 
6.4.3 Link-Layer Switches 481 6.4.4 Virtual Local Area Networks (VLANs) 487 6.5 Link 
Virtualization: A Network as a Link Layer 491 6.5.1 Multiprotocol Label Switching (MPLS) 492 6.6 
Data Center Networking 495 6.7 Retrospective: A Day in the Life of a Web Page Request 500 
6.7.1 Getting Started: DHCP, UDP, IP, and Ethernet 500 6.7.2 Still Getting Started: DNS and ARP 
502 6.7.3 Still Getting Started: Intra-Domain Routing to the DNS Server 503 6.7.4 Web Client-
Server Interaction: TCP and HTTP 504 6.8 Summary 506 Homework Problems and Questions 
507 Wireshark Lab 515 Interview: Simon S. Lam 516 Chapter 7 Wireless and Mobile Networks 
519 7.1 Introduction 520 7.2 Wireless Links and Network Characteristics 525 7.2.1 CDMA 528 
7.3 WiFi: 802.11 Wireless LANs 532 7.3.1 The 802.11 Architecture 533 7.3.2 The 802.11 MAC 
Protocol 537 7.3.3 The IEEE 802.11 Frame 542 7.3.4 Mobility in the Same IP Subnet 546 7.3.5 


## Page 10

Advanced Features in 802.11 547 7.3.6 Personal Area Networks: Bluetooth and Zigbee 548 7.4 
Cellular Internet Access 551 7.4.1 An Overview of Cellular Network Architecture 551 7.4.2 3G 
Cellular Data Networks: Extending the Internet to Cellular Subscribers 554 7.4.3 On to 4G: LTE 
557 7.5 Mobility Management: Principles 560 7.5.1 Addressing 562 7.5.2 Routing to a Mobile 
Node 564 7.6 Mobile IP 570 7.7 Managing Mobility in Cellular Networks 574 7.7.1 Routing Calls 
to a Mobile User 576 7.7.2 Handoffs in GSM 577 7.8 Wireless and Mobility: Impact on Higher-
Layer Protocols 580 7.9 Summary 582 Homework Problems and Questions 583 Wireshark Lab 
588 Interview: Deborah Estrin 589 Chapter 8 Security in Computer Networks 593 8.1 What Is 
Network Security? 594 8.2 Principles of Cryptography 596 8.2.1 Symmetric Key Cryptography 
598 8.2.2 Public Key Encryption 604 8.3 Message Integrity and Digital Signatures 610 8.3.1 
Cryptographic Hash Functions 611 8.3.2 Message Authentication Code 613 8.3.3 Digital 
Signatures 614 8.4 End-Point Authentication 621 8.4.1 Authentication Protocol ap1.0 622 8.4.2 
Authentication Protocol ap2.0 622 8.4.3 Authentication Protocol ap3.0 623 8.4.4 Authentication 
Protocol ap3.1 623 8.4.5 Authentication Protocol ap4.0 624 8.5 Securing E-Mail 626 8.5.1 
Secure E-Mail 627 8.5.2 PGP 630 8.6 Securing TCP Connections: SSL 631 8.6.1 The Big Picture 
632 8.6.2 A More Complete Picture 635 8.7 Network-Layer Security: IPsec and Virtual Private 
Networks 637 8.7.1 IPsec and Virtual Private Networks (VPNs) 638 8.7.2 The AH and ESP 
Protocols 640 8.7.3 Security Associations 640 8.7.4 The IPsec Datagram 641 8.7.5 IKE: Key 
Management in IPsec 645 8.8 Securing Wireless LANs 646 8.8.1 Wired Equivalent Privacy (WEP) 
646 8.8.2 IEEE 802.11i 648 8.9 Operational Security: Firewalls and Intrusion Detection Systems 
651 8.9.1 Firewalls 651 8.9.2 Intrusion Detection Systems 659 8.10 Summary 662 Homework 
Problems and Questions 664 Wireshark Lab 672 IPsec Lab 672 Interview: Steven M. Bellovin 
673 Chapter 9 Multimedia Networking 675 9.1 Multimedia Networking Applications 676 9.1.1 
Properties of Video 676 9.1.2 Properties of Audio 677 9.1.3 Types of Multimedia Network 
Applications 679 9.2 Streaming Stored Video 681 9.2.1 UDP Streaming 683 9.2.2 HTTP 
Streaming 684 9.3 Voice-over-IP 688 9.3.1 Limitations of the Best-Effort IP Service 688 9.3.2 
Removing Jitter at the Receiver for Audio 691 9.3.3 Recovering from Packet Loss 694 9.3.4 Case 
Study: VoIP with Skype 697 9.4 Protocols for Real-Time Conversational Applications 700 9.4.1 
RTP 700 9.4.2 SIP 703 9.5 Network Support for Multimedia 709 9.5.1 Dimensioning Best-Effort 
Networks 711 9.5.2 Providing Multiple Classes of Service 712 9.5.3 Diffserv 719 9.5.4 Per-
Connection Quality-of-Service (QoS) Guarantees: Resource Reservation and Call Admission 
723 9.6 Summary 726 Homework Problems and Questions 727 Programming Assignment 735 
Interview: Henning Schulzrinne 736 References 741 Index 783 Chapter 1 Computer Networks 
and the Internet Today’s Internet is arguably the largest engineered system ever created by 
mankind, with hundreds of millions of connected computers, communication links, and 
switches; with billions of users who connect via laptops, tablets, and smartphones; and with an 
array of new Internet-connected “things” including game consoles, surveillance systems, 
watches, eye glasses, thermostats, body scales, and cars. Given that the Internet is so large 
and has so many diverse components and uses, is there any hope of understanding how it 
works? Are there guiding principles and structure that can provide a foundation for 
understanding such an amazingly large and complex system? And if so, is it possible that it 
actually could be both interesting and fun to learn about computer networks? Fortunately, the 
answer to all of these questions is a resounding YES! Indeed, it’s our aim in this book to provide 
you with a modern introduction to the dynamic field of computer networking, giving you the 
principles and practical insights you’ll need to understand not only today’s networks, but 
tomorrow’s as well. This first chapter presents a broad overview of computer networking and 
the Internet. Our goal here is to paint a broad picture and set the context for the rest of this 
book, to see the forest through the trees. We’ll cover a lot of ground in this introductory chapter 


## Page 11

and discuss a lot of the pieces of a computer network, without losing sight of the big picture. 
We’ll structure our overview of computer networks in this chapter as follows. After introducing 
some basic terminology and concepts, we’ll first examine the basic hardware and software 
components that make up a network. We’ll begin at the network’s edge and look at the end 
systems and network applications running in the network. We’ll then explore the core of a 
computer network, examining the links and the switches that transport data, as well as the 
access networks and physical media that connect end systems to the network core. We’ll learn 
that the Internet is a network of networks, and we’ll learn how these networks connect with 
each other. After having completed this overview of the edge and core of a computer network, 
we’ll take the broader and more abstract view in the second half of this chapter. We’ll examine 
delay, loss, and throughput of data in a computer network and provide simple quantitative 
models for end-to-end throughput and delay: models that take into account transmission, 
propagation, and queuing delays. We’ll then introduce some of the key architectural principles 
in computer networking, namely, protocol layering and service models. We’ll also learn that 
computer networks are vulnerable to many different types of attacks; we’ll survey some of 
these attacks and consider how computer networks can be made more secure. Finally, we’ll 
close this chapter with a brief history of computer networking. 1.1 What Is the Internet? In this 
book, we’ll use the public Internet, a specific computer network, as our principal vehicle for 
discussing computer networks and their protocols. But what is the Internet? There are a couple 
of ways to answer this question. First, we can describe the nuts and bolts of the Internet, that 
is, the basic hardware and software components that make up the Internet. Second, we can 
describe the Internet in terms of a networking infrastructure that provides services to 
distributed applications. Let’s begin with the nuts-and-bolts description, using Figure 1.1 to 
illustrate our discussion. 1.1.1 A Nuts-and-Bolts Description The Internet is a computer 
network that interconnects billions of computing devices throughout the world. Not too long 
ago, these computing devices were primarily traditional desktop PCs, Linux workstations, and 
so-called servers that store and transmit information such as Web pages and e-mail messages. 
Increasingly, however, nontraditional Internet “things” such as laptops, smartphones, tablets, 
TVs, gaming consoles, thermostats, home security systems, home appliances, watches, eye 
glasses, cars, traffic control systems and more are being connected to the Internet. Indeed, the 
term computer network is beginning to sound a bit dated, given the many nontraditional devices 
that are being hooked up to the Internet. In Internet jargon, all of these devices are called hosts 
or end systems. By some estimates, in 2015 there were about 5 billion devices connected to the 
Internet, and the number will reach 25 billion by 2020 [Gartner 2014]. It is estimated that in 
2015 there were over 3.2 billion Internet users worldwide, approximately 40% of the world 
population [ITU 2015]. Figure 1.1 Some pieces of the Internet End systems are connected 
together by a network of communication links and packet switches. We’ll see in Section 1.2 
that there are many types of communication links, which are made up of different types of 
physical media, including coaxial cable, copper wire, optical fiber, and radio spectrum. 
Different links can transmit data at different rates, with the transmission rate of a link measured 
in bits/second. When one end system has data to send to another end system, the sending end 
system segments the data and adds header bytes to each segment. The resulting packages of 
information, known as packets in the jargon of computer networks, are then sent through the 
network to the destination end system, where they are reassembled into the original data. A 
packet switch takes a packet arriving on one of its incoming communication links and forwards 
that packet on one of its outgoing communication links. Packet switches come in many shapes 
and flavors, but the two most prominent types in today’s Internet are routers and link-layer 
switches. Both types of switches forward packets toward their ultimate destinations. Link-layer 


## Page 12

switches are typically used in access networks, while routers are typically used in the network 
core. The sequence of communication links and packet switches traversed by a packet from 
the sending end system to the receiving end system is known as a route or path through the 
network. Cisco predicts annual global IP traffic will pass the zettabyte (10 bytes) threshold by 
the end of 2016, and will reach 2 zettabytes per year by 2019 [Cisco VNI 2015]. Packet-switched 
networks (which transport packets) are in many ways similar to transportation networks of 
highways, roads, and intersections (which transport vehicles). Consider, for example, a factory 
that needs to move a large amount of cargo to some destination warehouse located thousands 
of kilometers away. At the factory, the cargo is segmented and loaded into a fleet of trucks. 
Each of the trucks then independently travels through the network of highways, roads, and 
intersections to the destination warehouse. At the destination warehouse, the cargo is 
unloaded and grouped with the rest of the cargo arriving from the same shipment. Thus, in 
many ways, packets are analogous to trucks, communication links are analogous to highways 
and roads, packet switches are analogous to intersections, and end systems are analogous to 
buildings. Just as a truck takes a path through the transportation network, a packet takes a path 
through a computer network. End systems access the Internet through Internet Service 
Providers (ISPs), including residential ISPs such as local cable or telephone companies; 
corporate ISPs; university ISPs; ISPs that provide WiFi access in airports, hotels, coffee shops, 
and other public places; and cellular data ISPs, providing mobile access to our smartphones 
and other devices. Each ISP is in itself a network of packet switches and communication links. 
ISPs provide a variety of types of network access to the end systems, including residential 
broadband access such as cable modem or DSL, high-speed local area network access, and 
mobile wireless access. ISPs also provide Internet access to content providers, connecting 
Web sites and video servers directly to the Internet. The Internet is all about connecting end 
systems to each other, so the ISPs that provide access to end systems must also be 
interconnected. These lower-tier ISPs are interconnected through national and international 
upper-tier ISPs such as Level 3 Communications, AT&T, Sprint, and NTT. An upper-tier ISP 
consists of high-speed routers interconnected with high-speed fiber-optic links. Each ISP 
network, whether upper-tier or lower-tier, is 21 managed independently, runs the IP protocol 
(see below), and conforms to certain naming and address conventions. We’ll examine ISPs and 
their interconnection more closely in Section 1.3. End systems, packet switches, and other 
pieces of the Internet run protocols that control the sending and receiving of information within 
the Internet. The Transmission Control Protocol (TCP) and the Internet Protocol (IP) are two of 
the most important protocols in the Internet. The IP protocol specifies the format of the packets 
that are sent and received among routers and end systems. The Internet’s principal protocols 
are collectively known as TCP/IP. We’ll begin looking into protocols in this introductory chapter. 
But that’s just a start—much of this book is concerned with computer network protocols! Given 
the importance of protocols to the Internet, it’s important that everyone agree on what each 
and every protocol does, so that people can create systems and products that interoperate. 
This is where standards come into play. Internet standards are developed by the Internet 
Engineering Task Force (IETF) [IETF 2016]. The IETF standards documents are called requests 
for comments (RFCs). RFCs started out as general requests for comments (hence the name) to 
resolve network and protocol design problems that faced the precursor to the Internet [Allman 
2011]. RFCs tend to be quite technical and detailed. They define protocols such as TCP, IP, 
HTTP (for the Web), and SMTP (for e-mail). There are currently more than 7,000 RFCs. Other 
bodies also specify standards for network components, most notably for network links. The 
IEEE 802 LAN/MAN Standards Committee [IEEE 802 2016], for example, specifies the Ethernet 
and wireless WiFi standards. 1.1.2 A Services Description Our discussion above has identified 


## Page 13

many of the pieces that make up the Internet. But we can also describe the Internet from an 
entirely different angle—namely, as an infrastructure that provides services to applications. In 
addition to traditional applications such as e-mail and Web surfing, Internet applications 
include mobile smartphone and tablet applications, including Internet messaging, mapping 
with real-time road-traffic information, music streaming from the cloud, movie and television 
streaming, online social networks, video conferencing, multi-person games, and location-
based recommendation systems. The applications are said to be distributed applications, 
since they involve multiple end systems that exchange data with each other. Importantly, 
Internet applications run on end systems— they do not run in the packet switches in the 
network core. Although packet switches facilitate the exchange of data among end systems, 
they are not concerned with the application that is the source or sink of data. Let’s explore a 
little more what we mean by an infrastructure that provides services to applications. To this 
end, suppose you have an exciting new idea for a distributed Internet application, one that may 
greatly benefit humanity or one that may simply make you rich and famous. How might you go 
about transforming this idea into an actual Internet application? Because applications run on 
end systems, you are going to need to write programs that run on the end systems. You might, 
for example, write your programs in Java, C, or Python. Now, because you are developing a 
distributed Internet application, the programs running on the different end systems will need to 
send data to each other. And here we get to a central issue—one that leads to the alternative 
way of describing the Internet as a platform for applications. How does one program running on 
one end system instruct the Internet to deliver data to another program running on another end 
system? End systems attached to the Internet provide a socket interface that specifies how a 
program running on one end system asks the Internet infrastructure to deliver data to a specific 
destination program running on another end system. This Internet socket interface is a set of 
rules that the sending program must follow so that the Internet can deliver the data to the 
destination program. We’ll discuss the Internet socket interface in detail in Chapter 2. For now, 
let’s draw upon a simple analogy, one that we will frequently use in this book. Suppose Alice 
wants to send a letter to Bob using the postal service. Alice, of course, can’t just write the letter 
(the data) and drop the letter out her window. Instead, the postal service requires that Alice put 
the letter in an envelope; write Bob’s full name, address, and zip code in the center of the 
envelope; seal the envelope; put a stamp in the upper-right-hand corner of the envelope; and 
finally, drop the envelope into an official postal service mailbox. Thus, the postal service has its 
own “postal service interface,” or set of rules, that Alice must follow to have the postal service 
deliver her letter to Bob. In a similar manner, the Internet has a socket interface that the 
program sending data must follow to have the Internet deliver the data to the program that will 
receive the data. The postal service, of course, provides more than one service to its 
customers. It provides express delivery, reception confirmation, ordinary use, and many more 
services. In a similar manner, the Internet provides multiple services to its applications. When 
you develop an Internet application, you too must choose one of the Internet’s services for your 
application. We’ll describe the Internet’s services in Chapter 2. We have just given two 
descriptions of the Internet; one in terms of its hardware and software components, the other in 
terms of an infrastructure for providing services to distributed applications. But perhaps you are 
still confused as to what the Internet is. What are packet switching and TCP/IP? What are 
routers? What kinds of communication links are present in the Internet? What is a distributed 
application? How can a thermostat or body scale be attached to the Internet? If you feel a bit 
overwhelmed by all of this now, don’t worry—the purpose of this book is to introduce you to 
both the nuts and bolts of the Internet and the principles that govern how and why it works. 
We’ll explain these important terms and questions in the following sections and chapters. 1.1.3 


## Page 14

What Is a Protocol? Now that we’ve got a bit of a feel for what the Internet is, let’s consider 
another important buzzword in computer networking: protocol. What is a protocol? What does 
a protocol do? A Human Analogy It is probably easiest to understand the notion of a computer 
network protocol by first considering some human analogies, since we humans execute 
protocols all of the time. Consider what you do when you want to ask someone for the time of 
day. A typical exchange is shown in Figure 1.2. Human protocol (or good manners, at least) 
dictates that one first offer a greeting (the first “Hi” in Figure 1.2) to initiate communication with 
someone else. The typical response to a “Hi” is a returned “Hi” message. Implicitly, one then 
takes a cordial “Hi” response as an indication that one can proceed and ask for the time of day. 
A different response to the initial “Hi” (such as “Don’t bother me!” or “I don’t speak English,” or 
some unprintable reply) might Figure 1.2 A human protocol and a computer network protocol 
indicate an unwillingness or inability to communicate. In this case, the human protocol would 
be not to ask for the time of day. Sometimes one gets no response at all to a question, in which 
case one typically gives up asking that person for the time. Note that in our human protocol, 
there are specific messages we send, and specific actions we take in response to the received 
reply messages or other events (such as no reply within some given amount of time). Clearly, 
transmitted and received messages, and actions taken when these messages are sent or 
received or other events occur, play a central role in a human protocol. If people run different 
protocols (for example, if one person has manners but the other does not, or if one understands 
the concept of time and the other does not) the protocols do not interoperate and no useful 
work can be accomplished. The same is true in networking—it takes two (or more) 
communicating entities running the same protocol in order to accomplish a task. Let’s consider 
a second human analogy. Suppose you’re in a college class (a computer networking class, for 
example!). The teacher is droning on about protocols and you’re confused. The teacher stops to 
ask, “Are there any questions?” (a message that is transmitted to, and received by, all students 
who are not sleeping). You raise your hand (transmitting an implicit message to the teacher). 
Your teacher acknowledges you with a smile, saying “Yes . . .” (a transmitted message 
encouraging you to ask your question—teachers love to be asked questions), and you then ask 
your question (that is, transmit your message to your teacher). Your teacher hears your 
question (receives your question message) and answers (transmits a reply to you). Once again, 
we see that the transmission and receipt of messages, and a set of conventional actions taken 
when these messages are sent and received, are at the heart of this question-and-answer 
protocol. Network Protocols A network protocol is similar to a human protocol, except that the 
entities exchanging messages and taking actions are hardware or software components of 
some device (for example, computer, smartphone, tablet, router, or other network-capable 
device). All activity in the Internet that involves two or more communicating remote entities is 
governed by a protocol. For example, hardware-implemented protocols in two physically 
connected computers control the flow of bits on the “wire” between the two network interface 
cards; congestion-control protocols in end systems control the rate at which packets are 
transmitted between sender and receiver; protocols in routers determine a packet’s path from 
source to destination. Protocols are running everywhere in the Internet, and consequently 
much of this book is about computer network protocols. As an example of a computer network 
protocol with which you are probably familiar, consider what happens when you make a 
request to a Web server, that is, when you type the URL of a Web page into your Web browser. 
The scenario is illustrated in the right half of Figure 1.2. First, your computer will send a 
connection request message to the Web server and wait for a reply. The Web server will 
eventually receive your connection request message and return a connection reply message. 
Knowing that it is now OK to request the Web document, your computer then sends the name of 


## Page 15

the Web page it wants to fetch from that Web server in a GET message. Finally, the Web server 
returns the Web page (file) to your computer. Given the human and networking examples 
above, the exchange of messages and the actions taken when these messages are sent and 
received are the key defining elements of a protocol: A protocol defines the format and the 
order of messages exchanged between two or more communicating entities, as well as the 
actions taken on the transmission and/or receipt of a message or other event. The Internet, and 
computer networks in general, make extensive use of protocols. Different protocols are used to 
accomplish different communication tasks. As you read through this book, you will learn that 
some protocols are simple and straightforward, while others are complex and intellectually 
deep. Mastering the field of computer networking is equivalent to understanding the what, why, 
and how of networking protocols. 1.2 The Network Edge In the previous section we presented a 
high-level overview of the Internet and networking protocols. We are now going to delve a bit 
more deeply into the components of a computer network (and the Internet, in particular). We 
begin in this section at the edge of a network and look at the components with which we are 
most familiar—namely, the computers, smartphones and other devices that we use on a daily 
basis. In the next section we’ll move from the network edge to the network core and examine 
switching and routing in computer networks. Recall from the previous section that in computer 
networking jargon, the computers and other devices connected to the Internet are often 
referred to as end systems. They are referred to as end systems because they sit at the edge of 
the Internet, as shown in Figure 1.3. The Internet’s end systems include desktop computers 
(e.g., desktop PCs, Macs, and Linux boxes), servers (e.g., Web and e-mail servers), and mobile 
devices (e.g., laptops, smartphones, and tablets). Furthermore, an increasing number of non-
traditional “things” are being attached to the Internet as end systems (see the Case History 
feature). End systems are also referred to as hosts because they host (that is, run) application 
programs such as a Web browser program, a Web server program, an e-mail client program, or 
an e-mail server program. Throughout this book we will use the Figure 1.3 End-system 
interaction CASE HISTORY THE INTERNET OF THINGS Can you imagine a world in which just 
about everything is wirelessly connected to the Internet? A world in which most people, cars, 
bicycles, eye glasses, watches, toys, hospital equipment, home sensors, classrooms, video 
surveillance systems, atmospheric sensors, store-shelf products, and pets are connected? 
This world of the Internet of Things (IoT) may actually be just around the corner. By some 
estimates, as of 2015 there are already 5 billion things connected to the Internet, and the 
number could reach 25 billion by 2020 [Gartner 2014]. These things include our smartphones, 
which already follow us around in our homes, offices, and cars, reporting our geolocations and 
usage data to our ISPs and Internet applications. But in addition to our smartphones, a wide-
variety of non-traditional “things” are already available as products. For example, there are 
Internet-connected wearables, including watches (from Apple and many others) and eye 
glasses. Internet-connected glasses can, for example, upload everything we see to the cloud, 
allowing us to share our visual experiences with people around the world in realtime. There are 
Internet-connected things already available for the smart home, including Internet-connected 
thermostats that can be controlled remotely from our smartphones, and Internet-connected 
body scales, enabling us to graphically review the progress of our diets from our smartphones. 
There are Internet-connected toys, including dolls that recognize and interpret a child’s speech 
and respond appropriately. The IoT offers potentially revolutionary benefits to users. But at the 
same time there are also huge security and privacy risks. For example, attackers, via the 
Internet, might be able to hack into IoT devices or into the servers collecting data from IoT 
devices. For example, an attacker could hijack an Internet-connected doll and talk directly with 
a child; or an attacker could hack into a database that stores personal health and activity 


## Page 16

information collected from wearable devices. These security and privacy concerns could 
undermine the consumer confidence necessary for the technologies to meet their full potential 
and may result in less widespread adoption [FTC 2015]. terms hosts and end systems 
interchangeably; that is, host = end system. Hosts are sometimes further divided into two 
categories: clients and servers. Informally, clients tend to be desktop and mobile PCs, 
smartphones, and so on, whereas servers tend to be more powerful machines that store and 
distribute Web pages, stream video, relay e-mail, and so on. Today, most of the servers from 
which we receive search results, e-mail, Web pages, and videos reside in large data centers. 
For example, Google has 50-100 data centers, including about 15 large centers, each with more 
than 100,000 servers. 1.2.1 Access Networks Having considered the applications and end 
systems at the “edge of the network,” let’s next consider the access network—the network that 
physically connects an end system to the first router (also known as the “edge router”) on a 
path from the end system to any other distant end system. Figure 1.4 shows several types of 
access Figure 1.4 Access networks networks with thick, shaded lines and the settings (home, 
enterprise, and wide-area mobile wireless) in which they are used. Home Access: DSL, Cable, 
FTTH, Dial-Up, and Satellite In developed countries as of 2014, more than 78 percent of the 
households have Internet access, with Korea, Netherlands, Finland, and Sweden leading the 
way with more than 80 percent of households having Internet access, almost all via a high-
speed broadband connection [ITU 2015]. Given this widespread use of home access networks 
let’s begin our overview of access networks by considering how homes connect to the Internet. 
Today, the two most prevalent types of broadband residential access are digital subscriber line 
(DSL) and cable. A residence typically obtains DSL Internet access from the same local 
telephone company (telco) that provides its wired local phone access. Thus, when DSL is used, 
a customer’s telco is also its ISP. As shown in Figure 1.5, each customer’s DSL modem uses the 
existing telephone line (twistedpair copper wire, which we’ll discuss in Section 1.2.2) to 
exchange data with a digital subscriber line access multiplexer (DSLAM) located in the telco’s 
local central office (CO). The home’s DSL modem takes digital data and translates it to high-
frequency tones for transmission over telephone wires to the CO; the analog signals from many 
such houses are translated back into digital format at the DSLAM. The residential telephone line 
carries both data and traditional telephone signals simultaneously, which are encoded at 
different frequencies: A high-speed downstream channel, in the 50 kHz to 1 MHz band A 
medium-speed upstream channel, in the 4 kHz to 50 kHz band An ordinary two-way telephone 
channel, in the 0 to 4 kHz band This approach makes the single DSL link appear as if there were 
three separate links, so that a telephone call and an Internet connection can share the DSL link 
at the same time. Figure 1.5 DSL Internet access (We’ll describe this technique of frequency-
division multiplexing in Section 1.3.1.) On the customer side, a splitter separates the data and 
telephone signals arriving to the home and forwards the data signal to the DSL modem. On the 
telco side, in the CO, the DSLAM separates the data and phone signals and sends the data into 
the Internet. Hundreds or even thousands of households connect to a single DSLAM 
[Dischinger 2007]. The DSL standards define multiple transmission rates, including 12 Mbps 
downstream and 1.8 Mbps upstream [ITU 1999], and 55 Mbps downstream and 15 Mbps 
upstream [ITU 2006]. Because the downstream and upstream rates are different, the access is 
said to be asymmetric. The actual downstream and upstream transmission rates achieved may 
be less than the rates noted above, as the DSL provider may purposefully limit a residential rate 
when tiered service (different rates, available at different prices) are offered. The maximum rate 
is also limited by the distance between the home and the CO, the gauge of the twisted-pair line 
and the degree of electrical interference. Engineers have expressly designed DSL for short 
distances between the home and the CO; generally, if the residence is not located within 5 to 10 


## Page 17

miles of the CO, the residence must resort to an alternative form of Internet access. While DSL 
makes use of the telco’s existing local telephone infrastructure, cable Internet access makes 
use of the cable television company’s existing cable television infrastructure. A residence 
obtains cable Internet access from the same company that provides its cable television. As 
illustrated in Figure 1.6, fiber optics connect the cable head end to neighborhood-level 
junctions, from which traditional coaxial cable is then used to reach individual houses and 
apartments. Each neighborhood junction typically supports 500 to 5,000 homes. Because both 
fiber and coaxial cable are employed in this system, it is often referred to as hybrid fiber coax 
(HFC). Figure 1.6 A hybrid fiber-coaxial access network Cable internet access requires special 
modems, called cable modems. As with a DSL modem, the cable modem is typically an 
external device and connects to the home PC through an Ethernet port. (We will discuss 
Ethernet in great detail in Chapter 6.) At the cable head end, the cable modem termination 
system (CMTS) serves a similar function as the DSL network’s DSLAM—turning the analog 
signal sent from the cable modems in many downstream homes back into digital format. Cable 
modems divide the HFC network into two channels, a downstream and an upstream channel. 
As with DSL, access is typically asymmetric, with the downstream channel typically allocated a 
higher transmission rate than the upstream channel. The DOCSIS 2.0 standard defines 
downstream rates up to 42.8 Mbps and upstream rates of up to 30.7 Mbps. As in the case of 
DSL networks, the maximum achievable rate may not be realized due to lower contracted data 
rates or media impairments. One important characteristic of cable Internet access is that it is a 
shared broadcast medium. In particular, every packet sent by the head end travels downstream 
on every link to every home and every packet sent by a home travels on the upstream channel to 
the head end. For this reason, if several users are simultaneously downloading a video file on 
the downstream channel, the actual rate at which each user receives its video file will be 
significantly lower than the aggregate cable downstream rate. On the other hand, if there are 
only a few active users and they are all Web surfing, then each of the users may actually receive 
Web pages at the full cable downstream rate, because the users will rarely request a Web page 
at exactly the same time. Because the upstream channel is also shared, a distributed multiple 
access protocol is needed to coordinate transmissions and avoid collisions. (We’ll discuss this 
collision issue in some detail in Chapter 6.) Although DSL and cable networks currently 
represent more than 85 percent of residential broadband access in the United States, an up-
and-coming technology that provides even higher speeds is fiber to the home (FTTH) [FTTH 
Council 2016]. As the name suggests, the FTTH concept is simple—provide an optical fiber path 
from the CO directly to the home. Many countries today—including the UAE, South Korea, Hong 
Kong, Japan, Singapore, Taiwan, Lithuania, and Sweden—now have household penetration 
rates exceeding 30% [FTTH Council 2016]. There are several competing technologies for optical 
distribution from the CO to the homes. The simplest optical distribution network is called direct 
fiber, with one fiber leaving the CO for each home. More commonly, each fiber leaving the 
central office is actually shared by many homes; it is not until the fiber gets relatively close to 
the homes that it is split into individual customer-specific fibers. There are two competing 
optical-distribution network architectures that perform this splitting: active optical networks 
(AONs) and passive optical networks (PONs). AON is essentially switched Ethernet, which is 
discussed in Chapter 6. Here, we briefly discuss PON, which is used in Verizon’s FIOS service. 
Figure 1.7 shows FTTH using the PON distribution architecture. Each home has an optical 
network terminator (ONT), which is connected by dedicated optical fiber to a neighborhood 
splitter. The splitter combines a number of homes (typically less Figure 1.7 FTTH Internet 
access than 100) onto a single, shared optical fiber, which connects to an optical line 
terminator (OLT) in the telco’s CO. The OLT, providing conversion between optical and 


## Page 18

electrical signals, connects to the Internet via a telco router. In the home, users connect a 
home router (typically a wireless router) to the ONT and access the Internet via this home 
router. In the PON architecture, all packets sent from OLT to the splitter are replicated at the 
splitter (similar to a cable head end). FTTH can potentially provide Internet access rates in the 
gigabits per second range. However, most FTTH ISPs provide different rate offerings, with the 
higher rates naturally costing more money. The average downstream speed of US FTTH 
customers was approximately 20 Mbps in 2011 (compared with 13 Mbps for cable access 
networks and less than 5 Mbps for DSL) [FTTH Council 2011b]. Two other access network 
technologies are also used to provide Internet access to the home. In locations where DSL, 
cable, and FTTH are not available (e.g., in some rural settings), a satellite link can be used to 
connect a residence to the Internet at speeds of more than 1 Mbps; StarBand and HughesNet 
are two such satellite access providers. Dial-up access over traditional phone lines is based on 
the same model as DSL—a home modem connects over a phone line to a modem in the ISP. 
Compared with DSL and other broadband access networks, dial-up access is excruciatingly 
slow at 56 kbps. Access in the Enterprise (and the Home): Ethernet and WiFi On corporate and 
university campuses, and increasingly in home settings, a local area network (LAN) is used to 
connect an end system to the edge router. Although there are many types of LAN technologies, 
Ethernet is by far the most prevalent access technology in corporate, university, and home 
networks. As shown in Figure 1.8, Ethernet users use twisted-pair copper wire to connect to an 
Ethernet switch, a technology discussed in detail in Chapter 6. The Ethernet switch, or a 
network of such Figure 1.8 Ethernet Internet access interconnected switches, is then in turn 
connected into the larger Internet. With Ethernet access, users typically have 100 Mbps or 1 
Gbps access to the Ethernet switch, whereas servers may have 1 Gbps or even 10 Gbps access. 
Increasingly, however, people are accessing the Internet wirelessly from laptops, smartphones, 
tablets, and other “things” (see earlier sidebar on “Internet of Things”). In a wireless LAN 
setting, wireless users transmit/receive packets to/from an access point that is connected into 
the enterprise’s network (most likely using wired Ethernet), which in turn is connected to the 
wired Internet. A wireless LAN user must typically be within a few tens of meters of the access 
point. Wireless LAN access based on IEEE 802.11 technology, more colloquially known as WiFi, 
is now just about everywhere—universities, business offices, cafes, airports, homes, and even 
in airplanes. In many cities, one can stand on a street corner and be within range of ten or 
twenty base stations (for a browseable global map of 802.11 base stations that have been 
discovered and logged on a Web site by people who take great enjoyment in doing such things, 
see [wigle.net 2016]). As discussed in detail in Chapter 7, 802.11 today provides a shared 
transmission rate of up to more than 100 Mbps. Even though Ethernet and WiFi access 
networks were initially deployed in enterprise (corporate, university) settings, they have recently 
become relatively common components of home networks. Many homes combine broadband 
residential access (that is, cable modems or DSL) with these inexpensive wireless LAN 
technologies to create powerful home networks [Edwards 2011]. Figure 1.9 shows a typical 
home network. This home network consists of a roaming laptop as well as a wired PC; a base 
station (the wireless access point), which communicates with the wireless PC and other 
wireless devices in the home; a cable modem, providing broadband access to the Internet; and 
a router, which interconnects the base station and the stationary PC with the cable modem. 
This network allows household members to have broadband access to the Internet with one 
member roaming from the kitchen to the backyard to the bedrooms. Figure 1.9 A typical home 
network Wide-Area Wireless Access: 3G and LTE Increasingly, devices such as iPhones and 
Android devices are being used to message, share photos in social networks, watch movies, 
and stream music while on the run. These devices employ the same wireless infrastructure 


## Page 19

used for cellular telephony to send/receive packets through a base station that is operated by 
the cellular network provider. Unlike WiFi, a user need only be within a few tens of kilometers 
(as opposed to a few tens of meters) of the base station. Telecommunications companies have 
made enormous investments in so-called third-generation (3G) wireless, which provides 
packet-switched wide-area wireless Internet access at speeds in excess of 1 Mbps. But even 
higher-speed wide-area access technologies—a fourth-generation (4G) of wide-area wireless 
networks—are already being deployed. LTE (for “Long-Term Evolution”—a candidate for Bad 
Acronym of the Year Award) has its roots in 3G technology, and can achieve rates in excess of 
10 Mbps. LTE downstream rates of many tens of Mbps have been reported in commercial 
deployments. We’ll cover the basic principles of wireless networks and mobility, as well as 
WiFi, 3G, and LTE technologies (and more!) in Chapter 7. 1.2.2 Physical Media In the previous 
subsection, we gave an overview of some of the most important network access technologies in 
the Internet. As we described these technologies, we also indicated the physical media used. 
For example, we said that HFC uses a combination of fiber cable and coaxial cable. We said 
that DSL and Ethernet use copper wire. And we said that mobile access networks use the radio 
spectrum. In this subsection we provide a brief overview of these and other transmission media 
that are commonly used in the Internet. In order to define what is meant by a physical medium, 
let us reflect on the brief life of a bit. Consider a bit traveling from one end system, through a 
series of links and routers, to another end system. This poor bit gets kicked around and 
transmitted many, many times! The source end system first transmits the bit, and shortly 
thereafter the first router in the series receives the bit; the first router then transmits the bit, and 
shortly thereafter the second router receives the bit; and so on. Thus our bit, when traveling 
from source to destination, passes through a series of transmitter-receiver pairs. For each 
transmitterreceiver pair, the bit is sent by propagating electromagnetic waves or optical pulses 
across a physical medium. The physical medium can take many shapes and forms and does 
not have to be of the same type for each transmitter-receiver pair along the path. Examples of 
physical media include twisted-pair copper wire, coaxial cable, multimode fiber-optic cable, 
terrestrial radio spectrum, and satellite radio spectrum. Physical media fall into two categories: 
guided media and unguided media. With guided media, the waves are guided along a solid 
medium, such as a fiber-optic cable, a twisted-pair copper wire, or a coaxial cable. With 
unguided media, the waves propagate in the atmosphere and in outer space, such as in a 
wireless LAN or a digital satellite channel. But before we get into the characteristics of the 
various media types, let us say a few words about their costs. The actual cost of the physical 
link (copper wire, fiber-optic cable, and so on) is often relatively minor compared with other 
networking costs. In particular, the labor cost associated with the installation of the physical 
link can be orders of magnitude higher than the cost of the material. For this reason, many 
builders install twisted pair, optical fiber, and coaxial cable in every room in a building. Even if 
only one medium is initially used, there is a good chance that another medium could be used in 
the near future, and so money is saved by not having to lay additional wires in the future. 
Twisted-Pair Copper Wire The least expensive and most commonly used guided transmission 
medium is twisted-pair copper wire. For over a hundred years it has been used by telephone 
networks. In fact, more than 99 percent of the wired connections from the telephone handset to 
the local telephone switch use twisted-pair copper wire. Most of us have seen twisted pair in 
our homes (or those of our parents or grandparents!) and work environments. Twisted pair 
consists of two insulated copper wires, each about 1 mm thick, arranged in a regular spiral 
pattern. The wires are twisted together to reduce the electrical interference from similar pairs 
close by. Typically, a number of pairs are bundled together in a cable by wrapping the pairs in a 
protective shield. A wire pair constitutes a single communication link. Unshielded twisted pair 


## Page 20

(UTP) is commonly used for computer networks within a building, that is, for LANs. Data rates 
for LANs using twisted pair today range from 10 Mbps to 10 Gbps. The data rates that can be 
achieved depend on the thickness of the wire and the distance between transmitter and 
receiver. When fiber-optic technology emerged in the 1980s, many people disparaged twisted 
pair because of its relatively low bit rates. Some people even felt that fiber-optic technology 
would completely replace twisted pair. But twisted pair did not give up so easily. Modern 
twisted-pair technology, such as category 6a cable, can achieve data rates of 10 Gbps for 
distances up to a hundred meters. In the end, twisted pair has emerged as the dominant 
solution for high-speed LAN networking. As discussed earlier, twisted pair is also commonly 
used for residential Internet access. We saw that dial-up modem technology enables access at 
rates of up to 56 kbps over twisted pair. We also saw that DSL (digital subscriber line) 
technology has enabled residential users to access the Internet at tens of Mbps over twisted 
pair (when users live close to the ISP’s central office). Coaxial Cable Like twisted pair, coaxial 
cable consists of two copper conductors, but the two conductors are concentric rather than 
parallel. With this construction and special insulation and shielding, coaxial cable can achieve 
high data transmission rates. Coaxial cable is quite common in cable television systems. As we 
saw earlier, cable television systems have recently been coupled with cable modems to 
provide residential users with Internet access at rates of tens of Mbps. In cable television and 
cable Internet access, the transmitter shifts the digital signal to a specific frequency band, and 
the resulting analog signal is sent from the transmitter to one or more receivers. Coaxial cable 
can be used as a guided shared medium. Specifically, a number of end systems can be 
connected directly to the cable, with each of the end systems receiving whatever is sent by the 
other end systems. Fiber Optics An optical fiber is a thin, flexible medium that conducts pulses 
of light, with each pulse representing a bit. A single optical fiber can support tremendous bit 
rates, up to tens or even hundreds of gigabits per second. They are immune to electromagnetic 
interference, have very low signal attenuation up to 100 kilometers, and are very hard to tap. 
These characteristics have made fiber optics the preferred longhaul guided transmission 
media, particularly for overseas links. Many of the long-distance telephone networks in the 
United States and elsewhere now use fiber optics exclusively. Fiber optics is also prevalent in 
the backbone of the Internet. However, the high cost of optical devices—such as transmitters, 
receivers, and switches—has hindered their deployment for short-haul transport, such as in a 
LAN or into the home in a residential access network. The Optical Carrier (OC) standard link 
speeds range from 51.8 Mbps to 39.8 Gbps; these specifications are often referred to as OC-n, 
where the link speed equals n ∞ 51.8 Mbps. Standards in use today include OC-1, OC-3, OC-12, 
OC-24, OC-48, OC96, OC-192, OC-768. [Mukherjee 2006, Ramaswami 2010] provide coverage 
of various aspects of optical networking. Terrestrial Radio Channels Radio channels carry 
signals in the electromagnetic spectrum. They are an attractive medium because they require 
no physical wire to be installed, can penetrate walls, provide connectivity to a mobile user, and 
can potentially carry a signal for long distances. The characteristics of a radio channel depend 
significantly on the propagation environment and the distance over which a signal is to be 
carried. Environmental considerations determine path loss and shadow fading (which decrease 
the signal strength as the signal travels over a distance and around/through obstructing 
objects), multipath fading (due to signal reflection off of interfering objects), and interference 
(due to other transmissions and electromagnetic signals). Terrestrial radio channels can be 
broadly classified into three groups: those that operate over very short distance (e.g., with one 
or two meters); those that operate in local areas, typically spanning from ten to a few hundred 
meters; and those that operate in the wide area, spanning tens of kilometers. Personal devices 
such as wireless headsets, keyboards, and medical devices operate over short distances; the 

