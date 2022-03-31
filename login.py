import requests
import urllib.parse
import time
import json

# Returns a dictoinary with all info / access tokens
def login(key, value):
    url = "https://api.partyinmydorm.com/game/login/oauth"
    payload = f"POST https://api.partyinmydorm.com/game/login/oauth/ HTTP/1.1\nHost: api.partyinmydorm.com\nContent-Type: application/x-www-form-urlencoded\nCookie: _ga=GA1.2.349209834.1593604627; _gid=GA1.2.2127787787.1603665128\nUser-Agent: PIMD/445 CFNetwork/1125.2 Darwin/19.4.0\nConnection: keep-alive\nAccept: */*\nAccept-Language: en-us\nContent-Length: 1143\nX-tuna-api: 445\nAccept-Encoding: gzip, deflate, br\n\nbundle_id=ata.tuna.pimd&version=2015&jailbroken=1&client_information=%7B%22ether_id%22%3A%7B%22ap1%22%3A2%2C%22en2%22%3A2%2C%22en0%22%3A2%2C%22awdl0%22%3A2%2C%22en1%22%3A2%7D%2C%22udid_advertising%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22version_name%22%3A%223.81%22%2C%22os_name%22%3A%22iOS%22%2C%22ether_type%22%3A1%2C%22application_tracking_enabled%22%3Atrue%2C%22hardware_version%22%3A%22iPhone9%2C3%22%2C%22openudid%22%3A%225459c0b7c6636ff45d376ab5de9f9a1e101f5fc5%22%2C%22af_id%22%3A%221161865954%22%2C%22locale%22%3A%22en_US%22%2C%22os_build%22%3A%2217E262%22%2C%22language%22%3A%22en%22%2C%22udid_vendor%22%3A%220BA2C476-275D-4B39-9BEE-F5BC971EF369%22%2C%22os_version%22%3A%2213.4.1%22%2C%22country%22%3A%22US%22%2C%22advertiser_tracking_enabled%22%3Afalse%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2013_4_1%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F15E148%22%7D&grant_type=password&scope=%5B%22all%22%5D&client_version=445&password={value}&channel_id=12&username={urllib.parse.quote(key)}&client_id=ata.tuna.pimd&client_secret=n0ts0s3cr3t"
    headers = {
        'Host': 'api.partyinmydorm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.2.349209834.1593604627; _gid=GA1.2.2127787787.1603665128',
        'User-Agent': 'PIMD/445 CFNetwork/1125.2 Darwin/19.4.0',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Accept-Language': 'en-us',
        'X-tuna-api': '445',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    r = requests.request("POST", url, headers=headers, data=payload)
    r_dict = r.json()
    # returns a dictionary with all variables 
    return r_dict