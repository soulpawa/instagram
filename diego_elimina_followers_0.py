# diego_elimina_followers_0
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
import time
from diego_util import get_followers_pk
from diego_util import get_followers_full
from diego_util import get_followers_full_TEST
from diego_util import login
from diego_util import get_followings
from diego_util import get_user_posts
from diego_util import pitar
import datetime


def lanzar_estadisticas():
    api = login()
    api.getProfileData()
    inicio = datetime.datetime.now()
    print("Process started at ... " + inicio.strftime("%c"))
    user_pk = api.LastJson['user']['pk']
    followers_list = get_followers_full_TEST(api, user_pk, 1000)
    print(datetime.datetime.now())
    print("-----------------------------Follower list obtained, length: " + str(len(followers_list)))

    my_posts = get_user_posts(api, user_pk)
    x = 0
    # file = open("diego_my_posts_likers.csv", "w")
    unique_likers_pk = []
    for post in my_posts:
        x += 1
        # file.write(str(x) + "LIKES;POST ID;USER_PK;USERNAME;" + "\n")
        post_id = post['id']
        items = post['taken_at']
        api.getMediaLikers(post_id)
        likers = api.LastJson
        y = 0
        for l in likers['users']:
            y += 1
            # file.write(str(y) + ";" + post_id + ";" + str(l['pk']) + ";" + str(l['username']) + "\n")
            # file.flush()
            if l['pk'] not in unique_likers_pk:
                unique_likers_pk.append(l['pk'])

    # file.close()
    print(datetime.datetime.now())
    print("-----------------------------Unique liking users list obtained, length: " + str(len(unique_likers_pk)))

    followers_have_not_liked = []
    followers_have_liked = []
    for f in followers_list:
        if f.pk not in unique_likers_pk:
            if f not in followers_have_not_liked:
                followers_have_not_liked.append(f)
        else:
            followers_have_liked.append(f)
    print("-----------------------------Followers that havent liked a post list obtained, length: " + str(len(followers_have_not_liked)))
    for f in followers_have_not_liked:
        f.print()
    print("-----------------------------Followers that have liked a post list obtained, length: " + str(len(followers_have_liked)))
    for f in followers_have_liked:
        f.print()
    print(datetime.datetime.now())

    followings_pk = get_followings(api, user_pk)
    f_not_liked_not_followed_y_private = []
    f_not_liked_not_followed_y_public_sin_posts = []
    f_not_liked_not_followed_y_public_con_posts = []
    f_not_liked_not_followed_y_public_con_pocos_posts = []
    x = 0
    for f in followers_have_not_liked:
        print(str(x) + ": Assigning follower " + f.username)
        x += 1
        if f.pk not in followings_pk:
            if f.private:
                f_not_liked_not_followed_y_private.append(f)
            else:
                if f.has_posts == "F":
                    f_not_liked_not_followed_y_public_sin_posts.append(f)
                elif f.has_posts == "T":
                    posts = get_user_posts(api, f.pk, 100)
                    f.posts = len(posts)
                    taken_at = posts[0]['taken_at']
                    f.msg = int((time.time() - taken_at)/3600/24)  # seconds to days

                    # todo ver cuando publicó por última vez o si tiene < X posts
                    if len(posts) >= 25:
                        f_not_liked_not_followed_y_public_con_posts.append(f)
                    else:
                        f_not_liked_not_followed_y_public_con_pocos_posts.append(f)


    print("__________f_not_liked_not_followed_y_private: " + str(len(f_not_liked_not_followed_y_private)))
    for f in f_not_liked_not_followed_y_private:
        f.print()

    print("__________f_not_liked_not_followed_y_public_sin_posts: " + str(len(f_not_liked_not_followed_y_public_sin_posts)))
    for f in f_not_liked_not_followed_y_public_sin_posts:
        f.print()

    print("__________f_not_liked_not_followed_y_public_con_posts: " + str(len(f_not_liked_not_followed_y_public_con_posts)))
    for f in f_not_liked_not_followed_y_public_con_posts:
        f.print()

    print("__________f_not_liked_not_followed_y_public_con_pocos_posts: " + str(len(f_not_liked_not_followed_y_public_con_pocos_posts)))
    for f in f_not_liked_not_followed_y_public_con_pocos_posts:
        f.short_print()

    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(fin))
    pitar()

    # from collections import Counter
    # cnt = Counter()
    # for foll in followers_have_liked:
    #     cnt[foll] += 1
    # print(cnt)

    # liking_users = []
    # with open('diego_my_posts_likers.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=';')
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             user = row[3]
    #             if user not in liking_users:
    #                 print(str(user))
    #                 liking_users.append(user)
    #                 line_count += 1
    #     print(liking_users)
    #     print(len(liking_users))

    #
    #
    #
    # file = open("idle.csv", "w")
    # for f in followers_list:
    #     user_posts = api.getUserFeed(f['pk'])
    #     info = api.LastJson
    #     try:
    #         items = info['items'][0]
    #         img_id = info['items'][0]['id']
    #         taken_at = info['items'][0]['taken_at']
    #         days = (time.time() - taken_at)/3600/24  # seconds to days
    #         #  print(str(f['username']) + " hasn't posted for " + str(days) + "days.")
    #         file.write("Keeping;" + str(f['username']) + ";\n")
    #         file.flush()
    #
    #     except IndexError as err:
    #         file.write("Blocking;" + str(f['username']) + ";\n")
    #         file.flush()
    #         print(err)
    #     except KeyError as err:
    #         file.write("Private;" + str(f['username']) + ";\n")
    #         file.flush()
    #         print(err)
    #     finally:
    #         file.close()


lanzar_estadisticas()
