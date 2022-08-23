import requests
from get_tasks import get_tasks

# PARAMS
#
# access_token = Acess Token 
# user_id = User ID
# 
# RETURNS 
# Request Responses in a list 
# 
def collect_side_quests(access_token, user_id):
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
    # Collect XC information
    xc_url = "https://api.partyinmydorm.com/game/competition/get_competition_game_state/"
    # This instance id is temporary and found from the past. Holds no value. 
    xc_payload = {'existing_competition_instance_ids': '385579753'}
    xc_response = requests.request("POST", xc_url, headers=headers, data=xc_payload, files=[])
    xc_dict = xc_response.json()
    xc_ids = xc_dict['competition_progresses']
    ################################

    collect_xc_url = "https://api.partyinmydorm.com/game/competition/collect_rewards"
    # Got the dictionary contaning ids and values
    for value in xc_ids.values():
        try:
            if value['uncollected_levels']:
                instance_id = value['competition_instance_id']
                list = value['uncollected_levels']
                counter = list[-1]
                # print(counter)
                for i in range(1, counter+1):
                    collect_xc_payload = {'participant_id': '{}'.format(user_id),
                                          'competition_instance_id': '{}'.format(instance_id),
                                          'level': '{}'.format(i),
                                          'add_up_to_max': '0'}
                    collect_xc_response = requests.request("POST", collect_xc_url, headers=headers, data=collect_xc_payload, files=files)
                    # print(collect_xc_response)
        except:
            pass