'''
 * Yu-Jhe Li.
 * Dept. Communication Institute at National Taiwan University  
 * 
'''
import json
import numpy as np
import requests
import sys

#Parse the userID from input
user_id = sys.argv[1]

#Request the result by url
r = requests.get('http://fg-69c8cbcd.herokuapp.com/user/'+str(user_id))

#Save the result to json format
user = json.loads(r.text)

#Count the number of friends
counter= 1

#Print the info. of the user
print "For the user ID: {}".format(user_id)
print "Name: {}\n".format(user['name'])
print "Friend list:"
print "----------------------------------"


#Query the friends of the input user
for i in user['friends']:

    #request
    req = requests.get('http://fg-69c8cbcd.herokuapp.com/user/'+str(i))

    #Save the result to json format
    friend = json.loads(req.text)

    print "{}".format(friend['name'])

    for j in friend['friends']:

        #request            
        req2 = requests.get('http://fg-69c8cbcd.herokuapp.com/user/'+str(j))

        #Save the result to json format
        new_user = json.loads(req2.text)

        print "has friend named {}".format(new_user['name'])

    print "----------------------------------"