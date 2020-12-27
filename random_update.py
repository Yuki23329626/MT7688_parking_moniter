import boto3
import json
import time
import string
import os
import requests
import mysql.connector
from mysql.connector import Error

# Obtain connection string information from the portal
connection= mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd=os.environ['MYSQL_ROOT_PASSWORD'],
    db ='pi_parking_monitor',)

cursor = connection.cursor()

sql = "UPDATE parking_space SET lisence_plate_head = %s lisence_plate_tail = %s WHERE camera_id = %s;"

cursor.execute(sql, ('ACE', '1234', 'A02'))

connection.commit()
cursor.close()
connection.close()
