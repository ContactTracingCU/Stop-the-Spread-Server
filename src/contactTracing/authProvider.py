import pyrebase

def setUpFirebase():
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

    # print(
    # '''
    # Initialized necessary firebase components
    # apiKey : {}
    # authDomain : {}
    # databaseURL : {}
    # storageBucket : {}
    # '''.format(apiKey, authDomain, databaseURL, storageBucket)  
    # )

    return locations, users, testedPositive, db