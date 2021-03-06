import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
alexa = pyttsx3.init()

voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():

    with sr.Microphone() as source:
        print('Device is listening, please speak...')
        voice = listener.listen(source)
        commands = listener.recognize_google(voice)
        commands = commands.lower()
        if 'alexa' in commands:
            commands = commands.replace('alexa', '')

    return commands


def run_alexa():
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        wiki = command.replace('tell me about', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    else:
        talk('Sorry I did not get your question, I can search it from google')
        pywhatkit.search(command)


run_alexa()