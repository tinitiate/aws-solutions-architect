# CloudFront
- A Content Delivery Network (CDN) service that gives easy and cost-effective way to distribute content with low latency and high data transfer speeds.
- Used for dynamic, static, streaming, and interactive content.
- Delivers the content through a worldwide network of data centers called edge locations. 
- When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency, 
  so that content is delivered with the best possible performance.
  - If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately.
  - If the content is not in that edge location, CloudFront retrieves it from an origin that you’ve defined.
- CloudFront supports the WebSocket protocol as well as the HTTP protocol with the following HTTP methods:
  - GET
  - HEAD
  - POST
  - PUT
  - DELETE
  - OPTIONS
  - PATCH
- CloudFront also has regional edge caches that bring more of your content closer to your viewers, even when the content is not popular enough to 
  stay at a CloudFront edge location, to help improve performance for that content.
- We can use a zone apex name on CloudFront
- CloudFront supports wildcard CNAME.
- Objects are cached for 24 hours by default. You can invalidate files in CloudFront edge caches even before they expire.
- We can configure CloudFront to automatically compress files of certain types and serve the compressed files 
  when viewer requests include Accept-Encoding: gzip in the request header.
- CloudFront can cache different versions of your content based on the values of query string parameters.
- Using Lambda@Edge with CloudFront enables a variety of ways to customize the content that CloudFront delivers. 
  It can help you configure your CloudFront distribution to serve private content from your own custom origin, as an option to using signed URLs 
  or signed cookies.(See AWS Compute Services Lambda Lambda@Edge)

## Different CloudFront Origins
- Using S3 buckets for your origin.
- Using S3 buckets configured as website endpoints for our origin.
- Using a mediastore container or a media package channel for our origin we can set up an S3 bucket that is configured as a MediaStore container, 
  or create a channel and endpoints with MediaPackage. Then you create and configure a distribution in CloudFront to stream the video.
- Using an Application Load Balancer
- Using a Lambda function URL 
- Using EC2 or other custom origins.
- Using CloudFront Origin Groups for origin failover 

## Using HTTPS with CloudFront
- We can choose HTTPS settings both for communication between viewers and CloudFront, and between CloudFront and your origin.
- If we want your viewers to use HTTPS and to use alternate domain names for your files, you need to choose one of the following options 
  for how CloudFront serves HTTPS requests:
  - Use a dedicated IP address in each edge location
  - Use Server Name Indication (SNI)

## CloudFront Distributions
- We Create a CloudFront distribution to tell CloudFront where you want content to be delivered from, and the details about how to track and manage content delivery.
- We create a distribution and choose the configuration settings you want:
  - Your content origin—that is, the Amazon S3 bucket, MediaPackage channel, MediaStore container, ELB load balancer, or HTTP server from which CloudFront 
    gets the files to distribute. You can specify any combination of up to 25 origins for a single distribution.
  - Access—whether you want the files to be available to everyone or restrict access to some users.
  - Security—whether you want CloudFront to require users to use HTTPS to access your content.
  - Cache key— uniquely identifies each file in the cache for a given distribution.
  - Origin request settings—whether you want CloudFront to forward cookies or query strings to your origin.
  -Geographic restrictions—whether you want CloudFront to prevent users in selected countries from accessing your content.
  -Logs—whether you want CloudFront to create access logs that show viewer activity, which is recorded in real-time.

