"""
A simple example for AWS S3 operations
"""


import sys

from s3_operations import upload_to_s3, down_and_edit

# Define your AWS S3 bucket name and file path
BUCKET_NAME = "your-bucket-name"  # Replace with your actual bucket name
FILE_PATH = "test_file.txt"  # Replace with your file path


def call_upload() -> None:
    """Call the upload function"""
    print(f"Uploading {FILE_PATH} to {BUCKET_NAME}")
    upload_to_s3(BUCKET_NAME, FILE_PATH)
    print("Upload complete")


def call_down_and_edit() -> None:
    """Call the edit with download function"""
    print(f"Downloading and editing file {FILE_PATH}")
    down_and_edit(bucket_name=BUCKET_NAME,
                  object_key=FILE_PATH,
                  new_content="Editing and updating a test file!"
                  )


def main() -> None:
    """
    Main function
    """
    order: str = sys.argv[1]
    if order == 'upload':
        call_upload()
    elif order == 'dedit':
        call_down_and_edit()


if __name__ == "__main__":
    main()
