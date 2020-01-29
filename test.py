# test.py
from unittest.mock import patch
import unittest
from requests.exceptions import Timeout
from s3_demo import requests
from s3_demo import create_bucket
from s3_demo import list_files


class MyTestCase(unittest.TestCase):
    '@patch("s3_demo.requests")'

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)

    def test_list_files(self, mock_requests):
        'mock_requests.get.side_effect = Timeout'
        with self.assertRaises(requests.exceptions.Timeout):
            list_files("rahulb-test-bucket")
            'mock_requests.get.assert_called_once()'


if __name__ == '__main__':
    unittest.main()
