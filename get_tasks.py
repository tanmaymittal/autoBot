import requests
import json


# PARAMS
#
# access_token = Acess Token 
# id = Id of the questline to start 
#
# RETURNS 
# JSON with all tasks
# 
def get_tasks(access_token):
    active_user_quests_url = "https://api.partyinmydorm.com/game/quest/get_active_user_quests/"
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
    active_user_quests_payload = {'ignore_collect': 'true'}
    tasks = requests.request("POST", active_user_quests_url,headers=headers, data=active_user_quests_payload, files=[])
    tasks_dict = tasks.json()
    return tasks_dict