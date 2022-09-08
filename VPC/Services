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
