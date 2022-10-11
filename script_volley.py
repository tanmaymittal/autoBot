from sys import argv
from login import login
import json
import gc
from get_user import get_user
from calculate_stats import calculate_stats
import csv
import itertools

from hire_user import hire_user
import time

# PARAMS
#
# args = file name to be opened
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def main(user_ign):
    r_dict = login('tanmaymittal2001@gmail.com', 'bitch2')
    access_token_one = r_dict['access_token']

    r_dict = login('oukzgml5vr@gmail.com', '09u#$F')
    access_token_two = r_dict['access_token']

    target_info = get_user(access_token_one, user_ign)
    user_id = target_info['user_id']
    keys = [access_token_one, access_token_two]

    for access_token in itertools.cycle(keys):
        x = hire_user(access_token, user_id)
        print(x.text)
        time.sleep(0.5)

    gc.collect()


"""
How to know which accounts will volley? 
- hard code
- psss pwd and email thru cli
- pass json file name through cli 

Collect ign from command line 
Collect user id from IGN

Have access tokens of two accounts 




"""

# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1])
    # args1 is the file to be opened that contains json for account that will track
    # args2 is the file to be opened that contains the IGNs of people to be tracked
