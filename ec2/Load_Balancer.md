# Elastic Load Balancers
- Load balancers are network devices that facilitate load sharing across servers. 
- Load balancers can help greatly with scalability by allowing the application to be deployed across multiple servers. 
- Load balancers can also increase availability by allowing multiple servers to be used simultaneously, removing single points of failure. 
- Load balancers can use health checks to remove unhealthy servers from being used, which further enhances application availability.
- Distributes incoming application or network traffic across multiple targets, such as EC2 instances, containers (ECS), Lambda functions, and IP addresses, 
  in multiple Availability Zones.
- We must specify one public subnet from at least two Availability Zones. 
- We can specify only one public subnet per Availability Zone.
- Accepts incoming traffic from clients and routes requests to its registered targets.
- Monitors the health of its registered targets and routes traffic only to healthy targets.
- Enable deletion protection to prevent your load balancer from being deleted accidentally. Disabled by default.
- Deleting ELB won’t delete the instances registered to it.
- Cross Zone Load Balancing – when enabled, each load balancer node distributes traffic across the registered targets in all enabled AZs.
- Supports SSL Offloading which is a feature that allows the ELB to bypass the SSL termination by removing the SSL-based encryption from the incoming traffic.
- By default, ELB idle timeout value to 60 seconds. 
- We can register each EC2 instance or IP address with the same target group multiple times using different ports, 
  which enables the load balancer to route requests to microservices.
- Listeners define the port and protocol to listen on.
- Listener rules determine how the load balancer routes requests to the targets in one or more target groups. 
- We can add rules that specify different target groups based on the content of the request. 
- If no rules are found, the default rule will be followed. Parts are:
  - Rule priority
  - Rule action
  - Rule conditions
- Slow Start Mode gives targets time to warm up before the load balancer sends them a full share of requests.
- Sticky sessions route requests to the same target in a target group. You enable sticky sessions at the target group level. 
- We can also set the duration for the stickiness of the load balancer-generated cookie, in seconds. Useful if you have stateful applications.

## Types of Load Balancers
1. Application Load Balancer (ALB)
2. Network Load Balancer (NLB)
3. Gateway Load Balancer (GWLB)
4. Classic Load Balancer (CLB)

### Application Load Balancer
- Functions at the application layer, the seventh layer of the Open Systems Interconnection (OSI) model.
- Allows HTTP and HTTPS.
- At least 2 subnets must be specified when creating this type of load balancer.
- We must define a default rule for each listener that specifies a target group, condition, and priority.
- Target group routes requests to one or more registered targets. 
- We can register a target with multiple target groups, and configure health checks on a per target group basis.
- Cross-zone load balancing is always enabled.
- We can also specify Lambda functions are targets to serve HTTP(S) requests.
- Supports path-based and host-based routing.
- Supports for routing requests to multiple applications on a single EC2 instance.
- Supports registering targets by IP address, including targets outside the VPC for the load balancer.
- Supports containerized applications.
- Supports monitoring the health of each service independently.
- Supports redirecting requests from one URL to another.
- Supports returning a custom HTTP response.
- Supports load balancer-generated cookies for sticky sessions.
- Supports Application-based cookie stickiness. This ensures that clients connect to the same load balancer target for the duration of their session 
  using application cookies.
- Supports dual-stack mode. This enables you to create IPv6 target groups and link IPv4 and IPv6 clients to targets in IPv6 or dual-stack subnets.

### Network Load Balancer
- Functions at the fourth layer of the Open Systems Interconnection (OSI) model. Uses TCP and UDP connections.
- At least 1 subnet must be specified when creating this type of load balancer, but the recommended number is 2.
- Cross-zone load balancing is disabled by default.
- If we specify targets using an instance ID, the source IP addresses of the clients are preserved and provided to your applications. 
- If we specify targets by IP address, the source IP addresses are the private IP addresses of the load balancer nodes.
- Network Load Balancers support connections from clients over inter-region VPC peering, AWS managed VPN, and third-party VPN solutions.
- We can deploy services that rely on the UDP protocol, such as Authentication and Authorization, Logging, DNS, and IoT, behind a Network Load Balancer
- Offers multi-protocol listeners, allowing you to run applications such as DNS that rely on both TCP and UDP protocols on the 
  same port behind a Network Load Balancer.
- We cannot enable or disable Availability Zones for a Network Load Balancer after you create it.
- Network Load Balancers use Proxy Protocol version 2 to send additional connection information such as the source and destination.
- Preserves the client-side source IP allowing the back-end to see the IP address of the client. This can then be used by applications for further processing.
- Automatically provides a static IP per Availability Zone (subnet) that can be used by applications as the front-end IP of the load balancer.
- Zonal Isolation
  - In the event that your Network load balancer is unresponsive, integration with Route 53 will remove the unavailable load balancer IP address from service 
    and direct traffic to an alternate Network Load Balancer in another region.
  - Supports TLS termination on Network Load Balancers. Additionally, Network Load Balancers preserve the source IP of the clients to the back-end applications, 
    while terminating TLS on the load balancer.

### Gateway Load Balancer
- Primarily used for deploying, scaling, and running third-party virtual appliances.
- The virtual appliances can be your custom firewalls, deep packet inspection systems, or intrusion detection and prevention systems in AWS
- Uses the Internet Protocol (IP) to pass the OSI Layer 3 traffic to its registered targets.
- GWLB Target groups support the Generic Networking Virtualization Encapsulation (GENEVE) on port: 6081
- Runs within one Availability Zone (AZ)
- We cannot specify publicly routable IP addresses as your target.
- We can provision a Gateway Load Balancer Endpoint that creates a secured, low-latency, connections to and from the virtual appliance.
- Does not support SSL Offloading, Server Name Indication (SNI), Back-end Server Encryption, User Authentication, 
  Custom Security Policy or Application-Layer Protocol Negotiation (ALPN)
  
### Classic Load Balancer
- Distributes incoming application traffic across multiple EC2 instances in multiple Availability Zones.
- For use with EC2 classic only. Register instances with the load balancer. AWS recommends using Application or Network load balancers instead.
- To ensure that your registered instances are able to handle the request load in each AZ, keep approximately the same number of instances in each 
  AZ registered with the load balancer.
- SupportS TCP and SSL listeners
- Classic load balancers are always Internet-facing.

### Monitoring:
- **CloudWatch metrics** – retrieve statistics about data points for your load balancers and targets as an ordered set of time-series data, known as metrics.
- **Access logs** – capture detailed information about the requests made to your load balancer and store them as log files in S3.
- **Request tracing** – track HTTP requests.
- **CloudTrail logs** – capture detailed information about the calls made to the Elastic Load Balancing API and store them as log files in S3.
