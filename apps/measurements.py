import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # [0] for male, [1] for female voice
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def measurements(amount, selection):
    selection = selection.split()
    lengths = {"inches to feet":12,
"inches to yards":36,
"inches to miles":63360,
"inches to kilometers":39370,
"inches to meters":39.37,
"inches to centimeters":0.3937,
"inches to millimeters":0.003937,
"inches to micrometers":0.00003937,
"inches to nanometers":0.00000003937,
"inches to picometers":0.00000000003937,
"feet to miles":5280,
"feet to kilometers":3280.84,
"feet to meters":3.28084,
"feet to centimeters":0.0328084,
"feet to millimeters":0.00328084,
"feet to micrometers":0.00000328084,
"feet to nanometers":0.00000000328084,
"feet to picometers":0.00000000000328084,
"feet to yards":3,
"yards to miles":1760,
"yards to kilometers":1093.61,
"yards to meters":1.9361,
"yards to centimeters":0.019361,
"yards to millimeters":0.0019361,
"yards to micrometers":0.0000019361,
"yards to nanometers":0.0000000019361,
"yards to picometers":0.0000000000019361,
"miles to kilometers":0.621371,
"miles to meters":0.000621371,
"miles to centimeters":0.00000621371,
"miles to millimeters":0.000000621371,
"miles to micrometers":0.000000000621371,
"miles to nanometers":0.000000000000621371,
"miles to picometers":0.000000000000000621371,
"kilometers to meters":0.001,
"kilometers to centimeters":0.00001,
"kilometers to millimeters":0.000001,
"kilometers to micrometers":0.000000001,
"kilometers to nanometers":0.000000000001,
"kilometers to picometers":0.000000000000001,
"meters to centimeters":0.01,
"meters to millimeters":0.001,
"meters to micrometers":0.000001,
"meters to nanometers":0.000000001,
"meters to picometers":0.000000000001,
"centimeters to millimeters":0.1,
"centimeters to micrometers":0.0001,
"centimeters to nanometers":0.0000001,
"centimeters to picometers":0.0000000001,
"millimeters to micrometers":0.001,
"millimeters to nanometers":0.000001,
"millimeters to picometers":0.000000001,
"micrometers to nanometers":0.001,
"micrometers to picometers":0.000001,
"nanometers to picometers":0.001}

    measurement1, dump, measurement2 = selection

    scenario1 = f"{measurement1} to {measurement2}" #scenario 1 looks at the measurement selection and if it is larger i.e inches to feet it will divide by 12
    scenario2 = f"{measurement2} to {measurement1}" #scenario 2 does the opposite, will multiply by 2

    if scenario1 in lengths.keys():
        speak(f'{amount} {measurement1} is equal to {float(amount) / float(lengths.get(scenario1))} {measurement2}')
    elif scenario2 in lengths.keys():
        speak(f'{amount} {measurement1} is equal to {float(lengths.get(scenario2)) * float(amount)} {measurement2}')



