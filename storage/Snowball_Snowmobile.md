# AWS Snowball Edge

- A type of Snowball device with on-board storage and compute power for select AWS capabilities. It can undertake local processing and edge-computing workloads in addition to transferring data between your local environment and the AWS Cloud.
- Has on-board S3-compatible storage and compute to support running Lambda functions and EC2 instances.
- Options for device configurations
  - Storage optimized – this option has the most storage capacity at up to 80 TB of useable storage space, 24 vCPUs, and 32 GiB of memory for compute functionality. You can transfer up to 100 TB with a single Snowball Edge Storage Optimized device.
  - Compute optimized – this option has the most compute functionality with 52 vCPUs, 208 GiB of memory, and 7.68 TB of dedicated NVMe SSD storage for instances. This option also comes with 42 TB of additional storage space.
  - Compute Optimized with GPU – identical to the compute optimized option, save for an installed GPU, equivalent to the one available in the P3 Amazon EC2 instance type.

## **Job Types**

- **Import To S3** – transfer of 80 TB or less of your local data copied onto a single device, and then moved into S3.
  - Snowball Edge devices and jobs have a one-to-one relationship. Each job has exactly one device associated with it. If you need to import more data, you can create new import jobs or clone existing ones.
- **Export From S3** – transfer of any amount of data located in S3, copied onto any number of Snowball Edge devices, and then move one Snowball Edge device at a time into your on-premises data destination.
  - When you create an export job, it’s split into job parts. Each job part is no more than 100 TB in size, and each job part has exactly one Snowball Edge device associated with it.
- **Local Compute and Storage Only** – these jobs involve one Snowball Edge device, or multiple devices used in a cluster. This job type is only for local use.
  - A **cluster job** is for those workloads that require increased data durability and storage capacity. Clusters have anywhere from 5 to 10 Snowball Edge devices, called **nodes**.
  - A cluster offers increased durability and increased storage  over a standalone Snowball Edge for local storage and compute.

## **Recommendations**

- Files should be in a static state while being written to the device.
- The *Job created* status is the only status in which you can cancel a job. When a job changes to a different status, it can’t be canceled.
- All files transferred to a Snowball be no smaller than 1 MB in size.
- Perform multiple write operations at one time by running each command from multiple terminal windows on a computer with a network connection to a single Snowball Edge device.
- Transfer small files in batches.

## **Security**

- All data transferred to a device is protected by SSL encryption over the network.
- To protect data at rest, Snowball Edge uses server side-encryption.
- Access to Snowball Edge requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access AWS resources, such an Amazon S3 bucket or an AWS Lambda function.

# SnowMobile

- An **exabyte-scale** data transfer service used to move extremely large amounts of data to AWS. You can transfer up to 100PB per Snowmobile.
- Snowmobile will be returned to your designated AWS region where your data will be uploaded into the AWS storage services you have selected, such as S3 or Glacier.
- Snowmobile uses multiple layers of security to help protect your data including dedicated security personnel:
  - GPS tracking, alarm monitoring
  - 24/7 video surveillance
  - an optional escort security vehicle while in transit
  - All data is encrypted with 256-bit encryption keys you manage through the AWS Key Management Service and designed for security and full chain-of-custody of your data.
- Snowmobile pricing is based on the amount of data stored on the truck per month.


