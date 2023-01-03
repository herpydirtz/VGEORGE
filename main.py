from apps import filer, rng, timer, measurements
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
#need to install pyaudio, webbrowser, pyttsx3, speechrecognition

def parse_request():  # takes user_input and turns it into the valid app
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            user_input = r.recognize_google(audio, language='en-in')
            print("the command is printed=", user_input)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return user_input


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # [0] for male, [1] for female voice
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


speak("Hello this is your virtual assistant, how may I be of service?")

def main():    
    while (True):
        user_input = parse_request().lower().split()
        if "timer" in user_input or "countdown" in user_input: # TODO: give the ability to use short phrase like "mins" and allow for the time to be inserted before the word timer ie "create a 5 minute timer"
            timer.timer(user_input)
        elif ("random" in user_input or "pick" in user_input) and ("number" in user_input or "numbers" in user_input) in user_input:   #add "pick a number"
            rng.rng(user_input)
        elif "flip" in user_input and ("coin" in user_input or "coins" in user_input):
            rng.coin(user_input)
        elif "roll" in user_input:
            rng.dice(user_input)
        elif "open" in user_input and "filer" in user_input:
            filer.filer(user_input)
        elif "open" in user_input and "google" in user_input:
            wb.open("www.google.com")
        elif "measurement" in user_input or "measurements" in user_input:
            speak("please enter the numerical quantity you would like to convert")
            amount = input("please enter the numerical quantity you would like to convert: ")
            #amount = r.recognize_google(audio, language='en-in')
            speak("type the conversion number you would like: ")
            #selection = r.recognize_google(audio, language='en-in')
            selection = input("type the conversion number you would like: ")
            measurements.measurements(amount, selection)
        #elif "area" in user_input and "circle" in user_input:
        #    measurements.measurements(user_input)
        elif "quit" in user_input or "leave" in user_input or "exit" in user_input: 
            exit()
        else:
            main()

if __name__ == "__main__":
    main()
'''

commands = {
    (("timer", "countdown")): (timer.timer,),
    (("random", "pick"), ("number", "numbers")): (rng.rng,),
    (("flip"), ("coin", "coins")): (rng.coin,),
    (("roll")): (rng.dice,),
    (("open"), ("filer")): (filer.filer,),
    (("open"), ("google")): (wb.open, "www.google.com"),
    #(("measurement", "measurements")): (measurements.measurementsxd ,)
}


def list_intersection(a, b):
    a_set = set(a)
    b_set = set(b)
    return a_set.intersection(b_set)


def main():
    speak("Hello this is your virtual assistant, how may I be of service?")
    while (True):
        user_input = parse_request().lower().split()

        if "quit" in user_input:
            exit()

        for keywords, actions in commands.items():
            input_matches = True

            for or_list in keywords:
                if len(list_intersection(or_list, user_input)) == 0:
                    input_matches = False

            if input_matches:
                if len(actions) > 1:
                    # this is for special input, see google
                    actions[0](actions[1])
                else:
                    actions[0](user_input)
                break


if __name__ == "__main__":
    main()
'''