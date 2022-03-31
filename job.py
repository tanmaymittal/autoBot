import requests

# PARAMS
#
# access_token = Acess Token 
# id = Job ID to hit 
# count = how many times to hit the job
#
# RETURNS 
# NULL
# list 

def job(access_token, id, count):
    job_url = "https://api.partyinmydorm.com/game/mission/attempt/"
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
    job_payload = f'mission_id={id}'
    # Hit job 15 times
    temp_count = 0
    for i in range(count):
        r_job = requests.request("POST", job_url, headers=headers, data=job_payload)
        if temp_count == 0:
            print(r_job)
            temp_count += 1
        