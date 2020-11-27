# timestampMath.py will determine difference between two unix timestamps
# order of timestamps does not matter as long as they are valid unix times
import datetime

# # timestamps for testing
# # d1, d2 will return a positive contact
# # d1, d3 will return a negative contact
# d1 = 1606294329209
# d2 = 1606294593286
# # d3 = 1606294999287

# from datetime import datetime
# ts = int("1606294335209")
# ts /= 1000
# ass = int("1606294329209")
# ass /= 1000
# print(datetime.utcfromtimestamp(ass).strftime('%Y-%m-%d %H:%M:%S'))

# # if you encounter a "year is out of range" error the timestamp
# # may be in milliseconds, try `ts /= 1000` in that case
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

def timestampMath(time1, time2):
    # convert time to something we can perform math on
    cD1 = datetime.datetime.fromtimestamp(round(time1 / 1000))
    cD2 = datetime.datetime.fromtimestamp(round(time2 / 1000))

    # take converted time and get the difference in minutes
    difference = (cD1 - cD2).total_seconds() / 60

    # determine if the timestamp was in the last x minutes
    if(difference >= -10 and difference <= 10):
        # print('difference was a contact: {}'.format(difference))
        return True
    else:
        # print('difference was not a contact: {}'.format(difference))
        return False