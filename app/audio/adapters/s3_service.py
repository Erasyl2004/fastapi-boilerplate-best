from typing import BinaryIO
import boto3
from boto3.session import Session
import os
from dotenv import load_dotenv
load_dotenv()

class S3Service:
    def __init__(self):
        self.s3 = boto3.client('s3', aws_access_key_id=os.getenv("aws_access_key_id"), aws_secret_access_key=os.getenv("aws_secret_access_key"))

    def upload_file(self, file: BinaryIO, filename: str):
        print(os.getenv("aws_access_key_id"))
        print(os.getenv("aws_secret_access_key"))
        bucket = "nyt20192004"
        filekey = f"posts/{filename}"
        
        self.s3.upload_fileobj(file, bucket, filekey)
        
        bucket_location = boto3.client('s3' , aws_access_key_id=os.getenv("aws_access_key_id"), aws_secret_access_key=os.getenv("aws_secret_access_key")).get_bucket_location(
            Bucket=bucket
        )
        object_url = "https://nyt20192004.s3.amazonaws.com/posts/" + filename
        return object_url