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
