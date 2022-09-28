# Serverless Application Repository

- Serverless Application Repository is a managed repository for deploying and publishing serverless applications.
- We can use pre-built applications instead of cloning, building, packaging, and publishing source code to AWS before deploying it.
- Each application includes an AWS SAM template that specifies the AWS resources that will be used.

## Publishing Applications

- You first define your application with an **AWS Serverless Application Model (AWS SAM) template.**
- To publish a serverless app, you can use the following to upload your code:
  - AWS Management Console
  - AWS SAM CLI
  - AWS SDKs
- When you publish your application, it's initially set to ***private***, and only accessible to the AWS account that created it.
- You can deploy and share your app by setting it to:
  - **Private**
    - Not shared with any other AWS accounts.
    - Only accessible to the AWS account that created it.
    - You have the permissions to deploy applications created with your AWS account.
  - **Privately Shared**
    - Shared to a specific set of AWS accounts.
    - Accessible in the AWS Region in which they are created.
    - You have the permissions to deploy applications shared with your AWS account.
  - **Publicly Shared**
    - Shared to everyone.
    - Accessible to all AWS Regions.
    - You have the permissions to deploy any publicly shared application.
- A link to the source code is included in publicly shared applications.
- If the public app is deployed to another Region, AWS SAR copies the app deployment artifacts to an Amazon S3 bucket in the destination Region.
- By sharing Lambda layers, you can deploy an instance of your layer to another AWS account.

## Deploying Applications

- To deploy an application, you must have permissions to do so *(see permissions above)*.
- Before deploying an app, AWS SAR also checks the application template for:
  - IAM roles
  - AWS resource policies
  - Nested applications specified by the template
- You can only search for and browse applications for which you have permission:
  - Created using your AWS account
  - Privately shared with your AWS account
  - Publicly shared
- Use AWS Console or AWS CLI to deploy and update applications.

# AWS Serverless Application Model (SAM)

- AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS.
- A **serverless application** is a combination of Lambda functions, event sources, and other resources that work together to perform tasks.
- It can include additional resources such as APIs, databases, and event source mappings.
- You create a JSON or YAML configuration template to model your applications.
- During deployment, SAM transforms and expands the SAM syntax into CloudFormation syntax.
- SAM CLI provides a Lambda-like execution environment that lets you locally build, test, and debug applications defined by SAM templates. 
- We can also use the SAM CLI to deploy your applications to AWS.
- We can use AWS SAM to build serverless applications that use any runtime supported by AWS Lambda.
- We  can also use SAM CLI to locally debug Lambda functions written in Node.js, Java, Python, and Go.

## AWS SAM template anatomy

- An AWS SAM template file closely follows the format of an AWS CloudFormation template file. 
- If you are writing an AWS Serverless Application Model template alone and not via CloudFormation, the Transform section is required.
- The Globals section is unique to AWS SAM templates. It defines properties that are common to all your serverless functions and APIs.
-  All the AWS::Serverless::Function , AWS::Serverless::Api, and AWS::Serverless::SimpleTable resources inherit the properties that are defined in the
  Globals section.
- The Resources section can contain a combination of AWS CloudFormation resources and AWS SAM resources.

## AWS SAM resource and property reference

- **AWS::Serverless::Api** - creates a collection of Amazon API Gateway resources and methods that can be invoked through HTTPS endpoints.
- **AWS::Serverless::Application** - embeds a serverless application from the Serverless Application Repository or from an Amazon S3 bucket as a nested application.
- **AWS::Serverless::Function** - creates an AWS Lambda function, an AWS Identity and Access Management (IAM) execution role, and event source mappings that trigger the function. We can describe any event source that you want to attach to the Lambda function.
- **AWS::Serverless::LayerVersion** - creates a Lambda LayerVersion that contains library or runtime code needed by a Lambda Function. When a Serverless LayerVersion is transformed, SAM also transforms the logical id of the resource so that old Layer Versions are not automatically deleted by CloudFormation when the resource is updated.
- **AWS::Serverless::SimpleTable** - creates a DynamoDB table with a single attribute primary key. 
- **AWS::Serverless::HttpApi** - creates an Amazon API Gateway HTTP API, which enables you to create RESTful APIs with lower latency and lower costs than REST APIs.
- **AWS::Serverless::StateMachine** - creates an AWS Step Functions state machine, which you can use to orchestrate AWS Lambda functions and other AWS resources to form complex and robust workflows.