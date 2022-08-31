# Lambda S3 to S3 Copy Trigger

> by Sri
> 
> (c) Syntaxboard 2019

- This tutorial demonstrates lambda triggering on a file being copied to one S3 bucket to another S3 bucket.

### STEP 1: Create Buckets

*

*

### STEP 2: Create Lambda Function

- 1 Select the Lambda
  
  ![](/lambda/images/lambda.png)
  
- 2 Click on `create function` to create a new function
  
  ![](/lambda/images/Lambda-01.png)
  
  ![](/lambda/images/Lambda-02.png)
  
  ![](/lambda/images/Lambda-03.png)
  
  ![](/lambda/images/Lambda-04.png)
  

### STEP 3: Create Trigger

![](/lambda/images/create-trigger-01.png)

![](/lambda/images/create-trigger-02.png)

![](/lambda/images/create-trigger-03.png)

![](/lambda/images/create-trigger-04.png)

![](/lambda/images/create-trigger-05.png)

![](/lambda/images/create-trigger-06.png)

```python
import boto3
import json

s3_client = boto3.client('s3')
response =[]


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file_name = event['Records'][0]['s3']['object']['key']
    csv_object = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
    file_reader = csv_object['Body'].read().decode("utf-8")
    csv_data = file_reader.split("\n")
    results = list(filter(None, csv_data))

    for result in results:
        result_data = result.split(",")
        respone_object={}
        respone_object['id'] =result_data[0]
        respone_object['name'] =result_data[1]
        respone_object['salary'] =result_data[2]
        response.append(respone_object)
    json_response = json.dumps(response)
    #print(json_response)
    return {
        'statusCode': 200,
        'body': json_response
    }
```

### STEP 4: Test

1. Run the following code to test the above Lambda execution.
  
2. Replace the **profile_name** with the your AWS profile.
  

```python
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
```
