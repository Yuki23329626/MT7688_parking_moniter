
import boto3

client = boto3.client('kinesis-video-media')

response = client.get_media(
    StreamName='MyKinesisVideoStream',
    StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
    StartSelector={
        'StartSelectorType': 'NOW'
    }
)

print("response: " + response)
