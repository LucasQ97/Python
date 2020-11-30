import mysql.connector
from mysql.connector import errorcode
from mysql.connector.errors import Error

con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            database="sistemareservas"
        )

cursorObj = con.cursor()