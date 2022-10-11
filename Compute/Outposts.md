# AWS Outposts

- Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. 
- By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.
- An Outpost is a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region. 
- We Can create subnets on our Outpost and specify them when you create AWS resources such as EC2 instances, EBS volumes, ECS clusters, and RDS instances. Instances in Outpost subnets communicate with other instances in the AWS Region using private IP addresses, all within the same VPC

![outpost-networking-components](/Compute/images/outpost-networking-components.png)

## Key concepts 

### Outpost site 

- The customer-managed physical buildings where AWS will install your Outpost. 
- The site must meet the facility, networking, and power requirements for your Outpost.

###  Outpost configurations 

- Configurations of Amazon EC2 compute capacity, Amazon EBS storage capacity, and networking support. 
- Each configuration has unique power, cooling, and weight support requirements. 
- The compute and storage resources are called **Outpost capacity**.
- We must have **Outpost equipment** to use the AWS Outposts service. This includes AWS-managed racks, servers, switches, and cabling.

### Outpost capacity 

- Compute and storage resources available on the Outpost. 
- We can view and manage the capacity for your Outpost from the AWS Outposts console. 

### Outpost equipment 

- Physical hardware that provides access to the AWS Outposts service. 
- The hardware includes racks, servers, switches, and cabling owned and managed by AWS. 

### Outpost racks 

- An Outpost form factor that is an industry-standard 42U rack. 
- Outpost racks include rack-mountable servers, switches, a network patch panel, a power shelf and blank panels. •
- Using an Outpost subnet, you can launch EC2 instances and EBS volumes.
- Supports EBS snapshots on Outpost.

### Outpost servers 

- An Outpost form factor that is an industry-standard 1U or 2U server, which can be installed in a standard EIA-310D 19 compliant 4 post rack. 
- Outpost servers provide local compute and networking services to sites that have limited space or smaller capacity requirements. 
- We can launch EC2 instances that use instance store.
- Back up instances to Amazon EBS in the AWS Region using EBS direct APIs.

### Service link 

- Network route that enables communication between your Outpost and its associated AWS Region. 
- An Outpost is an extension of an Availability Zone and its associated Region. 

### Local gateway 

- Local gateway

  - Allows communication between an Outpost rack and on-premises network.

  - Components:

    - Route tables
    - Virtual interfaces

  - It also serves as a target in your VPC route tables for on-premises traffic and performs NAT for instances with addresses from your customer-owned IP pool.

  - Each Outpost rack supports one local gateway.

  - With AWS RAM, you can share the local gateway route table with other AWS accounts or organizational units.

    ![outpost-networking-components](/VPC/images/outpost-private-connectivity.png)

### Local network interface

-  Network interface that enables communication from an Outpost server and your on-premises network.

### Outpost sharing

- Enable Outpost owner to share Outposts and Outpost resources with other AWS accounts in the same AWS organization.
- Owners cannot modify instances that AWS accounts launch into Capacity Reservations.
- AWS accounts are not allowed to view or modify resources owned by other consumers or the Outpost owner.
- You can share Outpost resources to AWS accounts, organizational units, or entire organizations in AWS Organizations.

### Monitoring

- You can use Amazon Cloudwatch to retrieve Outposts metrics.
- To capture API actions from services on an Outpost, you can use AWS CloudTrail.
- Use VPC Flow Logs to get detailed information about traffic to and from your Outpost, as well as traffic within your Outpost.
- You can also use Traffic Mirroring for content inspection, threat monitoring, troubleshooting, or copying and forwarding network traffic.
- To see changes in the health of AWS resources, you can use AWS Health Dashboard.

### Pricing

- You are charged for Outposts rack capacity for a 3-year term: All, Partial, or No Upfront.
- You are charged for the following:
  - AWS services running on Outposts
  - AWS Marketplace AMIs
  - Outposts and Outpost resources that you share
  - Data transfer associated with Outpost’s service link VPN traffic from AWS Region
- You are not charged for data transfers from Outpost to the parent AWS Region.
