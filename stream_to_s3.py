import boto3
import cv2
import time
from botocore.exceptions import ClientError
from datetime import datetime

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

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
s3 = boto3.client('s3')
BUCKET_NAME = "pistreambucket"
OBJECT_NAME = "currentFrame.jpg"

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()

    if ret:
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        cv2.imwrite("frame.jpg", frame)
        with open("frame.jpg", "rb") as f:
            s3.upload_fileobj(f, BUCKET_NAME, OBJECT_NAME)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("\n=== success ===")
        print("Current Time =", current_time)

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    # else:
    #     print("Frame is None")
    #     break
    time.sleep(10)


# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Stream to s3 stop")
