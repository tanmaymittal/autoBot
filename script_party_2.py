from sys import argv
from job import job
from login import login
from rewards import rewards
import json
import gc

from party_action import party_action
from collect_side_quests import collect_side_quests

# Returns true if won
def check_if_won(response):
    # Function that checks if action was won or not
    response_json = response.json()
    if 'won' in response_json:
        if response_json['won'] == False:
            return False
        else:
            return True


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
        
        # print(response.status_code)
        # boo = check_if_won(response)
        # print(boo)
        actions_list = ['steal', 'assassinate', 'attack', 'scout']
        for x in actions_list: 
            # print("Going for ", x)
            response = party_action(access_token, user_id, x, 1)
            won = check_if_won(response)
            # print(x, ': ', won, response.status_code)
            while (won == True):
                response = party_action(access_token, user_id, x, 1)
                won = check_if_won(response)
                print(x, ': ', won, response.status_code)
        # collect_side_quests(access_token, user_id)
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