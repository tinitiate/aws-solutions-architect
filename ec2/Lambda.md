# Lambda

- A serverless compute service.

- The Lambda functions are **stateless**, meaning that once the function is performed the function has been completed.

- Lambda has no affinity to the infrastructure they are running on.

- Applications built using lambda functions are triggered by events.

- Lambda assumes an IAM role when it executes the function.

- Lambda stores code in Amazon S3 and encrypts it at rest.

- Code in Lambda is executed only when needed and is automatically scaled up and down.

- Lambda provides continuous scaling – scales out not up.

- Lambda scales concurrently executing functions up to your default limit (1000).

- Lambda functions are serverless and independent, 1 event = 1 function.

- Functions can trigger other functions so 1 event can trigger multiple functions.

- Lambda Supports the following programing languages:

  - C#

  - Go

  - Java

  - Node.js

  - Python

  - PowerShell

  - Ruby

## **Components** 

- **Function** :
  - Script or program that runs in Lambda.
  - Lambda passes invocation events to function.
  - Function processes an event and returns a response.
  - Functions can access:
    - AWS services or non-AWS services.
    - AWS services running in VPCs (e.g. RedShift, ElastiCache, RDS instances).
    - Services running on EC2 instances in an AWS VPC.
  - To enable your Lambda function to access resources inside your private VPC, we must provide additional VPC-specific configuration information that includes VPC subnet IDs and security group IDs.
  - Lambda uses this information to set up elastic network interfaces (ENIs) that enable your function.
  - We can request additional memory in 1 MB increments from 128 MB to 10240 MB.
  - There is a maximum execution timeout.
    - Max is 15 minutes (900 seconds), default is 3 seconds.
    - You pay for the time it runs.
    - Lambda terminates the function at the timeout.
- **Runtimes**:
  - Lambda runtimes allow functions in different languages to run in the same base execution environment. 
  - The runtime sits in-between the Lambda service and the function code, relaying invocation events, context information, and responses between the two.
- **Layers**:
  - Lambda layers are a distribution mechanism for libraries, custom runtimes, and other function dependencies. 
  - Function can use up to 5 layers at a time.
  - Allow us to use libraries in function without needing to include them in your deployment package.
- **Event source** – an AWS service or a custom service that triggers your function and executes its logic.
- **Downstream resources** – an AWS service that your Lambda function calls once it is triggered.
- **Log streams**:
  - Lambda automatically monitors function invocations and reports metrics to CloudWatch.
  - We can also annotate function code with custom logging statements that allow you to analyze the execution flow and performance of the Lambda function.

## **Lambda@Edge**

- Lambda@Edge is a serverless CloudFront feature.
- Lambda@Edge works with the CloudFront content delivery network.
- Lambda@Edge enables the content to be closer to the customer and achieve higher performance.
- Lambda@Edge allows for running Lambda functions closer to the user.
- You can use Lambda functions to change CloudFront requests and responses at the following points:
  - After CloudFront receives a request from a viewer (viewer request)
  - Before CloudFront forwards the request to the origin (origin request)
  - After CloudFront receives the response from the origin (origin response)
  - Before CloudFront forwards the response to the viewer (viewer response)
- You can automate your serverless application’s release process using AWS CodePipeline and AWS CodeDeploy.
- Lambda will automatically track the behavior of your Lambda function invocations and provide feedback that you can monitor. In addition, it provides metrics that allows you to analyze the full function invocation spectrum, including event source integration and whether downstream resources perform as expected.

## Elastic Load Balancing

- Application Load Balancers (ALBs) support AWS Lambda functions as targets.

- We can register Lambda functions as targets and configure a listener rule to forward requests to the target group for your Lambda function.
- When the load balancer forwards the request to a target group with a Lambda function as a target, it invokes your Lambda function and passes the content of the request to the Lambda function, in JSON format.

### Limits:

- Lambda function and target group must be in the same account and in the same Region.
- The maximum size of the request body that you can send to a Lambda function is 1 MB.
- The maximum size of the response JSON that the Lambda function can send is 1 MB.
- WebSockets are not supported. Upgrade requests are rejected with an HTTP 400 code.

