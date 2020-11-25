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

# key is uid value is true or flase
for userID, isPositive in testedPositive.items():
  if isPositive == True:
    print('User: {} has tested positive, run tests'.format(userID))
    # TODO 
    # delete user from testedPositive to remove off 'queue'

    userLocationInfo = users[userID]['locationInfo']['locations']
    userLocations = []

    # key is county, value is timestamp
    for key, value in userLocationInfo.items():
      userLocations.append(key)
    print('User has been to {} location(s):'.format(len(userLocations)))
    for i in userLocations:
      print('\t{}'.format(i))
    print('\n\n')

    # step through all the users visited counties and collect the data for that county from locations
    for county in userLocations:
      currentCounty = locations[county]   # dictionary of all the tracked locations in current county

      allLocations = {}
      currentUserLocations = {}
      otherUserLocations = {}

      positiveContacts = []
      locationData = []

      for key, value in currentCounty.items():
        allLocations[key] = value
        
      # key = timestamp ; value = dictionary of location info
      for key, value in allLocations.items():
        locationData.append(value)

      currentUserLocationNumber = 1
      otherUsersLocationNumber = 1
      for i in locationData:
        # key = random string ; value = locatino info
        for key, value in i.items():
          if value['user'] == userID:
            currentUserLocations['Location_{}'.format(currentUserLocationNumber)] = value
            currentUserLocationNumber += 1
          else:
            otherUserLocations['Location_{}'.format(otherUsersLocationNumber)] = value
            otherUsersLocationNumber += 1

      print('positive user locations')
      for key, value in currentUserLocations.items():
        print(key, value)
      print('\n')
      print('other users locations')
      for key, value in otherUserLocations.items():
        print(key, value)
      print('****************\nend of {}\n****************'.format(county))
    print('****************\nend of {}\n****************'.format(userID))

  else:
    # TODO 
    # delete that user
    # add logic to app to only send negative results
    # print('User: {} has tested negative, don\'t runt tests'.format(key))
    pass
