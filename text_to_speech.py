import pyttsx3

engine = pyttsx3.init()


def speak(text, speed=140):
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.alex')
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()
    

    