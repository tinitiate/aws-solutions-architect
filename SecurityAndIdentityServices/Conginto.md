# Cognito 

- Amazon Cognito is a user management and authentication service that can be integrated to your web or mobile applications.
- Enables you to authenticate users through an external identity provider and provides temporary security credentials to 
  access your app’s backend resources in AWS or any service behind Amazon API Gateway.
- Cognito works with external identity providers that support SAML or OpenID Connect, social identity providers (Facebook, Twitter, Amazon, Google, Apple).
- We can also integrate your own identity provider.
- An Amazon Cognito ID token is represented as a JSON Web Token (JWT). 
- Amazon Cognito uses JSON Web Tokens for token authentication.

## User Pools

- A User Pool is like a directory of users.
- User pools are user directories that provide sign-up and sign-in options for your app users.
- Users can sign in to your web or mobile app through Amazon Cognito, or federate through a third-party identity provider (IdP).
- You can use the aliasing feature to enable your users to sign up or sign in with an email address and a password or a phone number and a password.
- User pools are each created in one AWS Region, and they store the user profile data only in that region. You can also send user data to a different AWS Region.
- **Tokens provided through user pools**:
  - Access tokens contain scopes and groups and are used to grant access to authorized resources. 
  - Access tokens can be configured to expire in as little as five minutes or as long as 24 hours.
  - Refresh tokens contain the information necessary to obtain a new ID or access token. 
  - Refresh tokens can be configured to expire in as little as one hour or as long as ten years.
- **Managing Users**
  - Amazon Cognito User Pools groups lets you manage your users and their access to resources by mapping IAM roles to groups.
  - User accounts are added to your user pool in one of the following ways:
    - The user signs up in your user pool’s client app, which can be a mobile or web app.
    - You can import the user’s account into your user pool.
    - You can create the user’s account in your user pool and invite the user to sign in.
    - Sign up authflow below

## Identity pools

- With an identity pool, your users can obtain temporary AWS credentials to access AWS services.
- Identity pools support anonymous guest users, as well as the following identity providers that you can use to authenticate users for identity pools:
  - Amazon Cognito user pools
  - Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple.
  - OpenID Connect (OIDC) providers
  - SAML identity providers
  - Developer authenticated identities

## Common Amazon Cognito scenarios

### Authenticate with a user pool

- You can enable your users to authenticate with a user pool. 
- App users can sign in either directly through a user pool, or federate through a third-party identity provider (IdP).
- After a successful authentication, your web or mobile app will receive user pool tokens from Amazon Cognito.
- You can use those tokens to retrieve AWS credentials that allow your app to access other AWS services.
  
    ![scenario-authentication-cup](/SecurityIdentityServices/images/scenario-authentication-cup.png)

### Access your server-side resources with a user pool

- After a successful user pool sign-in, your web or mobile app will receive user pool tokens from Amazon Cognito. 
- You can use those tokens to control access to your server-side resources. 
- You can also create user pool groups to manage permissions, and to represent different types of users.

### Access resources with API Gateway and Lambda with a user pool

- You can enable your users to access your API through API Gateway. 
- API Gateway validates the tokens from a successful user pool authentication, 
  and uses them to grant your users access to resources including Lambda functions, or your own API.

### Access AWS services with a user pool and an identity pool

- After a successful user pool authentication, your app will receive user pool tokens from Amazon Cognito. 
- You can exchange them for temporary access to other AWS services with an identity pool. 

### Authenticate with a third party and access AWS services with an identity pool

- You can enable your users access to AWS services through an identity pool. 
- An identity pool requires an IdP token from a user that's authenticated by a third-party identity provider (or nothing if it's an anonymous guest).
- In exchange, the identity pool grants temporary AWS credentials that you can use to access other AWS services.

### Access AWS AppSync resources with Amazon Cognito

- You can grant your users access to AWS AppSync resources with tokens from a successful Amazon Cognito authentication (from a user pool or an identity pool).
