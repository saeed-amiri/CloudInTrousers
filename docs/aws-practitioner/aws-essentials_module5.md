# Module 5: Storage and Databases

This module:
1. Summarize the basic concept of storage ans databases,
2. Describe the benefits of Amazon Elastic Block Store (Amazon EBS),
3. Describe the benefits of Amazon Simple Storage Service (Amazon S3),
4. Describe the benefits of Amazon Elastic File System (Amazon EFS),
5. Summarize various storage solutions,
6. Describe the benefits of Amazon Rational Database Service (Amazon RDS),
7. Describe the benefits of Amazon DynamoDB,
8. Summarize various database services.

## Instance Stores and Amazon Elastic Block Store (Amazon EBS)
### What is block storage?
Block storage is technology that **controls data storage and storage devices**. It takes any data, like a file or database entry, and divides it into blocks of equal sizes. The block storage system then stores the data block on underlying physical storage in a manner that is optimized for fast access and retrieval. Developers prefer block storage for applications that require efficient, fast, and reliable data access. Think of block storage as a more direct pipeline to the data. By contrast, file storage has an extra layer consisting of a file system (NFS, SMB) to process before accessing the data.

### Instance Store
An instance store provides **temporary block-level storage for your EC2 instance**. This storage is provided by disks that are physically attached to the host computer. Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content. It can also be used to store temporary data that you replicate across a fleet of instances, such as a load-balanced pool of web servers.


**Amazon Elastic Block Store (Amazon EBS):**
1. It is a service that provides **block-level storage** volumes that you can use with Amazon EC2 instances. If you stop or terminate an Amazon EC2 instance, all the data on the attached EBS volume remains available.
2. To create an EBS volume, you define the configuration (such as volume size and type) and provision it. After you create an EBS volume, it can attach to an Amazon EC2 instance.
3. Because EBS volumes are for data that needs to persist, it’s important to back up the data. You can take incremental backups of EBS volumes by creating Amazon EBS snapshots.

### EBS Snapshot:
- An EBS snapshot is an **incremental backup**. This means that the first backup taken of a volume copies all the data. For subsequent backups, only the blocks of data that have changed since the most recent snapshot are saved. 

- Incremental backups are different from full backups, in which all the data in a storage volume copies each time a backup occurs. The full backup includes data that has not changed since the most recent backup.

## Amazon Simple Storage Service (Amazon S3)
- **Amazon S3 (Simple Storage Service)** provides **object-level storage**.
  - Each **object** = **Data + Metadata + Unique Key**.
  - Examples: images, videos, text, backups, websites, archives.
  - **Max object size** = **5 TB**.
  - Supports **versioning** and **permissions**.
  - Data is stored in **buckets**.
  
- **Difference from block storage**:
  - In block storage: Only modified blocks are updated.
  - In object storage: Entire object is updated on modification.

- **Cost Efficiency**:
  - You pay only for what you use.
  - **Storage class choice** depends on:
    1. **Data retrieval frequency**
    2. **Data availability needs**

- **Lifecycle Policies**: Automatically move objects between storage classes.


### **Amazon S3 Storage Classes:**

| **Storage Class**                                  | **Purpose/Use Case**                                                                                  | **Availability & Durability**                                           | **Key Features**                                                                       |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **S3 Standard**                                    | Frequently accessed data (e.g., websites, analytics, content distribution)                            | Stored across **3+ Availability Zones**, 11 nines durability            | High availability, low latency, higher cost                                            |
| **S3 Standard-Infrequent Access (S3 Standard-IA)** | Infrequently accessed, but needs rapid access (e.g., backups, DR files)                               | Stored across **3+ Availability Zones**, same durability as Standard    | Lower storage price, higher retrieval cost                                             |
| **S3 One Zone-Infrequent Access (S3 One Zone-IA)** | Infrequent data, can tolerate AZ failure (non-critical, reproducible data)                            | Stored in **1 Availability Zone**, lower durability                     | Lower cost than Standard-IA, suitable when replication isn’t critical                  |
| **S3 Intelligent-Tiering**                         | Data with unknown or changing access patterns                                                         | Stored in **multiple AZs**, 11 nines durability                         | Auto-moves between frequent and infrequent tiers based on access; small monitoring fee |
| **S3 Glacier Instant Retrieval**                   | Archive data needing **immediate retrieval** (e.g., media archives with quick access needs)           | Stored in **3+ AZs**, same durability as Standard                       | Millisecond retrieval time, lower cost than Standard                                   |
| **S3 Glacier Flexible Retrieval**                  | Low-cost archival data, retrieved in **minutes to hours** (e.g., older photos, customer records)      | Stored in **3+ AZs**, high durability                                   | Retrieval time: **1 min to 12 hours**, optional vault locks for compliance             |
| **S3 Glacier Deep Archive**                        | **Lowest-cost**, long-term retention, rarely accessed (e.g., compliance records, digital preservation)| Stored in **3+ AZs**, high durability                                   | Retrieval time: **12 to 48 hours**, ideal for 1-2 accesses per year                    |
| **S3 Outposts**                                    | On-premises object storage (data residency/local processing needs)                                    | Stored across multiple devices/servers on **AWS Outposts hardware**     | Local storage for hybrid cloud environments, maintains AWS S3 APIs and durability      |

#### **Quick Decision Guide:**

| **Access Frequency**               | **Storage Class**                       |
|------------------------------------|-----------------------------------------|
| Frequent                           | S3 Standard                             |
| Infrequent but rapid               | S3 Standard-IA, S3 Intelligent-Tiering  |
| Infrequent, tolerant of AZ failure | S3 One Zone-IA                          |
| Unknown/Changing                   | S3 Intelligent-Tiering                  |
| Archival, quick retrieval          | S3 Glacier Instant Retrieval            |
| Archival, flexible retrieval       | S3 Glacier Flexible Retrieval           |
| Rarely accessed, cheapest          | S3 Glacier Deep Archive                 |
| On-premises storage                | S3 Outposts                             |

---

## Comparing the Storage Classes: **Amazon S3 (Object Storage)** vs. **Amazon EBS (Block Storage)**

| **Feature**                     | **Amazon S3 (Object Storage)**                           | **Amazon EBS (Block Storage)**                                 |
|---------------------------------|----------------------------------------------------------|----------------------------------------------------------------|
| **Max Object/Volume Size**      | Unlimited storage, **5 TB per object**                   | **16 TiB per volume**                                          |
| **Durability**                  | **99.999999999% (11 nines)**, stored across multiple AZs | Highly durable within a single AZ, survives EC2 termination    |
| **Structure**                   | **Objects** (data + metadata + unique key)               | **Blocks** (fixed-size parts, no metadata per block)           |
| **Modification Behavior**       | **Entire object must be re-uploaded** when modified      | **Only modified blocks updated**, no need to rewrite whole file|
| **Access Method**               | Accessible via web, each object has a unique URL         | Directly attached to EC2 instances (cannot access without EC2) |
| **Scalability**                 | Virtually **unlimited scalability**, globally accessible | Scales up to **16 TiB per volume**, limited to one AZ          |
| **Availability Zones (AZs)**    | Stored in **3+ AZs**                                     | Single AZ (but persists independently of EC2 instance life)    |
| **Server Requirement**          | **Serverless** - no EC2 needed                           | **Requires EC2 instances**                                     |
| **Best Use Cases**              | - Static content (images, documents) <br>- Backups & archives <br>- Websites & distribution <br>- Occasional changes | - Databases  <br>- Operating systems <br>- Applications needing high performance read/write  <br>- Large files with frequent edits |
| **Cost Efficiency**             | Lower storage cost for static, infrequent updates        | Higher cost due to provisioned size, IOPS                      |


- **Amazon S3**: Best when storing static, rarely changing objects (photos, backups, websites) with global scalability and serverless architecture.
- **Amazon EBS**: Best when you need fast, fine-grained read/write access (databases, OS, large editable files) attached to EC2 instances.

---



