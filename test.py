
import boto3

client = boto3.client('kinesis-video-media')

response = client.create_signaling_channel(
    ChannelName='string',
    ChannelType='SINGLE_MASTER',
    SingleMasterConfiguration={
        'MessageTtlSeconds': 123
    },
    Tags=[
        {
            'Key': 'string',
            'Value': 'string'
        },
    ]
)
