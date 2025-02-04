"""
Test cases for the s3_operations module.
"""
import os
import boto3
import pytest
from botocore.exceptions import ClientError
from s3_operations import upload_to_s3


BUCKET_NAME = "tinytrousers-storage"
TEST_FILE = "test-file.txt"


def test_upload_to_s3() -> None:
    # Create a temporary file
    with open(TEST_FILE, "w") as f:
        f.write("This is a test file.")

    # Upload the file
    upload_to_s3(BUCKET_NAME, TEST_FILE)

    # Check if the file exists in S3
    s3 = boto3.client("s3")
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=TEST_FILE)
        file_exists = True
    except ClientError:
        file_exists = False

    # Remove the temporary file
    os.remove(TEST_FILE)

    # Assert that file exists in S3
    assert file_exists, "File upload to S3 failed!"
