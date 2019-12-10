# Code written by Jerin Rajan on 09th Dece 2019,
# Email - jrajan @jprtech.co.uk

'''
Please develop a data processing application which subscribes to
the provided MQTT broker and consumes data from the following MQTT topic with
the format shown:

* write and structure a simple backend application in an appropriate language
of your choice
* parse and transform streamed telemetry data
* deliver a component to integrate into a stack of technologies
'''

'''
IMPORTANT NOTE:
================
- Please read myAppREADME.txt file before running the script.
- I have demonstrated my Python skills in reading and extracting information
from JSON files through this code.
- I dont have any experience with implementatiion of MQTT protocol.
- I am keen to learn this as i have looked up some tutorials online.

'''

import json
import myAppH

# Read INPUT JSON File
coordinates_data = myAppH.openJSON('position.json')
speed_data = myAppH.openJSON('speed.json')
event_data = myAppH.openJSON('event.json')

# Extracting and Parsing the JSON data
# 1) Car Status - Position Value & Timestamp
carCoordinates = coordinates_data['value']
carCoordinates_timestamp = coordinates_data['timestamp']
# 2) Car Status - Speed Value & Timestamp
speed = speed_data['value']
speed_timestamp = speed_data['timestamp']
# 3) Car Event - Text & Timestamp
event = event_data['text']
event_timestamp = event_data['timestamp']

# Outputting the key information extracted from the sources.
# 1) CarStatus Coordinates
print('Position Value: ', carCoordinates)
print('Position Timestamp: ', carCoordinates_timestamp)
# 2) App - Speed
print('Speed Value: ', speed)
print('Speed Timestamp: ', speed_timestamp)
# 3) App - Event
print('Event Status: ', event)
print('Event Timestamp: ', event_timestamp)

# The output information from MyAPP:
# - carCoordinates
# - speed
# - event
# needs to be packaged and send via MQTT Broker as MQTT Data packets.
