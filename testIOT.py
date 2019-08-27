import time
from firebase import firebase
from datetime import datetime
# from grovepi import *

# led = 4
# pinMode(led,"OUTPUT")
# time.sleep(1)

firebase = firebase.FirebaseApplication('https://test-960d0.firebaseio.com/')

while True:
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%m-%Y %I:%M %p")

    result = firebase.get('/MyTestData','timestamp')

    if result == timestampStr:
        result = firebase.get('/MyTestData','found')
        print(result)

        if(result == "Althony Lim" or result == "Clemente" or result == "Maheswar" or result == "Cia Ler"):
            print('Open')
            # digitalWrite(led,1)
            # time.sleep(1)
            # digitalWrite(led,0)
            # time.sleep(0.1)
        elif (result == "Unknown"):
            print("Close")
            # time.sleep(1)
            # digitalWrite(led,0)
            # time.sleep(0.1)
            # digitalWrite(led,1)
            # time.sleep(0.1)
            # digitalWrite(led,0)
            # time.sleep(0.1)
            # digitalWrite(led,1)
            # time.sleep(0.1)
            # digitalWrite(led,0)
            # time.sleep(0.1)
    else:
        print("Nothing Detected")