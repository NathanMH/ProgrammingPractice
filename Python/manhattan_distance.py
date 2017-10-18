"""####################
Author: Nathan Mador-House
Title: Manhattan Distance
####################"""

"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""

###################################################################
# 1. Imports and Readme
###################################################################

"""####################
Simple implementation of Manhattan Distance for data analysis and recommendation software
####################"""

import sys
sys.path.insert(0, "../assets")
from assets import music_preferences_dict

###################################################################
# 2. Functions
###################################################################

users = music_preferences_dict.users

def manhattan(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

def computeNearestNeighbour(username, users):
    """Creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances

def recommend(username, users):
    """Give list of recommendations"""
    nearest = computeNearestNeighbour(username, users)[0][1]
    recommendations = []
    neighbourRatings = users[nearest]
    userRatings = users[username]
    for artist in neighbourRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighbourRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

###################################################################
# 3. Main
###################################################################


###################################################################
# 4. Testing
###################################################################

print("Manhattan Distance: " + str(manhattan(users['Hailey'], users['Veronica'])))
print("Manhattan Distance: " + str(manhattan(users['Hailey'], users['Jordyn'])))
print(computeNearestNeighbour("Hailey", users))

print(recommend("Hailey", users))
