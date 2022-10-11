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
def main(file_name):
    # count = int(count)
    f = open('{}.json'.format(file_name))
    # f = open('test_account.json')
    data = json.load(f)
    # Has tupples with Access_Tokens and User ID 
    tokens = []
    for key, value in data.items():
        r_dict = login(key, value)
        access_token = r_dict['access_token']
        user_id = r_dict['game_user']['user_id']
        username = r_dict['game_user']['username']
        tokens.append((access_token, user_id))
        print(username)

        # maybe make it a tuple
    for access_token, user_id in tokens:
        # print(key, value)
        actions_list = ['steal', 'assassinate', 'attack', 'scout']
        response = party_action(access_token, user_id, 'steal', 1)
        print(response.status_code, response.text)
        for x in actions_list: 
            while True:
                if response.status_code != 200:
                    break
                response = party_action(access_token, user_id, x, 1)
                print(response.status_code, response.text)

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
    main(argv[1])