"""
A simple example for AWS S3 operations
"""

from s3_operations import upload_to_s3

# Define your AWS S3 bucket name and file path
BUCKET_NAME = "your-bucket-name"  # Replace with your actual bucket name
FILE_PATH = "test_file.txt"  # Replace with your file path

def main() -> None:
    """
    Main function
    """
    print(f"Uploading {FILE_PATH} to {BUCKET_NAME}")
    upload_to_s3(BUCKET_NAME, FILE_PATH)
    print("Upload complete")


if __name__ == "__main__":
    main()
