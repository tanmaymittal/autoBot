import requests

# PARAMS
#
# access_token = Acess Token 
# offer_bundle_id = 
# purchase_location = What store location
# offer_instance_id = 
#
# RETURNS 
# Request Response 

def redeem_offer(access_token, offer_bundle_id, purchase_location, offer_instance_id):
    url = "https://api.partyinmydorm.com/game/targeted_offers/purchase_targeted_offer/"
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
    payload = f'offer_bundle_id={offer_bundle_id}&purchase_location={purchase_location}&offer_instance_id={offer_instance_id}'
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
