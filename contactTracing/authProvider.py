# import pyrebase
import firebase_admin
from firebase_admin import db

def setUpFirebase():

    cred = firebase_admin.credentials.Certificate("sts0-76694-firebase-adminsdk-b669p-bfc15bac9b.json")
    apiKey = "AIzaSyCl2hHT9n6qPGyoqTOXsRqi_3QJcETx2YA"
    authDomain = "sts0-76694.firebaseapp.com"
    databaseURL = "https://sts0-76694.firebaseio.com/"
    storageBucket = "sts0-76694.appspot.com"

    
    config = {
    # "apiKey": apiKey,
    # "authDomain": authDomain,
    "databaseURL": databaseURL,
    "storageBucket": storageBucket
    }
    """
    # get a reference to the firebase, auth service, database service and storage service
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    db = firebase.database()
    storage = firebase.storage()"""

    firebase_admin.initialize_app(cred, config)

    # get dictionary of locations, users and testedPositive users
    locations = db.reference('locations').get()
    users = db.reference('users').get()
    testedPositive = db.reference('testedPositive').get()

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