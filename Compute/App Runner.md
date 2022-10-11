# AWS App Runner
- Service that provides a fast, simple, and cost-effective way to deploy from source code or a container image directly 
  to a scalable and secure web application in the AWS Cloud.
- App Runner connects directly to your code or image repository.
- Provides an automatic integration and delivery pipeline with fully managed operations, high performance, scalability, and security.
- App Runner enables automatic deployments each time a commit is pushed to the code repository or a new container image version is pushed to the image repository.

 ![app-deploy-lifecycle](/compute/images/app-deploy-lifecycle.png)

## Key Concepts
- **App Runner service** – An AWS resource that App Runner uses to deploy and manage application based on its source code repository or container image.
- **Source type** – The type of source repository that you provide for deploying your App Runner service.
- **Repository provider** – Repository service that contains application source.
- **App Runner connection** – AWS resource that lets App Runner access a repository provider account.
- **Runtime** – A base image for deploying a source code repository. 
- **Deployment** – An action that applies a version of your source repository to an App Runner service. The first deployment to the service occurs as part of service creation. Later deployments can occur in one of two ways:
  - Automatic deployment – A CI/CD capability. You can configure an App Runner service to automatically build (for source code) and deploy each version of your         application as it appears in the repository. This can be a new commit in a source code repository or a new image version in a source image repository.
  - Manual deployment – A deployment to your App Runner service that you explicitly start.

## Resources
| **Resource name**          | **Description**                                                                                                                                                                                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service                    | Represents a running version of your application. Much of the rest of this guide describes service types, management, configuration, and monitoring. ARN: ``arn:aws:apprunner:`region`:`account-id`:service/`service-name`[/`service-id`]``                                                           |
| Connection                 | Provides your App Runner services with access to private repositories stored with third-party providers. Exists as a separate resource for sharing across multiple services. ARN: ``arn:aws:apprunner:`region`:`account-id`:connection/`connection-name`[/`connection-id`]``                          |
| AutoScalingConfiguration   | Provides your App Runner services with settings that control the automatic scaling of your application. Exists as a separate resource for sharing across multiple services. ARN: ``arn:aws:apprunner:`region`:`account-id`:autoscalingconfiguration/`config-name`[/`config-revision`[/`config-id`]]`` |
| ObservabilityConfiguration | Configures additional application observability features for your App Runner services. Exists as a separate resource for sharing across multiple services. ARN: ``arn:aws:apprunner:`region`:`account-id`:observabilityconfiguration/`config-name`[/`config-revision`[/`config-id`]]``                |
| VpcConnector               | Configures VPC settings for your App Runner services. Exists as a separate resource for sharing across multiple services. ARN: ``arn:aws:apprunner:`region`:`account-id`:vpcconnector/`connector-name`[/`connector-revision`[/`connector-id`]]``                                                      |
