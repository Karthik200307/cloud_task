Prerequisites
1. *Install Boto3*: Install the AWS SDK for Python using pip:
   bash
   pip install boto3
   

2. *AWS Credentials*: Configure your AWS credentials using the AWS CLI or by placing them in ~/.aws/credentials.

---

### Python Script: AWS S3 File Operations
python
import boto3
import os

# Configuration
AWS_REGION = 'us-east-1'
BUCKET_NAME = 'your-unique-bucket-name'
LOCAL_FILE_PATH = 'path/to/your/local/file.txt'
DOWNLOAD_PATH = 'path/to/download/file.txt'

# Initialize S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION)

def create_bucket(bucket_name):
    """Create an S3 bucket."""
    try:
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': AWS_REGION},
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_file(bucket_name, local_file_path):
    """Upload a file to the S3 bucket."""
    try:
        file_name = os.path.basename(local_file_path)
        s3_client.upload_file(local_file_path, bucket_name, file_name)
        print(f"File '{file_name}' uploaded to bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def list_files(bucket_name):
    """List all files in the S3 bucket."""
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print("Files in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print("Bucket is empty.")
    except Exception as e:
        print(f"Error listing files: {e}")

def download_file(bucket_name, file_name, download_path):
    """Download a file from the S3 bucket."""
    try:
        s3_client.download_file(bucket_name, file_name, download_path)
        print(f"File '{file_name}' downloaded to '{download_path}'.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Create the S3 bucket
    create_bucket(BUCKET_NAME)

    # Upload a file to the bucket
    upload_file(BUCKET_NAME, LOCAL_FILE_PATH)

    # List files in the bucket
    list_files(BUCKET_NAME)

    # Download the file back
    file_name = os.path.basename(LOCAL_FILE_PATH)
    download_file(BUCKET_NAME, file_name, DOWNLOAD_PATH)


---

### Steps to Execute
1. Replace AWS_REGION, BUCKET_NAME, LOCAL_FILE_PATH, and DOWNLOAD_PATH with your details.
2. Run the script:
   bash
   python s3_script.py
   

---

### Notes
- Ensure the bucket name is globally unique.
- Configure proper IAM permissions for your AWS credentials to allow S3 operations.
- For more advanced use cases, consider error handling for specific AWS exceptions using botocore.exceptions.
