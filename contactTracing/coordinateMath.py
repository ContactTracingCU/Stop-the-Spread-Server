# coordinateMath.py takes two coordinates and returns distance in feet
# oder of coordinates in lat and long lists (function parameters) does not matter
import math

def coordinateMath(lats, longs):
    # convert to km * convert to ft
    convert = (20000 / 180) * 3280.84

    # radius of the eart
    radius = 6378

    location1_lat = lats[0] * convert
    location1_long = longs[0] * convert
    location2_lat = lats[1] * convert
    location2_long = longs[1] * convert

    dist = math.sqrt((location2_lat - location1_lat)**2 + (location2_long-location1_long)**2)

    # print('Distance in a straight line from location 1 to location 2 is: {} feet'.format(distInFeet))

    return dist