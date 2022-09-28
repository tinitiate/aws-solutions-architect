# Upload file to S3 bucket using  boto3

## Uploading a file to Bucket 

You must provide the following arguments to the **upload_file()** method:

- **file_name** – filename on the local filesystem
- **bucket_name** – the name of the S3 bucket
- **object_name** – the name of the uploaded file (usually equal to the **file_name**)

```
import pathlib
import boto3


base_dir = pathlib.Path(__file__).parent.resolve()

aws_region = "us-east-2"
bucket_name = "aws-demo"

s3_client = boto3.client("s3", region_name=aws_region)

# method which calls the S3 client and uploads the file.
def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{bucket_name}'")

upload_files(f"{BASE_DIR}/files/demo.txt", bucket_name)
```

## Uploading the file object data to Bucket 

- **upload_fileobj()** method requires opening a file in binary mode.

```
import io
import boto3

aws_region = "us-east-2"
bucket_name = "hands-on-cloud-demo-bucket"

s3_client = boto3.client("s3", region_name=aws_region)

def upload_generated_file_object(bucket, object_name):

    with io.BytesIO() as f:
        f.write(b'First line.\n')
        f.write(b'Second line.\n')
        f.seek(0)

        s3_client.upload_fileobj(f, bucket, object_name)

        print(f"Generated has been uploaded to '{bucket}'")

upload_generated_file_object(bucket_name, 'file.txt')
```

## Uploading multiple files to bucket

- The **glob()** method in the **glob module** can be used to upload multiple files to Amazon S3 buckets.
- **glob()** returns all file paths that match a given pattern as a Python list.
- Using wildcards in glob, we can select files based on a search pattern.

```
import os
import pathlib
from glob import glob
import boto3

base_dir = pathlib.Path(__file__).parent.resolve()

aws_region = "us-east-2"
bucket_name = "aws-demo"

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_file(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{bucket_name}'")


files = glob(f"{base_dir}/files/*.txt")

for file in files:
    upload_file(file, bucket_name)
```

## Copy file from one bucket to another

```
import boto3

source_bucket_name = "aws-demo"
dest_bucket_name = "aws-demo1"

source_file = 'demo.json'
dest_file= source_file
s3_client = boto3.resource('s3')
copy_source = {
    'Bucket': source_bucket_name,
    'Key': source_file
}

s3_client.meta.client.copy(copy_source, dest_bucket_name,dest_file )
```

