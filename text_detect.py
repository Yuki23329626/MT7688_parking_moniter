import boto3
import json
import time

client = boto3.client('rekognition')

BUCKET = "pistreambucket"
NAME = "currentFrame.jpg"

while(True):
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
    time.sleep(100)

# response json will be like this:
# {
#     "TextDetections": [
#         {
#             "DetectedText": "C",
#             "Type": "LINE",
#             "Id": 0,
#             "Confidence": 72.02649688720703,
#             "Geometry": {
#                 "BoundingBox": {
#                     "Width": 0.04000072553753853,
#                     "Height": 0.022570611909031868,
#                     "Left": 0.25833332538604736,
#                     "Top": 0.1862500011920929
#                 },
#                 "Polygon": [
#                     {
#                         "X": 0.25833332538604736,
#                         "Y": 0.1862500011920929
#                     },
#                     {
#                         "X": 0.2983340620994568,
#                         "Y": 0.18744535744190216
#                     },
#                     {
#                         "X": 0.29803428053855896,
#                         "Y": 0.21001596748828888
#                     },
#                     {
#                         "X": 0.2580335736274719,
#                         "Y": 0.20882061123847961
#                     }
#                 ]
#             }
#         },
#     ],
#     "TextModelVersion": "3.0"
# }
