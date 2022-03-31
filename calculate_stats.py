from datetime import datetime


# PARAMS
#
# user_dict = contains all information about the user
#
# RETURNS 
# list with all information about requested IGN
# 
def calculate_stats(user_information):
    f_won = user_information['fights_won']
    f_lost = user_information['fights_lost']
    r_won = user_information['steals_won']
    r_lost = user_information['steals_lost']
    lec_won = user_information['assassinates_won']
    lec_lost = user_information['assassinates_lost']
    sigh_won = user_information['scouts_won']
    sigh_lost = user_information['scouts_lost']
    now = datetime.now()
    # %Y-%m-%d 
    current_time = now.strftime("%H:%M:%S")
    current_date = datetime.now().date()
    # print(current_date)
    return [current_date, current_time, f_won, f_lost, r_won, r_lost, lec_won, lec_lost, sigh_won, sigh_lost]