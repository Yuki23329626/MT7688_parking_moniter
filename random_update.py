import boto3
import json
import time
import string
import os
import requests
import mysql.connector
from mysql.connector import Error
import random

# Obtain connection string information from the portal
connection= mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd=os.environ['MYSQL_ROOT_PASSWORD'],
    db ='pi_parking_monitor',)

cursor = connection.cursor()

car = [
    'ABC2345',
    'ETR2345',
    'JHG1374',
    'LKJ9053',
    'CBV4658',
    'RQE9632',
    'IUY7532',
    'LJH1285',
    'POI9631',
    'VFR9596',
    'CDE0088',
    'NHY4689',
    'MJU3797',
    'QIK6536',
    'XSW8885',
    'CDE3457',
    'VRF7642',
    'JDF2325',
    'EUR6543',
    'DGS2234',
    'DKE4973',
    'EJK3947',
    'JER2094',
    'CMS2065',
    'IIU9834',
    'PLM3853',
    'QME3295',
    'IIU2844',
    'JHD3754',
    'AAQ9843'
    ]

camera = [
    'A02',
    'A03',
    'A04',
    'A05',
    'A06',
    'A07',
    'A08',
    'A09',
    'A10',
    'A11',
    'A12',
    'A13',
    'A14',
    'A15',
    'A16',
    'B01',
    'B02',
    'B03',
    'B04',
    'B05',
    'B06',
    'B07',
    'B08',
    'B09',
    'B10',
    'B11',
    'B12',
    'B13',
    'B14',
    'B15',
    'B16']

exist_camera = []
exist_car = []

while True:
    number = random.randint(1,5)
    cursor.execute("SELECT camera_id, lisence_plate_head, lisence_plate_tail FROM parking_space;")
    for (camera_id, lisence_plate_head, lisence_plate_tail) in cursor:
        exist_camera.append(camera_id)
        exist_car.append(lisence_plate_head + lisence_plate_tail)

    while number:
        random_camera_id = random.randint(0,30)
        sql = "UPDATE parking_space SET lisence_plate_head = %s, lisence_plate_tail = %s WHERE camera_id = %s;"
        random_car_id = random.randint(0,29)
        if(car[random_car_id] in exist_car):
            print('1')
            cursor.execute(sql, ("", "", camera[random_camera_id]))
            exist_car.remove(car[random_car_id])
            exist_camera.remove(camera[random_camera_id])
        if(camera[random_camera_id] in exist_camera):
            while True:
                print('2')
                random_camera_id = random.randint(0,30)
                print(random_camera_id)
                if camera[random_camera_id] not in exist_camera:
                    cursor.execute(sql, (car[random_car_id][:3], car[random_car_id][3:], camera[random_camera_id]))
                    exist_camera.append(camera[random_camera_id])
                    exist_car.append(car[random_car_id])
                    break
        else:
            print('3')
            cursor.execute(sql, (car[random_car_id][:3], car[random_car_id][3:], camera[random_camera_id]))
            exist_camera.append(camera[random_camera_id])
            exist_car.append(car[random_car_id])
        connection.commit()
        number -= 1
    print('end of round')
    time.sleep(5)

cursor.close()
connection.close()
