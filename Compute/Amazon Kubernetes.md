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



