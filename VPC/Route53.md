# Amazon Route 53

- Every device on the network requires and IP address.
- It’s infeasible to remember every system’s IP address.
- The Domain Name System (DNS) maps a name with an address. Amazon Route 53 is Amazon’s implementation of DNS system.
- Route 53 offers the following functions:
  - Domain name registry.
  - DNS resolution.
  - Health checking of resources.

![DNS](/VPC/images/DNS.png)

## Key Points

- Route 53 provides name to IP address mappings just like any other DNS platform.
- Route 53 is a high-availability platform for DNS services.
-  Route 53 is highly scalable platform for DNS services and server health checks.
-  AWS uses anycast services, for which there are multiple servers with the same address placed over the internet.
-  Anycast provides extremely high availability and low latency. As a host it will connect to the closest DNS server based upon its IP address. If a DNS server were to become unavailable, the host will connect to the next closest Anycast address of the DNS server.
- Route 53 supports most of the available DNS record types.
- Route 53 uses TCP and UDP port 53.
- Route 53 works with health checks and can be used to create a high-availability solution.
- Route 53 supports most DNS record types.
- Route 53 has numerous options to optimize a web-based environment.
- AWS supports the following DNS record types:
  - A (address record)
  - AAAA (IPv6 address record)
  - CNAME (canonical name record)
  - CAA (certification authority authorization)
  - MX (mail exchange record)
  - NAPTR (name authority pointer record)
  - NS (name server record)
  - SOA (start of authority record)
  - SPF (sender policy framework)
  - SRV (service locator)
  - TXT (text record)

### A – Record
- The value for an A record is an IPv4 address in dotted decimal notation.
- A record mapping a name to an IP address.
-  The IPv6 equivalent is an AAAA record.

### AAAA Record Type

- The value for a AAAA record is an IPv6 address in colon-separated hexadecimal format.

### CNAME

- A record that maps a domain to another domain.
- It can map to another CNAME Record or an A record.
- CNAME records effectively redirect a request for one domain to another domain.
- i.e., map www.a.com to www.b.com.

### NS – Record

- Identifies the DNS servers that are responsible for your DNS zone.
- These authoritative name servers propagate an organization’s official DNS information
  to the DNS servers across the internet.
-  NS records can be several entities.

### MX – Record

- Each value for an MX record actually contains two values, priority
  and domain name.
- A MX record specifies which mail servers can accept mail for your domain.
- MX records are necessary to be able to receive email.

| CNAME Records                                                | Alias Records                                                |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Route 53 Charges for the CNAME queries.                      | Route 53 does not charge for the alias queries to AWS recourses. |
| Cannot create CNAME record at the **Zone apex**              | Can create alias record at the **Zone apex**, Alias records must have the same type as the record you’re routing traffic to. |
| A CNAME record redirects queries for a domain name regardless of record type. | Route 53 responds to a DNS query only when the name and type of the alias record matches the name and type in the query. |
| A CNAME record can point to any DNS record that is hosted anywhere. | Can only point to a **CloudFront distribution, Beanstalk environment, ELB, S3 bucket as static website** or to another record in the same hosted zone as the Alias Record. |
| Record appears as a CNAME record in response to dig or Name Server (NS) lookup queries. | An alias record appears as the record type that we specified when you created the record, such as A or AAAA. |

## Traffic Route 

![route-53-route](/VPC/images/route-53-route.png)

## Health Checks

![HealthCheck](/VPC/images/HealthCheck.png)

## Routing Policies

- **Simple routing policy** – route internet traffic to a single resource that performs a given function for your domain. You can’t create multiple records that have the same name and type, but you can specify multiple values in the same record, such as multiple IP addresses.
- **Failover routing policy** – use when you want to configure active-passive failover.
- **Geolocation routing policy** – use when you want to route internet traffic to your resources based on the location of your users.
- **Geoproximity routing policy** – use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
  You can also optionally choose to route more traffic or less to a given resource by specifying a value, known as a bias. A bias expands or shrinks the size of the geographic region from which traffic is routed to a resource.
  The effect of changing the bias for your resources depends on a number of factors,including the following:
  - The number of resources that you have.
  - How close the resources are to one another.
  - The number of users that you have near the border area between geographic regions.
- **Latency routing policy** – use when you have resources in multiple locations and you want to route traffic to the resource that provides the best latency.
- **Multivalue answer routing policy** – use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
- **Weighted routing policy** – use to route traffic to multiple resources in proportions that you specify.
- When you register a domain or transfer domain registration to Route 53, it configures the domain to renew automatically. The automatic renewal period is typically one year,although the registries for some top-level domains (TLDs) have longer renewal periods.
- When you register a domain with Route 53, it creates a hosted zone that has the same name as the domain, assigns four name servers to the hosted zone, and updates the domain to use those name servers.

## Hosted Zones

- Route 53 automatically creates the Name Server (NS) and Start of Authority (SOA)records for the hosted zones.
- Route 53 creates a set of 4 unique name servers (a delegation set) within each hosted zone.
- **Public hosted zone** – route internet traffic to your resources.
- **Private hosted zone** – route traffic within an Amazon VPC. You create a private hosted zone, and specify the VPCs that you want to associate with the hosted zone.
  - To use private hosted zones, you must set the following VPC settings to true:
    - enableDnsHostnames
    - enableDnsSupport
  - In a private hosted zone, you can associate Route 53 health checks only with weighted and failover records.
  - You can use the following routing policies when you create records in a private hosted zone:
    - Simple
    - Failover
    - Multivalue answer
    - Weighted
