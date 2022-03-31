import requests
import json


# PARAMS
#
# access_token = access token
# username = IGN to track
#
# RETURNS 
# dictionary with all information about requested IGN
# 
def get_user(access_token, username):
    get_person_url = "https://api.partyinmydorm.com/game/user/get_profile_by_username"
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
    person_payload = f"profile_username={username}"
    r_p = requests.request("POST", get_person_url, headers=headers, data=person_payload)
    return r_p.json()
    p_dict = r_p.json()
    f_won = p_dict['fights_won']
    f_lost = p_dict['fights_lost']
    r_won = p_dict['steals_won']
    r_lost = p_dict['steals_lost']
    lec_won = p_dict['assassinates_won']
    lec_lost = p_dict['assassinates_lost']
    sigh_won = p_dict['scouts_won']
    sigh_lost = p_dict['scouts_lost']
    tz_India = pytz.timezone('Asia/Kolkata')
    datetime_india = datetime.now(tz_India)
    # print("India time:", datetime_india.strftime("%H:%M:%S"))
    hours = int(datetime_india.strftime("%H"))
    mins = int(datetime_india.strftime("%M"))
    its = int(datetime_india.strftime("%S"))
    # print(its)
    # print(f"India time plus one second: {hours}:{mins}:{its}")
    it = f"{hours}:{mins}:{its}"
    india_time = datetime_india.strftime("%H:%M:%S")
    current_date = datetime.now().date()
    # print(current_date)
    list = [current_date, it, f_won, f_lost, r_won,
            r_lost, lec_won, lec_lost, sigh_won, sigh_lost]
    return list