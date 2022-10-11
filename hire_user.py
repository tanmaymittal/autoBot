import requests
import json


# PARAMS
#
# access_token = access token
# user_id = user id
#
# RETURNS 
# dictionary with all information about requested IGN
# 
def hire_user(access_token, user_id):
    url = "https://api.partyinmydorm.com/game/purchase/buy_clan_member/"
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
    payload = {
        'clan_member_id': '{}'.format(user_id)
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
