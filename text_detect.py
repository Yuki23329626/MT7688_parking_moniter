import boto3
import json
import time
import string
import requests

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

    # response = {
    #     "TextDetections": [
    #         {
    #         "DetectedText": "D",
    #         "Type": "LINE",
    #         "Id": 0,
    #         "Confidence": 89.84026336669922,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": -0.001997847342863679,
    #             "Height": -0.004109642934054136,
    #             "Left": 0.2948249280452728,
    #             "Top": 0.25775864720344543
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.2948249280452728,
    #                 "Y": 0.25775864720344543
    #             },
    #             {
    #                 "X": 0.2928270697593689,
    #                 "Y": 0.12418906390666962
    #             },
    #             {
    #                 "X": 0.3795737326145172,
    #                 "Y": 0.1200794205069542
    #             },
    #             {
    #                 "X": 0.38157156109809875,
    #                 "Y": 0.2536489963531494
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "106 104 105 ha 106",
    #         "Type": "LINE",
    #         "Id": 1,
    #         "Confidence": 92.05397033691406,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.7353270053863525,
    #             "Height": 0.1138446107506752,
    #             "Left": 0.07170797139406204,
    #             "Top": 0.27627551555633545
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.07170797139406204,
    #                 "Y": 0.27627551555633545
    #             },
    #             {
    #                 "X": 0.807034969329834,
    #                 "Y": 0.037286028265953064
    #             },
    #             {
    #                 "X": 0.8187168836593628,
    #                 "Y": 0.15113063156604767
    #             },
    #             {
    #                 "X": 0.08338989317417145,
    #                 "Y": 0.39012011885643005
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "HTZ-627",
    #         "Type": "LINE",
    #         "Id": 2,
    #         "Confidence": 96.61856842041016,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.7224305868148804,
    #             "Height": 0.3387344777584076,
    #             "Left": 0.09452363103628159,
    #             "Top": 0.34045395255088806
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.09452363103628159,
    #                 "Y": 0.34045395255088806
    #             },
    #             {
    #                 "X": 0.8169542551040649,
    #                 "Y": 0.20427235960960388
    #             },
    #             {
    #                 "X": 0.8371139764785767,
    #                 "Y": 0.5430068373680115
    #             },
    #             {
    #                 "X": 0.1146833747625351,
    #                 "Y": 0.6791884303092957
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "13rsza.",
    #         "Type": "LINE",
    #         "Id": 3,
    #         "Confidence": 72.5882797241211,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.22880719602108002,
    #             "Height": 0.03999384120106697,
    #             "Left": 0.5348837375640869,
    #             "Top": 0.6595460772514343
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.5348837375640869,
    #                 "Y": 0.6595460772514343
    #             },
    #             {
    #                 "X": 0.7636909484863281,
    #                 "Y": 0.6008010506629944
    #             },
    #             {
    #                 "X": 0.7669327855110168,
    #                 "Y": 0.6407949328422546
    #             },
    #             {
    #                 "X": 0.5381256341934204,
    #                 "Y": 0.6995398998260498
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "105",
    #         "Type": "WORD",
    #         "Id": 7,
    #         "ParentId": 1,
    #         "Confidence": 98.02530670166016,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.03147870674729347,
    #             "Height": 0.023004785180091858,
    #             "Left": 0.7576894164085388,
    #             "Top": 0.05740987882018089
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.7576894164085388,
    #                 "Y": 0.05740987882018089
    #             },
    #             {
    #                 "X": 0.7861965298652649,
    #                 "Y": 0.04405874386429787
    #             },
    #             {
    #                 "X": 0.789947509765625,
    #                 "Y": 0.06675567477941513
    #             },
    #             {
    #                 "X": 0.7614403367042542,
    #                 "Y": 0.08144192397594452
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "106",
    #         "Type": "WORD",
    #         "Id": 9,
    #         "ParentId": 1,
    #         "Confidence": 98.56523132324219,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.03093607909977436,
    #             "Height": 0.024323005229234695,
    #             "Left": 0.7794448733329773,
    #             "Top": 0.07076101750135422
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.7794448733329773,
    #                 "Y": 0.07076101750135422
    #             },
    #             {
    #                 "X": 0.8079519867897034,
    #                 "Y": 0.058744993060827255
    #             },
    #             {
    #                 "X": 0.8117029070854187,
    #                 "Y": 0.08277703821659088
    #             },
    #             {
    #                 "X": 0.7816954255104065,
    #                 "Y": 0.09612817317247391
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "104",
    #         "Type": "WORD",
    #         "Id": 6,
    #         "ParentId": 1,
    #         "Confidence": 98.62338256835938,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.032843612134456635,
    #             "Height": 0.024323005229234695,
    #             "Left": 0.7396849393844604,
    #             "Top": 0.08811748772859573
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.7396849393844604,
    #                 "Y": 0.08811748772859573
    #             },
    #             {
    #                 "X": 0.7696924209594727,
    #                 "Y": 0.07476635277271271
    #             },
    #             {
    #                 "X": 0.773443341255188,
    #                 "Y": 0.09879839420318604
    #             },
    #             {
    #                 "X": 0.7426856756210327,
    #                 "Y": 0.11214952915906906
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "ha",
    #         "Type": "WORD",
    #         "Id": 8,
    #         "ParentId": 1,
    #         "Confidence": 67.82682800292969,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.038279496133327484,
    #             "Height": 0.03218292444944382,
    #             "Left": 0.7674418687820435,
    #             "Top": 0.13351134955883026
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.7674418687820435,
    #                 "Y": 0.13351134955883026
    #             },
    #             {
    #                 "X": 0.804201066493988,
    #                 "Y": 0.12283044308423996
    #             },
    #             {
    #                 "X": 0.8072018027305603,
    #                 "Y": 0.15487316250801086
    #             },
    #             {
    #                 "X": 0.7696924209594727,
    #                 "Y": 0.16555407643318176
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "106",
    #         "Type": "WORD",
    #         "Id": 5,
    #         "ParentId": 1,
    #         "Confidence": 97.22907257080078,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.03612377494573593,
    #             "Height": 0.029525380581617355,
    #             "Left": 0.07576894015073776,
    #             "Top": 0.307076096534729
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.07576894015073776,
    #                 "Y": 0.307076096534729
    #             },
    #             {
    #                 "X": 0.11027757078409195,
    #                 "Y": 0.2963951826095581
    #             },
    #             {
    #                 "X": 0.11327832192182541,
    #                 "Y": 0.3257676959037781
    #             },
    #             {
    #                 "X": 0.07801950722932816,
    #                 "Y": 0.33778372406959534
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "HTZ-627",
    #         "Type": "WORD",
    #         "Id": 10,
    #         "ParentId": 2,
    #         "Confidence": 96.61856842041016,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.7351539731025696,
    #             "Height": 0.3393338620662689,
    #             "Left": 0.09452363103628159,
    #             "Top": 0.34045395255088806
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.09452363103628159,
    #                 "Y": 0.34045395255088806
    #             },
    #             {
    #                 "X": 0.8169542551040649,
    #                 "Y": 0.20427235960960388
    #             },
    #             {
    #                 "X": 0.8371139764785767,
    #                 "Y": 0.5430068373680115
    #             },
    #             {
    #                 "X": 0.1146833747625351,
    #                 "Y": 0.6791884303092957
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "D",
    #         "Type": "WORD",
    #         "Id": 4,
    #         "ParentId": 0,
    #         "Confidence": 89.84026336669922,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.13351978361606598,
    #             "Height": 0.08631288260221481,
    #             "Left": 0.29482370615005493,
    #             "Top": 0.257676899433136
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.29482370615005493,
    #                 "Y": 0.257676899433136
    #             },
    #             {
    #                 "X": 0.2933233380317688,
    #                 "Y": 0.12416555732488632
    #             },
    #             {
    #                 "X": 0.3795948922634125,
    #                 "Y": 0.1214953288435936
    #             },
    #             {
    #                 "X": 0.3810952603816986,
    #                 "Y": 0.2536715567111969
    #             }
    #             ]
    #         }
    #         },
    #         {
    #         "DetectedText": "13rsza.",
    #         "Type": "WORD",
    #         "Id": 11,
    #         "ParentId": 3,
    #         "Confidence": 72.5882797241211,
    #         "Geometry": {
    #             "BoundingBox": {
    #             "Width": 0.2362280935049057,
    #             "Height": 0.04012501984834671,
    #             "Left": 0.5348837375640869,
    #             "Top": 0.6595460772514343
    #             },
    #             "Polygon": [
    #             {
    #                 "X": 0.5348837375640869,
    #                 "Y": 0.6595460772514343
    #             },
    #             {
    #                 "X": 0.7636909484863281,
    #                 "Y": 0.6008010506629944
    #             },
    #             {
    #                 "X": 0.7669327855110168,
    #                 "Y": 0.6407949328422546
    #             },
    #             {
    #                 "X": 0.5381256341934204,
    #                 "Y": 0.6995398998260498
    #             }
    #             ]
    #         }
    #         }
    #     ],
    #     "TextModelVersion": "3.0",
    #     "ResponseMetadata": {
    #         "RequestId": "861427fb-a9e4-441a-9993-4bffe0db197f",
    #         "HTTPStatusCode": 200,
    #         "HTTPHeaders": {
    #         "content-type": "application/x-amz-json-1.1",
    #         "date": "Thu, 24 Dec 2020 05:21:08 GMT",
    #         "x-amzn-requestid": "861427fb-a9e4-441a-9993-4bffe0db197f",
    #         "content-length": "5215",
    #         "connection": "keep-alive"
    #         },
    #         "RetryAttempts": 0
    #     }
    # }
    # json_formatted_response = json.dumps(response, indent=2)

    print("\n===== response =====")
    keys = []
    values = []
    # print(json_formatted_response)

    # for element in response['TextDetections']:
    #     print(element['Geometry']['BoundingBox']['Width'])
    #     keys.append(element['DetectedText'])
    #     values.append(element['Geometry']['BoundingBox']['Width'])
    # width_dict = dict(zip(keys, values))
    # sorted_width_dict = dict(sorted(width_dict.items(), key=lambda item: item[1], reverse = True))
    # print(sorted_width_dict)
    
    # for key, value in width_dict.items() :
    #     if (len(key)>7 or len(key)<6):
    #         del sorted_width_dict[key]
    # print(sorted_width_dict)

    result = []

    i = 0
    for element in response['TextDetections']:
        if (len(element['DetectedText'])==6) or (len(element['DetectedText'])==7) or (len(element['DetectedText'])==8):
            if(element['Type'] == 'LINE'):
                if(element['DetectedText'].find('.')>=0):
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

                
    result = sorted(result, key=lambda k: k.get('Confidence'), reverse=True)
    result = sorted(result, key=lambda k: k['Geometry']['BoundingBox'].get('Width'), reverse=True)
    
    for i in result:
        print(i['DetectedText'])
        print(i['Geometry']['BoundingBox']['Width'])
        print()

    print(result[0]['DetectedText'])
    print()

    if (result[0]['DetectedText'].find('.')>=0):
        lisence_plate = result[0]['DetectedText'].split('.')
        print(lisence_plate)
        license_plate_head = result[0]['DetectedText'].split('.')[0]
        license_plate_tail = result[0]['DetectedText'].split('.')[1]
    elif (result[0]['DetectedText'].find('-')>=0):
        lisence_plate = result[0]['DetectedText'].split('-')
        print(lisence_plate)
        license_plate_head = result[0]['DetectedText'].split('-')[1]
        license_plate_tail = result[0]['DetectedText'].split('-')[1]
    elif (len(result[0]['DetectedText'])) == 6 or (len(result[0]['DetectedText'])) == 7 :
        print(result[0]['DetectedText'])
        license_plate_head = result[0]['DetectedText'][:3]
        license_plate_tail = result[0]['DetectedText'][3:]
        print(license_plate_head)
        print(license_plate_tail)

    my_data = {
        "camera_id" : "A01",
        "lisence_plate_head" : license_plate_head,
        "lisence_plate_tail" : license_plate_tail
        }

    res = requests.post('https://michael7105.csie.io/carLocatonSearch/Manager/location_update.php', data = my_data)

    print(res)

    # time.sleep(100)
    input()

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
