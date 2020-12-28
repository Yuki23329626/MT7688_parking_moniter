import boto3
import json
import time
import string
import requests

client = boto3.client('rekognition')

BUCKET = "pistreambucket"
NAME = "currentFrame.jpg"

# Since AWS rekognition API call is extremely expensive
# You culd setting the delay of api call(in seconds) right here
DELAY = 10

while(True):
    print("\n===== Start Detecting Via API =====")
    response = client.detect_text(
            Image={
                'S3Object':{
                    'Bucket':BUCKET,
                    'Name':NAME
                    }
                }
            )
    response_json_dumps = json.dumps(response, indent=4)

    print("\n===== Response =====")
    print(response_json_dumps)
    keys = []
    values = []
    result = []

    print('\n===== Filtering Legalled Candidates =====')
    i = 0
    for element in response['TextDetections']:
        if (len(element['DetectedText'])==6) or (len(element['DetectedText'])==7) or (len(element['DetectedText'])==8):
            if(element['Type'] == 'LINE'):
                if(element['DetectedText'].find('.')>=0 and element['DetectedText'].find(' ')<0):
                    if (element['DetectedText'].find('.')<2) or (element['DetectedText'].find('.')>4):
                        continue
                    # print('.')
                    # print(element['DetectedText'].find('.'))
                    result.append(element)
                    i += 1
                    continue
                elif(element['DetectedText'].find('-')>=0):
                    if (element['DetectedText'].find('-')<2) or (element['DetectedText'].find('-')>4):
                        continue
                    # print('-')
                    # print(element['DetectedText'].find('-'))
                    result.append(element)
                    i += 1
                    continue
                elif(len(element['DetectedText'])<8):
                    result.append(element)
                    i += 1

    print('\n===== Sorting Candidates With Width and Confidence =====')
    result = sorted(result, key=lambda k: k.get('Confidence'), reverse=True)
    result = sorted(result, key=lambda k: k['Geometry']['BoundingBox'].get('Width'), reverse=True)
    
    for i in result:
        print('DetectedText:\t' + i['DetectedText'])
        print('Width:\t\t' + str(i['Geometry']['BoundingBox']['Width']))
        print('Confidence:\t' + str(i['Confidence']))
        print()
    
    if result == []:
        print('\n===== Do Not Find Lisence Plate =====')
        # time.sleep(DELAY)
        input()
        continue
    else:
        print('\n===== The Most Likely Candidate =====')
        print(result[0]['DetectedText'])

    print('\n===== Split Lisence Plate =====')
    if (result[0]['DetectedText'].find('.')>=0):
        lisence_plate = result[0]['DetectedText'].split('.')
        print(lisence_plate)
        license_plate_head = result[0]['DetectedText'].split('.')[0]
        license_plate_tail = result[0]['DetectedText'].split('.')[1]
    elif (result[0]['DetectedText'].find('-')>=0):
        lisence_plate = result[0]['DetectedText'].split('-')
        print(lisence_plate)
        license_plate_head = result[0]['DetectedText'].split('-')[0]
        license_plate_tail = result[0]['DetectedText'].split('-')[1]
    elif (len(result[0]['DetectedText'])) == 6 or (len(result[0]['DetectedText'])) == 7 :
        print(result[0]['DetectedText'])
        license_plate_head = result[0]['DetectedText'][:3]
        license_plate_tail = result[0]['DetectedText'][3:]
        print(license_plate_head)
        print(license_plate_tail)

    print('\n===== Update Database =====')
    my_data = {
        "camera_id" : "A01",
        "lisence_plate_head" : license_plate_head,
        "lisence_plate_tail" : license_plate_tail
        }
    my_data = json.dumps(my_data)

    res = requests.post('https://michael7105.csie.io/carLocationSearch/Manager/location_update.php', data = my_data)

    print('\n===== Response From location_update() =====')
    print(res)
    time.sleep(DELAY)
    #input()
