import boto3
import json
import time
import string
import os
import requests
import mysql.connector as mc
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
    'host':'54.64.81.91',
    'port':'8080',
    'user':'root',
    'password':os.environ['MYSQL_ROOT_PASSWORD'],
    'database':'pi_parking_monitor'
}

# Construct connection string
try:
    connection = mc.connect(**config)
    print("Connection established")
except mc.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(e)
else:
    cursor = connection.cursor()

    # # Drop previous table of same name if one exists
    # cursor.execute("DROP TABLE IF EXISTS inventory;")
    # print("Finished dropping table (if existed).")

    # # Create table
    # cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    # print("Finished creating table.")

    # Insert some data into table
    cursor.execute("UPDATE parking_space SET lisence_plate_head=ACE lisence_plate_tail=2468 WHERE camera_id=A02")
    response = connection.commit()
    print('response:', response)
    cursor.close()
    connection.close()
    print("Done.")

