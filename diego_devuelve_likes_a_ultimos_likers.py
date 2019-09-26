# diego_devuelve_likes_a_ultimos_likers
from diego_util import login
import datetime
import time
import random
import winsound


def main(desde=None):
    inicio = datetime.datetime.now()
    print("...Start liking at ... " + inicio.strftime("%c"))
    api = login()
    user_pk = "289060797"  # PK AYUNO_INTERMITENTE
    user_pk = "2211285"
    # /ecto:2058288265 /themacrowizard:2211285 /joseca_lifts:904385495 /sergio.espinar:644593827
    # /marcos_gt:566286300 /guillenutriscientific:828934657 /thefitmedstudent:2205196357
    # /neatfitcouple:5886520324 /j.a.roa:1539017410 /sergvlc:364963984

    desde = 0 if desde is None else desde  # Para que funcione desde el cero si no mandamos param de continuar fallido
    x, likes = 0, 0
    api.getUsernameInfo(user_pk)
    username = api.LastJson['user']['username']

    api.getUserFeed(user_pk)
    last_json = api.LastJson
    taken = int((time.time() - last_json['items'][0]['taken_at']) / 3600 / 24)  # seconds to days
    post_id = last_json['items'][0]['id']

    api.getMediaLikers(post_id)
    likers = api.LastJson
    likers_len = len(likers['users'])
    print("Liking user:", username, ", number of likes:", likers_len, ", post has", taken, "days old")
    for l in likers['users']:
        x += 1
        try:
            print(str(x), "/", str(likers_len), ":", datetime.datetime.now().strftime("%c"), "/", str(l['username']), ":", str(l['pk']), end="")

            print("/Start new like /", end="")
            _ = api.getUserFeed(l['pk'])
            print("User feed retrieved /", end="")
            post_id = api.LastJson['items'][0]['id']
            print("Post ID retrieved /", end="")
            likes += 1

            # Cada 100 descansa para evitar spammeo
            if (likes % 100) == 0:
                print("Sleeping for 300s /", end="")
                time.sleep(300)

            if x > desde:
                api.like(post_id)
                print(" post liked!")

            else:
                print(" already liked!")

        except IndexError as err:
            print(datetime.datetime.now().strftime("%c"), "index errror: ", err)
        except KeyError as err:
            print(datetime.datetime.now().strftime("%c"), "Key error: ", err)
        except Exception as err:
            print(datetime.datetime.now().strftime("%c"), "exception: ", err)
            # TODO Si excepcion es por block, hacer un sleep de 5 mins y relanzarse a si
            #  TODO mismo con el count del proceso por el que vamos

        finally:
            if x > desde:
                t = datetime.datetime.now()
                print("Sleeping................................... ", end="")
                time.sleep(random.randint(50, 70))
                t2 = datetime.datetime.now() - t
                print("Slept for: " + str(t2))

    fin = datetime.datetime.now() - inicio
    print("...End working.... " + str(likes) + " posts liked! " + str(fin))
    winsound.Beep(2500, 250)


main()  # Mandar como aprametro la iteracion antes de fallar si continuamos proceso fallido
