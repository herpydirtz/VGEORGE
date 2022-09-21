import time

def timer():
    user_input = input("Please input the time: ").split() # "3 hours 5 minutes and 24 seconds"
    
    seconds = 0
    
    if "hour" in user_input or "hours" in user_input:
        if "hour" in user_input:
            try:
                seconds += 3600 * int(user_input[user_input.index("hour") - 1])
            except:
                print("invalid input")
                timer()
        elif "hours" in user_input:
            try:
                seconds += 3600 * int(user_input[user_input.index("hours") - 1])
            except:
                print("invalid input")
                timer()
    if "minute" in user_input or "minutes" in user_input:
        if "minute" in user_input:
            try:
                seconds += 60 * int(user_input[user_input.index("minute") - 1])
            except:
                print("invalid input")
                timer()
        elif "minutes" in user_input:
            try:
                seconds += 60 * int(user_input[user_input.index("minutes") - 1])
            except:
                print("invalid input")
                timer()
    if "second" in user_input or "seconds" in user_input:
        if "second" in user_input:
            try:
                seconds += int(user_input[user_input.index("second") - 1])
            except:
                print("invalid input")
                timer()
        elif "seconds" in user_input:
            try:
                seconds += int(user_input[user_input.index("seconds") - 1])
            except:
                print("invalid input")
                timer()
    
    if seconds > 0:
        for i in range(seconds, 0, -1): # i in range() is counting the items in a list that starts from seconds and ends at 0 decreasing in intervals of 1. This could be changed for example -2 would decrease 2x the rate
            m, s = divmod(i, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left)
            time.sleep(1)
        print('\n' + "The timer is complete.")
    else:
        print("inval2")