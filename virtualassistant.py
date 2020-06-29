import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime  # preinstalled
import webbrowser  # preinstalled
import wikipedia  # pypi
import googlesearch as google  # pip install google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Virtual Assistant. How can I help you?")


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

        print("Recognizing.")
        query = r.recognize_google(audio, language='en-in')

        print(f"You said: {query}")

    return query


if __name__ == '__main__':
    wish_me()
    while True:
        query = listen().lower()

        # Logic for the commands.

        if 'wikipedia' in query:
            print("Searching Wikipedia.")
            query = query.replace("wikipedia", '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to Wikipedia")
            speak(result)
        elif 'open' in query:
            options = {'google': 'google.com', 'stack overflow': 'stackoverflow.com'}
            for key in options.keys():
                if f'{key}' in query:
                    speak(f"Opening {key}")
                    webbrowser.open(options.get(key))
        elif 'thank you' in query:
            speak("My pleasure to help you mate!")
        elif 'google' in query:
            query = query.replace('google', '')
            for result in google.search(query, num=10, stop=10):
                print(result)
        elif 'exit' in query:
            speak("It was fun while it lasted.... Bye")
            exit()
        else:
            speak("I am not sure what you mean by that...")
