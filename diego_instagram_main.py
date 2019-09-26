# diego_instagram_main
from diego_instagram_bot import *
''' Modos:
1 - Generar estadísticas de followers
2 - Dar like a los likers del último post de un usuario
3 - Dar like a los followers de un usuario
'''


def main(proceso):
    if proceso == 1:
        print("1")
        diego_elimina_followers_0()
    elif proceso == 2:
        print("2")
        diego_devuelve_likes_a_ultimos_likers()
    elif proceso == 3:
        print("3")
        diego_da_likes_a_followers_de_user()




# sequence[start:stop:step]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(l))
print((len(l)-4))
print(l[(len(l)-8):(len(l)-4):1])
# main(1)
