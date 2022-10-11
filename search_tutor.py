import requests
import json

def search_tutor(access_token, cash, offset):
    url = "https://api.partyinmydorm.com/game/user/search_clan_members_by_cost/"
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
        'limit': '21',
        'offset': f'{offset}',
        'min_cost': '{}'.format(cash),
        'max_cost': '{}'.format(cash * 2)
    }
    response = requests.request("POST", url,headers=headers, data=payload, files=[])
    return response.json()['users']