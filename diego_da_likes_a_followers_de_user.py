# diego_da_likes_a_followers_de_user
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from diego_util import login
from diego_util import get_followers_pk
import time
import datetime
import random
from random import shuffle


def main():
    inicio = time.process_time()
    print("...Start liking at " + datetime.datetime.now().strftime("%c"))
    api = login()
    api.getProfileData()
    user_pk = api.LastJson['user']['pk']
    user_pk = "904385495"
    user_followers = get_followers_pk(api, user_pk)
    get_user_followers = shuffle(user_followers)
    # /ecto:2058288265 /themacrowizard:2211285 /joseca_lifts:904385495
    # potto:38273173 /iguazel:2647052134 /sirdavid10:289548141 /armando_firenze:185340079 /# r_marting:6363369111
    x = 0
    for f in get_user_followers:
        try:
            x += 1
            t = time.process_time()
            print("_________________________________________________________________________")
            print(str(x) + ": " + str(f) + ": Iniciando: " + str(datetime.datetime.now()))
            api.getUserFeed(f)
            info = api.LastJson
            t2 = time.process_time() - t
            print(str(x) + ": " + str(f) + ": Got JSON UserFeed: " + str(t2) + " seconds")
            img_id = info['items'][0]['id']
            api.like(img_id)
            t3 = time.process_time() - t2
            print(str(x) + ": " + str(f) + ": Post liked! " + str(t3) + " seconds")

        except IndexError:
            print("Index error")
        except KeyError:
            print("Key error")
        except BaseException as err:
            print(err)
        finally:
            t4 = time.process_time()
            print(str(x) + ": " + str(f) + ": Sleeping....... ")
            time.sleep(random.randint(60, 70))
            t5 = time.process_time() - t4
            print(str(x) + ": " + str(f) + ": Slept for " + str(t5) + " seconds")

    fin = time.process_time() - inicio
    print("...End working.... " + str(x) + " posts liked! " + str(fin))


main()
