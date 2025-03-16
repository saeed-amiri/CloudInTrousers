# Module 4: Networking

In this module:
* Describe the **basic concepts** of networking,
* Describe the difference between **public and private** networking resources,
* Explain a **virtual private gateway** using a real life scenario,
* Explain a **virtual private network (VPN)** using a real life scenario,
* Describe the benefit of AWS **Direct Connect**,
* Describe the benefit of **hybrid deployments**,
* Describe the layers of **security** used in an IT strategy,
* Describe the services customers use to interact with the **AWS global network**.

## Connectivity to AWS

### Some Definitions:
- **Virtual Private Cloud:**
    * *A virtual private cloud (VPC) is an on-demand configurable pool of shared resources allocated within a public cloud environment, providing a certain level of isolation between the different organizations (denoted as users hereafter) using the resources. The isolation between one VPC user and all other users of the same cloud (other VPC users as well as other public cloud users) is achieved normally through allocation of a private IP subnet and a virtual communication construct (such as a VLAN or a set of encrypted communication channels) per user [[wiki](https://en.wikipedia.org/wiki/Virtual_private_cloud)].*

- **Subnet:**
    * *A subnetwork, or subnet, is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called subnetting [[wiki](https://en.wikipedia.org/wiki/Subnet)].*

- **Internetgateway (IGW):**
    * *Ein Internetgateway ist eine Schlüsselstelle oder -adresse in einem lokalen Netzwerk, welche Teilnehmern innerhalb des Netzwerkes Datenaustausch mit dem Internet ermöglicht [[wiki](https://de.wikipedia.org/wiki/Internetgateway)].*

- **AWS Direct Connect:**
    * *AWS Direct Connect is a networking service that provides an alternative to using the internet to connect to AWS. Using AWS Direct Connect, data that would have previously been transported over the internet is delivered through a private network connection between your facilities and AWS [[aws](https://www.google.com/search?client=ubuntu-sn&channel=fs&q=AWS+Direct+Connect)].*

## Subnets and Network Access Control Lists
AWS provides comprehensive security solutions across every layer, including:
- network hardening,
- application security,
- user identity management,
- DDoS protection,
- data integrity,
- encryption.

Inside VPC, subnets primarily control access to gateways. Public subnets connect to the internet gateway; private subnets do not. Beyond gateway access, subnets manage traffic permissions through Network Access Control List (ACLs), which act as **stateless** filters—checking every incoming and outgoing packet independently.

Network ACLs evaluate traffic at subnet boundaries, much like passport control at country borders. Each packet crossing the subnet is independently checked against a predefined list of allowed or blocked addresses. This stateless approach ensures robust perimeter security but doesn't handle specific traffic rules for individual instances within the subnet.

Instance-specific traffic rules are managed by security groups, which act like the doorman at a building entrance. By default, security groups block all incoming traffic, making EC2 instances highly secure. To accept external traffic, rules must explicitly allow specific ports or IP addresses. Security groups are **stateful**, automatically allowing return traffic without needing explicit outbound rules.

Let's consider sending a packet from Instance A (subnet 1) to Instance B (subnet 2) within the same VPC:
- Instance A’s security group checks and allows outbound traffic,
- The packet crosses subnet 1’s network ACL boundary, where it’s evaluated against the stateless rules,
- After approval, the packet enters subnet 2 through its network ACL,
- Instance B’s security group evaluates inbound traffic rules before permitting the packet to reach Instance B.

Return traffic (from Instance B back to Instance A):
- Instance B’s security group allows return traffic automatically (stateful behavior),
- The packet crosses subnet 2’s network ACL, undergoing stateless evaluation again,
- Packet enters subnet 1’s network ACL, evaluated once more.

Though multiple evaluations occur, AWS networking is designed to handle these checks instantly, ensuring secure and efficient traffic management without noticeable latency.

In short, AWS's layered security using subnets and security groups effectively manages both broad network controls and fine-grained instance-level access, providing comprehensive protection for your resources.


## Global Networking:
When customers interact with our AWS-hosted website, two key AWS services come into play: **Route 53** and **Amazon CloudFront**.

**Route 53** is AWS's highly available and scalable **Domain Name Service (DNS)**. DNS translates website names into IP addresses that computers understand. When a customer types the website URL into their browser, Route 53 translates that request into an IP address, guiding the browser to the correct server location. Route 53 supports various routing policies to optimize performance, such as:
- **Latency-based Routing**: Directs users to the region with the lowest latency,
- **Geolocation DNS**: Routes traffic based on users' geographic location (e.g., North American traffic to Oregon, European traffic to Dublin),
- **Weighted Round Robin**: Distributes traffic according to assigned weights, balancing the load.

Additionally, Route 53 allows to purchase and manage the domain names directly within AWS.

**Amazon CloudFront**, on the other hand, is AWS’s **Content Delivery Network (CDN)**. It uses **Edge locations—servers** strategically placed around the world—to deliver website content quickly. By caching static web assets (images, GIFs, etc.) closer to users, CloudFront significantly reduces latency. For instance, North American users can access content served from nearby North American Edge locations, while European users get content served from Edge locations like Dublin. This ensures optimal performance and rapid content delivery worldwide.

Together, Route 53 and CloudFront help deliver a fast, reliable, and efficient web experience for your global customers.
