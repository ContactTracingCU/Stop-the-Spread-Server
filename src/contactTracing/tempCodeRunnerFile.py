      # # key = timestamp ; value = dictionary of location info
      # # get dictionary of only values and append to list 
      # for timestamp, locationInfo in allLocations.items():
      #   locationData.append(locationInfo)
        
      # currentUserLocationNumber = 1
      # otherUsersLocationNumber = 1
      # for i in locationData:
      #   # key = random string ; value = locatino info
      #   for key, value in i.items():
      #     if value['user'] == userID:
      #       currentUserLocations['Location_{}'.format(currentUserLocationNumber)] = value
      #       currentUserLocationNumber += 1
      #     else:
      #       otherUserLocations['Location_{}'.format(otherUsersLocationNumber)] = value
      #       otherUsersLocationNumber += 1