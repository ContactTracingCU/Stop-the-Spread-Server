import pyrebase
import time

config = {
  "apiKey": "AIzaSyCl2hHT9n6qPGyoqTOXsRqi_3QJcETx2YA",
  "authDomain": "sts0-76694.firebaseapp.com",
  "databaseURL": "https://sts0-76694.firebaseio.com/",
  "storageBucket": "sts0-76694.appspot.com"
}
# get a reference to the firebase
firebase = pyrebase.initialize_app(config)
# get a reference to the auth service
auth = firebase.auth()
# get a reference to the database service
db = firebase.database()
# get a reference to the storage service
storage = firebase.storage()

# get dictionary of locationss
locations = db.child('locations').get().val()
# get dictionary of users
users = db.child('users').get().val()

testOfRegion = 'Denver County'

while True:
  for key, value in locations.items():
    if key == testOfRegion:
        print('Found a matching region to a positive case: {}'.format(key))
        # run coordinate math on all locations in this region
    else:
        print('Positive case reported at {}; skipping {} region'.format(testOfRegion, key))
  time.sleep(10)
  

