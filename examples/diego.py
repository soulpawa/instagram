#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
# https://github.com/LevPasha/Instagram-API-python
# https://www.kdnuggets.com/2017/08/instagram-python-data-analysis.html

from InstagramAPI import InstagramAPI
import time
from moviepy.editor import *

api = InstagramAPI("ayuno_intermitente", "Zogeidinsta1")
if api.login():
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login succes!")

    #1
    api.getProfileData()
    result = api.LastJson
    print("Account Status:" + str(result['status']))
    print("Username: " + result['user']['username'])

    api.timelineFeed()
    timelineFeed = api.LastJson
    '''print("####timelineFeed######################################################: ")
print(timelineFeed)'''

    print("username: " + str(timelineFeed['items'][0]['user']['username']))
    print("comment_count: " + str(timelineFeed['items'][0]['comment_count']))
    # print("text: " + str(timelineFeed['items'][0]['caption']['text']))
    print("like_count: " + str(timelineFeed['items'][0]['like_count']))

else:
    print("Can't login!")


api.getProfileData()
user_id = api.LastJson
user_id = user_id['user']['pk']
print("user_id:" + str(user_id))

api.getUserFollowings(user_id)
getUserFollowings = api.LastJson
print("getUserFollowings [0]:" + str(getUserFollowings['users'][0]['username']))
print("getUserFollowings len:" + str(len(getUserFollowings['users'])))

api.getUserFollowers(user_id)
getUserFollowers = api.LastJson
print("getUserFollowers [0]: " + str(getUserFollowers['users'][0]['username']))
print("getUserFollowers len: " + str(len(getUserFollowers['users'])))

followers_list=api.LastJson['users']
print("followers_list: " + str(followers_list))
print("getUserFollowers len: " + str(len(followers_list)))


# ########FOLLOW############# FUNCIONA
'''
import json
testPK = "1267406320"
def follow(api, userId):
    data = json.dumps({'_uuid': api.uuid, '_uid': api.username_id, 'user_id': userId, '_csrftoken': api.token})
    return api.SendRequest('friendships/create/' + str(userId) + '/', api.generateSignature(data))

#follow(api,"curysdd")
follow(api,testPK)
'''

# ########UNFOLLOW############# FUNCIONA
testPK = "1267406320" #https://www.instagram.com/gloriavizcaya/?hl=en
api.unfollow(testPK)


# #######################ELIMINAR IDLE FOLLOWERS################################################
print("ELIMINAR IDLE FOLLOWERS")
api.getUserFollowers(user_id)
getUserFollowers = api.LastJson
print("username: " + str(getUserFollowers['users'][0]['username']))

for f in getUserFollowers['users']:
    print("username: " + str(f['username']) + " //PK: " + str(f['pk']))


# #######################FOLLOW FOLLOWERS' FOLLOWERS################################################
api.getUserFollowers("289548141") # username: sirdavid10 //PK: 289548141
getUserFollowers = api.LastJson
print("getUserFollowers [0]: " + str(getUserFollowers['users'][0]['username']))
print("getUserFollowers len: " + str(len(getUserFollowers['users'])))
for f in getUserFollowers['users']:
    print("username: " + str(f['username']) + " //PK: " + str(f['pk']))
    # api.follow(f['pk']) CUIDADO!! ESTO FOLLOWEA!!!


# #######################LIKE FOLLOWERS' FOLLOWERS POSTS################################################ FUNCIONA
api.getUserFollowers("289548141") # username: sirdavid10 //PK: 289548141
getUserFollowers = api.LastJson
print(getUserFollowers)
for f in getUserFollowers['users']:
    usrname = f['username']
    if usrname == "armando_firenze":
        print("username: " + str(usrname) + " //PK: " + str(f['pk']))
        if not f['is_private']:
            user_posts = api.getUserFeed(f['pk'])
            info = api.LastJson
            items = info['items'][0]
            print("items: " + str(items))
            last_post_img_url = items['image_versions2']['candidates'][0]['url'].split("?")[0]
            print("img_url: " + str(last_post_img_url))
            img_id = info['items'][0]['id']
            print("img_id: " + str(img_id))
            # username: armando_firenze //PK: 185340079
            api.like(img_id)
            print("SUCCESS!")

# #########A TESTEAR#####################
'''result = api.tag_recent_media(tag_name='castle')
media = result[0]

for m in media:
    print (m.images)
    print (m.user)
    print (m.tags)
'''
# #######A TESTEAR##########################
'''
followers = []
next_max_id = True
while next_max_id:
    print(next_max_id)
    # first iteration hack
    if next_max_id == True: next_max_id = ''
    _ = api.getUserFollowers(user_id, maxid=next_max_id)
    followers.extend(api.LastJson.get('users', []))
    next_max_id = api.LastJson.get('next_max_id', '')
    time.sleep(1)

followers_list = followers

#######################################
user_list = map(lambda x: x['username'] , followers_list)
followers_set= set(user_list)
print(len(followers_set))
'''