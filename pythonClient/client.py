"""
order, address for pickup, address for drop off, customer name. customer phone number or email, restaurant phone and email

import socket

s = socket.socket()
host = "127.0.0.1"
port = 56789

s.connect((host,port))

orderList = ["FOOD_FOOD_FOOD_FOOD_FOOD", "ADDRESS_PICKUP", "ADDRPESS_DROPOFF", "CUSTOMER_NAME", "CUSTOMER_PHONE", "RESTAURANT_PHONE"]
s.send(orderList)
s.recv(1024)
s.close
"""

import requests
import json

emailTestPost = requests.post('http://127.0.0.1:8000/emails/', json = {
	'order': {
		'item1':'FOOD1',
		'item2':'FOOD2',
		'item3':'FOOD3'
	},
	'pickupAddress':'ADDRESS_PICKUP',
	'dropoffAddress':'ADDRPESS_DROPOFF',
	'customerName':'CUSTOMER_NAME',
	'customerPhone':'CUSTOMER_PHONE',
	'restarauntPhone':'RESTAURANT_PHONE',})

print(emailTestPost)
print("done!")