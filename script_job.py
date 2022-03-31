from sys import argv
from job import job
from login import login
from rewards import rewards
import json
import gc


def main(args, count):
    count = int(count)
    file_opened = args
    f = open('{}'.format(file_opened))
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
        print(username, ecs, cash)
        rewards(access_token)
        job(access_token, 2, count)
    gc.collect(generation=0)
    gc.collect(generation=1)
    gc.collect(generation=2)


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2])

