# Amazon FSx for Windows

- Amazon FXs are hosted Microsoft Windows file servers.

-  It uses SSD storage to provide fast performance with low latency.

- Fully managed native Microsoft Windows file system with full support for the SMB protocol, Windows NTFS, and Microsoft Active Directory (AD) integration.

- Windows-based SMB file shares can be accessed by Windows, macOS, and Linux hosts.

- FSx is a high-availability service with high-availability single and multiple availability zone options. 

- FSx provides data protection through encryption, both in transit and at rest.

  ![FSx](/compute/images/FSx.png)

### **Use Cases**

- File systems that is accessible by multiple users, and can establish permissions at the file or folder level.
- Application workloads that require shared file storage provided by **Windows-based file systems (NTFS)** and that use the **SMB protocol**.
- Media workflows like media transcoding, processing, and streaming.
- Data-intensive analytics workloads.
- Content management and web serving applications such as IIS

- Works with the following compute services:
  - Amazon EC2
  - Amazon Workspaces instances
  - Amazon AppStream 2.0 instances
  - VMs running in VMWare Cloud on AWS Environments

- Works with Microsoft Active Directory (AD) to integrate your file system with your existing Windows environments.
- Supports the use of AWS Direct Connect or AWS VPN to access your file systems from your on-premises compute instances.
- Microsoft Windows File Share
  - A **Microsoft Windows file share** is a specific folder in your file system, including that folder’s subfolders, which you make accessible to your compute instances with the Server Message Block (SMB) protocol.
  - Your file system comes with a default Windows file share, named *share*. You can create and manage as many other Windows file shares as you want by using the Windows graphical user interface (GUI) tool called Shared Folders.
  - To access your file shares, you use the Windows Map Network Drive functionality to map a drive letter on your compute instance to your Amazon FSx file share.

## **Amazon FSx for Lustre**

- A high-performance file system optimized for fast processing of workloads. Lustre is a popular open-source parallel file system.
- You can choose between SSD storage options and HDD storage options, each offering different levels of performance. The HDD options reduce storage costs by up to 80% for throughput-intensive workloads that don’t require the sub-millisecond latencies of SSD storage.
- Since this is a high-performance parallel file system, you can use Amazon FSx as “hot” storage for your highly accessed files, and Amazon S3 as “cold” storage for rarely accessed files.
- When linked to an S3 bucket, an FSx for Lustre file system transparently presents S3 objects as files and allows you to write results back to S3. 
- The Lustre file system provides a POSIX-compliant file system interface.
- Also supports concurrent access to the same file or directory from thousands of compute instances
