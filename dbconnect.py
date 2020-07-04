import mysql.connector
import os
import sys

os.environ["USERNAME"] = "ghinestrosa"
os.environ['MYSQLPASSWORD'] = "2021Dubio!"

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ['MYSQLPASSWORD']
HOST = "3.17.193.54"
PORT = "54322"

conn = mysql.connector.connect(user=USERNAME, 
                               password=PASSWORD,
                               host=HOST,
                               port=3306)
                               #database='employees')