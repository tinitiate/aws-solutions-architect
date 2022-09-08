# Amazon VPC

- An Amazon VPC is an isolated portion of the AWS cloud. We use Amazon VPC to create a virtual network topology for our Amazon EC2 resources.
- We have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.
- We can create a public-facing subnet for your webservers that has access to the Internet, and place your backend systems such as databases or application servers in a private-facing subnet with no Internet access.

## VPC Example

![AWS-VPC](/VPC/images/AWS-VPC.png)

## Subnets

- A subnet defines a range of IP addresses in your VPC. 
- We can launch AWS resources into a subnet that we select.
- A private subnet should be used for resources that won’t be accessible over the Internet.
- A public subnet should be used for resources that will be accessed over the Internet.
- Each subnet must reside entirely within one Availability Zone and cannot span zones.
- Types of Subnets
  - Public Subnet – has an internet gateway
  - Private Subnet – doesn’t have an internet gateway
  - VPN-only Subnet – has a virtual private gateway instead
- We cannot increase or decrease the size of an existing CIDR (Classless Inter-Domain Routing) block.
- The first 4 and last 1 IP addresses in a subnet are reserved.
- When we associate a CIDR block with our VPC, a route is automatically added to your VPC route tables to enable routing within the VPC (the destination is the CIDR block and the target is *local*).


## Subnet Routing
- Each subnet must be associated with a **route table**, which specifies the allowed routes for **outbound** **traffic** leaving the subnet.
- Every subnet that we create is automatically associated with the main route table for the VPC.
- We can change the association, and contents of the main route table.
- We can allow an instance in your VPC to initiate outbound connections to the internet over IPv4 but prevent unsolicited inbound connections from the internet using a 
  **NAT gateway or NAT instance**.
- To initiate outbound-only communication to the internet over IPv6, you can use an egress-only internet gateway.



## **Subnet Security**
 - AWS provides two features that we can use to increase security in our VPC: 
   - Security Groups 
   - Network Access Control Lists

### **Security Groups**

  - Security Groups control inbound and outbound traffic for your instances
  - We can associate one or more (up to five) security groups to an instance in your VPC.
  - If you don’t specify a security group, the instance automatically belongs to the default security group.
  - When you create a security group, it has no inbound rules. By default, it includes an outbound rule that allows all outbound traffic.
  - Security groups are associated with network interfaces.

### **Network Access Control Lists**

  - Network Access Control Lists — control inbound and outbound traffic for your subnets
  - Each subnet in our VPC must be associated with a network ACL. 
  - Every subnet that we create is automatically associated with the default network ACL for the VPC.
  - We can associate a network ACL with multiple subnets; however, a subnet can be associated with only one network ACL at a time.
  - A network ACL contains a numbered list of rules that is evaluated in order, starting with the lowest numbered rule, to determine whether traffic is allowed in or       out of any subnet associated with the network ACL.
  - The default network ACL is configured to **allow all traffic to flow in and out** of the subnets to which it is associated.
  - For custom ACLs, you need to add a rule for ephemeral ports, usually with the range of 32768-65535. If you have a NAT Gateway, ELB or a Lambda function in a VPC,       you need to enable 1024-65535 port range.  ​

| *Security Group*                         | *Network ACL*                            |
| ---------------------------------------- | ---------------------------------------- |
| Operates at the **instance level**       | Operates at the **subnet level**         |
| Supports **ALLOW rules **only            | Supports **ALLOW rules and DENY rules**  |
| Is **stateful: **Return traffic is automatically allowed, regardless of any rules | Is **stateless**: Return traffic must be explicitly allowed by rules |
| We evaluate **all rules **before deciding whether to allow traffic | We process **rules in number order **when deciding whether to allow traffic |
| Applies only to EC2 instances and similar services that use EC2 as a backend. | Automatically **applies to all**         |
| Security group is specified when launching the instances, or is associated with the instance later on | **Instances in the subnets it’s associated with** |

- Diagram of security groups and NACLs in a VPC

![VPC-Security](/VPC/images/VPC-Security.png)

  ## **VPC Networking Components**

  - ### Network Interfaces

    - A virtual network interface that can include:
      - a primary private IPv4 address
      - one or more secondary private IPv4 addresses
      - one Elastic IP address per private IPv4 address
      - one public IPv4 address, which can be auto-assigned to the network interface for eth0 when you launch an instance
      - one or more IPv6 addresses
      - one or more security groups
      - a MAC address
      - a source/destination check flag
      - a description
    - Network interfaces can be attached and detached from instances, however, you cannot detach a primary network interface.

  - ### Route Tables

    - Contains a set of rules, called *routes*, that are used to determine where network traffic is directed.
    - A subnet can only be associated with one route table at a time, but you can associate multiple subnets with the same route table.
    - We cannot delete the main route table, but we can replace the main route table with a custom table that we’ve created.
    - We must update the route table for any subnet that uses gateways or connections.
    - Uses the most specific route in your route table that matches the traffic to determine how to route the traffic (longest prefix match).



  - ### VPC Endpoints

    - Privately connect your VPC to supported AWS services and VPC endpoint services powered by PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
    - Endpoints are virtual devices.
    - Two Types
      - Interface Endpoints
        - An elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported service.
        - Can be accessed through AWS VPN connections or AWS Direct Connect connections, through intra-region VPC peering connections from Nitro instances, and through inter-region VPC peering connections from any type of instance.
        - For each interface endpoint, you can choose only one subnet per Availability Zone. Endpoints are supported within the same region only.
        - You can add endpoint policies to interface endpoints. The Amazon VPC endpoint policy defines which principal can perform which actions on which resources. An endpoint policy does not override or replace IAM user policies or service-specific policies. It is a separate policy for controlling access from the endpoint to the specified service.
        - An interface endpoint supports IPv4 TCP traffic only.
      - **Gateway Endpoints**
        - A gateway that is a target for a specified route in your route table, used for traffic destined to a supported AWS service.
        - You can create multiple endpoints in a single VPC, for example, to multiple services. You can also create multiple endpoints for a single service, and use different route tables to enforce different access policies from different subnets to the same service.
        - You can modify the endpoint policy that’s attached to your endpoint, and add or remove the route tables that are used by the endpoint.
        - Endpoints are supported within the same region only. You cannot create an endpoint between a VPC and a service in a different region.
        - Endpoints support IPv4 traffic only.
        - You must enable DNS resolution in your VPC, or if you’re using your own DNS server, ensure that DNS requests to the required service (such as S3) are resolved correctly to the IP addresses maintained by AWS.

  - You can create your own application in your VPC and configure it as an AWS PrivateLink-powered service (referred to as an *endpoint service*). You are the *service provider*, and the AWS principals that create connections to your service are *service consumers*.

### VPC Flow Logs

- Flow Logs is a feature that enables you to **capture information about the IP traffic going to and from network interfaces in your VPC**. 
- Flow log data is **stored using Amazon S3 / CloudWatch Logs**. 
- Flow logs can help you with a number of tasks, such as:
  - Diagnosing overly restrictive security group rules
  - Monitoring the traffic that is reaching your instance
  - Determining the direction of the traffic to and from the network interfaces

- There are three levels of abstraction:
  - VPC Flow Logs
  - Subnet Flow Logs
  - Elastic Network Interface Flow Logs
- Helps to monitor & troubleshoot connectivity issues
- We cannot enable flow logs for VPCs that are peered with your VPC unless the peer VPC is in your account.
- You cannot tag a flow log.
- After you’ve created a flow log, you cannot change its configuration; for example, you can’t associate a different IAM role with the flow log.
- Not ALL IP Traffic is monitored
  - Traffic that goes to Route53.
  - Traffic generated for Windows license activation.
  - Traffic to and from 169.254.169.254 (instance metadata).
  - Traffic to and from 169.254.169.123 for the Amazon Time Sync Service.
  - DHCP traffic.
  - Traffic to the reserved IP address for the default VPC router.

- To query VPC Flow Logs, we can use Athena on S3 or CloudWatch Logs Insights.

- Amazon security groups and network ACLs don’t filter traffic to or from link-local addresses or AWS-reserved IPv4 addresses. Flow logs do not capture IP traffic to or from these addresses.

### Bastion Hosts

- We use a Bastion Host to SSH into our private instances

- The bastion is in the public subnet which is then connected to all other private subnets

- Bastion Host security group must be tightened

- A Bastion is used to **securely** administrate EC2 instances (using SSH or RDP).

- We **cannot** use a NAT Gateway as a Bastion host.

  ![BastionHost](/VPC/images/BastionHost.png)



#### AWS PrivateLink (VPC Endpoints Services)

- #### Most secure & scalable way o expose a service to 1000s of VPC (own or other accounts)

- Does not require VPC Peering, Internet Gateway, NAT, Route Tables

##### VPN CloudHub

- Provide secure communication between sites, if you have multiple VPN connections
- Low-cost hub-and-spoke model for primary or secondary network connectivity between locations
- it’s a VPN connection so it goes over the public internet
- Requires a network load balancer (Service VPC) and ENI (Customer VPC)


#### ![aws-privatelink](/VPC/images/aws-privatelink.png)

| Service                             | Description                              |
| ----------------------------------- | ---------------------------------------- |
| CIDR                                | IP Range                                 |
| VPC                                 | Virtual Private Cloud => we define a list of IPv4 & IPv6 CIDR |
| Subnets                             | Tied to an AZ, we define a CIDR          |
| Route Tables                        | Must be edited to add routes from subnets to the IGW, VPC Peering Connections, VPC Endpoints, etc.. |
| NAT Instances                       | Gives internet access to instances in private subnets. Old, must be set up in a public subnet, disable `Source / Destination check` flag |
| NAT Gateway                         | Managed by AWS, provides scalable internet access to private instances, IPv4 only |
| Private DNS + Route 53              | Enable DNS Resolution + DNS Hostnames (VPC) |
| NACL                                | Stateless, subnet rules for inbound and outbound, don’t forget ephemeral ports |
| Security Groups                     | Stateful, operate at the EC2 instance level |
| VPC Peering                         | Connect two VPC with non-overlapping CIDR, non-transitive |
| VPC Endpoints                       | Provide private access to AWS Services (S3, DynamoDB, CloudFormation, SSM) within VPC |
| VPC Flow Logs                       | Can be set up at the VPC / Subnet / ENI Level, for `ACCEPT` and `REJECT` traffic, helps to identify attacks, analyze using Athena or CloudWatch Log Insights |
| Bastion Host                        | Public instance to SSH into, that has SSH connectivity to instances in subnets |
| Site to Site VPN                    | Setup a Customer Gateway on DC, a Virtual Private Gateway on VPC, and site-to-site VPN over public internet |
| Direct Connect                      | Setup a Virtual Private Gateway on VPC, and establish a direct private connection to an AWS Direct Connect Location |
| Direct Connect Gateway              | Setup a Direct Connect to many VPCs in different regions |
| Internet Gateway Egress             | Like a NAT Gateway, but for IPv6         |
| PrivateLink / VPC Endpoint Services | Connect services privately from your service VPC to customers VPC; Does not need VPC peering, public internet, NAT gateway, route tables; Must be used with Network Load Balancer & ENI |
| ClassicLink                         | Connect EC2-Classic instances privately to your VPC |
| VPC CloudHub                        | Hub-and-spoke VPN model to connect your sites |
| Transit gateway                     | Peering between thousands of VPC and on-premises, hub-and-spoke (star) connection |
