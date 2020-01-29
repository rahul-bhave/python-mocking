from moto import mock_s3
from lambada_example import lambda_handler

@mock_s3
def test_lambda_handler():
    lambda_handler()