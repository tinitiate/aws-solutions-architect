# AWS Batch

- AWS Batch helps you to run batch computing workloads on the AWS Cloud. 
- AWS Batch automatically provisions compute resources and optimizes the workload distribution based on the quantity and scale of the workloads.
- Regional service that simplifies running batch jobs across multiple AZs within a region.
- Batch manages compute environments and job queues, allowing you to easily run thousands of jobs of any scale using EC2 and EC2 Spot.
- Batch chooses where to run the jobs, launching additional AWS capacity if needed.
- Batch carefully monitors the progress of your jobs. When capacity is no longer needed, it will be removed.
- There is no additional charge for AWS Batch. You pay for resources you create to store and run your application.

## Components of AWS Batch

### Jobs

- A unit of work (such as a shell script, a Linux executable, or a Docker container image) that you submit to AWS Batch.

- Runs as a containerized application on AWS Fargate or Amazon EC2 resources in your compute environment.

- We can configure a timeout duration for your jobs so that if a job runs longer than that, AWS Batch terminates the job,

  By default, AWS Batch doesn't have a job timeout.

- Jobs can reference other jobs by name or by ID, and can be dependent on the successful completion of other jobs.

- We can apply a retry strategy to jobs and job definitions that allows failed jobs to be automatically retried. 

- Possible failure scenarios include:

  - Any non-zero exit code from a container job
  - Amazon EC2 instance failure or termination
  - Internal AWS service error or outage

- Job types

  - **Single for single Job**
  - **Array** for array Job of size 2 to 10,000

- An **Array job** shares common job parameters, such as the job definition, vCPUs, and memory. It runs as a collection of related, yet separate, basic jobs that may be distributed across multiple hosts and may run concurrently.

- **Multi-node parallel jobs** enable you to run single large-scale, tightly coupled, high performance computing applications and distributed GPU model training jobs that span multiple Amazon EC2 instances.

  - Batch lets you specify up to five distinct node groups for each job. Each group can have its own container images, commands, environment variables, and so on.
  - Each multi-node parallel job contains a *main node*, which is launched first. After the main node is up, the *child nodes* are launched and started. If the main node exits, the job is considered finished, and the child nodes are stopped.
  - Not supported on compute environments that use Spot Instances.

- **Dependencies**

  - A job may have up to 20 dependencies.
  - For **Job depends on**, enter the job IDs for any jobs that must finish before this job starts.
  - (Array jobs only) For **N-To-N job dependencies**, specify one or more job IDs for any array jobs for which each child job index of this job should depend on the corresponding child index job of the dependency.
  -  **Run children sequentially** creates a SEQUENTIAL dependency for the current array job. 

### **Job Definitions**

- Specifies how jobs are to be run.
- The definition can contain:
  - An IAM role to provide programmatic access to other AWS resources.
  - Memory and CPU requirements for the job.
  - Controls for container properties, environment variables, and mount points for persistent storage.

### **Job Queues**

- This is where a Batch job resides until it is scheduled onto a compute environment.
- You can associate one or more compute environments with a job queue.
- You can assign priority values for the compute environments and even across job queues themselves.
- The **Batch Scheduler** evaluates when, where, and how to run jobs that have been submitted to a job queue. Jobs run in approximately the order in which they are submitted as long as all dependencies on other jobs have been met.

### **Compute Environment**

- A set of managed or unmanaged compute resources (such as EC2 instances) that are used to run jobs.
- Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.
- A given compute environment can be mapped to one or many job queues.
- **Managed Compute Environment:**
  - Batch manages the capacity and instance types of the compute resources within the environment, based on the compute resource specification that you define when you create the compute environment.
  - You can choose to use EC2 On-Demand Instances or Spot Instances in your managed compute environment.
  - ECS container instances are launched into the VPC and subnets that you specify when you create the compute environment.
- **Unmanaged Compute Environment:**
  - You manage your own compute resources in this environment.
  - After you have created your unmanaged compute environment, use the DescribeComputeEnvironments API operation to view the compute environment details and find the ECS cluster that is associated with the environment and manually launch your container instances into that cluster.