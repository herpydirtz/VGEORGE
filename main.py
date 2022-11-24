from apps import filer, rng, timer
import speech_recognition as sr
import pyttsx3

def parse_request():  # takes user_input and turns it into the valid app
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Compiling")
            user_input = r.recognize_google(audio, language='en-in')
            print("You said ", user_input)
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

speak("hello sir, I am your desktop assistant. Tell me, how may I assist you?") 

def main():   

    while (True):
        user_input = parse_request().lower().split()
        if "timer" in user_input or "countdown" in user_input: # TODO: give the ability to use short phrase like "mins" and allow for the time to be inserted before the word timer ie "create a 5 minute timer"
            timer.timer(user_input)
        elif "random" in user_input and "number" in user_input:   
            rng.rng(user_input)
        elif "flip" in user_input and ("coin" in user_input or "coins" in user_input):
            rng.coin(user_input)
        elif "roll" in user_input:
            rng.dice(user_input)
        elif "open" in user_input and "filer" in user_input:
            filer.filer(user_input)
        elif "what is your name" in user_input:
            speak("I am Vgeorge, your desktop assistant")
        elif "quit" in user_input:
            exit()
        else:
            main() 

if __name__ == "__main__":
    main()
