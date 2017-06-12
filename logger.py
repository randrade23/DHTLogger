import serial
import MySQLdb
import secret
import time

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd=secret.pwd(),
                  db=secret.db())
cursor = conn.cursor()
query = "INSERT INTO dht(epoch, temperature, humidity, heatindex) VALUES(%d,%f,%f,%f)"

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    line = ser.readline()
    spl = line.split()
    epoch_time = int(time.time())
    cursor.execute(query, (epoch_time, spl[0], spl[1], spl[2]))