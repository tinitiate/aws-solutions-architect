import boto3

def delete_all_in_folder(bucket_name, folder_name):
    """
    Deletes all files and subfolders within a specific folder in an S3 bucket.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - folder_name (str): The folder name within the S3 bucket.

    Returns:
    None
    """
    # Initialize a session using your credentials
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Ensure folder name ends with '/'
    if not folder_name.endswith('/'):
        folder_name += '/'
    
    # List all objects in the specified folder
    objects_to_delete = bucket.objects.filter(Prefix=folder_name)
    
    # Delete the objects
    for obj in objects_to_delete:
        obj.delete()

# Example usage
# delete_all_in_folder('my-bucket', 'my-folder')
