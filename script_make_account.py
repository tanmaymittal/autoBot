import random
import string
import requests
import urllib.parse
import json
from sys import argv
from login import login
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



# Structure of script is that it is 
if __name__ == '__main__':
    main(argv[1], argv[2])
    # args1 is the file to be opened that contains names of the new accounts
    # args2 unknown
