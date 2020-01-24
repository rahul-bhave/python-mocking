import pytest
import os
import boto3
import requests
import sys

import tempfile
import unittest
import boto3
import botocore

from moto import mock_s3
from s3_demo import list_files
import json


"""

BUCKET = 'Foo'

@pytest.fixture()
def moto_boto():
    @mock_s3
    def boto_resource():
        res = boto3.resource('s3')
        response =res.create_bucket(Bucket=BUCKET)
        return response
    return boto_resource

@mock_s3
def test_with_fixture(moto_boto):
        moto_boto()
        client = boto3.client('s3')
        response = client.list_objects(Bucket=BUCKET)
        return response

"""
MY_BUCKET = "MY_BUCKET"
fixtures_dir = "mock_folder"


@mock_s3
class TestListFile(unittest.TestCase):

    def setUp(self):
        client = boto3.client(
            "s3",
            region_name="eu-west-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        try:
            s3 = boto3.resource(
                "s3",
                region_name="eu-west-1",
                aws_access_key_id="fake_access_key",
                aws_secret_access_key="fake_secret_key",
            )
            s3.meta.client.head_bucket(Bucket=MY_BUCKET)
        except botocore.exceptions.ClientError:
            pass
        else:
            err = "{bucket} should not exist.".format(bucket=MY_BUCKET)
            raise EnvironmentError(err)
        response = client.create_bucket(Bucket=MY_BUCKET)
        current_dir = os.path.dirname(__file__)
        fixtures_dir = os.path.join(current_dir, "fixtures")
        _upload_fixtures(MY_BUCKET, fixtures_dir)
    
    def test_list_files(self):
        contents= []
        contents= list_files(MY_BUCKET)
        'return contents'
        for i in contents:
            print (i)
        

    def tearDown(self):
        s3 = boto3.resource(
            "s3",
            region_name="eu-west-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        bucket = s3.Bucket(MY_BUCKET)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()


def _upload_fixtures(bucket: str, fixtures_dir: str) -> None:
        client = boto3.client("s3")
        fixtures_paths = [
        os.path.join(path,  filename)
        for path, _, files in os.walk(fixtures_dir)
        for filename in files
        ]
        for path in fixtures_paths:
           key = os.path.relpath(path, fixtures_dir)
           client.upload_file(Filename=path, Bucket=bucket, Key=key)

if __name__ == "__main__":
    unittest.main()