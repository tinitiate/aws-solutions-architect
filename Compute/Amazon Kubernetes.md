# Amazon Elastic Kubernetes Service

- The Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service for running Kubernetes on AWS and on-premises.
- Amazon EKS can run on Amazon EC2 or AWS Fargate.
- Integrates with Application Load Balancers, AWS IAM for RBA and Amazon VPC.
- Amazon EKS provides a scalable and highly available Kubernetes control plane running across multiple AWS Availability Zones (AZs).
- Amazon EKS automatically manages availability and scalability of Kubernetes API servers and etcd persistence layer.
- Amazon EKS runs the Kubernetes control plane across three AZs to ensure high availability, and automatically detects and replaces unhealthy control plane nodes.
- Integration with various AWS services to provide scalability and security for your applications:
  - Amazon ECR for container images
  - Elastic Load Balancing for load distribution
  - IAM for authentication
  - Amazon VPC for isolation
## Clusters
 - EKS cluster uses IAM / OIDC for authentication and Kubernetes RBAC for authorization.
 - An EKS cluster has two main components:
   - EKS control plane
   - EKS nodes   
 - By default, the API server endpoint is public, but you can enable private access to keep communication between nodes and the API server within the VPC.
 - CloudWatch Logs does not receive cluster control plane logs by default; you must enable each log type individually.
 - EKS supports two types of autoscaling:
   - Cluster Autoscaler – uses AWS Auto Scaling groups.
   - Karpenter – works directly with the Amazon EC2 Fleet.
### Control Pane
 - An EKS Control Panel is formed by nodes that run the Kubernetes API server and EKS daemon.
 - The clusters are single-tenant and unique, and each runs on its own EC2 instance.
 - Cluster control planes are distributed across multiple AZs and backed up by ELB Network Load Balancers.
 - Use AWS KMS to encrypt data stored by etcd nodes and associated EBS volumes.
### EKS nodes
 - A cluster consists of one or more EC2 nodes on which pods are scheduled.
 - Connects to the cluster’s control plane via the API server endpoint.
## Nodes
 - Nodes must be in the same VPC as the subnets when creating a cluster.
 - Nodes represent the compute resources provisioned for cluster.
 - Taints and tolerations prevent pods from being scheduled on the wrong nodes.
### Self-managed nodes
 - Cluster can have several node groups.
 - Node groups are collections of Amazon EC2 instances deployed in Amazon EC2 Auto Scaling groups.
 - Node group instances must have the following :
   - Same instance type
   - Same AMI
   - Same EKS node IAM role
 - Node groups with different instance types and host operating systems can exist in a cluster.
 - In a cluster, self-managed node groups can be updated using two methods:
   - Migrating to a new node group
   - Updating an existing self-managed node group
### Managed node groups
 - Automates the provisioning and lifecycle management of nodes in EKS clusters.
 - Every managed node is provisioned as part of Amazon EC2 Auto Scaling group.
 - When nodes are launched as part of a managed node group, they are automatically tagged for auto-discovery by Kubernetes Cluster Autoscaler.
 - Use node group to apply Kubernetes labels to nodes.
 - Multiple managed node groups can exist in a single cluster.
 - When you create a managed node group, you have the option of selecting On-Demand or Spot instances.
 - To ensure that your applications remain available, node updates and terminations drain nodes automatically.
### AWS Fargate
 - You must first define a Fargate profile before scheduling pods on Fargate in your cluster.
 - If a pod matches more than one Fargate profile, Amazon EKS picks one at random.
 - Fargate profiles are immutable and contains the following components:
   - Pod execution role
   - Subnets
   - Selectors
   - Namespace
   - Labels
- Fargate runs only one pod per node.
- Pod storage is ephemeral, and data is encrypted with AWS Fargate managed keys.
- To encrypt ephemeral pod storage, you can use AWS Fargate managed keys.
## Workloads
 - Workloads are deployed in containers and defines the applications that run on a Kubernetes cluster.
 - A pod can contain one or more containers.
 - Vertical Pod Autoscaler adjusts your pods’ CPU and memory reservations.
 - Horizontal Pod Autoscaler adjusts the number of pods in a deployment, replication controller, or replica set based on CPU utilization.
## EKS Connector
 - Enables you to register and connect any Kubernetes cluster to AWS.
 - You can view the status, configuration, and workloads of the cluster in the Amazon EKS console after it has been connected.
## Storage
 - Kubernetes' Container Storage Interface (CSI) allows third-party storage providers to develop and deploy plugins that provide 
   alternative storage without altering the core code.
 - Amazon EBS CSI driver.
   - The lifecycle of persistent volumes, such as EBS volumes, is handled by EKS clusters.
   - To make calls to AWS APIs, the EBS CSI plugin requires IAM permissions.
   - Although the Amazon EBS CSI controller can be run on Fargate, volumes cannot be mounted to Fargate pods.
   - You can also manage the EBS CSI driver as an EKS add-on.
 - Amazon EFS CSI driver
   - EKS clusters manage the EFS file system lifecycle.
   - Container images based on Windows are incompatible with the EFS CSI driver.
   - Fargate nodes only support static provisioning.
   - A pod running on Fargate automatically mounts an EFS file system.
 - Amazon FSx for Lustre CSI driver
   - EKS clusters can also manage the lifecycles of FSx file systems.
   - Fargate does not support the Lustre CSI driver.
 - Amazon FSx for NetApp ONTAP CSI driver.
   - A storage service to fully managed ONTAP file systems in the cloud.



