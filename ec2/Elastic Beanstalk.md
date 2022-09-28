# Elastic Beanstalk

- AWS Elastic Beanstalk is a service for provisioning, deploying, and scaling web applications and services.
- It is a Platform-as-a-Service
- Elastic Beanstalk provisions and manages the environment while allowing the administrator to manage the environment if desired after the computing platform is deployed.
- Elastic Beanstalk monitors application health and is integrated with CloudWatch logs for performance monitoring.
- There is no additional charge for Elastic Beanstalk. You pay only for the underlying AWS resources that your application consumes.
- Elastic Beanstalk supports the following programming languages:
  - Go
  - Java
  - .NET
  - Node.js
  - PHP
  - Python
  - Ruby
- Elastic Beanstalk supports Docker containers.

![Beanstalk](/ec2/images/clearbox-flow-00.png)

## **Concepts**

- **Application** – a logical collection of Elastic Beanstalk components, including environments, versions, and environment configurations. It is conceptually similar to a folder.
- **Application Version** – refers to a specific, labeled iteration of deployable code for a web application. An application version points to an Amazon S3 object that contains the deployable code. Applications can have many versions and each application version is unique.
- **Environment** – a version that is deployed on to AWS resources. Each environment runs only a single application version at a time, however you can run the same version or different versions in many environments at the same time.
- **Environment Tier** – determines whether Elastic Beanstalk provisions resources to support an application that handles HTTP requests or an application that pulls tasks from a queue. An application that serves HTTP requests runs in a **web server environment**. An environment that pulls tasks from an Amazon SQS queue runs in a **worker environment**.
- **Environment Configuration – identifies a collection of parameters and settings that define how an environment and its associated resources behave.**
- **Saved Configuration** – a starting point for creating unique environment configurations.
- **Platform** – a combination of OS, language runtime, web/application server and Elastic Beanstalk components.
- There is a limit to the number of application versions you can have. You can avoid hitting the limit by applying an *application version lifecycle policy* to your applications to tell Elastic Beanstalk to delete application versions that are old, or to delete application versions when the total number of versions for an application exceeds a specified number.

## **Environment Types**

- Load-balancing, AutoScaling Environment – automatically starts additional instances to accommodate increasing load on your application.
- Single-Instance Environment – contains one Amazon EC2 instance with an Elastic IP address.

### **Environment Configurations**

- Your environment contains:
  - Your **EC2 virtual machines** configured to run web apps on the platform that you choose.
  - An **Auto Scaling group** that ensures that there is always one instance running in a single-instance environment, and allows configuration of the group with a range of instances to run in a load-balanced environment.
  - When you enable load balancing, Elastic Beanstalk creates an **Elastic Load Balancing load balancer** to distributes traffic among your environment’s instances.
  - Elastic Beanstalk provides integration with **Amazon RDS** to help you add a database instance to your Elastic Beanstalk environment : **MySQL, PostgreSQL, Oracle, or SQL Server**. When you add a database instance to your environment, Elastic Beanstalk provides connection information to your application by setting environment properties for the database hostname, port, user name, password, and database name.
  - You can use **environment properties** to pass secrets, endpoints, debug settings, and other information to your application. Environment properties help you run your application in multiple environments for different purposes, such as development, testing, staging, and production.
  - You can configure your environment to use **Amazon SNS** to notify you of important events that affect your application.
  - Your environment is available to users at a **subdomain of elasticbeanstalk.com**. When you create an environment, you can choose a unique subdomain that represents your application.
- You can use a shared Application Load Balancer to serve traffic for multiple applications running on multiple Elastic Beanstalk environments within the same VPC. 
- The connections between your application’s component environments can be specified as named references using **environment links**.
- You can rebuild terminated environments within six weeks of their termination with the same name, ID, and configuration.

### **Deployment policies:**

| Supported deployment policies        |                                 |                              |                                     |
| :----------------------------------- | :------------------------------ | :--------------------------- | :---------------------------------- |
| Deployment policy                    | Load-balanced environments      | Single-instance environments | Legacy Windows Server environments† |
| **All at once**                      | Yes                             | Yes                          | Yes                                 |
| **Rolling**                          | Yes                             | No                           | Yes                                 |
| **Rolling with an additional batch** | Yes                             | No                           | No                                  |
| **Immutable**                        | Yes                             | Yes                          | No                                  |
| **Traffic splitting**                | Yes (Application Load Balancer) | No                           | No                                  |

| Deployment methods                   |                                                              |                                                              |                   |                   |                                             |                            |
| :----------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :---------------- | :---------------- | :------------------------------------------ | :------------------------- |
| **Method**                           | **Impact of failed deployment**                              | **Deploy time**                                              | **Zero downtime** | **No DNS change** | **Rollback process**                        | **Code deployed to**       |
| **All at once**                      | Downtime                                                     | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) | No                | Yes               | Manual redeploy                             | Existing instances         |
| **Rolling**                          | Single batch out of service; any successful batches before failure running new application version | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) † | Yes               | Yes               | Manual redeploy                             | Existing instances         |
| **Rolling with an additional batch** | Minimal if first batch fails; otherwise, similar to **Rolling** | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) † | Yes               | Yes               | Manual redeploy                             | New and existing instances |
| **Immutable**                        | Minimal                                                      | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) | Yes               | Yes               | Terminate new instances                     | New instances              |
| **Traffic splitting**                | Percentage of client traffic routed to new version temporarily impacted | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) †† | Yes               | Yes               | Reroute traffic and terminate new instances | New instances              |
| **Blue/green**                       | Minimal                                                      | ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) ![img](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clock.png) | Yes               | No                | Swap URL                                    | New instances              |

## **Security**

- When you create an environment, Elastic Beanstalk prompts you to provide two AWS IAM roles: 
  - Service role
  - IAM instance profile
  - EC2 key pair
- Service Roles – assumed by Elastic Beanstalk to use other AWS services on your behalf.
- Instance Profiles – applied to the instances in your environment and allows them to retrieve application versions from S3, upload logs to S3, and perform other tasks that vary depending on the environment type and platform.
- User Policies – allow users to create and manage Elastic Beanstalk applications and environments.
