# Name: Samar Joshi
# Student ID: 241ADB043
# Github:
#importing libraries
import csv
import json
from datetime import datetime
#opening csv file and reading it line by line
with open('db.csv',encoding='utf-8-sig') as opener:
    reader = csv.reader(opener,delimiter=',')
    # skipping header file
    header = next(reader)
    for line in reader:
        if line[0].startswith('#'): # skipping comment lines
         continue
        flight = dict(zip(header, line))  # combining header + row
        # for easier changing
        flight_id = flight['flight_id']
        origin = flight['origin']
        destination = flight['destination']
        departure = flight['departure_datetime']
        arrival = flight['arrival_datetime']
        price = flight['price']
        depart = datetime.strptime(departure, "%Y-%m-%d %H:%M")
        arrive = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
        # for checking the validitiy of flight details
        if not (2 <=len(flight_id) <= 8):
            print("Invalid Flight ID")
        if not len(origin) == 3 or not origin.isupper():
            print("Invalid Origin")  
        if not len(destination) == 3 or not destination.isupper():
            print("Invalid Destination")
        if not float(price) > 0:
            print("Invalid Price")
        if arrival <= departure:
            print("Invalid Arrival/Departure")
            
        print(flight)