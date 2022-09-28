# Delete operations on bucket and bucket objects using boto3

## Deleting objects/file from buckets 

```
import boto3

bucket_name = "aws-demo"
key ='demo.json'
client = boto3.client('s3')
client.delete_object(Bucket=bucket_name, Key=key)
print("S3 Key {key} has been deleted from the Bucket{bucket_name}")
```

## Deleting empty buckets

Using **client**

```
import boto3

aws_region = "us-east-2"

client = boto3.client("s3", region_name=aws_region)

bucket_name = "aws-demo"

client.delete_bucket(Bucket=bucket_name)

print("Amazon S3 Bucket has been deleted")
```

Using **resource**

```
import boto3

aws_region = "us-east-2"

resource = boto3.resource("s3", region_name=aws_region)

bucket_name = "aws-demo"

s3_bucket = resource.Bucket(bucket_name)

s3_bucket.delete()

print("Amazon S3 Bucket has been deleted")

```

## Deleting non-empty buckets

```
import boto3

aws_region = "us-east-2"

bucket_name = "aws-demo"

resource = boto3.resource("s3", region_name=aws_region)

s3_bucket = resource.Bucket(bucket_name)

def cleanup_s3_bucket():
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()
    print("S3 Bucket cleaned up")

cleanup_s3_bucket()

s3_bucket.delete()

print("S3 Bucket deleted")

```

