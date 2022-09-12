from sys import argv
from login import login
import json
import gc
from hit_action import hit_action

# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(file_name, ign, type, count):
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
        print(username)
        hit_action(access_token, ign, type, count)
    # gc.collect is used to free up variables and I guess clear memeory
    gc.collect(generation=0)
    gc.collect(generation=1)
    gc.collect(generation=2)


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])

