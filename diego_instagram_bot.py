# diego_instagram_bot
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
from diego_util import get_followers_pk
from diego_util import get_followers_full_TEST
from diego_util import login
from diego_util import get_followings
from diego_util import get_user_posts
import datetime


def diego_da_likes_a_followers_de_user():
    inicio = datetime.datetime.now()
    print("...Start liking.... at ... " + inicio.strftime("%c"))
    api = login()
    api.getProfileData()
    user_pk = api.LastJson['user']['pk']
    #user_pk = "904385495"
    getUserFollowers = get_followers_pk(api, user_pk)
    print(getUserFollowers)
    # /ecto:2058288265 /themacrowizard:2211285 /joseca_lifts:904385495
    # potto:38273173 /iguazel:2647052134 /sirdavid10:289548141 /armando_firenze:185340079 /# r_marting:6363369111
    x = 0
    for f in getUserFollowers:
        try:
            t = datetime.datetime.now()
            print(str(x) + ": " + str(f) + " : Iniciando____________________")
            user_posts = api.getUserFeed(f)
            info = api.LastJson
            t2 = datetime.datetime.now() - t
            print(str(x) + ": " + str(f) + ": got JSON UserFeed " + t2)
            items = info['items'][0]
            last_post_img_url = items['image_versions2']['candidates'][0]['url'].split("?")[0]
            img_id = info['items'][0]['id']
            api.like(img_id)
            t3 = datetime.datetime.now() - t2
            print(str(x) + ": " + datetime.datetime.now().strftime("%c") + " - " + str(f) + " post liked!" + t3)
            x += 1
            t4 = datetime.datetime.now() - t3
            print(str(x) + ": " + str(f) + ": sleeping....... " + t4)
            time.sleep(1 + random.randint(5, 10))
            t5 = datetime.datetime.now() - t4
            print(str(x) + ": " + str(f) + ": slept " + t5)
        except IndexError:
            print("Index error")
        except KeyError:
            print("Key error")
        except BaseException as err:
            print(err)

    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(x) + " posts liked! " + str(fin))


def diego_devuelve_likes_a_ultimos_likers():
    inicio = datetime.datetime.now()
    print("...Start liking.... at ... " + inicio.strftime("%c"))
    api = login()
    user_pk = "289060797"  # PK DIEGO: modificar para dar likes a otros
    user_pk = "289060797"
    # /ecto:2058288265 /themacrowizard:2211285 /joseca_lifts:904385495 /sergio.espinar:644593827
    # /diego 289060797 /potto 38273173 /iguazel:2647052134 /ecto:2058288265 /sirdavid10:289548141 /armando_firenze:185340079

    x = 0
    api.getUserFeed(user_pk)
    lj = api.LastJson
    post_id = lj['items'][0]['id']
    print(post_id)
    api.getMediaLikers(post_id)
    likers = api.LastJson
    likers_len = len(likers['users'])
    print("Number of likers: ", likers_len)
    y = 0
    for l in likers['users']:
        try:
            y += 1
            user_posts = api.getUserFeed(l['pk'])
            post_id = api.LastJson['items'][0]['id']
            api.like(post_id)
            print(str(x) + "/" + likers_len + ": " + datetime.datetime.now().strftime("%c") + " - " + str(l['username']) + ":" + str(l['pk']) + " post liked!")
            x += 1
            t = datetime.datetime.now()
            print("Sleeping................................... ", end="")
            time.sleep(random.randint(60, 70))
            t2 = datetime.datetime.now() - t
            print("Slept for: " + str(t2))
        except IndexError as err:
            e = err
        except KeyError as err:
            e = err
        except BaseException as err:
            e = err

    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(x) + " posts liked! " + str(fin))


def diego_elimina_followers_0():
    api = login()
    api.getProfileData()
    inicio = datetime.datetime.now()
    print("Process started at ... " + inicio.strftime("%c"))
    user_pk = api.LastJson['user']['pk']
    followers_list = get_followers_full_TEST(api, user_pk, 50)
    print("Follower list obtained, length: " + str(len(followers_list)))
    print(datetime.datetime.now())
    my_posts = get_user_posts(api, user_pk, 10)

    x = 0
    unique_likers_pk = []
    for post in my_posts:
        x += 1
        post_id = post['id']
        items = post['taken_at']
        api.getMediaLikers(post_id)
        likers = api.LastJson
        y = 0
        for l in likers['users']:
            y += 1
            if l['pk'] not in unique_likers_pk:
                unique_likers_pk.append(l['pk'])
        if x == 10:
            break
    print(datetime.datetime.now().strftime("%c") + "Unique liking users list obtained, length: " + str(len(unique_likers_pk)))

    followers_have_not_liked = []
    followers_have_liked = []
    for f in followers_list:
        if f.pk not in unique_likers_pk:
            if f not in followers_have_not_liked:
                followers_have_not_liked.append(f)
        else:
            followers_have_liked.append(f)
    print(datetime.datetime.now())
    print("Followers that havent liked a post list obtained, length: " + str(len(followers_have_not_liked)))
    print("Followers that have liked a post list obtained, length: " + str(len(followers_have_liked)))

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
                    posts = get_user_posts(api, f.pk)
                    f.posts = len(posts)
                    taken_at = posts[0]['taken_at']
                    f.msg = int((time.time() - taken_at)/3600/24)  # seconds to days

                    # todo ver cuando publicó por última vez o si tiene < X posts
                    if len(posts) >= 25:
                        f_not_liked_not_followed_y_public_con_posts.append(f)
                    else:
                        f_not_liked_not_followed_y_public_con_pocos_posts.append(f)

    print("__________f_not_liked_not_followed_y_private: " +
          str(len(f_not_liked_not_followed_y_private)))
    for f in f_not_liked_not_followed_y_private:
        f.print()

    print("__________f_not_liked_not_followed_y_public_sin_posts: " +
          str(len(f_not_liked_not_followed_y_public_sin_posts)))
    for f in f_not_liked_not_followed_y_public_sin_posts:
        f.print()

    print("__________f_not_liked_not_followed_y_public_con_posts: " +
          str(len(f_not_liked_not_followed_y_public_con_posts)))
    for f in f_not_liked_not_followed_y_public_con_posts:
        f.print()

    print("__________f_not_liked_not_followed_y_public_con_pocos_posts: " +
          str(len(f_not_liked_not_followed_y_public_con_pocos_posts)))
    for f in f_not_liked_not_followed_y_public_con_pocos_posts:
        f.print()

    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(fin))

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
