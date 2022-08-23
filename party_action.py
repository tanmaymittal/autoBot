import requests

from get_instance import get_instance

# PARAMS
#
# access_token = Acess Token 
# user_id = user id
# type = Action type = [Rave, lecture, fight, sigh]
# count = how many times to hit the job
#
# RETURNS 
# NULL

def party_action(access_token, user_id, type, count):
    types = ['steal', 'assassinate', 'attack', 'scout']
    # Steal = Rave
    # Assassinate = Lecture 
    # Attack = Fight 
    # Scout = Sigh 
    url = f"https://api.partyinmydorm.com/game/group/mission/instance/{type}/"
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
    instance = get_instance(access_token, user_id)
    payload = f"instance_id={instance}&count=1&graceful_no_effect=true&target=1&stage=1"
    for i in range(count):
        response = requests.request("POST", url, headers=headers, data=payload)
    
    return response
        