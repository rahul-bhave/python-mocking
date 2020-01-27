# test.py
from unittest.mock import patch
import unittest
from requests.exceptions import Timeout
from s3_demo import requests
from s3_demo import list_files
import conf
BUCKET = conf.BUCKET


class MyTestCase(unittest.TestCase):

    """Approach: Monkey Pataching replacing another object as runtime"""

    @patch("s3_demo.requests")
    def test_list_files(self, mock_requests):
        try:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                list_files(BUCKET)
                mock_requests.get.assert_called_once()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
