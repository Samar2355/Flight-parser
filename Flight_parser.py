# Name: Samar Joshi
# Student ID: 241ADB043
# Github:https://github.com/Samar2355/Flight-parser
# Importing Libaries
import csv
import json
from datetime import datetime
# For appending flights to valid or invalid
valid = []
invalid = []
# Reading the csv file line by line
with open('db.csv', encoding='utf-8-sig') as opener:
    reader = csv.reader(opener, delimiter=',')
    #skipping the header
    header = next(reader)
    #skipping the comment line
    for line in reader:
        if line[0].startswith('#'):
            continue
        #making the header line in a dict
        flight = dict(zip(header, line))
        error = []
        #using the dict to easily change required error validation
        flight_id = flight['flight_id']
        origin = flight['origin']
        destination = flight['destination']
        departure = flight['departure_datetime']
        arrival = flight['arrival_datetime']
        price = flight['price']

        # To check for correct time of arrival and ddeparture
        try:
            depart = datetime.strptime(departure, "%Y-%m-%d %H:%M")
        except ValueError:
            error.append("Invalid Departure")

        try:
            arrive = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
        except ValueError:
            error.append("Invalid Arrival")
            

        # To check for other errors such as flight id, origin, destination and price
        if not (2 <= len(flight_id) <= 8):
            error.append("Invalid Flight ID")
        if not (len(origin) == 3 and origin.isupper()):
            error.append("Invalid Origin")
        if not (len(destination) == 3 and destination.isupper()):
            error.append("Invalid Destination")
        try:
            if not float(price) > 0:
                error.append("Invalid Price")
        except ValueError:
            error.append("Invalid Price")

        # To check if arrive comes before or at the same time as departure
        if depart and arrive:
            if arrive <= depart:
                error.append("Invalid Arrival/Departure")

        # Append to lists for the error and json file
        if error:
            invalid.append(f"{flight_id}: {', '.join(error)}")
        else:
            valid.append(flight)

# Writing to json and error file
with open('db.json', 'w') as jsonfile:
    json.dump(valid, jsonfile, indent=4)

with open('error.txt', 'w') as f:
    for line in invalid:
        f.write(line + '\n')
