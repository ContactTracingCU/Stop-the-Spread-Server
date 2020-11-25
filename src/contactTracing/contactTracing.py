import pyrebase
import time
import coordinateMath

print('Contact tracing worker file up')

apiKey = "AIzaSyCl2hHT9n6qPGyoqTOXsRqi_3QJcETx2YA"
authDomain = "sts0-76694.firebaseapp.com"
databaseURL = "https://sts0-76694.firebaseio.com/"
storageBucket = "sts0-76694.appspot.com"

config = {
  "apiKey": apiKey,
  "authDomain": authDomain,
  "databaseURL": databaseURL,
  "storageBucket": storageBucket
}

# get a reference to the firebase, auth service, database service and storage service
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

# get dictionary of locations, users and testedPositive users
locations = db.child('locations').get().val()
users = db.child('users').get().val()
testedPositive = db.child('testedPositive').get().val()

print(
'''
Initialized necesarry firebase components
apiKey : {}
authDomain : {}
databaseURL : {}
storageBucket : {}
'''.format(apiKey, authDomain, databaseURL, storageBucket)
)

for key, value in testedPositive.items():
  if value == True:
    print('User: {} has tested positive, run tests'.format(key))
    # TODO 
    # delete user from testedPositive to remove off 'queue'
    userLocationInfo = users[key]['locationInfo']['locations']
    userLocations = []

    for key, value in userLocationInfo.items():
      userLocations.append(key)
    print('User has been to {} location(s):'.format(len(userLocations)))
    for i in userLocations:
      print('\t{}'.format(i))
    

  else:
    # TODO 
    # delete that user
    # add logic to app to only send negative results
    print('User: {} has tested negative, don\'t runt tests'.format(key))

