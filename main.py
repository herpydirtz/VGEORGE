import time

def timer():
    #while True:
        uin = input("Please input the time in seconds: ")
        try:
            when_to_stop = abs(int(uin))        #here****
        except KeyboardInterrupt:  #ctrl C
            return
        except:
            print("Not a number!")

        for i in range(when_to_stop):   #while when_to_stop > 0:
            m, s = divmod(when_to_stop, 60)     #****convert numbers to x amount of seconds or statement
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print('\r' + time_left, end="")
            time.sleep(1)
        print('\n' + "the timer is complete")


while True:
    user_input = input("What is your request?: ").split(" ")
    if "timer" in user_input:
        timer()