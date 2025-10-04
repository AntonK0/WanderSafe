import pyttsx3

engine = pyttsx3.init()

def speak(text, speed=140):
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    speak("Hello, Anton! Are u ok??", 180)
    