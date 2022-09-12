import requests

from get_user import get_user

# PARAMS
#
# access_token = Acess Token 
# user_id = user id
# type = Action type = [Rave, lecture, fight, sigh]
# count = how many times to hit the job
#
# RETURNS 
# NULL

def hit_action(access_token, target_ign, type, count):
    types = ['steal', 'assassinate', 'attack', 'scout']
    # Steal = Rave
    # Assassinate = Lecture = Prank
    # Attack = Fight 
    # Scout = Sigh 
    if type == 'attack':
        url = f"https://api.partyinmydorm.com/game/fight/attack/"
    else:
        url = f"https://api.partyinmydorm.com/game/fight/espionage/{type}/"
    
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
    target_info = get_user(access_token, target_ign)
    defender_id = target_info['user_id']
    payload = f"defender_id={defender_id}"
    try: 
        for i in range(count):
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.status_code, response.text)
    except KeyboardInterrupt:
        exit()
    return response
        