# diego_elimina_followers_0
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from diego_util import login
from diego_util import get_followings
import datetime


def __main__():
    api = login()
    api.getProfileData()
    inicio = datetime.datetime.now()
    print("Process started at ... " + inicio.strftime("%c"))
    user_pk = api.LastJson['user']['pk']
    print(datetime.datetime.now())
    followings_pk = get_followings(api, user_pk)

    file = open("followings.csv", "w")
    file.flush()
    x = 0
    for f in followings_pk:
        print(str(x), ": ", str(f))
        file.write(str(f) + ";" + "\n")
        file.flush()
        x += 1

    file.flush()
    file.close()
    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(fin))


__main__()
