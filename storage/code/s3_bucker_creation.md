# Creating aws buckets using  boto3

## Prerequisites

- Python 3
- Boto3
- AWS CLI

## Connecting to S3 using Boto3

- We can access low-level API data through this ``client``.

  ```
  import boto3

  aws_region = "us-east-1"

  client = boto3.client("s3", region_name=AWS_REGION)
  ```

  ​


- The resource that allows you to use AWS services in a higher-level object-oriented way. 

  ```
  import boto3

  resource = boto3.resource('s3')
  ```

## Creating S3 Bucket

- Using ```client``

```
import boto3

aws_region = "us-east-2"

client = boto3.client("s3", region_name=aws_region)

bucket_name = "aws-demo"
location = {'LocationConstraint': aws_region}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")
```

- Using ``resource``

  ```
  import boto3

  aws_region = "us-east-2"

  resource = boto3.resource("s3", region_name=aws_region)

  bucket_name = "aws-demo"
  location = {'LocationConstraint': aws_region}

  bucket = resource.create_bucket(
      Bucket=bucket_name,
      CreateBucketConfiguration=location)

  print("Amazon S3 bucket has been created")
  ```

  ​

