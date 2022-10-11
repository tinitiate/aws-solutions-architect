# AWS Secrets Manager
- Secrets Manager enables you to replace hardcoded credentials in your code, including passwords, 
  with an API call to Secrets Manager to retrieve the secret programmatically.
  
  ![ASM-Basic-Scenario](/SecurityAndIdentityServices/images/ASM-Basic-Scenario.png)
  
- A secret consists of a set of credentials (user name and password), and the connection details used to access a secured service.
- A secret also contains metadata which include:
  - Basic information includes the name of the secret, a description, and the Amazon Resource Name (ARN) to serve as a unique identifier.
  - The ARN of the AWS KMS key Secrets Manager uses to encrypt and decrypt the protected text in the secret. If you don’t provide this information, 
    Secrets Manager uses the default AWS KMS key for the account.
  - Information about how frequently to rotate the key and what Lambda function to use to perform the rotation.
  - A user-provided set of tags. You can attach tags as key-value pairs to AWS resources for organizing, logical grouping, and cost allocation.
- A secret can contain versions:
  - Although you typically only have one version of the secret active at a time, multiple versions can exist while you rotate a secret on the database or service. 
    Whenever you change the secret, Secrets Manager creates a new version.
  - Each version holds a copy of the encrypted secret value.
  - Each version can have one or more staging labels attached identifying the stage of the secret rotation cycle.
- Supported Secrets
  - Database credentials, on-premises resource credentials, SaaS application credentials, third-party API keys, and SSH keys. 
  - You can also store JSON documents.
- To retrieve secrets, you simply replace secrets in plain text in your applications with code to pull in those 
  secrets programmatically using the Secrets Manager APIs.
- Secrets Manager lets you easily copy your secrets to multiple AWS Regions, which includes the primary secret and the associated metadata such as tags,
  resource policies and secret updates such as rotation.
- Secrets can be cached on the client side, and updated only during a secret rotation.
- You can create two secrets that have different permissions
  - User Secret – can be used to connect to linked services, but it cannot be rotated. 
    - The user will have to wait for the master secret to be rotated and propagated for it to change.
  - Master Secret – has sufficient permissions to rotate secrets of linked services. 
    - This scenario is typically used when you have users that are actively using the old secret, and you do not want to break operations after you rotate the secret. 
    - You can have your users  update their clients first before using the newly rotated credentials.
- During the secret rotation process, Secrets Manager tracks the older credentials, as well as the new credentials you want to start using,
  until the rotation completes. It tracks these different versions by using staging labels.
    - The rotation function contacts the secured service authentication system and creates a new set of credentials to access the database. 
    - Secrets Manager stores these new credentials as the secret text in a new version of the secret with the AWSPENDING staging label attached.
    - The rotation function then tests the AWSPENDING version of the secret to ensure that the credentials work, 
      and grants the required level of access to the secured service.
    - If the tests succeed, the rotation function then moves the label AWSCURRENT to the new version to mark it as the default version. 
      Then, all of the clients start using this version of the secret instead of the old version. 
      The function also assigns the label AWSPREVIOUS to the old version. 
      The version that had AWSPREVIOUS staging label now has no label, and therefore deprecated.
