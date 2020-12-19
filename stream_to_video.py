import boto3
import cv2
import time

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

    if ret:
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        cv2.imwrite("frame.jpg", frame)

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break
    time.sleep(1)
    break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")
