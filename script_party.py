from sys import argv
from job import job
from login import login
from rewards import rewards
import json
import gc

from party_action import party_action

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
    f = open('{},json'.format(file_name))
    # f = open('test_account.json')
    data = json.load(f)
    for key, value in data.items():
        r_dict = login(key, value)
        access_token = r_dict['access_token']
        user_id = r_dict['game_user']['user_id']
        username = r_dict['game_user']['username']
        print(username)
        # maybe make it a tuple
        actions = []
        actions.append((party_action(access_token, user_id, 'steal', 1), 'steal'))
        actions.append((party_action(access_token, user_id, 'assassinate', 1), 'assassinate'))
        actions.append((party_action(access_token, user_id, 'attack', 1), 'attack'))
        actions.append((party_action(access_token, user_id, 'scout', 1), 'scout'))


        for response, type in actions:
            if response.status_code == 200:
                if type == 'steal':
                    party_action(access_token, user_id, 'steal', 8)
                elif type == 'assassinate':
                    party_action(access_token, user_id, 'assassinate', 15)
                elif type == 'attack':
                    party_action(access_token, user_id, 'attack', 10)
                elif type == 'scout':
                    party_action(access_token, user_id, 'scout', 25)
        gc.collect()


################################################################
"""
List of functions I need to make to use 
- Hit Patry
    - Guild Information


Done
- Timer Box 
    - Open
    - Unlock
- Collect XC 
- Collect Side Quests 
- Start Questline 
- Open Boxes - Lite or Whatever 
    - Get server time 

"""


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2])