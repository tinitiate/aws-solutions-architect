
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
