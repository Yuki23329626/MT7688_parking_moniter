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
    'DGS2234'
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

exist = []

while True:
    number = random.randint(1,5)
    cursor.execute("SELECT camera_id, lisence_plate_head, lisence_plate_tail FROM parking_space;")
    for (camera_id, lisence_plate_head, lisence_plate_tail) in cursor:
        exist.append(lisence_plate_head + lisence_plate_tail)

    while number:
        random_camera_id = random.randint(1,31)
        sql = "UPDATE parking_space SET lisence_plate_head = %s, lisence_plate_tail = %s WHERE camera_id = %s;"
        random_car_id = random.randint(1,20)
        if(car[random_car_id] in exist):
            cursor.execute(sql, ("", "", camera[random_camera_id]))
            exist.remove(car[random_car_id])
        else:
            cursor.execute(sql, (car[random_car_id][:3], car[random_car_id][3:], camera[random_camera_id]))
        connection.commit()
        number -= 1
    input()

cursor.close()
connection.close()
