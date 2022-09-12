import requests

def join_club(access_token, guild_id):
    join_club_url = 'https://api.partyinmydorm.com/game/guild/request_join/'
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
    join_payload = {
        'return_profile' : 'true',
        'guild_id' : f'{guild_id}'
    }
    join = requests.request("POST", join_club_url,headers=headers, data=join_payload, files=[])
    return join