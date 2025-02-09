# Clouds Basic:
It is on-demand delivery of IT resources (storage, compute power, databases) over the internet. Instead of managing the hardware, clouds providers offer services for rent like AWS, Azure, or Google Cloud.

## Five Essential Characteristics of Cloud Computing:
* On-Demand: Users can provision and manage computing resources (such as storage and processing power) as needed, without requiring human intervention from the provider.
* self-Service: By going through the provider's web server, user can see and manage their usage.
* Broad Network Access: The users are able to access the cloud services via portable devices uses a local network.
* Resource Pooling: he cloud provider uses a multi-tenant model to serve multiple customers by dynamically allocating and reallocating resources based on demand, while ensuring security and privacy.
* Rapid elasticity: Cloud resources can be automatically scaled up or down to accommodate workload fluctuations, ensuring optimal performance and cost efficiency.
* Measured service: Cloud usage is metered, meaning users are charged based on what they consume (e.g., storage, bandwidth, or computing power), promoting cost-effectiveness and transparency [see](https://www.synopsys.com/blogs/chip-design/essential-cloud-computing-characteristics.html).

## Cloud Service Models:
There are three main types of the cloud computing
* `IaaS` Infrastructure as a Service: Virtual servers, networking, and storage (e.g., AWS EC2, Google computing Engine)
* `PaaS` Platform as a Service: Provides a platform for developers to build applications (e.g., AWS Elastic Beanstalk, Google App Engine)
* `SaaS` Software as a Service: Fully managed application available via the internet (e.g., Gmail, Dropbox. AWS Workspaces)

## Cloud Deployment Models:
* Public Cloud: services are owned and operated by a third-party (AWS, Google Cloud, Azure)
* Private Cloud: Infrastructure dedicated to one organization, usually on-premises (For Banking, Governments, Healthcare)
* Hybrid Cloud: Combination of public and private clouds

## The future:
* Processing data closer to where it's generated
* Serverless Computing for running code without managing servers (AWS Lambda, Azure Functions)
* AI and ML - Cloud platforms providing AI models and processing power (Google Vertex AI, AWS SageMaker)
* Quantum Cloud Computing - Future tech that uses quantum physics for computing (IBM Quantum, AWS Braket)

## AWS key Concepts:
AWS (Amazon Web Service) provides overs 200 cloud services.

### Some of the main ones:
* `S3`: Simple Storage Service, for files, images, logs.
* `EC2`: Elastic Compute Cloud, provides virtual machines for computing power.
* `IAM`: Identity and Access Management, which controls the access to AWS resources.
* `Lambda`: Serverless computing to run code without provisioning servers.
* `DynamoDB`: NoSQL database.
* `RDS`: Relational Database Service for managing SQL database.

#### What is `S3`:
* `S3` is an object storage service that allows storing and retrieving files.
* Files (object) are stored in `buckets`, which are like folders in AWS.

### `IAM` and Security in AWS:
**Key Concepts:**
* Users: Individual accounts.
* Groups: Collection of users with shared permissions.
* Roles: Temporary access for AWS services.
* Policies: Define what actions a user or service can perform.

**Important Security Best Practices:**
* Never expose AWS credentials in public repositories.
* Use `IAM` roles instead of access keys.
* Enable `MFA` (Multi-Factor Authentication)
* Use least privilege principle (granted only necessary permissions)