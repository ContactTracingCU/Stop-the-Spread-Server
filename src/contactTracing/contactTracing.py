# contactTracing.py will determine if there was positive contact between two users
# program will determined this by implementing different algorithms 
# these algorithms include:
# difference in feet between coordinates 
# difference in minutes between unix timestamps
# import time
import authProvider as ap
import timestampMath as tsm
import coordinateMath as cm

print('Contact tracing worker file running...')
locations, users, testedPositive, db = ap.setUpFirebase()

# BEGINING OF CONTACT TRACING ALGORITHM
testedPositive = db.child('testedPositive').get().val()
if testedPositive != None:
  # key is uid value is true or flase
  for userID, isPositive in testedPositive.items():
    if isPositive == True:
      userLocationInfo = users[userID]['locationInfo']['locations']
      userLocations = []

      # get all counties this user has visited
      # key is county, value is timestamp
      for key, value in userLocationInfo.items():
        userLocations.append(key)

      # step through all the counties that the positive user visited and
      # get all the locations from all users in that county
      for county in userLocations:
        positiveUserLocations = {}        # dictionary for the positive user locations
        otherUserLocations = {}           # dictionary for all the other users locations
        allLocations = locations[county]  # dictionary of all the tracked locations in current county

        positiveContacts = []             # list to keep track of what userID came in contact with the positive user

        for timestamp, locationInfoWithRandomString in allLocations.items():
          for randomString, locationInfo in locationInfoWithRandomString.items():
            if locationInfo['user'] == userID:
              positiveUserLocations[timestamp] = locationInfo
            else:
              otherUserLocations[timestamp] = locationInfo

        lats = [None, None]
        longs = [None, None]
        for i, positiveCoordinates in positiveUserLocations.items():
          lats[0] = positiveCoordinates['lat']
          longs[0] = positiveCoordinates['long']
          for j, otherCoordinates in otherUserLocations.items():
            lats[1] = otherCoordinates['lat']
            longs[1] = otherCoordinates['long']
            distanceBetweenCoordinates = cm.coordinateMath(lats, longs)
            if distanceBetweenCoordinates <= 6:
              if(tsm.timestampMath(int(i), int(j))):
                print('Positive contact for userID: {} with positive userID: {} @ {}'.format(otherCoordinates['user'], positiveCoordinates['user'], county))
                db.child('positiveContact').child(otherCoordinates['user']).child(j).update({'lat': lats[1], 'long': longs[1]})

        db.child("testedPositive").child(userID).remove()
    else:
      db.child("testedPositive").child(userID).remove()
# time.sleep(10)