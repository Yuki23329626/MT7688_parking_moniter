
import boto3
import json

video_client = boto3.client('kinesisvideo', region_name='ap-northeast-1')

response = video_client.get_data_endpoint(
	StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
	APIName='GET_MEDIA'
)

print("\n==== response ====")
print(response)

result = json.dumps(response)
print("\n==== endpoint-url ====\n" + result[314:374])

video_client = boto3.client(
	'kinesis-video-media',
        endpoint_url=result[314:374],
	region_name='ap-northeast-1'
)

stream = video_client.get_media(
	StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
	StartSelector={
		'StartSelectorType': 'NOW'
	}
)

#response = client.get_media(
#    StreamName='MyKinesisVideoStream',
#    StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
#    StartSelector={
#        'StartSelectorType': 'NOW'
#    }
#)

print("\n==== stream ====")
print(stream)

