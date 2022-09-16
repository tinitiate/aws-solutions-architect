# Elastic File System (EFS)

- EFS is a high-performance, highly scalable file system for networked computers.
- EFS is best used when a **high-performance network file system** is required.
- EFS supports the Network File System version 4 protocol.
- We can mount EFS filesystems onto EC2 instances running **Linux or MacOS Big Sur**. **Windows** is not supported.
- Aside from EC2 instances, you can also mount EFS filesystems on ECS tasks, EKS pods, and Lambda functions.
- There are two versions of EFS:
  - Standard
  - Infrequent

- Standard EFS is the normal version and the highest performance option. 
- EFS-Infrequent access is a lower-cost option for files not accessed frequently.
- EFS has numerous benefits:
  - Scalable – High throughput, high IOPS, high capacity, and low latency.
  - Elastic – EFS will automatically adjust sizing to meet the required storage capacity.
  - Pricing – Pay for what is used.
  - POSIX compatible – This enables access from standard file servers both on premises and on the cloud. Works with traditional NFS-based file permissions and directories

## **Performance Modes**

- General purpose performance mode (default)
  - Ideal for latency-sensitive use cases.
- Max I/O mode
  - Can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for file operations.

### **Throughput Modes**

- Bursting Throughput mode (default)
  - Throughput scales as your file system grows.
- Provisioned Throughput mode
  - You specify the throughput of your file system independent of the amount of data stored.

![EFS](D:\AWS\ec2\EFS.png)