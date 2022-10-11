from sys import argv
from recycle import recycle
from login import login
from rewards import rewards
import json
import gc
from forfeit import forfeit
from search_tutor import search_tutor
import csv

# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(file_name):
    f = open('{}.json'.format(file_name))
    data = json.load(f)
    mega_list = []
    for key, value in data.items():
        r_dict = login(key, value)
        access_token = r_dict['access_token']
        user_id = r_dict['game_user']['user_id']
        username = r_dict['game_user']['username']
        cash = r_dict['bank_account']['balance']
        # print(username)
        # rewards(access_token)
    # gc.collect is used to free up variables and I guess clear memeory
        offset_list = [0, 21, 42, 63, 84]
        for x in offset_list:
            tutor_list = search_tutor(access_token, 550000000000, x)
            print(tutor_list[0])
            mega_list.extend(tutor_list)

        # Now we have a mega list and just need to parse it and add it to an excel 
        fields = ['Username', 'User ID', 'Price', 'Strength', 'Intel', 'Combined']
        with open('tutor_list_5.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            
            for x in mega_list:
                templist = [x['username'], x['user_id'], x['cost'], x['bonus']['attack'], x['bonus']['spy_attack'], int(x['bonus']['attack']) + int(x['bonus']['spy_attack'])]
                writer.writerow(templist)

    gc.collect()


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1])

