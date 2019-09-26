# diego2
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
# https://github.com/LevPasha/Instagram-API-python
# https://www.kdnuggets.com/2017/08/instagram-python-data-analysis.html

'''DA LIKES A USUARIOS SEGUIDORES DE UN USUARIO PREDEFINIDO'''
from InstagramAPI import InstagramAPI
import time

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




# #######################ELIMINAR IDLE FOLLOWERS################################################
print("ELIMINAR IDLE FOLLOWERS")
api.getUserFollowers(user_id)
getUserFollowers = api.LastJson
print("username: " + str(getUserFollowers['users'][0]['username']))

for f in getUserFollowers['users']:
    print("username: " + str(f['username']) + " //PK: " + str(f['pk']))

'''
# #######################LIKE FOLLOWERS' FOLLOWERS POSTS################################################ FUNCIONA
api.getUserFollowers("38273173") # username: sirdavid10 //PK: 289548141 #POTTO: 38273173
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
'''

# #######################LIKE SPECIFIC USER'S POST################################################ FUNCIONA

user_posts = api.getUserFeed("38273173")# POTTO: 38273173
print(user_posts)
info = api.LastJson
items = info['items'][0]
last_post_img_url = items['image_versions2']['candidates'][0]['url'].split("?")[0]
img_id = info['items'][0]['id']
api.like(img_id)
print("SUCCESS!")

