# Amazon Elastic Container Registry (ECR)

- Amazon Elastic Container Registry (ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.
- Amazon ECR is a regional service.
- ECR supports Docker Registry HTTP API V2 allowing you to use Docker CLI commands or your preferred Docker tools in maintaining your existing development workflow.
- ECR stores your container images in Amazon S3.
- ECR supports the ability to define and organize repositories in your registry using namespaces.
- You can transfer your container images to and from Amazon ECR via HTTPS.
- Amazon ECR hosts your images in a highly available and scalable architecture, allowing you to reliably deploy containers for your applications.
- Integration with AWS Identity and Access Management (IAM) provides resource-level control of each repository.

## Registry
- A registry is provided to each AWS account; you can create image repositories in your registry and store images in them.
- The URL for your default registry is https://aws_account_id.dkr.ecr.region.amazonaws.com.
- You must be authenticated before you can use your registry.
## Authorization token
- Docker client needs to authenticate to ECR registries as an AWS user before it can push and pull images. 
- The AWS CLI get-login command provides you with authentication credentials to pass to Docker.
## Repository
- An image repository contains your Docker images.
- ECR uses resource-based permissions to let you specify who has access to a repository and what actions they can perform on it.
- ECR lifecycle policies enable you to specify the lifecycle management of images in a repository.
## Repository policy
- We can control access to our repositories and the images using repository policies.
## Image
- We can push and pull Docker images to our repositories. 
- We can use these images locally on your development system, or you can use them in ECS task definitions.
- We can replicate images in your private repositories across AWS regions.
## Security
- By default, IAM users don’t have permission to create or modify Amazon ECR resources, or perform tasks using the Amazon ECR API.
- Use IAM policies to grant or deny permission to use ECR resources and operations.
- ECR partially supports resource-level permissions.
- ECR supports the use of customer master keys (CMK) managed by AWS Key Management Service (KMS) to encrypt container images stored in your ECR repositories.
