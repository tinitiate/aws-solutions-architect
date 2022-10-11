# Amazon API Gateway
- API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale.
- Allows creating, deploying, and managing a RESTful API to expose backend HTTP endpoints, Lambda functions, or other AWS services.
- Lambda and API Gateway form the serverless infrastructure's app-facing part.
##  Concepts
- **API deployment** – a point-in-time snapshot of your API Gateway API resources and methods. To be available for clients to use, the deployment must 
  be associated with one or more API stages.
- **API endpoints** – host names APIs in API Gateway, which are deployed to a specific region and of the format: rest-api-id.execute-api.region.amazonaws.com
- **API key** – An alphanumeric string that API Gateway uses to identify an app developer who uses your API.
- **API stage** – A logical reference to a lifecycle state of your API. API stages are identified by API ID and stage name.
- **Model** – Data schema specifying the data structure of a request or response payload.
- **Private API** – An API that is exposed through interface VPC endpoints and isolated from the public internet
- **Private integration** – An API Gateway integration type for a client to access resources inside a customer’s VPC through a private API endpoint without 
  exposing the resources to the public internet.
- **Proxy integration** 
  - For the HTTP proxy integration, API Gateway passes the entire request and response between the frontend and an HTTP backend.
  - For the Lambda proxy integration, API Gateway sends the entire request as an input to a backend Lambda function.

## Endpoint type
- The endpoint type refers to the endpoint that API Gateway creates for your API.
  |Endpoint types| REST API |HTTP API|
  |--------------|----------|--------|
  |Edge-optimized| ✓ | |
  |Regional | ✓ | ✓ |
  |Private | ✓ | |
## Development 

| Features                         | REST API | HTTP API |
| :------------------------------- | :------- | :------- |
| CORS configuration               | ✓        | ✓        |
| Test Invocations                 | ✓        |          |
| Caching                          | ✓        |          |
| User-controlled deployments      | ✓        | ✓        |
| Automatic deployments            |          | ✓        |
| Custom gateway responses         |          |          |
| Request validation               |          |          |
| Request parameter transformation | ✓        | ✓        |
| Request body transformation      |          |          |


## Integrations

| Feature                                              | REST API                                                     | HTTP API                                                     |
| :--------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| Public HTTP endpoints                                | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/setup-http-integrations.html) | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-http.html) |
| AWS services                                         | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-integration-types.html) | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html) |
| AWS Lambda functions                                 | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-integrations.html) | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html) |
| Private integrations with Network Load Balancers     | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html) | [✓](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-private.html) |
| Private integrations with Application Load Balancers |                                                              | ✓                                                            |
| Private integrations with AWS Cloud Map              |                                                              | ✓                                                            |
| Mock integrations                                    | ✓                                                            |                                                              |
