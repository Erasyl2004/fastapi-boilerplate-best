from typing import BinaryIO
import boto3
from boto3.session import Session


class S3Service:
    def __init__(self):
        access_key_id = "AKIARZHXKL6VDWTZRACR"
        secret_access_key = "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"
        self.s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    def upload_file(self, file: BinaryIO, filename: str):
        access_key_id = "AKIARZHXKL6VDWTZRACR"
        secret_access_key = "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"
        bucket = "nyt20192004"
        filekey = f"posts/{filename}"
        
        self.s3.upload_fileobj(file, bucket, filekey)
        
        bucket_location = boto3.client('s3' , aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key).get_bucket_location(
            Bucket=bucket
        )
        object_url = "https://nyt20192004.s3.amazonaws.com/posts/" + filename
        return object_url