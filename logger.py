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
    cursor.execute(query, [int(epoch_time), float(spl[0]), float(spl[1]), float(spl[2])])