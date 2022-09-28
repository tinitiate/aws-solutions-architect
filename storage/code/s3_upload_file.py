import pathlib
import boto3

boto3.setup_default_session (profile_name='sb') 
aws_region = "us-east-2"
bucket_name = "sb-lamda-training"


s3_client = boto3.client("s3", region_name=aws_region)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{bucket_name}'")

upload_files("demo.json", bucket_name)
