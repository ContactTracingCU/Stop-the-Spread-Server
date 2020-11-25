import math
from matplotlib import pyplot as plt
from scipy.stats import pearsonr

convert = 20000 / 180
kmToFeet = 3280.84

# 39.691138, -105.046686
# 39.691072, -105.046600


# new york to boston
#longs = [-74.0060, -71.0589]
#lats = [40.7128, 42.36]

# local coordinates on the same block
lats = [39.691138, 39.691072]
longs = [-105.046686, -105.046600]

# radius of the eart
radius = 6378

# print(-104.673 * convert)

location1_lat = lats[0] * convert
location1_long = longs[0] * convert

location2_lat = lats[1] * convert
location2_long = longs[1] * convert

dist = math.sqrt((location2_lat - location1_lat)**2 + (location2_long-location1_long)**2)

distInFeet = dist * kmToFeet

print('Distance in a straight line from location 1 to location 2 is: {} feet'.format(distInFeet))
# print('Distance in a straight line from location 1 to location 2 is: {} miles'.format(distInFeet/5280))