# Module 8: Pricing and Support
The subject of this module:
* Describe AWS pricing and support models.
* Describe the AWS Free Tier.
* Describe key benefits of AWS Organizations and consolidated billing.
* Explain the benefits of AWS Budgets.
* Explain the benefits of AWS Cost Explorer.
* Explain the primary benefits of the AWS Pricing Calculator.
* Distinguish between the various AWS Support Plans.
* Describe the benefits of AWS Marketplace.

## AWS Free Tier
The AWS Free Tier is a program that allows you to use certain AWS services for free, up to specified limits, for a limited time. It is designed to help you get started with AWS and explore its services without incurring costs.
### Key Features of the AWS Free Tier
* **Always Free**: Offers free usage of certain services that are always free, regardless of when you sign up, such as:
    * Amazon CloudWatch: 10 custom metrics and 1 million API requests per month.
    * AWS Lambda: 1 million free requests and 400,000 GB-seconds of compute time per month.
    * Amazon SNS: 1 million mobile push notifications per month.

* **12-Month Free Tier**: Offers free usage of certain services for 12 months after signing up for an AWS account, like:
    * Amazon EC2: 750 hours of t2.micro instances each month.
    * Amazon S3: 5 GB of standard storage.
    * Amazon RDS: 750 hours of db.t2.micro instances each month.
    * Amazon DynamoDB: 25 GB of storage and 200 million requests per month.

* **Short-Term Trials**: Offers free trials of certain services for a limited time, such as:
    * Amazon Redshift: 2 months of free usage for 750 hours of dc2.large nodes.
    * Amazon SageMaker: 2 months of free usage for 250 hours of ml.t2.medium instances.
    * Amazon QuickSight: 1 month of free usage for 1 user and 1 GB of SPICE capacity.


## AWS Pricing Conccepts
AWS pricing concepts are essential for understanding how AWS services are billed and how to manage costs effectively. Here are some key concepts:
* **Pay-as-you-go**: You pay only for the services you use, with no upfront costs or long-term contracts. This allows you to scale resources up or down based on demand.
* **On-Demand Pricing**: You pay for compute capacity by the hour or second, with no long-term contracts or upfront payments. This is ideal for applications with unpredictable workloads.
* **Reserved Instances**: You can reserve capacity for a one- or three-year term, which provides significant savings compared to on-demand pricing. This is ideal for applications with predictable workloads.
* **Spot Instances**: You can bid on unused EC2 capacity at a lower price than on-demand instances. This is ideal for applications with flexible start and end times.
* **Savings Plans**: You can commit to a specific amount of usage (measured in $/hour) for a one- or three-year term, which provides significant savings compared to on-demand pricing. This is ideal for applications with predictable workloads.
* **Free Tier**: AWS offers a free tier for new customers, which provides limited usage of certain services for free for the first 12 months. This is ideal for exploring AWS services without incurring costs.
### AWS Pricing Calculator
The AWS Pricing Calculator is a web-based tool that helps you estimate the cost of using AWS services. It allows you to create and customize your own pricing estimates based on your specific usage patterns and requirements.
### Key Features of the AWS Pricing Calculator
* **Service Selection**: Choose from a wide range of AWS services to include in your estimate.
* **Configuration Options**: Customize the configuration of each service, including instance types, storage options, and data transfer.
* **Cost Estimates**: Get detailed cost estimates based on your configuration choices and usage patterns.
* **Export and Share**: Export your estimates to a PDF or share them with others.
* **Cost Comparison**: Compare the costs of different configurations and services to find the most cost-effective solution.
* **Cost Breakdown**: View a detailed breakdown of costs by service, region, and usage type.
* **Interactive Interface**: Use an interactive interface to easily adjust your configuration and see how it affects costs.


## AWS Dashboard
The AWS Management Console provides a dashboard that gives you an overview of your AWS resources and services. It allows you to manage your AWS account, access services, and monitor usage and costs.

## Consolidated Billing
AWS Organizations is a service that allows you to manage multiple AWS accounts from a single master account. It provides consolidated billing, which allows you to combine usage across multiple accounts and receive a single bill.
### Key Features of AWS Organizations
* **Consolidated Billing**: Combine usage across multiple accounts and receive a single bill.
* **Service Control Policies (SCPs)**: Define policies that control access to AWS services and resources across accounts.
* **Organizational Units (OUs)**: Group accounts into OUs for easier management and policy application.
* **Account Management**: Create, manage, and delete accounts within your organization.
* **Cost Management**: Monitor and manage costs across multiple accounts.

## AWS Budgets
AWS Budgets is a service that allows you to set custom cost and usage budgets for your AWS account. It helps you monitor your spending and receive alerts when you exceed your budget thresholds.
### Key Features of AWS Budgets
* **Cost Budgets**: Set budgets for specific cost categories, such as service costs or linked accounts.
* **Usage Budgets**: Set budgets for specific usage types, such as EC2 instance hours or S3 storage.
* **Alerts**: Receive alerts when you exceed your budget thresholds or when your usage approaches your budget limits.
* **Cost Explorer Integration**: Use AWS Cost Explorer to visualize and analyze your spending patterns.
* **Forecasting**: Use historical data to forecast future spending and usage trends.

## AWS Cost Explorer
AWS Cost Explorer is a service that allows you to visualize and analyze your AWS spending patterns. It provides detailed reports and insights into your usage and costs, helping you identify trends and optimize your spending.
### Key Features of AWS Cost Explorer
* **Cost and Usage Reports**: Generate detailed reports on your AWS spending and usage.
* **Custom Reports**: Create custom reports based on specific services, accounts, or time periods.
* **Forecasting**: Use historical data to forecast future spending and usage trends.
* **Cost Allocation Tags**: Use tags to categorize and track costs by project, department, or other criteria.
* **Interactive Interface**: Use an interactive interface to explore and analyze your spending patterns.

## AWS Support Plans
AWS offers several support plans to help you manage your AWS resources and resolve issues. Each plan provides different levels of support, including technical assistance, account management, and access to AWS resources.
### Key Features of AWS Support Plans
* **Basic Support**: Provides access to AWS documentation, whitepapers, and support forums. Ideal for customers who need minimal support.
* **Developer Support**: Provides access to AWS support engineers via email and chat, as well as access to AWS Trusted Advisor. Ideal for customers who need technical support for development and testing.
* **Business Support**: Provides 24/7 access to AWS support engineers via phone, email, and chat, as well as access to AWS Trusted Advisor and AWS Support API. Ideal for customers who need technical support for production workloads.
* **Enterprise Support**: Provides 24/7 access to AWS support engineers via phone, email, and chat, as well as access to AWS Trusted Advisor, AWS Support API, and a designated Technical Account Manager (TAM). Ideal for customers with mission-critical workloads.
* **AWS Marketplace**: AWS Marketplace is an online store that offers a wide range of software applications and services that run on AWS. It allows you to discover, purchase, and deploy software solutions from third-party vendors.
### Technical Account Manager (TAM)
A Technical Account Manager (TAM) is a designated AWS support engineer who provides personalized support and guidance to customers with Enterprise Support plans. The TAM helps customers optimize their AWS environment, resolve issues, and achieve their business goals.

## AWS Marketplace
AWS Marketplace is an online store that offers a wide range of software applications and services that run on AWS. It allows you to discover, purchase, and deploy software solutions from third-party vendors.
### Key Features of AWS Marketplace
* **Wide Range of Software**: Offers a variety of software applications, including security, networking, storage, and machine learning solutions.
* **Easy Deployment**: Allows you to deploy software solutions with just a few clicks, without the need for complex installation processes.
* **Pay-as-you-go Pricing**: Offers flexible pricing options, including pay-as-you-go, subscription, and free trials.
* **Integration with AWS Services**: Seamlessly integrates with AWS services, allowing you to easily deploy and manage software solutions in your AWS environment.
* **Customer Reviews**: Provides customer reviews and ratings to help you make informed decisions about software solutions.