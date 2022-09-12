import requests
from get_instance import get_instance
# PARAMS
#
# access_token = Acess Token 
# id = user_id
#
# RETURNS 
# NULL
# 
def forfeit(access_token, user_id):
    rewards_url = "https://api.partyinmydorm.com/game/group/mission/instance/forfeit/"
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
    payload = f"instance_id={instance}"
    response = requests.request("POST", rewards_url, headers=headers, data=payload)
    # print("Spinner Collected: ", response)
    print(response.status_code)
    return response
        