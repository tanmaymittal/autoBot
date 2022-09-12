import requests
from server_time import get_time

# PARAMS
#
# access_token = Acess Token 
# id = Box ID to open
#
# RETURNS 
# Request Code
def open_box(access_token, id):
    open_lite = "https://api.partyinmydorm.com/game/collection/open_collection_pack/"
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
    server_time = get_time(access_token)
    open_lite_payload = f"item_id={id}&client_time={server_time}"
    open_lite_response = requests.request("POST", open_lite, headers=headers, data=open_lite_payload)
    return open_lite_response