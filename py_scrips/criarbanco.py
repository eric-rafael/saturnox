
# importing required libraries
import mysql.connector
import os
from dotenv import load_dotenv

dataBase = mysql.connector.connect(
  host = os.getenv("HOST"),
  user = os.getenv("USER"),
  passwd = os.getenv("PASSWD")
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE saturnox")