# Notes from AWS Cloud Practitioner Essentials
[Text are from AWS, otherwise mentioned]

## Client-Server Model:
The client–server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients [wiki].

## How the Browser Interacts With the Servers? [[see](https://www.geeksforgeeks.org/client-server-model/)]


When a user tries to access a website or file, several steps occur in the background to fetch and display the content:

   1. The user enters a URL (Uniform Resource Locator) into their web browser. This prompts the browser to send a request to the DNS (Domain Name System) server to locate the corresponding web server.
   2. The DNS server searches for the IP address linked to the requested domain.
   3. Once found, the DNS server returns the web server’s IP address to the browser.
   4. The browser then sends an HTTP/HTTPS request to the identified web server’s IP address.
   5. The web server processes the request and responds by sending the required files (such as HTML, CSS, JavaScript, and media files) back to the browser.
   6. The browser interprets these files and constructs the webpage using various components:
      *  DOM (Document Object Model) interpreter for structuring the page.
      *  CSS interpreter for styling and layout.
      *  JavaScript engine for dynamic interactions.
      *  These are optimized by JIT (Just-In-Time) compilation for better performance.
    7. Finally, the fully rendered website is displayed to the user.

## Advantages and Disadvantages of the Client-Server Model
**Advantages:**

- Centralized Management: All data and resources are stored in a single location, making it easier to manage and secure.
- Cost Efficiency: Requires lower maintenance costs compared to distributed systems, and data recovery is more feasible.
- Scalability: The client and server can be upgraded independently, allowing for flexible system expansion.

**Disadvantages:**

- Security Risks: If the server is compromised, clients can be infected with viruses, Trojans, or worms.
- Vulnerability to Attacks: Servers are susceptible to Denial of Service (DoS) attacks, which can disrupt access.
- Data Integrity Risks: Information transmitted between the client and server can be spoofed, intercepted, or altered by attackers.
- Phishing & MITM Attacks: Hackers can steal login credentials or sensitive data through Man-in-the-Middle (MITM) attacks or phishing schemes.


## Deployment Models for Cloud Computing:
1. cloud-based:
    - Run all parts of the application in the cloud.
    - Migrate existing applications to the cloud.
    - Design and build new applications in the cloud.
2. on-premises:
    - Deploy resources by using virtualization and resource management tools.
    - Increase resource utilization by using application management and virtualization technologies.
3. hybrid:
    - Connect cloud-based resources to on-premises infrastructure.
    - Integrate cloud-based resources with legacy IT applications.
    
### Benefits of Cloud Computing:
1. Pay for what you use!
2. Pay when you use!
3. No need to `alloc` or `malloc`!
4. Use more, pay less!
5. Speed up as you in run!
6. Be Marco Polo!


## Elastic Cloud Computing (**EC2**):
Amazon EC2 offers the broadest and deepest compute platform, with over 750 instances and choice of the latest processor, storage, networking, operating system, and purchase model to help you best match the needs of your workload. We are the first major cloud provider that supports Intel, AMD, and Arm processors, the only cloud with on-demand EC2 Mac instances, and the only cloud with 400 Gbps Ethernet networking. We offer the best price performance for machine learning training, as well as the lowest cost per inference instances in the cloud. More SAP, high performance computing (HPC), ML, and Windows workloads run on AWS than any other cloud.

**Benefits of EC2:**
1. Access reliable, scalable (SLA) infrastructure on demand. Scale capacity within minutes with SLA commitment of 99.99% availability.
2. Provide secure compute for your applications. Security is built into the foundation of Amazon EC2 with the `AWS Nitro` System,
    * The Nitro System is a collection of hardware and software components built by AWS that enable high performance, high availability, and high security. 
3. Optimize performance and cost: Migrate and build apps with ease using AWS Migration Tools, AWS Managed Services, or `Amazon Lightsail`. Learn how AWS can help:
    * Amazon Lightsail is a powerful virtual server that is built for reliability and performance. Intuitive management console with preconfigured Linux and Windows application stacks. Virtual private Cloud. Easily Manage Clusters. No Upfront Commitment. Highly Scalable.


## Amazon EC2 Instance Types:
1. **General purpose instances:**
    * Application servers,
    * Gaming servers,
    * Backend servers for enterprise applications,
    * Small and medium databases.
2. **Compute optimized instances:**
    * Dedicated and compute-intensive applications.
3. **Memory optimized instances:**
    * Large datasets,
    * High-performance database in real-time processing.
4. **Accelerated computing instances:**
    *  floating-point number calculations,
    * Graphics processing,
    * Data pattern matching.
5. **Storage optimized instances:**
    * High, sequential read and write access to large datasets
    * Distributed file systems,
    * Data warehousing applications,
    * High-frequency online transaction processing (OLTP) systems.
    * are designed to deliver tens of thousands of low-latency, random input/output operations per second (IOPS) to applications. 

## Amazon EC2 Pricing:
- **On-Demand:**
    * Pay for the duration of use,
    * Per hour or per second,
    * No long term commitment,
    * No upfront payments.
- **Savings Plans:**
    * For commitment usage for one or three-year term.
    * Can lead to $72%$ saving.
- **Reserved Instances:**
    * For one or three-year commitment,
    * For steady-state workload,
    * Up to $75%$ less versus On-Demand,
    *  Three options:
        - All upfront,
        - Partial upfront,
        - No upfront at the beginning.
- **Spot Instances:**
    * Up to $90%$ less than On-Demand,
    * AWS can reclaim the instance at any time they need it, with two mins warning!
    * Resumable.
- **Dedicated Hosts:**
    * Dedicated for use in EC2,
    * Exclusive to spacial needs,
    * No share tendency of the host.
