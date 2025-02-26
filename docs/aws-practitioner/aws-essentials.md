# Notes from AWS Cloud Practitioner Essentials
[Text are from AWS, otherwise mentioned]

## Client-Server Model:
The client–server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients [wiki].

## How the Browser Interacts With the Servers? [[see](https://www.geeksforgeeks.org/client-server-model/)]


When a user tries to access a website or file, several steps occur in the background to fetch and display the content:

   1. The user enters a URL (Uniform Resource Locator) into their web browser. This prompts the browser to send a request to the DNS (Domain Name System) server to locate the corresponding web server.
   2. The DNS server searches for the IP address linked to the requested domain.
   3. Once found, the DNS server returns the web server's IP address to the browser.
   4. The browser then sends an HTTP/HTTPS request to the identified web server's IP address.
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
    * Can lead to $72\\%$ saving.
- **Reserved Instances:**
    * For one or three-year commitment,
    * For steady-state workload,
    * Up to $75\\%$ less versus On-Demand,
    *  Three options:
        - All upfront,
        - Partial upfront,
        - No upfront at the beginning.
- **Spot Instances:**
    * Up to $90\\%$ less than On-Demand,
    * AWS can reclaim the instance at any time they need it, with two mins warning!
    * Resumable.
- **Dedicated Hosts:**
    * Dedicated for use in EC2,
    * Exclusive to spacial needs,
    * No share tendency of the host.

## Scalability:
It involves beginning with only the resources that needed at the time being. Also, AWS service provides an automization option for auto scaling: **Amazon EC2 Auto Scaling**.

### Amazon EC2 Auto Scaling
EC2 offers two approaches:
* Dynamic scaling responds to changing demand,
* Predictive scaling automatically schedules the right number of Amazon EC2 instances based on the predicted demand.

Also, one can use both of these options simultaneously.

* **Minimum Capacity** is the Amazon EC2 instances that lunch immediately after the Auto Scaling group is created.
* **Desired Capacity** is the number of instances desired to have for the application.
* **Maximum Capacity** is the maximum number of the instances can run for the application.

---

## Elastic Load Balancing (ELB)
**Load Balancing**

Load balancing involves allocating a group of tasks among multiple computing resources to enhance overall processing efficiency [wiki].

**Advantages of Load Balancing:**

- **Enhanced Application Availability:**
  - Enables maintenance or upgrades on application servers without causing downtime.
  - Offers automatic disaster recovery by rerouting traffic to backup sites.
  - Regularly checks system health to preemptively address issues that might lead to downtime.

- **Improved Application Scalability:**
  - Eliminates traffic bottlenecks by preventing overload on any single server.
  - Anticipates traffic patterns, allowing for the flexible addition or removal of servers as needed.
  - Incorporates redundancy into the system, ensuring reliable scalability.

- **Strengthened Application Security:**
  - Mitigates attacks by managing millions of simultaneous requests.
  - Monitors incoming traffic to identify and block malicious content.
  - Automatically diverts attack traffic across multiple backend servers to minimize its impact.
  - Channels traffic through a series of network firewalls for added protection.

- **Boosted Application Performance:**
  - Enhances response times, leading to better overall performance.
  - Balances loads evenly across servers to optimize efficiency.
  - Directs client requests to servers located closer to them, thereby reducing latency.
  - Guarantee that both physical and virtual computing resources operate reliably and perform at their best.

ELB is an AWS service designed to automatically distribute incoming application traffic across multiple resources, such as Amazon EC2 instances. It functions as a single point of contact for all incoming web traffic directed to your Auto Scaling group.

**Key Use Cases:**

- **Modernize Applications with Serverless and Containers:**
  Easily scale contemporary applications to meet demand without the need for complex configurations or additional API gateways.

- **Enhance Hybrid Cloud Network Scalability:**
  Efficiently balance loads across both AWS and on-premises resources using a unified load balancer.

- **Preserve Existing Network Appliances:**
  Deploy your preferred vendor's network appliances while leveraging the scalability and flexibility provided by the cloud.

---

## Messaging and Queuing

### **Tightly Coupled Architecture [[CloudNative](https://glossary.cncf.io/tightly-coupled-architecture/)]**
Tightly coupled architecture refers to a system where multiple application components are **highly interdependent**. Unlike loosely coupled architectures, any change in one component is likely to impact others. While this approach is often **easier to implement**, it can introduce risks such as **cascading failures** and reduced flexibility. Additionally, it requires **coordinated updates** across components, which can slow down development workflows.

This architectural style is a **traditional approach** to building applications. While it does not always align with modern **microservices best practices**, it can still be beneficial in certain scenarios. Tightly coupled architectures are typically **simpler and faster to develop**, much like **monolithic applications**, making them advantageous for accelerating the **initial development process**.

#### **Advantages [[Gik4Gik](https://www.geeksforgeeks.org/difference-between-loosely-coupled-and-tightly-coupled-multiprocessor-system/)]:**
- **Faster Communication:** Processors share memory and use high-speed buses, enabling **efficient inter-processor communication**.
- **Efficient Resource Sharing:** Shared memory and I/O devices allow **seamless data exchange** between processors.
- **Optimized for Synchronized Tasks:** Ideal for **high-interaction workloads**, such as call centers or dispatch systems.

#### **Disadvantages [[Gik4Gik](https://www.geeksforgeeks.org/difference-between-loosely-coupled-and-tightly-coupled-multiprocessor-system/)]:**
- **High Cost:** Requires **specialized hardware and high-speed connections**, making implementation expensive.
- **Limited Scalability:** Adding processors is **challenging** due to shared resource dependencies.
- **Failure Impact:** A **single failure** in a processor or shared component can **disrupt the entire system**, reducing reliability

### **Loosely Coupled Architecture [[CloudNative](https://glossary.cncf.io/tightly-coupled-architecture/)]**
Loosely coupled architecture is a design approach where individual components of an application **function independently** of one another. Unlike tightly coupled systems, each component—often referred to as a **microservice**—is built to perform a **specific function** and can be utilized by multiple services without direct dependencies. While this architecture can take **longer to implement**, it offers significant advantages, especially as applications grow in complexity and scale.

One of the key benefits of loosely coupled systems is that **teams can develop, deploy, and scale components independently**. This autonomy allows organizations to iterate quickly on specific features without disrupting the entire system. Additionally, development teams can be structured around their **expertise**, focusing on their individual service, leading to **faster innovation and more efficient workflows**.

### **Microservices Architecture [[CloudNative](https://glossary.cncf.io/tightly-coupled-architecture/)]**
Microservices architecture is a design approach that **breaks applications into independent services**, each handling a specific function. These services work together seamlessly, appearing as a single entity to the user. For example, **Netflix** utilizes microservices for authentication, search, and video previews, allowing independent updates and scaling.

#### **Problem it Solves**
Traditional **monolithic applications** require scaling the entire system even if demand increases for just one feature. This leads to **inefficient resource use**. In contrast, microservices enable **targeted scaling**, allowing individual components to handle increased demand without affecting the whole application.

#### **Benefits**
Microservices enable **faster deployments, independent scaling, and parallel development** by different teams. This approach enhances **modularity, maintainability, and agility**. However, it introduces **operational complexity**, as managing multiple services requires more infrastructure and monitoring.

### **Monolithic Applications [[CloudNative](https://glossary.cncf.io/tightly-coupled-architecture/)]**
A **monolithic application** integrates all functionality into a **single deployable program**. It is often the **simplest and fastest way** to build an application, but as complexity grows, maintenance becomes challenging. More developers working on the same codebase **increase the risk of conflicts and communication overhead**.

#### **Problem it Addresses**
Microservices introduce **operational complexity** with more components to test, deploy, and manage. Early in development, a monolithic approach helps **avoid unnecessary overhead** until the product proves its value.

#### **How it Helps**
A well-structured monolith follows **lean development principles**, enabling a **quick launch with minimal complexity**. Once successful, it can be **gradually refactored into microservices**. Premature microservices adoption can **waste engineering effort** if the application doesn’t succeed.

### **Amazon Simple Queue Service (SQS):**

**SQS** allows you to send, store, and receive messages between software components at any volume. This is without losing messages or requiring other services to be available.

#### **Benefits of Amazon SQS:**

- Overhead made simple:
    * Eliminate overhead with no upfront costs and without needing to manage software or maintain infrastructure,
- Reliability at scale:
    * Reliably deliver large volumes of data, at any level of throughput, without losing messages or needing other services to be available.
- Security:
    * Securely send sensitive data between applications and centrally manage your keys using AWS Key Management.
- Cost-effective scalability:
    * Scale elastically and cost-effectively based on usage so you don’t have to worry about capacity planning and preprovisioning.

#### **Amazon Simple Notification Service (SNS):**

Fully managed Pub/Sub service for A2A and A2P messaging.
    - **Publish-subscribe messaging**, or **pub/sub messaging**, is an asynchronous communication model that makes it easy for developers to build highly functional and architecturally complex applications in the cloud. In modern cloud architecture, applications are decoupled into smaller, independent building blocks called services. Pub/sub messaging provides instant event notifications for these distributed systems. It supports scalable and reliable communication between independent software modules.
    - **Application-to-Application (A2A)** Integration (or Enterprise Application Integration) connects applications and business processes within the same organization to streamline operations.
    - **Application-to-Person (A2P)** Messaging is the automated process of sending mobile messages from a business application to a user, typically for marketing or service notifications.


Amazon SNS simplifies **A2A** messaging by separating publishers from subscribers, which supports microservices, distributed systems, and serverless applications. Messages are sent to Amazon SNS topics, where they can be filtered and delivered to subscribers like Lambda, Amazon SQS, or HTTP endpoints. If delivery fails, the messages are stored in a dead-letter queue for further analysis or reprocessing.

Amazon SNS **A2P** messaging lets you to deliver notifications and alerts directly to your customers' mobile devices through SMS (Short Message Service). Using this feature, you can send push notifications to mobile apps, text messages to mobile phone numbers, and plain-text emails to email addresses. Additionally, you have the flexibility to distribute messages by using topics to reach multiple recipients, or publish messages directly to individual mobile endpoints for personalized communication.

**Usage:**
- Integrate your applications with FIFO messaging:
    * Deliver messages in a strictly ordered, first in, first out (FIFO) manner to maintain accuracy and consistency across independent applications.
- Learn more about message ordering and deduplication:
    * Securely encrypt notification message delivery.
- Encrypt messages with AWS Key Management Service (KMS), ensure traffic privacy with AWS PrivateLink, and control access with resource policies and tags.:
    * Learn more about security and message encryption.
- Capture and fan out events from over 60 AWS services:
    * Fan out events across AWS categories, such as analytics, compute, containers, databases, IoT, machine learning (ML), security, and storage.

## **Additional Compute Services:**
With EC2, user is responsible for:
- Patching the instances when new software packages come out,
- Setting up the scaling of those instances as well as ensuring that user has architected the solutions to be hosted in a highly available manner.

The AWS solution is **Serverless Computing**

### **Serverless:**
Serverless means the user cannot see or access the underlying infrastructure or instances that are hosting the application, instead, AWS does:
- Provisioning,
- Scaling,
- High availability,
- Maintenance.

AWS has several serverless compute options, such as **Lambda**.

#### **Lambda:**
AWS Lambda is a compute service that runs your code in response to events and automatically manages the compute resources, making it the fastest way to turn an idea into a modern, production, serverless applications.

##### **Benefits of Lambda:**
- No need for managing servers:
    * Run code without provisioning or managing infrastructure. Simply write and upload code as a .zip file or container image.
- Automatic scaling:
    * Automatically respond to code execution requests at any scale, from a dozen events per day to hundreds of thousands per second.
- Pay-as-you-go pricing:
    * Save costs by paying only for the compute time you use—by the millisecond—instead of provisioning infrastructure upfront for peak capacity.
- Performance optimization:
    * Optimize code execution time and performance with the right function memory size. Respond to high demand in double-digit milliseconds with Provisioned Concurrency.

##### **Use cases:**
- Quickly process data at scale:
    * Meet resource-intensive and unpredictable demand by using AWS Lambda to instantly scale out to more than 18k vCPUs. Build processing workflows quickly and easily with suite of other serverless offerings and event triggers.
- Run interactive web and mobile backends:
    * Combine AWS Lambda with other AWS services to create secure, stable, and scalable online experiences.
- Enable powerful ML insights:
    * Preprocess data before feeding it to your machine learning (ML) model. With Amazon Elastic File System (EFS) access, AWS Lambda handles infrastructure management and provisioning to simplify scaling.
- Create event-driven applications:
    * Build event-driven functions for easy communication between decoupled services. Reduce costs by running applications during times of peak demand without crashing or over-provisioning resources.
