
import boto3
import json

video_client = boto3.client('kinesisvideo', region_name='ap-northeast-1')

response = video_client.get_data_endpoint(
	StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
	APIName='GET_MEDIA'
)

print("\n==== response ====")
dataEndpoint = response['DataEndpoint']
print(dataEndpoint)

print("\n==== endpoint-url ====\n" + dataEndpoint)

video_client = boto3.client(
	'kinesis-video-media',
        endpoint_url=dataEndpoint,
	region_name='ap-northeast-1'
)

stream = video_client.get_media(
	StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
	StartSelector={
		'StartSelectorType': 'NOW'
	}
)

payload = stream['Payload']

#response = client.get_media(
#    StreamName='MyKinesisVideoStream',
#    StreamARN='arn:aws:kinesisvideo:ap-northeast-1:593275627923:stream/MyKinesisVideoStream/1608059745417',
#    StartSelector={
#        'StartSelectorType': 'NOW'
#    }
#)

print("\n==== stream ====")
print(payload.read(1000))

import boto3
import cv2

STREAM_NAME = "MyKinesisVideoStream"

kv = boto3.client("kinesisvideo")

# Grab the endpoint from GetDataEndpoint
dataEndpoint = kv.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
)['DataEndpoint']

print(dataEndpoint)

# # Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media", endpoint_url=dataEndpoint)
url = kvam.get_hls_streaming_session_url(
    StreamName=STREAM_NAME,
    PlaybackMode="LIVE"
)['HLSStreamingSessionURL']


vcap = cv2.VideoCapture(url)

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()

    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")
