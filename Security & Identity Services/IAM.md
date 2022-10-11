# AWS Identity and Access Management
- AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources.
- AWS account root users are single sign-on identities that have complete access to all AWS services and resources.## IAM features
- 
## IAM features
- AWS allows you to grant others access to your account without sharing passwords or access keys.
- Permissions can be granted for different resources to different people.
- You can use IAM features to securely provide credentials for applications that run on EC2 instances. 
- You can add two-factor authentication to your account and to individual users for extra security.
- You can allow users to use identity federation to get temporary access to your AWS account.
- Using AWS CloudTrail, we can receive log records that include information about those who made requests for resources in your account.
- IAM, like many other AWS services, is eventually consistent.
- IAM achieves high availability by replicating data across multiple servers within Amazon's data centers around the world. 
- IAM and AWS Security Token Service (STS) are offered at no additional charge.

## Accessing IAM
- AWS Management Console
- AWS Command Line Tools
- AWS SDKs
- IAM HTTPS API

## Terms
- **IAM Resources** -- The user, group, role, policy, and identity provider objects that are stored in IAM.
- **IAM Identities** -- The IAM resource objects that are used to identify and group. You can attach a policy to an IAM identity. 
  - These include users, groups, and roles.
- **IAM Entities** -- The IAM resource objects that AWS uses for authentication. These include IAM users and roles.
- **Principals** -- A person or application that uses the AWS account root user, an IAM user, or an IAM role to sign in and make requests to AWS. 
  - Principals include federated users and assumed roles.

## Request
- When a principal tries to use the AWS Management Console, the AWS API, or the AWS CLI, that principal sends a request to AWS.
- Requests includes the following information:
  - Actions or operations – the actions or operations that the principal wants to perform.
  - Resources – the AWS resource object upon which the actions or operations are performed.
  - Principal – the user, role, federated user, or application that sent the request.
  - Environment data – information about the IP address, user agent, SSL enabled status, or the time of day.
  - Resource data – data related to the resource that is being requested.

## Authentication
- To authenticate from the console as a user, you must sign in with your user name and password.
- To authenticate from the API or AWS CLI, you must provide your access key and secret key.
## Authorization
- AWS uses values from the request context to check for policies that apply to the request. 
- It then uses the policies to determine whether to allow or deny the request.
- Policies types can be categorized as permissions policies or permissions boundaries.
  - Permissions policies define the permissions for the object to which they’re attached. These include identity-based policies, resource-based policies, and ACLs.
  - Permissions boundary is an advanced feature that allows you to use policies to limit the maximum permissions that a principal can have.
- To provide your users with permissions to access the AWS resources in their own account, you need identity-based policies.
- Resource-based policies are for granting cross-account access.
- Evaluation logic rules for policies:
  - By default, all requests are denied.
  - An explicit allow in a permissions policy overrides this default.
  - A permissions boundary overrides the allow. If there is a permissions boundary that applies, that boundary must allow the request. 
  - An explicit deny in any policy overrides any allows.
## Actions or Operations
- Operations are defined by a service, and include things that you can do to a resource, such as viewing, creating, editing, and deleting that resource.
## Resource
- An object that exists within a service. The service defines a set of actions that can be performed on each resource.

## IAM Users
- IAM users are not separate accounts; they are users within your account.
- Each user can have its own password for access to the AWS Management Console. 
- You can also create an individual access key for each user so that the user can make programmatic requests to work with resources in your account.
- By default, a brand new IAM user has NO permissions to do anything.
- Users are global entities.

## Federated Users
- Users in your organization already have a way to be authenticated, you can federate those user identities into AWS.

## IAM Groups
- You can organize IAM users into IAM groups and attach a policy to a group. 
- A user can belong to multiple groups.
- Groups cannot belong to other groups.
- Users or groups can have multiple policies attached to them that grant different permissions.
- The permissions for the users are calculated based on the combination of policies. 

## IAM Role
- An IAM user can assume a role to temporarily take on different permissions for a specific task. 
- AWS service role is a role that a service assumes to perform actions in your account on your behalf. 
- This service role must include all the permissions required for the service to access the AWS resources that it needs.
- AWS service role for an EC2 instance is a special type of service role that a service assumes to launch an EC2 instance that runs your application. 
- This role is assigned to the EC2 instance when it is launched.
- AWS service-linked role is a unique type of service role that is linked directly to an AWS service. 
- Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf.
- An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.

## Policies
- Permission policies are JSON policy documents.
- The IAM console includes policy summary tables that describe the access level, resources, and conditions that are allowed or denied for each service in a policy.
- The policy summary table includes a list of services. Choose a service there to see the service summary.
- To assign permissions to federated users, you can create an entity referred to as a role and define permissions for the role.
- **Identity-Based Policies**
  - Permissions policies that you attach to a principal or identity.
  - Managed policies are standalone policies that you can attach to multiple users, groups, and roles in your AWS account.
  - Inline policies are policies that you create and manage and that are embedded directly into a single user, group, or role.
- **Resource-based Policies**
  - Permissions policies that you attach to a resource such as an Amazon S3 bucket.
  - Resource-based policies are only inline policies.
  - Trust policies – resource-based policies that are attached to a role and define which principals can assume the role.
## AWS Security Token Service (STS)
- Create and provide trusted users with temporary security credentials that can control access to your AWS resources.
- Temporary security credentials are short-term and are not stored with the user but are generated dynamically and provided to the user when requested.
- By default, AWS STS is a global service with a single endpoint at https://sts.amazonaws.com.
## Assume Role Options
- **AssumeRole** – 
  - Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. 
  - These temporary credentials consist of an access key ID, a secret access key, and a security token. 
  - Typically, you use AssumeRole within your account or for cross-account access. 
  - You can include multi-factor authentication (MFA) information when you call AssumeRole. 
- **AssumeRoleWithSAML** 
  - Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This allows you to link your enterprise identity store or directory to role-based AWS access without user-specific credentials or configuration.
- **AssumeRoleWithWebIdentity** 
  - Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. 
  - Example providers include Amazon Cognito, Login with Amazon, Facebook, Google, or any OpenID Connect-compatible identity provider.

## STS Get Tokens
- **GetFederationToken** 
  - Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a federated user. 
  - Typical use is in a proxy application that gets temporary security credentials on behalf of distributed applications inside a corporate network.
- **GetSessionToken** – 
  - Returns a set of temporary credentials for an AWS account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token.
  - Typically, you use GetSessionToken if you want to use MFA to protect programmatic calls to specific AWS API operations.

|                   When to Create IAM User                    |                  When to Create an IAM Role                  |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| You created an AWS account and you’re the only person who works in your account. | You’re creating an application that runs on an Amazon EC2 instance and that application makes requests to AWS. |
| Other people in your group need to work in your AWS account, and your group is using no other identity mechanism. | You’re creating an app that runs on a mobile phone and that makes requests to AWS. |
| You want to use the command-line interface to work with AWS. | Users in your company are authenticated in your corporate network and want to be able to use AWS without having no sign in again (federate into AWS) |
