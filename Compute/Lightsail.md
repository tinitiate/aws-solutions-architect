# Lightsail

- A cloud-based virtual private server (VPS) solution.
- Lightsail includes everything we need for websites and web applications :
  - virtual machine (choose either Linux or Windows OS)
  - SSD-based storage
  - Data transfer
  - DNS management 
  - Static IP address.
- Supported Operating Systems
  - Ubuntu
  - Debian
  - FreeBSD
  - OpenSUSE
  - CentOS
  - Windows Server

- Pre-configured Application Stacks
  - WordPress
  - Magento
  - Drupal
  - Joomla
  - Ghost
  - Redmine
  - Plesk
  - cPanel & WHM
  - Django
- Development Stacks
  - Node JS
  - Gitlab
  - LAMP (Linux, MySQL, Apache, PHP)
  - MEAN (MongoDB, ExpressJS, Angular JS, Node JS)
  - Nginx
- We can migrate projects to Amazon EC2 by taking snapshots of the virtual servers and SSD volumes.
- Lightsail CDN, backed by Amazon CloudFront, lets us create and manage content delivery network (CDN) distributions for Lightsail applications.
- Lightsail resources operate in dual-stack mode, accepting both IPv4 and IPv6 client connections. 
- IPv6 is supported on Lightsail resources such as instances, containers, load balancers and CDN. 
- Lightsail also supports firewall rules for IPv6 traffic.

##  Lightsail Features

### Lightsail Load Balancers

- Lightsail’s load balancers route web traffic across your instances so that your websites and applications can accommodate variations in traffic.
- During load balancer creation, we need to specify a path for Lightsail to ping. 
- Lightsail load balancers direct traffic to your healthy target instances based on a round robin algorithm.
- Lightsail supports session persistence for applications that require visitors to hit the same target instances for data consistency.
-  Load balancer does not consume your data transfer allowance.
- Traffic between the load balancer and the target instances is metered and counts towards the data transfer allowance for instances.

### Lightsail Certificates

- Lightsail load balancers include integrated certificate management, providing free SSL/TLS certificates that can be quickly provisioned and added to a load balancer.
-  AWS handles your certificate renewals automatically.
- Lightsail certificates are domain validated, meaning that you need to provide proof of identity by validating that you own or have access to your website’s domain before the certificate can be provisioned by the certificate authority.
- You can add up to 10 domains or subdomains per certificate. Lightsail does not currently support wild card domains.

### Lightsail Instances and Volumes

- Lightsail offers virtual servers (instances) where we can launch website, web application, or project.
- We can choose from a variety of hardware configurations to suit our workloads. 
- Lightsail uses SSD for its virtual servers.
- Each attached disk can be up to 16 TB, and we can attach up to 15 disks per Lightsail instance.
- Lightsail offers automatic and manual snapshots for instances and SSD volumes.

### Managed Databases

- We can launch a fully configured MySQL or PostgreSQL managed database.
- Managed databases are available in Standard and High Availability plans.
- High Availability plans give us redundancy and durability by automatically creating standby database in a separate AZ from the primary database.
- Synchronously replication to the standby database.
- Lightsail automatically encrypts data at rest and in transit for increased security.

## **Limits**

- You can currently create up to 20 Lightsail instances, 5 static IPs, 3 DNS zones, 20 TB of attached block storage, and 5 load balancers in a Lightsail account. 
- You can also generate up to 20 certificates during each calendar year.

## Amazon EC2 and Lightsail

|                                       | **Amazon Lightsail**                                         | **Amazon EC2**                                               |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Usage**                             | Used for simple web applications and websites, including custom code, and common CMS. | Used for small scale to Enterprise applications such as HPC, big data, and analytics workloads. |
| **Performance**                       | Used for applications with workloads ranging from small to medium. | Used for small scale to higher workloads with complex architecture. |
| **Administrative support**            | Less system admin and system architect efforts are needed in Lightsail. | Based on the type of environment, the administrative effort varies. Most of the services in EC2 require a thorough understanding about the components. |
| **Network**                           | Managed by AWS. Customers can add rules to [Lightsail firewall](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-firewall-and-port-mappings-in-amazon-lightsail). | Managed by the customer using VPC and related components.    |
| **Subnets**                           | Lightsail has no concept of private subnets.                 | Customers can create subnets as public or private based on their application needs. |
| **Scalability**                       | Automatic instance scalability isn't supported in Lightsail.  Instances can't be modified after launch. You must launch a new instance to change your plan | Instances can be scaled automatically using an Amazon EC2 Auto Scaling group. EC2 instances can be modified to a new type or to a new virtualization. |
| **Flexibility in managing resources** | Minimal flexibility in managing resources such as network, hard disk, load balancer, and so on. | Customers can manage all the related components based on the application demands. |
| **Elastic volumes**                   | Not supported                                                | Supported                                                    |
| **Resource management**               | All resources are managed from the same dashboard.           | Each resource has its own console and options.               |
| **Pricing**                           | Prices are low and there is a [fixed pricing model](https://aws.amazon.com/lightsail/pricing/). | Pricing follows the pay as you go model.                     |
| **Load balancing**                    | The Lightsail load balancer is available for use with Lightsail instances. | There are multiple types of load balancers available.        |
| **Monitoring**                        | Monitoring is available, but is restricted to a few options. | Detailed monitoring options are available using Amazon Cloudwatch. |
| **Backup**                            | Backups are available by using [Lightsail snapshots](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-instance-snapshots-in-amazon-lightsail). | Backups are available as snapshots and AMIs.                 |
| **Encryption**                        | Encryption is enabled by default and is managed by AWS.      | Customers can choose to enable or disable encryption.        |

**References:**
https://aws.amazon.com/premiumsupport/knowledge-center/lightsail-considerations-for-use/

