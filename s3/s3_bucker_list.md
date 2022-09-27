# Listing S3 buckets using  boto3

Using **client**

```
import boto3

aws_region = "us-east-2"

client = boto3.client("s3", region_name=aws_region)

response = client.list_buckets()

print("Listing Amazon S3 Buckets:")

for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")
```

Using **resource**

```
import boto3

aws_region = "us-east-2"

resource = boto3.resource("s3", region_name=aws_region)

iterator = resource.buckets.all()

print("Listing Amazon S3 Buckets:")

for bucket in iterator:
    print(f"-- {bucket.name}")

```

















