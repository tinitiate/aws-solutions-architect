# NAT Devices

- Enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating connections with the instances.
- The NAT device replaces the source IPv4 address of the instances with the address of the NAT device.
  When sending response traffic to the instances, the NAT device translates the addresses back to the
  original source IPv4 addresses.
- NAT devices are not supported for IPv6 traffic—use an egress-only internet gateway instead. For more
  information, see Enable outbound IPv6 traffic using an egress-only internet gateway (p. 137).
- AWS uses the term NAT  to follow common IT practice, though the actual role of a NAT device is both address translation and port address translation (PAT).
- We can use a managed NAT device offered by AWS:
  - **NAT Gateway**
  - NAT device on an EC2 instance, called a **NAT instance**. 

## NAT Instance 

NAT stands for **Network Address Translation**, it allows *instances in private subnets* to connect to the internet

- When you try to create a NAT Instance, **disable the source/destination check** on the instance first
- NAT instances must be in a **public subnet**.
- Route table must be configured to route traffic from the private subnet to the NAT instance, for this to work.
- Must have Elastic IP attached to it
- The amount of traffic that NAT instances can support depends on the **instance size**. If you are bottlenecking, increase the instance size.
- You can create **high availability** using Autoscaling Groups, multiple subnets in different AZs, and a script to automate failover.
- It is behind the Security Group

Must manage security groups and rules

- Inbound
  - Allow HTTP/HTTPS traffic from Private Subnets
  - Allow SSH from your home network (access provided through Internet Gateway)
- Outbound
  - Allow HTTP/HTTPS traffic to the internet

## NAT Gateways

- AWS managed NAT, higher bandwidth, better availability, no administration
- NAT Gateways are redundant inside the Availability Zone. **One NAT gateway per availability zone**.
- **Not associated with security groups**.
- You must specify the **public subnet** in which the NAT gateway should reside.
- NAT Gateway is created in a specific AZ, using an Elastic IP
- Deleting a NAT gateway disassociates its Elastic IP address, but does not release the address from your account.
- A NAT gateway supports the following protocols: TCP, UDP, and ICMP.
- A NAT gateway can support up to 55,000 simultaneous connections to each unique destination.
- A NAT gateway cannot send traffic over VPC endpoints, VPN connections, AWS Direct Connect, or VPC peering connections.
- A NAT gateway uses ports 1024-65535. Make sure to enable these in the inbound rules of your network ACL.

### NAT Gateway with High Availability

- NAT Gateway is resilient within a single-AZ
- However, we must create multiple NAT Gateway in multiple AZ for fault-tolerance
- There is no cross AZ failover needed because if an AZ goes down it does not need NAT

## Comparison of NAT Instance and NAT Gateway

| Attribute            | NAT gateway                              | NAT instance                             |
| -------------------- | ---------------------------------------- | ---------------------------------------- |
| Availability         | Highly available. NAT gateways in each Availability Zone are implemented with redundancy. Create a NAT gateway in each Availability Zone to ensure zone-independent architecture. | Use a script to manage failover between instances. |
| Bandwidth            | Scale up to 100 Gbps.                    | Depends on the bandwidth of the instance type. |
| Maintenance          | Managed by AWS. You do not need to perform any maintenance. | Managed by you, for example, by installing software updates or operating system patches on the instance. |
| Performance          | Software is optimized for handling NAT traffic. | A generic AMI that's configured to perform NAT. |
| Cost                 | Charged depending on the number of NAT gateways you use, duration of usage, and amount of data that you send through the NAT gateways. | Charged depending on the number of NAT instances that you use, duration of usage, and instance type and size. |
| Type and size        | Uniform offering; you don’t need to decide on the type or size. | Choose a suitable instance type and size, according to your predicted workload. |
| Public IP addresses  | Choose the Elastic IP address to associate with a public NAT gateway at creation. | Use an Elastic IP address or a public IP address with a NAT instance. You can change the public IP address at any time by associating a new Elastic IP address with the instance. |
| Private IP addresses | Automatically selected from the subnet's IP address range when you create the gateway. | Assign a specific private IP address from the subnet's IP address range when you launch the instance. |
| Security groups      | You cannot associate security groups with NAT gateways. You can associate them with the resources behind the NAT gateway to control inbound and outbound traffic. | Associate with your NAT instance and the resources behind your NAT instance to control inbound and outbound traffic. |
| Network ACLs         | Use a network ACL to control the traffic to and from the subnet in which your NAT gateway resides. | Use a network ACL to control the traffic to and from the subnet in which your NAT instance resides. |
| Flow logs            | Use flow logs to capture the traffic.    | Use flow logs to capture the traffic.    |
| Port forwarding      | Not supported.                           | Manually customize the configuration to support port forwarding. |
| Bastion servers      | Not supported.                           | Use as a bastion server.                 |
| Traffic metrics      | View CloudWatch metrics for the NAT gateway. | View CloudWatch metrics for the instance. |
| Timeout behavior     | When a connection times out, a NAT gateway returns an RST packet to any resources behind the NAT gateway that attempt to continue the connection (it does not send a FIN packet). | When a connection times out, a NAT instance sends a FIN packet to resources behind the NAT instance to close the connection. |
| IP fragmentation     | Supports forwarding of IP fragmented packets for the UDP protocol.Does not support fragmentation for the TCP and ICMP protocols. Fragmented packets for these protocols will get dropped. | Supports reassembly of IP fragmented packets for the UDP, TCP, and ICMP protocols. |