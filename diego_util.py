# diego_util
from InstagramAPI import InstagramAPI
import winsound
import datetime
import time


class InstaFollower:
    def __init__(self, pk, private, has_posts, username=None, posts=None, msg=None, age=None):
        self.pk = pk
        self.private = private
        self.has_posts = has_posts
        self.username = username
        self.posts = posts
        self.msg = msg
        self.age = age

    def print(self):
        print(str(self.username) + ";" + str(self.pk) + ";" + str("Private" if self.private else "Public")
              + ";HAS_POSTS: " + str(self.has_posts) + ";NUM_POSTS: " + str(self.posts)
              + ";Dias sin publicar: " + str(self.msg) + ";Age: " + str(self.age))

    def short_print(self):
        print(str(self.username) + ";" + str(self.pk) + ";" + str("Private;" if self.private else "Public;")
              + str(self.posts) + ";" + str(self.msg) + ";" + str(self.age))


def get_followers_full(api, pk, cuantos=None):
    print("Starting get_followers_full..........................")
    util_followers = []
    next_max_id = True
    unique_followers = []
    x = 0

    while next_max_id:
        print(str(x) + " next_max_id: " + datetime.datetime.now().strftime('%c'))
        x += 1
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowers(pk, maxid=next_max_id)
        util_followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

    x = 0
    for f in util_followers:
        if f['is_private']:
            insta_follower = InstaFollower(f['pk'], True, "U", f['username'])
        else:
            try:
                api.getUserFeed(f['pk'])
                api.LastJson['items'][0]
                insta_follower = InstaFollower(f['pk'], False, "T", f['username'])
            except IndexError as err:
                insta_follower = InstaFollower(f['pk'], False, "F", f['username'])

        unique_followers.append(insta_follower)
        # print(str(x) + "-" + str(insta_follower.username) + "-" + str(insta_follower.pk) + "-" + str(insta_follower.private) + "-" + str(insta_follower.has_posts))
        print("Follower number: " + str(x))
        insta_follower.print()
        x += 1
        if cuantos is not None and x >= cuantos:
            break

    return unique_followers


def get_followers_full_TEST(api, pk, cuantos=None):
    print("Starting get_followers_full..........................")
    util_followers = []
    next_max_id = True
    x = 0
    unique_followers = []
    # file = open("get_followers_full_TEST.csv", "w")
    # file.write(str(x) + "ITE;USERNAME;PK;" + "\n")
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowers(pk, maxid=next_max_id)
        users = api.LastJson.get('users', [])
        x += 1
        print()
        print(str(x) + ";" + str(len(users)), end=';')
        for u in users:
            u['profile_pic_url'] = x  # TODO en profile_pic_url metemos el 'next_max_id' (GRUPO)
            print(str(u['username']), end=';')
            # print(str(u['pk']) + ";" + str(u['username']), end=';')
        util_followers.extend(users)
        next_max_id = api.LastJson.get('next_max_id', '')

    # todo cambio TEMPORAL para coger los ultimos, de x en x
    # sequence[start:stop:step]
    util_followers = util_followers[(len(util_followers) - 5400):(len(util_followers) - 4600):]
    # util_followers = util_followers[(len(util_followers)-200)::]
    print()
    print("util_followers: ")
    print(util_followers)

    x = 0
    for f in util_followers:
        if f['is_private']:
            insta_follower = InstaFollower(f['pk'], True, "U", f['username'], age=f['profile_pic_url'])
            # file.write(str(f['profile_pic_url']) + ";" + str(f['username']) + ";" + str(f['pk']) + ";" +
            #           str(True) + ";" + "U" + "\n")
            #file.flush()
        else:
            try:
                api.getUserFeed(f['pk'])
                api.LastJson['items'][0]
                insta_follower = InstaFollower(f['pk'], False, "T", f['username'], age=f['profile_pic_url'])
                # file.write(str(f['profile_pic_url']) + ";" + str(f['username']) + ";" + str(f['pk']) + ";" +
                #            str(False) + ";" + "T" + "\n")
                #file.flush()
            except IndexError as err:
                insta_follower = InstaFollower(f['pk'], False, "F", f['username'], age=f['profile_pic_url'])
                # file.write(str(f['profile_pic_url']) + ";" + str(f['username']) + ";" + str(f['pk']) + ";" +
                #            str(False) + ";" + "F" + "\n")
                #file.flush()
        unique_followers.append(insta_follower)
        # insta_follower.print()
        # file.flush()

        x += 1
        if cuantos is not None and x >= cuantos:
            break

    # file.close()
    return unique_followers


def get_followers_pk(api, pk, num=None):
    util_followers = []
    next_max_id = True
    x = 0

    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = '' # stop condition
        _ = api.getUserFollowers(pk, maxid=next_max_id)
        util_followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        if num is not None and x >= num:
            break

    unique_followers = {
        f['pk']: f  # username vs pk (for id)
        for f in util_followers
    }

    return unique_followers


def get_followings(api, pk):
    util_followings = []
    next_max_id = True

    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(pk, maxid=next_max_id)
        util_followings.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')

    unique_followings = {
        f['pk']: f  # username vs pk (for id)
        for f in util_followings
    }
    return unique_followings


def login():
    api = InstagramAPI("ayuno_intermitente", "Zogeidinsta1")
    api.login()
    return api


def buscar_user(api):
    api.searchUsername()


def bloquear(api, f):
    api.block(f)
    api.unblock(f)
    print(str(f) + " ya no me sigue")


def pitar():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    x = 0
    while x < 3:
        winsound.Beep(frequency, duration)
        x += 1


def get_user_posts(api, user_pk, num=None):
    # print("Starting get_user_posts..............................")
    next_max_id = True
    my_posts = []
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''  # stop condition
        _ = api.getUserFeed(user_pk, maxid=next_max_id)
        my_posts.extend(api.LastJson.get('items', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        if num is not None and len(my_posts) >= num:
            break
    print("Returning: " + str(len(my_posts)) + " posts")
    # print("MY_POSTS")
    # print(my_posts)
    return my_posts



