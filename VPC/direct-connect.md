# Direct Connect
- AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS.
- Provides a dedicated private connection from a remote network to your VPC.
- Dedicated connection must be set up between your DC and AWS Direct Connect locations.
- We need to set up a Virtual Private Gateway on our VPC.
- Access public resources (S3) and private (EC2) on the same connection
- Use cases:
  - Increase bandwidth throughput - working with large datasets, lower cost.
  - More consistent network experience - applications using real-time data feeds.
  - Hybrid Environments (on-prem + cloud)
- Supports both IPv4 and IPv6
- If we want to set up a Direct Connect to one or more VPC in many different regions (same account), you must use a Direct Connect Gateway.
- There are two types of connections:
  - Dedicated Connection
  - Hosted Connection

## Dedicated Connection: 
- A physical Ethernet connection associated with a single customer. 
- We can request a dedicated connection through the AWS Direct Connect console, the CLI, or the API.
- Request made to AWS first, then completed by Direct Connect Partners

## Hosted Connection: 
- A physical Ethernet connection that an AWS Direct Connect Partner provisions on behalf of a customer. 
- Customers request a hosted connection by contacting a partner in the AWS Direct Connect Partner Program, who provisions the connection.
- Lead times are often longer than 1 month to establish a new connection.
- Capacity can be added or removed on demand.
- 1,2,5,10 Gbps available at select AWS Direct Connection Partners.
- If you want to set up a Direct Connect to one or more VPC in many different regions (same account), you must use a Direct Connect Gateway.

## Direct Connect - Encryption
- Data in transit is **not encrypted** but is private
- AWS Direct Connect + VPN provides an IPsec-encrypted private connection
- Good for an extra level of security, but slightly more complex to put in place

### Routing Policies
- AWS Direct Connect applies inbound (from your on-premises data center) and outbound (from your AWS Region) routing policies for a public AWS Direct Connect connection. 
- We can also use Border Gateway Protocol (BGP) community tags on routes advertised by Amazon and apply BGP community tags on the routes you advertise to Amazon.

#### Public virtual interface routing policies
- If we're using AWS Direct Connect to access public AWS services, you must specify the public IPv4 prefixes or IPv6 prefixes to advertise over BGP.
- The following inbound routing policies apply:
  - You must own the public prefixes and they must be registered as such in the appropriate regional internet registry
  - Traffic must be destined to Amazon public prefixes. 
  - Transitive routing between connections is not supported.
  - AWS Direct Connect performs inbound packet filtering to validate that the source of the traffic originated from your advertised prefix.
- The following outbound routing policies apply:
  - AWS Direct Connect advertises prefixes with a minimum path length of 3.
  - AWS Direct Connect advertises all public prefixes with the well-known NO_EXPORT BGP community.
  - AS_PATH and Longest Prefix Match is used to determine the routing path, and AWS Direct Connect is the preferred path for traffic sourced from Amazon.
  - AWS Direct Connect advertises all local and remote AWS Region prefixes where available and includes on-net prefixes from other AWS non-Region points of presence       (PoP) where available; for example, CloudFront and Route 53.
  - If we have multiple AWS Direct Connect connections, you can adjust the load-sharing of inbound traffic by advertising prefixes with similar path attributes.

![aws-privatelink](/VPC/images/direct-connect-overview.png)

![aws-privatelink](/VPC/images/dc-high-resiliency.png)

![aws-privatelink](/VPC/images/dc-max-resiliency.png)
