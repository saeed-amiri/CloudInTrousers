# Module 9: Migration and Innovation
The following topics are covered in this module:
* Understand migration and innovation in the AWS Cloud.
* Summarize the AWS Cloud Adoption Framework (AWS CAF).
* Summarize the six key factors of a cloud migration strategy.
* Describe the benefits of AWS data migration solutions, such as AWS Snowcone, AWS Snowball, and AWS Snowmobile.
* Summarize the broad scope of innovative solutions that AWS offers.

## AWS Cloud Adoption Framework (AWS CAF)
The AWS Cloud Adoption Framework (AWS CAF) is a framework that helps organizations develop and implement a comprehensive cloud adoption strategy. It provides guidance on how to align cloud adoption with business goals, identify gaps in skills and processes, and establish best practices for cloud migration and management.
### Key Components of AWS CAF
* **Business Perspective**: Align cloud adoption with business goals and objectives:
    - The Business Perspective ensures that IT aligns with business needs and that IT investments link to key business results.  
    - Use the Business Perspective to create a strong business case for cloud adoption and prioritize cloud adoption initiatives. Ensure that your business strategies and goals align with your IT strategies and goals.
    - Common roles in the Business Perspective include: 
        * Business managers
        * Finance managers
        * Budget owners
        * Strategy stakeholders
* **People Perspective**: Develop the skills and capabilities needed for cloud adoption.
    - The People Perspective focuses on the people and organizational aspects of cloud adoption. It helps organizations identify the skills and capabilities needed for successful cloud adoption and develop training and development plans to build those skills.
    - Common roles in the People Perspective include:
        * Human resources
        * Staffing
        * People managers
* **Governance Perspective**: Establish governance and compliance frameworks for cloud adoption.
    - The Governance Perspective focuses on the governance and compliance aspects of cloud adoption. It helps organizations establish governance frameworks, policies, and processes to ensure compliance with regulations and standards.
    - Common roles in the Governance Perspective include:
        * hief Information Officer (CIO)
        * Program managers
        * Enterprise architects
        * Business analysts
        * Portfolio managers
* **Platform Perspective**: Design and implement a cloud architecture that meets business needs.
    - The Platform Perspective focuses on the technical aspects of cloud adoption. It helps organizations design and implement cloud architectures that meet business needs and align with best practices.
    - Common roles in the Platform Perspective include:
        * Chief Technology Officer (CTO)
        * IT managers
        * Solutions architects
* **Security Perspective**: Establish security and compliance frameworks for cloud adoption.
    - The Security Perspective focuses on the security and compliance aspects of cloud adoption. It helps organizations establish security frameworks, policies, and processes to ensure the security of cloud environments.
    - Common roles in the Security Perspective include:
        * Chief Information Security Officer (CISO)
        * Security architects
        * Security analysts
        * Risk management
* **Operations Perspective**: Establish operational processes and practices for cloud adoption.
    - The Operations Perspective focuses on the operational aspects of cloud adoption. It helps organizations establish operational processes and practices to ensure the smooth operation of cloud environments.
    - Common roles in the Operations Perspective include:
        * IT operations
        * Service desk
        * Incident management
        * Change management

## AWS Migration Strategy
The AWS Migration Strategy is a framework that helps organizations plan and execute their cloud migration initiatives. It provides guidance on how to assess the current environment, identify migration opportunities, and develop a migration strategy that aligns with business goals.
### Key Components of AWS Migration Strategy
* **Rehost**: Move applications to the cloud without changes (lift-and-shift).
    - Rehosting is the process of moving applications to the cloud without making any changes to the application architecture or code. This approach is often referred to as "lift-and-shift" and is typically used for legacy applications that cannot be easily modified.
* **Replatform**: Move applications to the cloud with minimal changes.
    - Replatforming is the process of moving applications to the cloud with minimal changes to the application architecture or code. This approach is often used for applications that can benefit from cloud-native services but do not require a complete rewrite.
* **Refactor**: Re-architect applications to take advantage of cloud-native features.
    - Refactoring is the process of re-architecting applications to take advantage of cloud-native features and services. This approach is often used for applications that require significant changes to the architecture or code to fully leverage the benefits of the cloud.
* **Repurchase**: Replace applications with cloud-native alternatives.
    - Repurchasing is the process of replacing existing applications with cloud-native alternatives. This approach is often used for applications that are no longer supported or that do not meet business needs.
* **Retire**: Decommission applications that are no longer needed.
    - Retiring is the process of decommissioning applications that are no longer needed. This approach is often used for legacy applications that are no longer supported or that do not meet business needs.
* **Retain**: Keep applications on-premises or in a hybrid environment.
    - Retaining is the process of keeping applications on-premises or in a hybrid environment. This approach is often used for applications that cannot be easily migrated to the cloud or that do not meet business needs.

## AWS Snow Family
The AWS Snow Family is a suite of physical devices and services that help organizations transfer large amounts of data to and from the AWS Cloud. The Snow Family includes AWS Snowcone, AWS Snowball, and AWS Snowmobile.
### AWS Snowcone
AWS Snowcone is a small, rugged, and portable device that can be used to transfer data to and from the AWS Cloud. It is designed for edge computing and can be used in remote locations with limited connectivity. It features 2 CPUs, 4 GB of memory, and up to 14 TB of usable storag
### AWS Snowball
AWS Snowball is a larger, rugged device that can be used to transfer large amounts of data to and from the AWS Cloud. It is designed for data transfer and can be used in environments with limited connectivity. offers two types of devices:
* **Snowball Edge Storage Optimized**: Designed for data transfer and edge computing use cases. It features 42 TB of usable storage and can be used to run AWS Lambda functions: 
    - Storage: 80 TB of hard disk drive (HDD) capacity for block volumes and Amazon S3 compatible object storage, and 1 TB of SATA solid state drive (SSD) for block volumes. 
    - Compute: 40 vCPUs, and 80 GiB of memory to support Amazon EC2 sbe1 instances (equivalent to C5).
* **Snowball Edge Compute Optimized**: Designed for edge computing use cases. It features 52 TB of usable storage and can be used to run AWS Lambda functions and Amazon EC2 instances:
    - Storage: 80-TB usable HDD capacity for Amazon S3 compatible object storage or Amazon EBS compatible block volumes and 28 TB of usable NVMe SSD capacity for Amazon EBS compatible block volumes. 
    - Compute: 104 vCPUs, 416 GiB of memory, and an optional NVIDIA Tesla V100 GPU. Devices run Amazon EC2 sbe-c and sbe-g instances, which are equivalent to C5, M5a, G3, and P3 instances.
### AWS Snowmobile
AWS Snowmobile is a massive, rugged device that can be used to transfer exabytes of data (up to 100 petabytes of data per Snowmobile) to and from the AWS Cloud. It is designed for large-scale data transfer and can be used in environments with limited connectivity. 
### Key Features of AWS Snow Family
* **Data Transfer**: Transfer large amounts of data to and from the AWS Cloud.
* **Rugged Design**: Designed for use in remote locations with limited connectivity.
* **Edge Computing**: Supports edge computing use cases.
* **Security**: Provides secure data transfer and storage.
* **Integration**: Integrates with other AWS services for data transfer and storage.

## AWS Innovative Solutions
AWS offers a broad scope of innovative solutions that help organizations leverage the power of the cloud to drive business transformation and innovation. These solutions include:
* **Machine Learning**: AWS provides a range of machine learning services and tools that help organizations build, train, and deploy machine learning models. These services include Amazon SageMaker, Amazon Rekognition, and Amazon Comprehend.
* **Artificial Intelligence**: AWS provides a range of artificial intelligence services and tools that help organizations build intelligent applications. These services include Amazon Lex, Amazon Polly, and Amazon Transcribe.
* **Internet of Things (IoT)**: AWS provides a range of IoT services and tools that help organizations build and manage IoT applications. These services include AWS IoT Core, AWS IoT Greengrass, and AWS IoT Analytics.
* **Serverless Computing**: AWS provides a range of serverless computing services that help organizations build and run applications without managing servers. These services include AWS Lambda, Amazon API Gateway, and AWS Step Functions.
### Amazon Q Developer
Amazon Q Developer is a machine learning-powered code generator that provides you with code recommendations in real time.
### Amazon SageMaker
Amazon SageMaker is a fully managed service that provides developers and data scientists with the ability to build, train, and deploy machine learning models quickly. It offers a range of tools and services for every step of the machine learning process, including data preparation, model training, and deployment.
### Amazon Rekognition
Amazon Rekognition is a fully managed image and video analysis service that uses machine learning to identify objects, people, text, scenes, and activities in images and videos. It can also detect inappropriate content and recognize celebrities.
### Amazon TextTract
Amazon Textract is a fully managed machine learning service that automatically extracts text, handwriting, and data from scanned documents. It can analyze documents in various formats, including PDFs and images, and extract structured data for further processing.
