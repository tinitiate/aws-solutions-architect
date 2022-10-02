# Wavelength

- *Wavelength* enables developers to build applications that deliver ultra-low latencies to mobile devices and end users. 
- Wavelength Zones can be used to extend an Amazon VPC in order to run ultra-low latency applications that use the same AWS services, APIs, tools, and functionalities.
- Wavelength Zones support a wide range of compute instances for general purpose, gaming, and machine learning inference.
- Connectivity to 5G networks using VPC and Carrier Gateway.
- Use cases:
  - Create and distribute augmented/virtual reality (AR/VR) apps, as well as HD live video streaming.
  - Use AI and ML-powered video and image analytics at the edge to accelerate 5G applications in medical diagnostics, retail, and smart manufacturing settings.
  - With near-real-time communication between automobiles and the cloud, you’ll be able to create advanced driver assistance, autonomous driving, and in-vehicle entertainment experiences.

## Resources on Wavelength

- The services in Wavelength are part of a VPC that is connected over a reliable connection to an AWS Region for easy access to services running in Regional subnets.

- You can create Amazon EC2 instances, Amazon EBS volumes, and Amazon VPC subnets and carrier gateways in Wavelength Zones.

- You can also use services that orchestrate or work with EC2, EBS, and VPC, such as:

  - Amazon EC2 Auto Scaling

  - Amazon EKS clusters

  - Amazon ECS clusters

  - Amazon EC2 Systems Manager

  - Amazon CloudWatch

  - AWS CloudTrail

  - AWS CloudFormation

##  Concepts

The following are the key concepts for Wavelengths:

- **Wavelength** — to run workloads that require ultra-low latency over mobile networks.
- **Wavelength Zone (WZ)** — 
  - A zone in the carrier location where the Wavelength infrastructure is deployed. 
  - Wavelength Zones are associated with an AWS Region.
  -  A Wavelength Zone is a logical extension of the Region, and is managed by the control plane in the Region.
  - To give the most scalable, robust, and cost-effective alternatives for components, AWS recommends that you design the edge applications in a hub and spoke model with the Region.
- **VPC** — A customer virtual private cloud (VPC) that spans Availability Zones, Local Zones, and Wavelength Zones, and has deployed resources such as Amazon EC2 instances in the subnets that are associated with the zones.
- **Subnet** — A subnet that you create in a Wavelength Zone. You can create one or more subnets, and then run and manage AWS services, such as Amazon EC2 instances, in the subnet.
- **Carrier gateway** — 
  - A carrier gateway serves two purposes. 
    - It allows inbound traffic from a carrier network in a specific location.
    - allows outbound traffic to the carrier network and internet.
  - Only available for VPCs with WZ subnets.
  - Supports IPv4 traffic.
  - To assign a network interface, use a carrier IP address from the network border group.
- **Network Border Group** — A unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses.
- **Wavelength application** — An application that you run on an AWS resource in a Wavelength Zone.

## Pricing

- Prices for AWS resources in WZs will differ from those in the parent region.
- In WZs, EC2 instances are only available on demand.
- Wavelength Zones can be used with your Instance Savings Plan.
