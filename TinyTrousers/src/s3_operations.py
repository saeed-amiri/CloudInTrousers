"""
A simple example for AWS S3 operations
"""

import boto3

def upload_to_s3(bucket_name: str,
                 file_path: str,
                 object_name: str|None = None
                 ) -> None:
    """
    Upload a file to an S3 bucket
    """
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_path.split("/")[-1]

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name} as {object_name}")
    except Exception as e:
        print(f"Error: {e}")
