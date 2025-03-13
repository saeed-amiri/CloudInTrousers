# Module 3: Global Infrastructure and Reliability
This module is all about:
- The benefits of the AWS Global Infrastructure,
- Describing the basic concept of Availability Zones,
- Describing the benefits of Amazon CloudFront and edge locations,
- Comparing different methods for provisioning AWS services.

## AWS Global Infrastructure
### Factors to Choose a Region:
1. Compliance,
2. Proximity,
3. Feature availability,
4. Pricing.

### Availability Zone  
An *Availability Zone* is **a single data center or a group of data centers within a Region**. These zones are located tens of miles apart, a distance that maintains low latency between them while reducing the risk that a disaster will affect multiple zones.

## Edge Locations  
Edge locations are AWS data centers designed to deliver services with the lowest latency possible. Amazon operates dozens of these centers around the globe—often in major cities—ensuring fast and snappy responses. Key services that leverage edge locations include:  
- **CloudFront:** Caches copies of the content it serves, positioning them closer to users for faster delivery.  
- **Route 53:** Provides DNS responses from nearby edge locations to resolve queries more quickly.  
- **Web Application Firewall and AWS Shield:** Filter traffic at edge locations to stop unwanted traffic as soon as possible [[LastWeekInAws](https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/)].

### Cache  
The term *cache* primarily refers to something that is hidden or stored away. More recently, it has come to mean “short-term computer memory where information is stored for easy retrieval” [Merriam-Webster]. In computing, a cache is a hardware or software component that stores data so that future requests can be served faster—whether that data is the result of an earlier computation or a copy of information stored elsewhere [wiki].

### Content Delivery Network (CDN)  
A content delivery network is a system of interconnected servers that accelerates webpage loading for data-heavy applications. It can also be referred to as a content distribution network [AWS].

### CloudFront  
- Amazon CloudFront is a CDN service operated by Amazon Web Services. It creates a globally distributed network of proxy servers to cache content—such as web videos or other large media files—closer to consumers, thereby improving download speeds [wiki].
- CloudFront accelerates the delivery of both static and dynamic web content (e.g., .html, .css, .js, and image files) by utilizing a worldwide network of data centers known as edge locations. When a user requests content:
  - If the content is already present at the edge location with the lowest latency, it is delivered immediately,
  - If not, CloudFront retrieves the content from an origin specified by you, such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server that stores the definitive version of the content [[AWS_Docs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)].

## How to Provision AWS Resources?
**Ways to interact with AWS services:**
- **AWS Management Console:**
    * The AWS Management Console is a web-based interface for accessing and managing AWS services. You can quickly access recently used services and search for other services by name, keyword, or acronym. The console includes wizards and automated workflows that can simplify the process of completing tasks.
- **AWS Command Line Interface (CLI):**
    * AWS CLI enables you to control multiple AWS services directly from the command line within one tool. 
- **AWS Software Development Kits (SDK):**
    * DKs enable us to use AWS services with our existing applications or create entirely new applications that will run on AWS.

### AWS Management Tools:
- **AWS Elastic Beanstalk:**
- *AWS Elastic Beanstalk is an orchestration service offered by Amazon Web Services for deploying applications which orchestrates various AWS services, including EC2, S3, Simple Notification Service (SNS), CloudWatch, autoscaling, and Elastic Load Balancers. Elastic Beanstalk provides an additional layer of abstraction over the bare server and OS;[wiki]*
- With AWS Elastic Beanstalk, you provide code and configuration settings, and Elastic Beanstalk deploys the resources necessary to perform the following tasks:
    * Adjust capacity
    * Load balancing
    * Automatic scaling
    * Application health monitoring

### AWS CloudFormation:

**Benefits:**

- **Scalable Infrastructure:**  
  Scale your infrastructure globally and manage resources across all AWS accounts and regions with one operation.

- **Extended and Managed Infrastructure:**  
  Enhance and manage your infrastructure to incorporate cloud resources available in the AWS CloudFormation Registry, from both the developer community and the library.

- **Automated Resource Management:**  
  Simplify resource management organization-wide through AWS service integrations that provide turnkey application distribution and governance controls.

**Use Cases:**

- **DevOps-Driven Infrastructure Management:**  
  Automate, test, and deploy infrastructure templates using continuous integration and delivery (CI/CD) workflows.

- **Scaling Production Stacks:**  
  Efficiently run environments ranging from a single Amazon Elastic Compute Cloud (EC2) instance to complex, multi-region applications.

- **Sharing Best Practices:**  
  Easily define components such as an Amazon Virtual Private Cloud (VPC) subnet or provisioning services like AWS OpsWorks or Amazon Elastic Container Service (ECS).

---

### AWS Outposts Family

AWS Outposts is a suite of fully managed solutions that bring AWS infrastructure and services to virtually any on-premises or edge location, ensuring a consistent hybrid experience. Outposts enables you to extend and run native AWS services on premises and is offered in various form factors—from compact 1U and 2U servers to full 42U racks and multiple rack deployments.

With AWS Outposts, you can run select AWS services locally while still connecting to a wide array of services available in the local AWS Region. This allows you to run applications and workloads on premises using familiar AWS services, tools, and APIs. Outposts is ideal for workloads and devices that require:
- Low latency access to on-premises systems,
- Local data processing,
- Data residency, and
- Application migration that must maintain local system interdependencies.

**Benefits:**

- **Local AWS Services:**  
  Extend AWS compute, networking, security, and other services to on-premises locations to meet low latency, local data processing, and data residency requirements.

- **Fully Managed Infrastructure:**  
  Minimize time, resources, operational risk, and maintenance downtime with a fully managed IT infrastructure.

- **Consistent Hybrid Experience:**  
  Benefit from the same hardware, APIs, tools, and management controls as in the cloud, ensuring a seamless experience for developers and IT operations.

**Use Cases:**

- **Low Latency Compute:**  
  Deliver high-quality, interactive experiences (e.g., real-time multiplayer gaming) when public cloud servers are too distant to meet single-digit millisecond latency requirements. Outposts is also well-suited for use cases such as manufacturing execution systems (MES), high-frequency trading, or medical diagnostics.

- **Data Residency:**  
  Keep data within specific geographical boundaries to meet regulatory, contractual, or information security mandates, which is crucial for sectors like financial services, healthcare, and oil and gas.

- **Migration and Modernization:**  
  Migrate legacy on-premises applications with latency-sensitive dependencies in incremental stages, preserving low-latency connections between application components until a full migration is feasible.

- **Local Data Processing:**  
  Process data on-site for applications like data lakes and machine learning model training, or maintain a consistent hybrid architecture to handle large or bandwidth-constrained datasets, moving data to the cloud for long-term storage as needed.