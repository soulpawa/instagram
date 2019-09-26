# diego_devuelve_likes_a_ultimos_likers
from diego_util import login
import datetime
import time
import random
import winsound


def main(desde=None):
    inicio = datetime.datetime.now()
    print("...Start following.... at ... " + inicio.strftime("%c"))
    api = login()
    user_pk = "289060797"  # PK DIEGO: modificar para dar likes a otros
    user_pk = "2058288265"
    # /ecto:2058288265 /themacrowizard:2211285 /joseca_lifts:904385495 /sergio.espinar:644593827
    # /marcos_gt:566286300 /guillenutriscientific:828934657

    # COntrolamos si no queremos que empiece desde cero porque estamos reanudando
    desde = 0 if desde is None else desde
    x, likes = 0, 0
    api.getUsernameInfo(user_pk)
    username = api.LastJson['user']['username']

    api.getUserFeed(user_pk)
    lastJson = api.LastJson
    taken = int((time.time() - lastJson['items'][0]['taken_at']) / 3600 / 24)  # seconds to days
    post_id = lastJson['items'][0]['id']

    api.getMediaLikers(post_id)
    likers = api.LastJson
    likers_len = len(likers['users'])
    print("Following likers of user:", username, ", number of likes:", likers_len, ", post has", taken, "days old")
    file = open("followed_TEST.csv", "a")
    file.flush()

    for l in likers['users']:
        x += 1
        try:
            likes += 1
            api.follow(l['pk'])
            print(str(x) + "/" + str(likers_len) + ": " + datetime.datetime.now().strftime("%c") + " - " + str(l['username']) + ":" + str(l['pk']) + " followed!")
            file.write(str(x) + ";" + str(l['username']) + ";" + str(l['pk']) + ";" + "\n")
            file.flush()

            user_posts = api.getUserFeed(l['pk'])
            post_id = api.LastJson['items'][0]['id']
            api.like(post_id)

        except IndexError as err:
            print("index errror: ", err)
        except KeyError as err:
            print("Key error: ", err)
        except Exception as err:
            print("exception: ", err)
        finally:
            if x > desde:
                t = datetime.datetime.now()
                print("Sleeping................................... ", end="")
                time.sleep(random.randint(60, 70))
                t2 = datetime.datetime.now() - t
                print("Slept for: " + str(t2))
                file.flush()

    file.flush()
    file.close()
    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(likes) + " posts liked! " + str(fin))
    winsound.Beep(2500, 250)


main()  # Mandar como aprametro la iteracion antes de fallar si continuamos proceso fallido
