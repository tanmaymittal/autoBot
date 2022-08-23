from sys import argv
from recycle import recycle
from login import login
from rewards import rewards
import json
import gc
from forfeit import forfeit


# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(file_name):
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
    # gc.collect is used to free up variables and I guess clear memeory
        forfeit(access_token, user_id)
    gc.collect(generation=0)
    gc.collect(generation=1)
    gc.collect(generation=2)


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1])

