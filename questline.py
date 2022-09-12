import requests


# PARAMS
#
# access_token = Acess Token 
# id = Id of the questline to start 
#
# RETURNS 
# Request Response
# 
def start_questline(access_token, id):
    start_questline_url = "https://api.partyinmydorm.com/game/quest/start_questline/"
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
    lite_payload = f"questline_id={id}" 
    questline_response = requests.request("POST", start_questline_url, headers=headers, data=lite_payload)
    return questline_response