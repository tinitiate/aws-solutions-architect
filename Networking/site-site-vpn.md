# Site-to-Site VPN
  - We can enable access to your remote network from your VPC by creating an AWS Site-to-Site VPN (Site-to-Site VPN) connection, 
    and configuring routing to pass traffic through the connection.
  - The following are the key concepts for Site-to-Site VPN:
    - VPN connection: A secure connection between your on-premises equipment and your VPCs.
    - VPN tunnel: An encrypted link where data can pass from the customer network to or from AWS.
    - Each VPN connection includes two VPN tunnels which you can simultaneously use for high availability.
    - Customer gateway: An AWS resource which provides information to AWS about your customer gateway device.
    - Customer gateway device: A physical device or software application on your side of the Site-to-Site VPN connection.
    - Target gateway: A generic term for the VPN endpoint on the Amazon side of the Site-to-Site VPN connection.
    - Virtual private gateway: A virtual private gateway is the VPN endpoint on the Amazon side of your Site-to-Site VPN connection
      that can be attached to a single VPC.
    - Transit gateway: A transit hub that can be used to interconnect multiple VPCs and on-premises networks, and as a VPN endpoint for the Amazon side of the Site-to-Site VPN connection.

## Virtual Private Gateway

- VPN cocentrator on the Amazon side of the Site-to-Site VPN connection
- VGW is created and attached to the VPC from which you want to create the Site-to-Site VPN connection
- When we create a virtual private gateway, you can specify the private Autonomous System Number (ASN) for the Amazon side of the gateway.

## Customer Gateway

- Software application or physical device on client side of the Site-to-Site VPN connection.
- IP Address
  - Use static, internet-routable IP address for your customer gateway device
  - if a CGW behind NAT (NAT-T), use the public IP address of the NAT.
  
## Transit Gateway

- A transit gateway is a transit hub that you can use to interconnect your virtual private clouds (VPC) and on-premises networks
- Connects your VPCs and on-premises networks through a central hub. This simplifies your network and puts an end to complex peering relationships. It acts as a cloud    router – each new connection is only made once.
- For having **transitive peering between thousands of VPC and on-premises**, hub-and-spoke (star) connection
- Regional resource, can work cross-region
- Share cross-account using Resource Access Manager (RAM)
- You can peer Transit Gateways across regions
- Route Tables: limit which VPC can talk with other VPC
- Works with Direct Connect Gateway, VPN connections
- **Supports IP Multicast** (not supported by any other AWS service)

Another use case for Transit Gateway is to increase the bandwith of your site-to-site VPN connection using **ECMP**.
- ECMP = Equal-cost multi-path routing
- Routing strategy to allow to forward a packet over multiple best path
- Use case: create multiple Site to-Site VPN connections to increase the bandwidth of your connection to AWS.





![aws-Site-to-Site](/VPC/images/site-basic-diagram.png)

![aws-Site-to-Site](/VPC/images/site-site-transit-gateway-basic.png)

![aws-Site-to-Site](/VPC/images/branch-offices-diagram.png)

![aws-Site-to-Site](/VPC/images/branch-off-transit-gateway.png)
