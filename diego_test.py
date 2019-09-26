# diego_elimina_followers_0
from diego_util import get_followers_full_TEST
from diego_util import login

api = login()
api.getProfileData()
user_pk = api.LastJson['user']['pk']
followers_list = get_followers_full_TEST(api, user_pk)
print("Follower list obtained, length: " + str(len(followers_list)))

