from sys import argv
from login import login
import json
import gc
from get_user import get_user
from calculate_stats import calculate_stats
import csv

# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(file_name, text_file):
    f = open('{}'.format(file_name))
    data = json.load(f)
    for key, value in data.items():
        r_dict = login(key, value)
        access_token = r_dict['access_token']
        user_id = r_dict['game_user']['user_id']
        username = r_dict['game_user']['username']
        print(username)
        with open(text_file, 'r') as file: 
            for line in file: 
                for ign in line.split():
                    print(ign)
                    user_information = get_user(access_token, ign)
                    stats = calculate_stats(user_information)
                    print(stats)
                    fileName = ign + '.csv'
                    with open(fileName, 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow(stats)
        
    gc.collect(generation=0)
    gc.collect(generation=1)
    gc.collect(generation=2)


# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2])
    # args1 is the file to be opened that contains json for account that will track
    # args2 is the file to be opened that contains the IGNs of people to be tracked
