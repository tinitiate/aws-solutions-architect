# Amazon Elastic Container Registry (ECR)

- Amazon Elastic Container Registry (ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.
- Amazon ECR is a regional service.
- ECR supports Docker Registry HTTP API V2 allowing you to use Docker CLI commands or your preferred Docker tools in maintaining your existing development workflow.
- ECR stores your container images in Amazon S3.
- ECR supports the ability to define and organize repositories in your registry using namespaces.
- You can transfer your container images to and from Amazon ECR via HTTPS.
- Amazon ECR hosts your images in a highly available and scalable architecture, allowing you to reliably deploy containers for your applications.
- Integration with AWS Identity and Access Management (IAM) provides resource-level control of each repository.

# Elastic Container Service

- Amazon Elastic Container Service (Amazon ECS) is a highly scalable and fast container management service, supports Docker containers.
- Amazon ECS is a regional service.
- Amazon ECS eliminates the need for you to install, operate, and scale your own cluster management infrastructure.
- There is no additional charge for Amazon ECS. You pay for:
  - Resources created with the EC2 Launch Type (e.g. EC2 instances and EBS volumes).
  - The number and configuration of tasks you run for the Fargate Launch Type.

- AWS Compute SLA guarantees a Monthly Uptime Percentage of at least 99.99% for Amazon ECS.

## Launch Types

An Amazon ECS launch type determines the type of infrastructure on which your tasks and services are hosted.

There are two launch types, and the table below describes some of the differences between the two launch types:

| **Amazon EC2**                                               | **Amazon Fargate**                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| You can explicitly provision EC2 instances                   | The control plan asks for resources and Fargate automatically provisions |
| You’re responsible for upgrading, patching, care of EC2 pool | Fargate provisions compute as needed                         |
| You must handle cluster optimization                         | Fargate handles customer optimizations                       |
| More granular control over infrastructure                    | Limited control, as infrastructure is automated              |

### Fargate Launch Type

- The Fargate launch type allows you to run your containerized applications without the need to provision and manage the backend infrastructure. 
- Fargate Launch Type is a serverless infrastructure managed by AWS.
- Fargate only supports container images hosted on Elastic Container Registry (ECR) or Docker Hub.

### EC2 Launch Type

- The EC2 launch type allows you to run your containerized applications on a cluster of Amazon EC2 instances that you manage.
- Private repositories are only supported by the EC2 Launch Type.

## Terminology

| **Amazon ECS Term** | **Definition**                                               |
| ------------------- | ------------------------------------------------------------ |
| Cluster             | Logical Grouping of EC2 Instances                            |
| Container Instance  | EC2 instance running the ECS agent                           |
| Task Definition     | Blueprint that describes how a docker container should launch |
| Task                | A running container using settings in a Task Definition      |
| Service             | Defines long running tasks – can control task count with Auto Scaling and attach an ELB |

## Clusters

- ECS Clusters are a logical grouping of container instances that you can place tasks on.

- A default cluster is created but you can then create multiple clusters to separate resources.

- ECS allows the definition of a specified number (desired count) of tasks to run in the cluster.

- Clusters can contain tasks using the Fargate and EC2 launch type.

- For clusters with the EC2 launch type clusters can contain different container instance types.
- Each container instance may only be part of one cluster at a time.
- “Services” provide auto-scaling functions for ECS.
- You can create IAM policies for your clusters to allow or restrict users’ access to specific clusters.
- Before you can delete a cluster, you must delete the services and deregister the container instances inside that cluster.
- Enabling managed Amazon ECS cluster auto scaling allows ECS to manage the scale-in and scale-out actions of the Auto Scaling group.

## Services
- ECS allows you to run and maintain a specified number of instances of a task definition simultaneously in a cluster.
- In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind a load balancer.
- There are two deployment strategies in ECS:
  - **Rolling Update**
    - This involves the service scheduler replacing the current running version of the container with the latest version.
    - The number of tasks ECS adds or removes from the service during a rolling update is controlled by the deployment configuration.
  - **Blue/Green Deployment with AWS CodeDeploy**
    - This deployment type allows you to verify a new deployment of a service before sending production traffic to it.
    - The service must be configured to use either an Application Load Balancer or Network Load Balancer.

## ECS Container Agent

- The ECS container agent allows container instances to connect to the cluster.
- The container agent runs on each infrastructure resource on an ECS cluster.
- The ECS container agent is included in the Amazon ECS optimized AMI and can also be installed on any EC2 instance that supports the ECS specification (only supported on EC2 instances).
- Linux and Windows based.
- For non-AWS Linux instances to be used on AWS you must manually install the ECS container agent.

## Containers and Images

- Your application components must be architected to run in containers.
- Containers are created from a read-only template called an image.
- Images are typically built from a  **Dockerfile**, a plain text file that specifies all of the components that are included in the container. These images are then stored in a registry from which they can be downloaded and run on your cluster.
- When you launch a container instance, you have the option of passing user data to the instance. The data can be used to perform common automated configuration tasks and even run scripts when the instance boots.
- Docker Volumes can be a local instance store volume, EBS volume or EFSvolume. Connect your Docker containers to these volumes using Docker drivers and plugins.

## **Task definitions**

- Specify various parameters for your application. It is a text file,in JSON format, that describes one or more containers, up to a maximum of ten,that form your application.
- Task definitions are split into separate parts:
  - Task family – the name of the task, and each family can have multiple revisions.
  - IAM task role – specifies the permissions that containers in the task should have.
  - Network mode – determines how the networking is configured for your containers.
  - Container definitions – specify which image to use, how much CPU and memory the container are allocated, and many more options.
  - Volumes – allow you to share data between containers and even persist the data on the container instance when the containers are no longer running.
  - Task placement constraints – lets you customize how your tasks are placed within the infrastructure.
  - Launch types – determines which infrastructure your tasks use.

### Task Definitions for Fargate Launch Type

- Fargate task definitions require that the network mode is set to awsvpc. The awsvpc network mode provides each task with its own elastic network interface.
- Fargate task definitions require that you specify CPU and memory at the task level.
- Fargate task definitions only support the awslogs log driver for the log configuration. This configures your Fargate tasks to send log information to Amazon CloudWatchLogs.
- Task storage is ephemeral.
- Amazon ECS tasks running on both Amazon EC2 and AWS Fargate can mount Elastic File System (EFS) file systems.
- Put multiple containers in the same task definition if:
  - Containers share a common lifecycle.
  - Containers are required to be run on the same underlying host.
  - You want your containers to share resources.
  - Your containers share data volumes.

### Task Definitions for EC2 Launch Type
- Create task definitions that group the containers that are used for a common purpose,and separate the different components into multiple task definitions.
- After you have your task definitions, you can create services from them to maintain theavailability of your desired tasks.
- For EC2 tasks, the following are the types of data volumes that can be used:
  - Docker volumes
  - Bind mounts
- Private repositories are only supported by the EC2 Launch Type.

