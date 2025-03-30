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
| **S3 Standard**                                    | Frequently accessed data (e.g., websites, analytics, content distribution)                            | Stored across **3+ Availability Zones (AZs)**, 11 nines durability            | High availability, low latency, higher cost                                            |
| **S3 Standard-Infrequent Access (S3 Standard-IA)** | Infrequently accessed, but needs rapid access (e.g., backups, DR files)                               | Stored across **3+ AZs**, same durability as Standard    | Lower storage price, higher retrieval cost                                             |
| **S3 One Zone-Infrequent Access (S3 One Zone-IA)** | Infrequent data, can tolerate AZ failure (non-critical, reproducible data)                            | Stored in **1 AZs**, lower durability                     | Lower cost than Standard-IA, suitable when replication isn’t critical                  |
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

## **Amazon Elastic File System (Amazon EFS)**:

  ### Comparing **File Storage (Amazon EFS)** to **Block Storage (Amazon EBS)**:
  - **File Storage** allows **multiple clients** (users, servers, applications) to access shared data through **file paths**.
  - It uses **block storage underneath**, organized with a **local file system**.
  - **Best for scenarios** where **many services/resources need concurrent access** to the same files.
  
- **Type:** File Storage Service.
- **Scaling:** **Automatically grows or shrinks** as files are added/removed, up to **petabytes**.
- **Availability:** **Regional** (spanning **multiple AZs**).
- **Access:** Supports **simultaneous access** from multiple EC2 instances, services, and even **on-premises servers** via **AWS Direct Connect**.
- **Use Cases:**  
  - Web serving & content management systems  
  - Big data & analytics  
  - Lift-and-shift enterprise applications  
  - Home directories shared by multiple users


#### **Quick Takeaway:**
- Use **Amazon EBS** when you need **low-latency, single-instance block storage**.
- Use **Amazon EFS** when you need a **shared, scalable file system** accessible **across AZs and on-premises**, with **concurrent access** by multiple clients.

---

## Relational databases
- **Definition:**  
  Data is stored in **tables with rows and columns**, where different pieces of data are **related to each other**.
  
- **Query Language:**  
  Uses **SQL (Structured Query Language)** to store, retrieve, and manage data efficiently.

- **Advantages:**
  - Easy to understand, consistent structure
  - Highly scalable
  - Supports complex queries and relationships


### **Amazon Relational Database Service (Amazon RDS)**

| **Feature**                              | **Details**                                                                                                |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Type**                                | **Managed relational database service**                                                                     |
| **Automation**                          | Automates:  <br>- Hardware provisioning  <br>- Database setup  <br>- Patching  <br>- Backups                |
| **Security Options**                    | - **Encryption at rest**  <br>- **Encryption in transit**  <br>- Fine-grained access controls               |
| **Integration**                         | Can integrate with other AWS services (e.g., **AWS Lambda** for serverless queries)                         |
| **Database Engines Supported**          | 1. **Amazon Aurora**  <br>2. **PostgreSQL**  <br>3. **MySQL**  <br>4. **MariaDB**  <br>5. **Oracle Database**  <br>6. **Microsoft SQL Server**  |


### **Amazon Aurora Highlights**

| **Feature**                              | **Details**                                                                                     |
|-----------------------------------------|--------------------------------------------------------------------------------------------------|
| **Type**                                | Enterprise-class relational database engine                                                      |
| **Compatibility**                       | **MySQL** and **PostgreSQL** compatible                                                          |
| **Performance**                         | - Up to **5x faster than standard MySQL**   <br>- Up to **3x faster than standard PostgreSQL**   |
| **Cost Efficiency**                     | Reduces unnecessary **I/O operations** to lower costs                                            |
| **High Availability**                   | - **6 copies of data replicated across 3 AZs**  <br>- Continuous backup to **Amazon S3** |
| **Use Case**                            | Ideal for applications requiring **high performance & high availability**                        |

- **Amazon RDS** handles the **heavy lifting** of relational database management—perfect if you want scalability without worrying about infrastructure.
- Choose **Amazon Aurora** for **high availability, better performance, and MySQL/PostgreSQL compatibility**.

---

## Amazon DynamoDB
| **Feature**                       | **Details**                                                                                     |
|-----------------------------------|-------------------------------------------------------------------------------------------------|
| **Database Type**                 | **Non-relational**, **NoSQL**                                                                   |
| **Purpose-Built**                 | Designed for specific use cases; **not ideal for all workloads**                                |
| **Performance**                   | **Millisecond response times**                                                                  |
| **Scalability**                   | **Highly scalable**, handles massive workloads automatically                                    |
| **Management**                    | **Fully managed service** — no need to manage hardware, software, or scaling manually           |
| **Example Use Case**              | On **Prime Day 2019**, handled:  <br>- **7.11 trillion API calls** over 48 hours  <br>- Peaked at **45.4 million requests/sec** |


### **Key Strengths:**
- Perfect for applications needing:
  - **Ultra-low latency**
  - **Massive scalability**
  - **Seamless management**

### **Best Use Cases:**
- Real-time applications
- Gaming leaderboards
- IoT data storage
- Shopping carts & recommendation engines
- High-traffic events (e.g., Prime Day)

---

## Amazon Redshift
| **Feature**                         | **Details**                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **Type**                            | **Cloud-based Data Warehouse** (for large-scale data analytics)                                                                 |
| **Performance**                     | - **3x better price-performance**  <br>- **7x higher throughput** than other cloud data warehouses                              |
| **Scalability**                     | Handles **petabytes of data**, supports **Redshift Serverless** for effortless, automatic scaling (no infrastructure burden)    |
| **Analytics Speed**                 | Supports **near real-time analytics** via **zero-ETL integrations** (connects to streaming data, databases, third-party apps)   |
| **SQL Integration**                 | Simplified SQL querying with **Amazon Q in Redshift**, allowing **natural language** query generation                           |
| **AI & ML Integration**             | Seamlessly integrates with **Amazon SageMaker** for AI/ML workflows through **Redshift Lakehouse integration**                  |
| **Knowledge Base for Generative AI**| Acts as a **structured knowledge base** to power more accurate outputs in **Amazon Bedrock's generative AI assistants**         |
| **Data Sources Supported**          | - Redshift data warehouse  <br>- Amazon S3 data lakes  <br>- Operational databases  <br>- Federated data sources                |

### **Key Advantages:**
- **High performance analytics** at lower costs
- **Serverless scaling** for big data workloads
- **Zero-ETL**: Eliminates need for complex pipelines
- **Integrated with AI/ML (Amazon SageMaker & Bedrock)**
- Supports **natural language SQL queries** with Amazon Q

### **Best Use Cases:**
- Business intelligence & dashboards
- Big data analytics
- Real-time decision-making
- AI/ML model training & predictions on large datasets
- Supporting generative AI applications with structured knowledge bases

---

## AWS Database Migration Service (AWS DMS)

| **Feature**            | **Details**                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Purpose**            | **Migrate relational, non-relational databases, and other data stores**                                                    |
| **Source & Target**    | - Supports **same-type or cross-type** migrations (e.g., MySQL → MySQL, or MySQL → Aurora)                                 |
| **Downtime**           | **Minimal downtime**: Source database stays **operational during migration**                                               |
| **Management**         | Fully managed service, handles replication, monitoring, and error handling automatically                                   |


| **Use Case**                                 | **Description**                                                                                                      |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Database Migration**                       | Move databases from **on-premises or cloud** to another database (e.g., MySQL → Aurora, Oracle → PostgreSQL)         |
| **Development & Test Database Migrations**   | **Copy production data** to dev/test environments **without affecting production users**                             |
| **Database Consolidation**                   | Combine several smaller databases into **one single database**                                                       |
| **Continuous Replication**                   | Keep **ongoing copies** of data synced to other databases, not just one-time migration (e.g., cross-region replication) |

**AWS DMS is ideal for:**
- **Seamless database migrations** with near-zero downtime
- **Testing and development** without risking production data
- **Consolidating databases** for simplified management
- **Real-time replication** to enhance availability, disaster recovery, or analytics

---

## Choosing the Right Database

###  **Additional AWS Database & Accelerator Services**

| **Service**                          | **Type**                     | **Primary Use Cases**                                                                                                                                 |
|--------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Amazon DocumentDB**                | **Document Database**        | Content management systems, catalogs, user profiles. <br>Supports **MongoDB workloads**. Ideal for semi-structured data (JSON-like).                  |
| **Amazon Neptune**                   | **Graph Database**           | Highly connected datasets (social networks, recommendation engines, fraud detection, knowledge graphs).                                               |
| **Amazon QLDB (Quantum Ledger DB)**  | **Ledger Database**          | Immutable, cryptographically verifiable transaction logs.  <br>Use cases: Financial records, supply chain tracking, audit trails.                     |
| **Amazon Managed Blockchain**        | **Blockchain Service**       | Create and manage decentralized blockchain networks.  <br>Use cases: Decentralized apps (DApps), multi-party transactions without a central authority.|
| **Amazon ElastiCache**               | **Caching Layer**            | In-memory caching to reduce database read latency.  <br>Supports **Redis** & **Memcached**. Ideal for apps needing fast, repeated read access (e.g., gaming, leaderboards).    |
| **DynamoDB Accelerator (DAX)**       | **In-memory Cache for DynamoDB** | Native caching layer for **DynamoDB** to improve read times from milliseconds to microseconds.  <br>Perfect for high-throughput, low-latency NoSQL workloads. |


| **Requirement**                                             | **AWS Service**                         |
|-------------------------------------------------------------|-----------------------------------------|
| Flexible, document-oriented storage (JSON, catalogs)        | **Amazon DocumentDB**                   |
| Complex, relationship-heavy datasets (social networks)      | **Amazon Neptune**                      |
| Immutable, auditable transaction logs                       | **Amazon QLDB**                         |
| Decentralized, distributed ledger with no central authority | **Amazon Managed Blockchain**           |
| Faster database read performance (general)                  | **Amazon ElastiCache** (Redis/Memcached)|
| Faster DynamoDB reads                                       | **DynamoDB Accelerator (DAX)**          |

### **Core Principle:**
AWS offers **specialized databases and accelerators** tailored to specific workloads—**choose the best tool for the job, not a one-size-fits-all solution**.

