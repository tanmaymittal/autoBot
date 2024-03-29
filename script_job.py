from sys import argv
from recycle import recycle
from login import login
from rewards import rewards
import json
import gc

# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(file_name, count):
    count = int(count)
    f = open('{}'.format(file_name))
    data = json.load(f)
    # f = open('test_account.json')
    # data = json.load(f)
    for key, value in data.items():
        r_dict = login(key, value)
        access_token = r_dict['access_token']
        user_id = r_dict['game_user']['user_id']
        username = r_dict['game_user']['username']
        ecs = r_dict['bank_account']['points']  # Gets me Extra Credits of the user
        cash = r_dict['bank_account']['balance']
        print(username)
        # rewards(access_token)
        recycle(access_token, 114444, 4)
        recycle(access_token, 114445, 66)
        recycle(access_token, 109662, 43)
        recycle(access_token, 108543, 21)
        recycle(access_token, 114443, 46)
        recycle(access_token, 109660, 27)
        recycle(access_token, 110425, 53)
        recycle(access_token, 113134, 64)
        recycle(access_token, 108541, 22)
        recycle(access_token, 114446, 46)
        recycle(access_token, 101867, 10)
    # gc.collect is used to free up variables and I guess clear memeory
    gc.collect(generation=0)
    gc.collect(generation=1)
    gc.collect(generation=2)


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2])

