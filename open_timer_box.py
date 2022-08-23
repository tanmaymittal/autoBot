import requests

from get_server_time import get_server_time

# PARAMS
#
# access_token = Acess Token 
# id = box id 
#
# RETURNS 
# JSON with all tasks
# 
def open_timer_box(access_token, id):
    url = "https://api.partyinmydorm.com/game/timer_box/open_timer_box"
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
    server_time = get_server_time(access_token)
    payload = f"client_time={server_time}&slot_number=1&unlocked_with_time=1&item_id={id}&position=1"
    timer_box_unlock = requests.request("POST", url, headers=headers, data=payload)
    return timer_box_unlock