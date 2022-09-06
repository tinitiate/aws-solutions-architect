# Internet Gateways

- Allows communication between instances in your VPC and the internet.
- Imposes no availability risks or bandwidth constraints on your network traffic.
- Provides a target in VPC route tables for internet-routable traffic, and performs network address translation for instances that have been assigned public IPv4 addresses.
- The following table provides an overview of whether your VPC automatically comes with the components required for internet access over IPv4 or IPv6.
- To enable access to or from the Internet for instances in a VPC subnet, you must do the following:
  - Attach an Internet Gateway to your VPC
  - Add a route to subnet's route table that directs internet-bound traffic to the internet gateway.
  - Ensure that instances in your subnet have a globally unique IP address (public IPv4 address, Elastic IP address, or IPv6 address).
  - Ensure that your network access control and security group rules allow the relevant traffic to flow to and from your instance.
    ![internet gateway](/VPC/images/internet-gateway.png)

## Egress-Only Internet Gateways

- IPv6 addresses are globally unique, and are therefore public by default. If we want our instance to be able to access the internet, but prevent resources on the       internet from initiating communication with your instance, you can use an egress-only internet gateway..
- An egress-only Internet gateway is Stateful : it forwards traffic from the instances in the subnet to the internet or other AWS services, and then sends the response back to the instances.
- We cannot associate a security group with an egress-only Internet gateway.
- We can use a network ACL to control the traffic to and from the subnet for which the egress-only Internet gateway routes traffic.
  ![internet gateway](/VPC/images/egress-only-igw.png)

## Elastic IP Addresses

- A **static, public IPv4 address** designed for dynamic cloud computing.
- Elastic IP address can be associated with a single instance or network interface at a time.
- Elastic IP address can be moved from one instance or network interface to another.
- Elastic IP addresses remain associated with our account until you explicitly release them.
- Elastic IP addresses for IPv6 are not supported.