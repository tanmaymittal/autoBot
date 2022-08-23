import requests
import json


# PARAMS
#
# access_token = Acess Token 
# id = Id of the questline to start 
#
# RETURNS 
# Server time as an integer
# 
def get_server_time(access_token):
    regen_url = "https://api.partyinmydorm.com/game/poll/regen/"
    headers = {
        'Host': 'api.partyinmydorm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.2.349209834.1593604627; _gid=GA1.2.2127787787.1603665128',
        'User-Agent': 'PIMD/445 CFNetwork/1125.2 Darwin/19.4.0',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Language': 'en-us',
        'X-tuna-api': '445',
        'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Bearer {}'.format(access_token)
        }
    # regen_payload = ""
    regen = requests.request("POST", regen_url, headers=headers, data="")
    regen_dict = regen.json()
    servertime = regen_dict['server_time']
    return int(servertime)