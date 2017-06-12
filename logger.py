import serial
import MySQLdb
import secret

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd=secret.pwd(),
                  db=secret.db())

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    