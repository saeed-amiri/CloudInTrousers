# TinyTrousers
A simple exercise to get to know clouds, using, and coding in it.

*Also some key words to remember!*

`s3`: Simple Storage Service

`IAM`: Identity and Access Management; It controls who can access AWS services and what actions they cam perform.

- IAM Users -> Individual accounts with access.
- IAM Policies -> Rules defining permissions;
- IAM Roles -> Temporary permissions for apps.

`EC2`: Elastic Compute Cloud it is AWS's virtual machine (VM) service.

- Run applications like on a physical server.
- Choose OS
- Scale server up/sown based on the load.

`CLI` in AWS:

**Examples:**
```bash
aws s3 ls  # List S3 buckets
aws s3 cp myfile.text s3://my-bucket/  # upload a file
aws ec2 describe-instances  # Show running EC2 instances