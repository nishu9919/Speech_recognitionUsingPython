import pyttsx3 , datetime, wikipedia, webbrowser, os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print(voices[0].id)
print(voices[1].id)
print(voices[2].id)
engine.setProperty('rate', voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    pass

def wishMe () :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        engine.say("Good Evening")
    speak("Please tell me How may I help you")

def takeCommand():
    #It takes microphone input from the uesr and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising......")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said :  {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..........")
        return "None"
    return query



if __name__ == "__main__":
    speak("Welcome Nishu ,I hope you are doing well")
    wishMe()
    #while True:
    if 1 :
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3) #senetences cnt for info
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("goggle.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverfolw.com")

        elif 'open quora' in query:
            webbrowser.open("quora.com")

        elif 'play music' in query:
            music_dir = 'E:/Music'
            music_dir = 'E:/Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open visual studio' in query:
            vs_path = "C:\\Users\\Sony Vaio\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(vs_path)          #path to Visual studio

