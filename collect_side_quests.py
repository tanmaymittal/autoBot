import requests
from get_tasks import get_tasks

# PARAMS
#
# access_token = Acess Token 
#
# RETURNS 
# Request Responses in a list 
# 
def collect_side_quests(access_token):
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
    ################################
    tasks_dict = get_tasks(access_token)

    collect_url = "https://api.partyinmydorm.com/game/quest/collect_user_quest/"
    # Loop through all dict values
    tasks_values = tasks_dict.values()
    response = []
    for item in tasks_values:
        # print(item)
        if 'user_quest_tasks' in item.keys():
            parent_task = item['user_quest_tasks']
            # Now there are multiple key-value. Values further have dicts
            try:
                parent_task_values = parent_task.values()
                for child in parent_task_values:
                    child_user_quest_id = child['user_quest_id']
                    collect_payload = {'completed': 'true',
                                       'user_quest_id': '{}'.format(child_user_quest_id),
                                       'add_up_to_max': 'false'
                                       }
                    collect_task = requests.request("POST", collect_url, headers=headers, data=collect_payload, files=[])
                    response.append(collect_task)
                    # print(collect_task)
                    # Now send request with this
            except:
                pass
    return response

