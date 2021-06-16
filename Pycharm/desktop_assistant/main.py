import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id)


# engine.runAndWait()
# engine.stop()
print(voices[5].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# if __name__ == '__main__':
#     speak("What are you doing?")
