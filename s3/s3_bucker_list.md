# Listing S3 buckets using  boto3

## Requirements

pip install boto3

## Session

It stores the configuration information (primarily credentials and the selected region)
It initiates the connection with AWS services.
Both the client and the resource use it, by default.

## Client

Low-level object to access all AWS services.
It typically maps 1:1 with the service API.

## Resource

High-level object to access the AWS services.
It does not provide 100% API coverage of AWS services.
It exposes subresources and collections.
How to connect to S3 using Boto3.

### Using **client**

```
import boto3

aws_region = "us-east-2"

client = boto3.client("s3", region_name=aws_region)

response = client.list_buckets()

print("Listing Amazon S3 Buckets:")

for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")
```

### Using **resource**

```
import boto3

aws_region = "us-east-2"

resource = boto3.resource("s3", region_name=aws_region)

iterator = resource.buckets.all()

print("Listing Amazon S3 Buckets:")

for bucket in iterator:
    print(f"-- {bucket.name}")

```

















