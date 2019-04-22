#!/usr/bin/python

import serial 
import MySQLdb
import psycopg2
import time

#establish connection to MySQL. You'll have to change this for your database.
dbConn = psycopg2.connect(host="ec2-50-19-109-120.compute-1.amazonaws.com",database="d7i76p9do8qnha", user="ggoqkekkefjkub", password="151614019057fb208ab3ed5fed64297891e890f500d44a661591b74f8308731e") or die ("could not connect to database")
#open a cursor to the database


device = '/dev/ttyUSB0' #this will have to be changed to the serial port you are using
print "Trying...",device 
i = 1 
while i ==1:
	cursor = dbConn.cursor()
	arduino = serial.Serial(device, 9600, timeout=3)
	arduino.read()
	data = arduino.readline()  #read the data from the arduino
	pieces = data.split("\t")  #split the data by the tab
  	print data
  	#Here we are going to insert the data into the Database
	cursor.execute("INSERT INTO weatherData3 VALUES (%s,%s,%s,%s,%s,%s)",(pieces[0],pieces[1],pieces[2],pieces[3],pieces[4],pieces[5]))
	dbConn.commit() #commit the insert
	cursor.close()  #close the cursor
