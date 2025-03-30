# Module 6: Security
## This module covers:
- Benefits of the shared responsibility model,
- Multi-factor authentication (MFA),
- AWS Identity and Access Management (IAM) levels,
- AWS Organizations,
- Security policies at a basic level,
- Benefits of compliance with AWS,
- Addtitional AWS security services,

## AWS Shared Responsibility Model
In nutshell, the AWS is responsible for the security of the cloud, while the customer is responsible for security in the cloud. This means that AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud, while customers are responsible for securing their data and applications that run on AWS.

This model is known as **the shared responsibility model**. It is important to understand this model because it helps customers understand their responsibilities when using AWS services and how to secure their data and applications in the cloud.

AWS is responsible for and manges the security of:
* Physical security of data centers,
* Hardware and software infrastructure,
* Network infrastructure,
* Virtualization layer,
* Global network security,

Customers are responsible for and manage the security of:
* Whatever they put in the cloud,
* Setting permissions for Amazon S3 objects,
* Patching software on Amazon EC2 instances.

## User Permissions and Access
### AWS Identity and Access Management (IAM)
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS services and resources for your users. IAM enables you to create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

### Multi-Factor Authentication (MFA)
Multi-Factor Authentication (MFA) is an additional layer of security for your AWS account. It requires not only a password and username but also something that only the user has on them, such as a physical device or a mobile app that generates a time-sensitive code.

### IAM Features:
* IAM users and groups,
* IAM roles,
* IAM policies,
* MFA.

### IAM Account Root User
The IAM account root user is the identity that is created when you first create an AWS account. The root user has full access to all AWS services and resources in the account. It is recommended to use the root user only for tasks that require root user access, such as changing your AWS support plan or closing your AWS account.

### IAM Users
IAM users are identities that you create in your AWS account to represent the people or applications that need to access your AWS resources. Each IAM user has its own set of security credentials, such as an access key ID and secret access key, which are used to sign programmatic requests to AWS services.
### IAM Policies
IAM policies are JSON documents that define permissions for AWS resources. Policies can be attached to IAM users, groups, or roles to grant or deny access to specific AWS resources. Policies can be managed policies (created and managed by AWS) or inline policies (created and managed by you).
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "AWSDOC-EXAMPLE-BUCKET"
        }
    ]
}
```

### IAM Groups
IAM groups are collections of IAM users. You can use groups to manage permissions for multiple users at once. For example, you can create a group for developers and attach a policy that grants them access to specific AWS resources. All users in the group will inherit the permissions defined in the policy.

### IAM Roles
IAM roles are identities that you can create in your AWS account that have specific permissions. Roles are similar to IAM users, but they are not associated with a specific person or application. Instead, roles can be assumed by trusted entities, such as IAM users, applications, or AWS services. This allows you to grant temporary access to AWS resources without sharing long-term security credentials.

## AWS Organizations
AWS Organizations is a service that allows you to create and manage multiple AWS accounts from a single master account. It enables you to consolidate billing, apply policies, and manage access to AWS resources across multiple accounts. AWS Organizations helps you simplify account management and improve security by allowing you to apply policies at the organization level.

### Organizational Units (OUs)
Organizational Units (OUs) are containers within AWS Organizations that allow you to group accounts for management and policy application. You can create OUs to represent different departments, teams, or projects within your organization. By applying policies at the OU level, you can enforce security and compliance requirements across multiple accounts.

### Service Control Policies (SCPs)
Service Control Policies (SCPs) are policies that you can use to manage permissions across your AWS Organization. SCPs allow you to define the maximum available permissions for accounts in your organization or organizational units. This helps you enforce security and compliance requirements by restricting access to specific AWS services or actions.

### AWS Control Tower
AWS Control Tower is a service that helps you set up and govern a secure, multi-account AWS environment based on AWS best practices. It provides a pre-configured landing zone, which includes accounts, organizational units, and guardrails to help you manage security and compliance across your organization. AWS Control Tower simplifies the process of setting up and managing multiple AWS accounts while ensuring that they adhere to security best practices.

## Compliance
AWS compliance refers to the adherence of AWS services and infrastructure to various industry standards, regulations, and best practices. AWS provides a range of compliance certifications and attestations to help customers meet their regulatory requirements. Some of the key compliance frameworks supported by AWS include:
* General Data Protection Regulation (GDPR),
* Health Insurance Portability and Accountability Act (HIPAA),
* Federal Risk and Authorization Management Program (FedRAMP),
* Payment Card Industry Data Security Standard (PCI DSS),
* International Organization for Standardization (ISO) standards,
* Service Organization Control (SOC) reports,
* Cloud Security Alliance (CSA) STAR certification,
* National Institute of Standards and Technology (NIST) Cybersecurity Framework,
* ...

### AWS Artifact
AWS Artifact is a service that provides on-demand access to AWS compliance reports and security and compliance documentation. It allows customers to download compliance reports, such as SOC 1, SOC 2, and ISO certifications, as well as AWS's security and compliance policies. AWS Artifact helps customers understand AWS's compliance posture and how it aligns with their own compliance requirements.

### AWS Customer Compliance Center
The AWS Customer Compliance Center is a centralized resource that provides customers with information about AWS compliance programs, certifications, and security best practices. It offers access to compliance documentation, **whitepapers**, and other resources to help customers understand how AWS services can help them meet their compliance requirements.

#### Whitepapers
AWS whitepapers are technical documents that provide in-depth information about AWS services, architectures, and best practices. They cover a wide range of topics, including security, compliance, architecture, and operational excellence. Whitepapers are valuable resources for customers looking to understand AWS services and how to implement them securely and efficiently.

## Distributed Denial of Service (DDoS) Attacks
A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the normal functioning of a targeted server, service, or network by overwhelming it with a flood of traffic. DDoS attacks can be carried out using a network of compromised computers, known as a botnet, which are controlled by the attacker.
DDoS attacks can target various layers of the OSI model, including the application layer, transport layer, and network layer. The goal of a DDoS attack is to make a service unavailable to its intended users by consuming its resources or exploiting vulnerabilities in the system.
### AWS Shield
AWS Shield is a managed DDoS protection service that safeguards applications running on AWS. It provides two levels of protection:
* AWS Shield Standard: Automatically protects all AWS customers from common and most frequently occurring DDoS attacks at no additional cost. It provides protection against network and transport layer attacks.
* AWS Shield Advanced: Provides additional protection against larger and more sophisticated DDoS attacks. It includes features such as real-time attack visibility, DDoS cost protection, and access to the AWS DDoS Response Team (DRT) for assistance during an attack.
### AWS WAF
AWS WAF (Web Application Firewall) is a security service that helps protect web applications from common web exploits and vulnerabilities. It allows you to create custom rules to filter and monitor HTTP and HTTPS requests based on specific criteria, such as IP addresses, HTTP headers, and request body content.
AWS WAF can be used in conjunction with AWS Shield to provide an additional layer of security against DDoS attacks and other web-based threats. It helps you protect your applications from attacks such as SQL injection, cross-site scripting (XSS), and other common vulnerabilities.
### AWS Firewall Manager
AWS Firewall Manager is a security management service that simplifies the administration of AWS WAF rules and policies across multiple accounts and resources. It allows you to centrally configure and manage firewall rules, including AWS WAF rules, AWS Shield Advanced protections, and VPC security groups.
AWS Firewall Manager helps you enforce consistent security policies across your organization and ensures that all accounts are protected against common threats. It also provides visibility into the security posture of your AWS resources and helps you respond to security incidents more effectively.

## Additional AWS Security Services
### AWS Key Management Service (KMS)
AWS Key Management Service (KMS) is a managed encryption service that allows you to create and control the encryption keys used to encrypt your data. KMS provides a centralized key management solution that integrates with other AWS services, enabling you to encrypt data at rest and in transit.
### AWS Secrets Manager
AWS Secrets Manager is a service that helps you protect access to your applications, services, and IT resources without the upfront investment and on-going maintenance costs of operating your own infrastructure. It enables you to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.
### AWS CloudTrail
AWS CloudTrail is a service that enables you to monitor and log API calls made in your AWS account. It provides a history of AWS API calls for your account, including the identity of the API caller, the time of the API call, and the source IP address. CloudTrail helps you track changes to your AWS resources and provides visibility into user activity for security and compliance purposes.
### AWS Inspector
AWS Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It automatically assesses applications for vulnerabilities and deviations from best practices, such as network accessibility and operating system configuration.
AWS Inspector provides detailed findings and recommendations for remediation, helping you identify and address security issues in your applications.
### AWS GuardDuty
AWS GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and unauthorized behavior. It uses machine learning, anomaly detection, and integrated threat intelligence to identify potential security threats in real-time.
GuardDuty provides actionable security findings and alerts, allowing you to respond quickly to potential threats and improve your overall security posture.


