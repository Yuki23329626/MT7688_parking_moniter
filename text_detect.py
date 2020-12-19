import boto3
import json
import time

client = boto3.client('rekognition')

BUCKET = "pistreambucket"
NAME = "currentFrame.jpg"

while(true){
    response = client.detect_text(
            Image={
                'S3Object':{
                    'Bucket':BUCKET,
                    'Name':NAME
                    }
                }
            )
    json_formatted_response = json.dumps(response, indent=2)

    print("\n===== response =====")
    print(json_formatted_response)
    time.sleep(1)
}



