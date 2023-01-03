import time
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # [0] for male, [1] for female voice
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def timer(user_input):
    seconds = 0

    grandfather = {
        "hour": 3600,
        "minute": 60,
        "second": 1
    }

    for type in grandfather.keys():
        if type in user_input:
            try:
                seconds += grandfather[type] * \
                    int(user_input[user_input.index(type) - 1])
            except ValueError:
                speak("invalid input")
                timer(user_input)
        elif type + "s" in user_input:
            try:
                seconds += grandfather[type] * \
                    int(user_input[user_input.index(type + "s") - 1])
            except ValueError:
                speak("invalid input")
                timer(user_input)

    if seconds > 0:
        for i in range(seconds, 0, -1):  # i in range() is counting the items in a list that starts from seconds and ends at 0 decreasing in intervals of 1. This could be changed for example -2 would decrease 2x the rate
            m, s = divmod(i, 60)
            h, m = divmod(m, 60)
            print(f"{h:02d}:{m:02d}:{s:02d}", end='\r')
            time.sleep(1)
        print("00:00:00", end="\r")
        speak('\n' + "The timer is complete.")
    else:
        print("inval2")
