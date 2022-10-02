# Amazon Elastic Compute Cloud

- Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud.
- With Amazon EC2 you launch virtual server instances on the AWS cloud. Each virtual server is known as an “instance”.
- A Linux-based/Windows-based/Mac-based virtual server that you can provision.
- We are limited to running On-Demand Instances per your vCPU-based On-Demand Instance limit, purchasing 20 Reserved Instances, and requesting Spot Instances per your dynamic Spot limit per region.
- We use preconfigured templates for your instances known as Amazon Machine Images (AMIs).
- Each AMI includes the information needed to launch your EC2 instance (including the operating system and any included software packages).

## Instance Types

- The instance type defines the virtual hardware supporting an Amazon EC2 instance.
- here are dozens of instance types available, varying in the following dimensions:

  - Virtual CPUs (vCPUs)
  - Memory
  - Storage (size and type)
  - Network performance
- Instance types are grouped into families based on the ratio of these values to each other.
- The network performance increases within a family as the instance type grows.
- Every instance type can be ordered in various sizes.
- Table below lists some of the families available:

| Family |             Specialty             |               **Use Cases**               |
| :----- | :--------------------------------- | :----------------------------------------------- |
|   A1   |        Arm-based Workloads        |                   Web Servers                   |
|   C5   | Compute Optimized Batch Processing |       Batch Processing, Media Transcoding       |
|   G3   |        GPU Based Workloads        |                 Machine Learning                 |
|   I3   |         High Speed Storage         |   Data Warehousing, High Performance Databases   |
|   M5   |          General Purpose          |                    Databases                    |
|   M6   |          General Purpose          |       Application Servers, Gaming Servers       |
|   R5   |          Memory Optimized          |        Caches, High Performance Databases        |
|   T3   |    Burstable Computing Platform    |           Web apps, Test Environments           |
|   X1   |     Lowest Pricing Per GB DRAM     | Bid Data Processing Engines, In-Memory Databases |

## Amazon Machine Images (AMIs)

- The Amazon Machine Image (AMI) defines the initial software that will be on an instance when it is launched.
- AMI’s are regional. We can only launch an AMI from the region in which it was stored.
- When you create an AMI, by default its marked private. We have to manually change the permissions to make the image public or share images with individual accounts
- An AMI defines every aspect of the software state at instance launch:

  - The Operating System (OS) and its configuration.
  - The initial state of any patches.
  - Application or system software.
- AMI Includes :

  - A template for the root volume for the instance (OS, application server, and applications).
  - Launch permissions that control which AWS accounts can use the AMI to launch instances.
  - A block device mapping that specifies the volumes to attach to the instance when it’s launched.

    ![ami_lifecycle](/compute/images/ami_lifecycle.png)

    |        Characteristic        |                                                                Amazon EBS-backed AMI                                                                |                         Amazon instance store-backed AMI                         |
    | :--------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
    |  Boot time for an instance  |                                                             Usually less than 1 minute                                                             |                            Usually less than 5 minutes                            |
    | Size limit for a root device |                                                                      64 TiB**                                                                      |                                      10 GiB                                      |
    |      Root device volume      |                                                                     EBS volume                                                                     |                               Instance store volume                               |
    |       Data persistence       | By default, the root volume is deleted when the instance terminates.* Data on any other EBS volumes persists after instance termination by default. | Data on any instance store volumes persists only during the life of the instance. |
    |        Modifications        |                          The instance type, kernel, RAM disk, and user data can be changed while the instance is stopped.                          |            Instance attributes are fixed for the life of an instance.            |
    |           Charges           |                            You're charged for instance usage, EBS volume usage, and storing your AMI as an EBS snapshot.                            |       You're charged for instance usage and storing your AMI in Amazon S3.       |
    |    AMI creation/bundling    |                                                             Uses a single command/call                                                             |                    Requires installation and use of AMI tools                    |
    |        Stopped state        |              Can be in a stopped state. Even when the instance is stopped and not running, the root volume is persisted in Amazon EBS              |         Cannot be in a stopped state; instances are running or terminated         |
- Sources of AMIs:

  - Published by AWS.
  - The AWS Marketplace (online store for AMI).
  - Generated from Existing Instances.
  - Uploaded Virtual Servers (Using AWS VM Import/Export service).Automating the First Boot for EC2 Instances
- **Automating the First Boot for EC2 Instances:**

  - There are two possible ways to take an AMI and configure it for an organization’s use.
    1. The first option is to launch the EC2 instance with the premade AMI. After the instance boots, manually update the operating system and then install necessary services.
    2. Instance can be automatically updated upon boot with a bootstrap script. Bootstrap scripts for Linux can be as simple as a basic shell script. Windows systems can be bootstrapped with a power shell script.

## Instance Lifecycle

- When we launch an instance, it enters the pending state and it uses the specified AMI to launch.
- It  enters the running stat where you can start connecting to it and use it.
- We can stop and start your instance to try to fix a problem. When we stop our instance, it enters the stopping state and then the stopped state.
- if we no longer need an instance, you can terminate it. As soon as the status of an instance changes to shutting-down or terminated, we stop incurring charges for that instance.
- If we enable termination protection, we can’t terminate the instance using the console, CLI, or API.
- Termination protection does not work for instances that are part of the auto-scaling group, launched as Spot instance or when terminated by initiating shutdown command.
- Data on an instance store is lost when the instance is stopped or terminated.Instance store data survives an OS reboot.
- An instance is scheduled to be retired when AWS detects an irreparable failure of the underlying hardware hosting the instance

### Instance States

| Instance State |                                                            Description                                                            |                         Billed                         |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
|    Pending    | An instance enters the pending state when it launches for the first time, or when it is started after being in the stopped state. |                           No                           |
|    Running    |                                            The instance is running and ready for use.                                            |                          Yes                          |
|    Stopping    |                                    The instance is preparing to be stopped or stop-hibernated.                                    | No if preparing to stop, Yes if preparing to hibernate |
|    Stopped    |                                           The instance is shut down and cannot be used.                                           |                           No                           |
| Shutting-Down |                                            The instance is preparing to be terminated.                                            |                           No                           |
|   Terminated   |                                             The instance has been permanently deleted                                             |                           No                           |

![instance_lifecycle](/compute/images/instance_lifecycle.png)

## Root device volumes

- Root Volumes cannot be encrypted by default, you need a 3rd party utility. Other volumes added to an instance can be encrypted.
- Non-root EBS volumes attached to the instance are preserved if we delete the instance.
- Amazon EC2 supports two types of block devices:
  - Instance Store (Ephemeral)
  - Amazon Elastic Block Store (EBS)

### Instance Store

- Not **persistent storage**.
- Instance store is ideal for temporary storage of information that changes frequently ,such as buffers, caches, scratch data.
- Instances using instance store storage cannot be stopped.
- Instance store volumes cannot be detached and reattached to other instances; They exist only for the life of that instance.
- If we change the instance type, an instance store will not be attached to the new instance type.

### Amazon Elastic Block Store

- For workloads requiring more durable block storage , Amazon EBS is the right choice.
- Each Amazon EBS volume is automatically replicated within its Availability Zone to protect you from component failure, offering high availability and durability.
- Multiple Amazon EBS volumes can be attached to a single EC2instance , although a volume can only be attached to a single instance at a time.
- Types of EBS Volumes :
  - General-Purpose SSD.
  - Provisioned IOPS SSD.
  - Throughput Optimized HDD.
  - Cold HDD.

#### General-Purpose SSD

- Ideal for a broad range of workloads.
- Volume can range in size from 1 GB to 16 TB, up to 16,000 IOPS per volume.
- Some of the use cases:
  - System boot volumes.
  - Virtual desktops.
  - Small-to-medium sized databases.
  - Development and test environments.
- General-purpose SSD volumes are billed based on the amount of **data space** provisioned.

#### Provisioned IOPS SSD

- Designed to meet the needs of **I/O-intensive workloads** , particularly database workloads.
- Provide the **highest performance** of any Amazon EBS.
- Volume can range in size from 4 GB to 16 TB, Consistently performs at provisioned level, up to
- 64,000 IOPS maximum per volume.
- The **most expensive** Amazon EBS volume type per gigabyte.

#### Throughput Optimized HDD

- Designed for frequently accessed, throughput-intensive workloads.
- Low-cost HDD volume.
- volume can range in size from 500 GiB to 16 TiB , max IOPS per volume is 500.
- use cases:
  - Streaming workloads requiring consistent, fast throughput at a low price.
  - Big data, Data warehouses, Log processing.
- **Cannot be a boot volume**.

#### Cold HDD

- **Lowest cost** HDD volume designed for less frequently accessed workloads.
- volume can range in size from 500 GiB to 16 TiB , max IOPS per volume is 250.
- Scenarios where the **lowest storage cost is important**.
- **Cannot be a boot volume**.

## Pricing

### On-Demand

- No long-term commitments or upfront payments.
- On-demand instances are charged by either the second or hour of use, and facilitate autoscaling.
- On-demand instances are optimal when reliable computing capacity is needed without complete knowledge of how long the application will be used or its capacity requirements.

### Reserved

- Reserved instance is an instance where an organization commits to purchase a specified compute capacity for a specified period of time.
- Contract term is one to three years.
  - It has two offering classes:
    - Standard
    - Convertible.
  - The Standard class provides the most significant discount but you can only modify some of its attributes during the term. It can also be sold in the Reserved Instance Marketplace.
  - The Convertible class provides a lower discount than Standard Reserved Instances, but can be exchanged for another Convertible Reserved Instance with different instance attributes. However, this one cannot be sold in the Reserved Instance Marketplace.
- Reserved instances are optimal when an organization knows how long the application will be used and its capacity requirements.

### Spot

- Spot instance is an instance that is pulled from unused AWS capacity.
- Spot instances are deeply discounted and can be a great option.
- Spot Instances are available at up to a 90% discount compared to On-Demand prices.
- We  can use Spot Instances for various stateless, fault-tolerant, or flexible applications such as big data, containerized workloads, CI/CD, web servers, high-performancecomputing (HPC), and other test & development workloads.
- The drawback of spot instances is that they can be terminated if the spot price exceeds our maximum price.
- Spot instances are ideal when an organization needs extra computing capacity at a great price for non-mission-critical use.

  - Spot Instances with a defined duration (also known as Spot blocks ) are designed not to be interrupted and will run continuously for the duration we select. This makes them ideal for jobs that take a finite time to complete, such asbatch processing, encoding and rendering, modeling and analysis, and continuous integration.
  - A Spot Fleet is a collection of Spot Instances and optionally On-Demand Instances. The service attempts to launch the number of Spot Instances and On-Demand Instances to meet your specified target capacity. The request for Spot Instances is fulfilled if there is available capacity and the maximum price we specified in the request exceeds the current Spot price. The Spot Fleet also attempts to maintain its target capacity fleet if your Spot Instances are interrupted.
  - A Spot Instance pool is a set of unused EC2 instances with the same instance type, operating system, Availability Zone, and network platform.
    You can start and stop your Spot Instances backed by Amazon EBS at will.
  - We can modify instance types and weights for a running EC2 Fleet or Spot Fleet without having to recreate it.
  - Allocation strategy for Spot Instances

    - LowestPrice

      - The Spot Instances come from the pool with the lowestprice. This is the default strategy.
    - Diversified.

      - The Spot Instances are distributed across all pools.
    - CapacityOptimized

      - The Spot Instances come from the pool withoptimal capacity for the number of instances that are launching.
    - InstancePoolsToUseCount

      - The Spot Instances are distributed across the number of Spot pools that you specify. This parameter is valid only when used in combination with the lowest Price.
        |                          | Spot Instances                                               | On-Demand Instances                                          |
        | :----------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
        | Launch  Time             | Can only be launched immediately if the Spot Request is active and capacity is available. | Can only be launched immediately if we make a manual launch request and capacity is available. |
        | Available Capacity       | Spot Request continues to automatically make the launch request until the capacity is available. | We will get an insufficient capacity error if capacity is not avialable. |
        | Hourly Price             | Varies based on demand.                                      | static.                                                      |
        | Rebalance recommendation | The signal that EC2 emits for a running Spot instance is at an elevated risk of interruption. | We determine when an instance is interrupted.                |
        | Instance interruption    | We can stop and start an EBS backed instance. EC2 Spot service can interrupt an individual Spot Instance if capacity is no longer available, Spot price exceeds our maximum price or demand for Spot instances increases. | We determine when an instance is interrupted.                |

## **Tenancy Options**

- The tenancy, or where the instances are located, can make a substantial impact on performance and availability. The tenancy options are:
  - Shared tenancy
  - Dedicated instances
  - Dedicated hosts
  - Placement groups

### Shared Tenancy

- With shared tenancy, the physical server hosted at AWS will contain virtual machines for several customers.

### Dedicated Instance

- Dedicated host is a dedicated server.
- Bare metal server is a physical server without an operating system or applications installed.
- We can install any operating system or application required.
- Dedicated hosts are optimal when an organization needs access to system-level information, such as actual CPU usage.
- Dedicated hosts are an excellent option when an application that has a license that is dedicated to a physical machine.

#### Dedicated Host

- Bare metal server and is dedicated to a single customer.

### **Placement Groups**

- We can launch or start instances in a placement group, which determines how instances are placed on underlying hardware.
- Partition placement groups is an Amazon EC2 placement strategy that helps reduce the likelihood of correlated failures for large distributed and replicated workloads such as HDFS, HBase and Cassandra running on EC2.
- Partition placement groups spread EC2 instances across logical partitions and ensure that instances in different partitions do not share the same underlying hardware. In addition, partition placement groups offer visibility into the partitions and allow topology aware applications to use this information to make intelligent data replication decisions, increasing data availability and durability.

#### Cluster

- Clusters instances into a low-latency group in a single Availability Zone.
- Recommended for applications that benefit from low network latency, high network throughput, or both, and if the majority of the network traffic is between the instances in the group.

#### Spread

- Spreads instances across underlying hardware.
- Recommended for applications that have a small number of critical instances that should be kept separate from each other.
- Note: A spread placement group can span multiple Availability Zones, and you can have a maximum of seven running instances per Availability Zone per group.

#### Rules

- The name you specify for a placement group must be unique within your AWS account for the region.
- You can’t merge placement groups.
- An instance can be launched in one placement group at a time; it cannot span multiple placement groups.
- Instances with a tenancy of host cannot be launched in placement groups.

## Metadata and User Data

- User data is data that is supplied by the user at instance launch in the form of a script.
- Instance metadata is data about your instance that you can use to configure or managethe running instance.
- User data is limited to 16KB.
- User data and metadata are not encrypted.
- Instance metadata is available at : http://169.254.169.254/latest/meta-data/ (the trailing“/” is required).
- Instance user data is available at: http://169.254.169.254/latest/user-data.
- The IP address 169.254.169.254 is a link-local address and is valid only from the instance.
- The Instance Metadata Query tool allows you to query the instance metadata without having to type out the full URI or category names.
- On Linux you can use the curl command to view metadata and userdata, e.g.

  ```
  “curl http://169.254.169.254/latest/meta-data/”.
  ```
