# AWS WAF
- A web application firewall that helps protect web applications from attacks by allowing you to configure rules that allow, block, or monitor (count) 
  web requests based on conditions that you define.
- These conditions include:
  - IP addresses
  - HTTP headers
  - HTTP body
  - URI strings
  - SQL injection
  - Cross-site scripting.
- Resources that you can protect with AWS WAF:
  - Amazon CloudFront distribution
  - Amazon API Gateway REST API
  - Application Load Balancer
  - AWS AppSync GraphQL API
  - Amazon Cognito user pool
- WAF lets you create rules to filter web traffic based on conditions that include IP addresses, HTTP headers and body, or custom URIs.
- WAF provides real-time metrics and captures raw requests that include details about IP addresses, geo locations, URIs, User-Agent and Referers.
- AWS WAF can parse request body JSON content to inspect specific keys or values in the JSON content with WAF rules.
- AWS WAF Security Automations is a solution that automatically deploys a single web access control list (web ACL) 
  with a set of AWS WAF rules designed to filter common web-based attacks. 
## Components
- Central components of AWS WAF:
  - **Web ACLs** 
    - You use a web access control list (ACL) to protect a set of AWS resources. 
    - You create a web ACL and define its protection strategy by adding rules. 
    - Rules define criteria for inspecting web requests and they specify the action to take on requests that match their criteria. 
    - You also set a default action for the web ACL that indicates whether to block or allow through any requests that the rules haven't already blocked or allowed.

  - **Rules** 
    - Each rule contains a statement that defines the inspection criteria, and an action to take if a web request meets the criteria. 
    - When a web request meets the criteria, that's a match. 
    - You can configure rules to block matching requests, allow them through, count them, or run CAPTCHA controls against them.    
    - You combine conditions into rules to precisely target the requests that you want to allow, block, or count. WAF provides two types of rules:
      - **Regular rules** – use only conditions to target specific requests.
      - **Rate-based rules** – are similar to regular rules, with a rate limit. 
        - Rate-based rules count the requests that arrive from a specified IP address every five minutes. 
        - The rule can trigger an action if the number of requests exceed the rate limit.

  - **Rules groups**  
    - You can use rules individually or in reusable rule groups. 
    - AWS Managed Rules and AWS Marketplace sellers provide managed rule groups for your use. 
    - You can also define your own rule groups.

