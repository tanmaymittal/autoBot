import requests

# PARAMS
#
# access_token = Acess Token 
# id = Job ID to hit 
# count = how many times to hit the job
#
# RETURNS 
# NULL
# 
def rewards(access_token):
    rewards_url = "https://api.partyinmydorm.com/game/video_reward/get_periodic_reward/"
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
    rewards_payload = {}
    rewards_response = requests.request("POST", rewards_url, headers=headers, data=rewards_payload)
    # print("Spinner Collected: ", rewards_response)
    return rewards_response
        