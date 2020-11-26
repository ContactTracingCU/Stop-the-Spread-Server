import pyrebase
import time
import authProvider
import coordinateMath

# TODO 
# add while loop to check every x seconds after deletion of queue so we don't calculate on same information twice

print('Contact tracing worker file running...')
locations, users, testedPositive, db = authProvider.setUpFirebase()

# BEGINING OF CONTACT TRACING ALGORITHM
  # TODO 
  # in isPositive == True:
    # delete user from testedPositive to remove off 'queue'
while True:
  testedPositive = db.child('testedPositive').get().val()
  if testedPositive != None:
    # key is uid value is true or flase
    for userID, isPositive in testedPositive.items():
      if isPositive == True:
        print('User: {} has tested positive, run tests'.format(userID))

        userLocationInfo = users[userID]['locationInfo']['locations']
        userLocations = []

        # get all counties this user has visited
        # key is county, value is timestamp
        for key, value in userLocationInfo.items():
          userLocations.append(key)
        print('User has been to {} location(s):'.format(len(userLocations)))
        for i in userLocations:
          print('\t{}'.format(i))
        print('\n')

        positiveUserLocations = {}        # dictionary for the positive user locations
        otherUserLocations = {}           # dictionary for all the other users locations

        # step through all the counties that the positive user visited and
        # get all the locations from all users in that county
        for county in userLocations:
          allLocations = locations[county]  # dictionary of all the tracked locations in current county

          positiveContacts = []             # list to keep track of what userID came in contact with the positive user

          currentUserLocationNumber = 1     # variables too keep track of the location number to set as key
          otherUsersLocationNumber = 1

          for timestamp, locationInfoWithRandomString in allLocations.items():
            for randomString, locationInfo in locationInfoWithRandomString.items():
              if locationInfo['user'] == userID:
                positiveUserLocations['Location_{}'.format(currentUserLocationNumber)] = locationInfo
                currentUserLocationNumber += 1
              else:
                otherUserLocations['Location_{}'.format(otherUsersLocationNumber)] = locationInfo
                otherUsersLocationNumber += 1
        lats = []
        longs = []
        for i, positiveCoordinates in positiveUserLocations.items():
          lats.append(positiveCoordinates['lat'])
          longs.append(positiveCoordinates['long'])
          for j, otherCoordinates in otherUserLocations.items():
            lats.append(otherCoordinates['lat'])
            longs.append(otherCoordinates['long'])

            distanceBetweenCoordinates = coordinateMath.coordinateMath(lats, longs)
            if distanceBetweenCoordinates <= 6:
              print('Positive contact for userID: {}'.format(userID))
              db.child('positiveContact').push({userID:'positiveContact'})
            else:
              print('Distance was greater than 6 feet')
            lats[1] = None
            longs[1] = None
          lats = []
          longs = []

        db.child("testedPositive").child(userID).remove()

      else:
        # TODO 
        # delete that user
        # add logic to app to only send negative results
        # print('User: {} has tested negative, don\'t runt tests'.format(key))
        pass
  else:
    print('no users to run contact tracing')
  time.sleep(10)
