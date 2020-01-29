import boto3


client = boto3.client('sqs', 'us-east-1')


class MyMessageCreator(object):
    queue_url = client.get_queue_url(QueueName='your-queue-name')['QueueUrl']

    def send_message(self, message):
        client.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message
        )
