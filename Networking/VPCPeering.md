# VPC Peering

- A networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network.

- Allows you to connect one VPC with another via a **direct network route** using private IP addresses.

- Instances behave as if they were on the same private network.

- A VPC peering connection is neither a gateway nor a AWS Site-to-Site VPN connection, and does not rely on a separate piece of physical hardware. There is no single point of failure for communication or a bandwidth bottleneck.

- **Must not have overlapping CIDR**.

  ![overlapping-cidrs-diagram](/Networking/images/overlapping-cidrs-diagram.png)
  
  
  ![overlapping-cidrs-ipv6-diagram](/Networking/images/overlapping-cidrs-ipv6-diagram.png)

   			

  ![overlapping-multiple-cidrs-diagram](/Networking/images/overlapping-multiple-cidrs-diagram.png)

  ​

- We can peer VPCs with other AWS accounts as well as with other VPCs in the same account

- You must update route tables in **each VPC’s subnets** to ensure instances can communicate

- VPC Peering can work **inter-region, cross-account**

- You can reference a security group of a peered VPC (works across account)

- Does not support transitive peering.

  ![transitive-peering-diagram](/Networking/images/transitive-peering-diagram.png)

## Establishing A Peering Connection

- The owner of the requester VPC sends a request to the owner of the accepter VPC to create the VPC peering connection. The accepter VPC cannot have a CIDR block that overlaps with the requester VPC’s CIDR block.
- To enable the flow of traffic between the VPCs using private IP addresses, the owner of each VPC in the VPC peering connection must manually add a route to one or more of their VPC route tables that points to the IP address range of the other VPC (the peer VPC).
- Update the security group rules that are associated with your instance to ensure that traffic to and from the peer VPC is not restricted.
- By default, if instances on either side of a VPC peering connection address each other using a public DNS hostname, the hostname resolves to the instance’s public IP address. To change this behavior, enable DNS hostname resolution for your VPC connection. This will allow the DNS hostname to resolve to the instance’s private IP address.

## Limitations

- You cannot create a VPC peering connection between VPCs that have matching or overlapping IPv4 or IPv6 CIDR blocks.
- You cannot have more than one VPC peering connection between the same two VPCs at the same time.
- **Unicast reverse path forwarding** in VPC peering connections is not supported.
- If the VPCs are in the same region, you can enable the resources on either side of a VPC peering connection to communicate with each other over IPv6.
- For inter-region peering, you cannot create a security group rule that references a peer VPC security group. Communication over IPv6 is not supported as well.
