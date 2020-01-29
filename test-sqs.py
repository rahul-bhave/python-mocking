import json

import pytest
from moto import mock_sqs
import boto3

import MyMessageCreator


@pytest.fixture
def sqs(scope='session', autouse=True):
    mock = mock_sqs()
    mock.start()

    print("starting mock")

    sqs_client = boto3.client('sqs', 'us-west-1')
    queue_name = 'connect-responses-{}'.format(stage)
    queue_url = sqs_client.create_queue(
        QueueName='test'
    )['QueueUrl']


    yield (sqs_client, queue_url)
    print ("stopping mock")

    mock.stop()

def test_message_received(sqs):
    client, queue_url = sqs
    MyMessageCreator.queue_url = queue_url
    creator = MyMessageCreator()
    creator.send_message({'key': 'value'})
    response = client.receive_messsage(QueueUrl=queue_url)
    assert response['Messages'][0]['Body'] == json.dumps({'key':  'value'})

