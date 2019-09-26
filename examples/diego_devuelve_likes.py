# diego_devuelve_likes
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from diego_util import login
import datetime

api = login()
api.getProfileData()
inicio = datetime.datetime.now()
print("...Start liking.... at ... " + inicio.strftime("%c"))
user_pk = api.LastJson['user']['pk']

user_posts = api.getUserFeed(user_pk)
post_id = api.LastJson['items'][0]['id']
api.getMediaLikers(post_id)
likers = api.LastJson
num_likes = 0
for l in likers['users']:
    try:
        api.getUserFeed(l['pk'])
        api.like(api.LastJson['items'][0]['id'])
        num_likes += 1
        print(str(l['username']) + " last post liked ")

    except IndexError as err:
        e = err
    except KeyError as err:
        e = err

fin = datetime.datetime.now() - inicio
print("...End working.... " + str(num_likes) + " given: " + str(fin))
