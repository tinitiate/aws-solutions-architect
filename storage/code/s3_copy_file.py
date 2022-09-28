import boto3
 
source_bucket_name = "syntaxboard"
dest_bucket_name = "sb-lamda-training" 
source_file = "demo2.csv"

boto3.setup_default_session (profile_name='sb') 

dest_file= source_file
s3_client = boto3.resource('s3')
copy_source = {
    'Bucket': source_bucket_name,
    'Key': source_file
}
 
s3_client.meta.client.copy(copy_source, dest_bucket_name,dest_file )
