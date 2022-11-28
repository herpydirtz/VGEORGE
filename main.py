from apps import filer, rng, timer, measurements
import speech_recognition as sr
import pyttsx3
import webbrowser as wb

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
    engine.setProperty('voice', voices[1].id)  # [0] for male, [1] for female voice
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
            measurements.measurements(user_input)
        elif "quit" in user_input:
            exit()
        else:
            main()

if __name__ == "__main__":
    main()
