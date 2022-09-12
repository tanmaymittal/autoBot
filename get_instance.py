import requests
import json


# What is instance? 
# It is something related to the guild

# PARAMS
#
# access_token = Access Token 
# id = user id
#
# RETURNS 
# Guild Instance for the user
# 
def get_instance(access_token, id):
    url = "https://api.partyinmydorm.com/game/guild/get_guild_for_user/"
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
    payload = f"user_id={id}"
    guild = requests.request("POST", url,headers=headers, data=payload, files=[])
    guild_dict = guild.json()
    try:
        instance = guild_dict['guild_info']['instance_id']
        return instance
    except:
        return 0