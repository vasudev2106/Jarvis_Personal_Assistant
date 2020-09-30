import pyttsx3 #text to speech
import datetime #for using datetime functions
import speech_recognition as sr #speech to text
import wikipedia #for using wikipedia 
import webbrowser #for using webbrowser
import os # for using os releated calls

engine = pyttsx3.init("sapi5")#pyttsx3.init([driverName : string, debug : bool]) → pyttsx3.Engine
#Gets a reference to an engine instance that will use the given driver. If the requested driver is already in use by another 
# engine instance, that engine is returned. Otherwise, a new engine is created.
voices = engine.getProperty("voices") #Queues a command to set an engine property. The new property value affects all utterances queued
                                     # after this command.
                                     #Parameters:	1)name – Name of the property to change.
                                     #              2)value – Value to set.
                                     #Properties:
                                     #rate:Integer speech rate in words per minute.
                                     #voice:String identifier of the active voice.
                                     #volume:Floating point volume in the range of 0.0 to 1.0 inclusive.


#print(voices[0].id)
engine.setProperty("voice",voices[0].id)#for setting voice property

#it speaks the audio
def speak(audio):
    '''#it speaks the audio'''
    engine.say(audio) #Queues a command to speak an utterance. The speech is output according to the properties set before this 
                      #command in the queue.
                      #Parameters:	1)text – Text to speak.
                      #             2)name – Name to associate with the utterance. Included in notifications about this utterance.
    engine.runAndWait() #Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately.
                       # Returns when all commands queued before this call are emptied from the queue.

#function to wish the Boss
def wishMe():
    '''#function to wish the Boss'''
    hour = int(datetime.datetime.now().hour) #it will give the hour value from the current time
    if hour>=0 and hour<12:    #if hour value  is between 0(inclusive) and 12 system will speak "Hi!Good Morning Boss!"
        speak("Hi!Good Morning Boss!")
    elif hour>=12 and hour<18:  #if hour value  is between 12(inclusive) and 18 system will speak "Hi!Good Afternoon Boss!"
        speak("Hi!Good Afternoon Boss!")  
    else: 
        speak("Hi!Good Evening Boss!")
    speak("Jarvis Here!Speed 1 terahertz!Memory 1 zetabyte!What you want me to do sir?")  

#function to speak user defined text 
def openingJarvis(): 
    '''#function to speak user defined text '''
    speak("Opening Jarvis")
    os.startfile("C:\\Users\\vasu\\Documents\\Python projects\\Jarvis_chatbot\\jarvis_wallpaper.png")# open wallpaper file
    speak("Collecting all remote servers!Establishing secure connection!Starting all system!Downloading and installing all required drivers!")
    speak("Just a second Boss!Secure connection established! All systems have started!All drivers are securely installed in your private servers!")
    speak("Please wait for a moment Boss!Now I am Online!")

#function to take command from user and interpret it to text
def takeCommand():
    '''#function to take command from user and interpret it to text'''
    r=sr.Recognizer() #creating a object of recognizer class of speech_recognition
    with sr.Microphone() as source: #using microphone as source
        print("Listening.....")
        r.pause_threshold = 1 #it will inc the time limit for listening the voice of user
        audio = r.listen(source) #it will listen the voice of user and  save it into audio variable
    try: #if sound  is recognised properly
        print("Recognizing.....")
        query = r.recognize_google(audio,language="en-in") #uses google recognizer to decode the audio of user and convert it into text
        print(f"User said:{query}\n")    
    except Exception as e:#For exception it will ask for speaking again
        print("Say that again please....")
        return "None"    
    return query #return query


#code runs from here   
if __name__ == "__main__":

    openingJarvis() #calling openingJarvis() function 
    wishMe()     #calling wishMe() function 
    
    while True:#loop for executing again and again

        query = takeCommand().lower() #convert query into lower case 


        if "wikipedia" in query:# id wikipedia in query
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")#replace wikipedia word from space so it will search only for special keyword
            results = wikipedia.summary(query,sentences=2)#sumaary function stores the 2lines summary of keyword in result variable
            speak("According to wikipedia")
            #print(results)
            speak(results)#speak the result
            speak("What else you want me to do")

        elif "notepad" in query: #if notepad in query
            os.startfile("C:\\Windows\\system32\\notepad.exe")   #start the notepad
            speak("What else you want me to do") 

        elif "youtube" in query:#if youtube in query
            webbrowser.open("https://www.youtube.com/") #start the youtube through link provide
            speak("What else you want me to do")

        elif " google" in query:#if google in query
            webbrowser.open("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")   #start the  google in chrome
            speak("What else you want me to do") 

        elif " stack" in query:#if stack in query
            webbrowser.open("https://stackoverflow.com/")  #opens stackoverflow link
            speak("What else you want me to do")

        elif " linkedin" in query:#if linkedin in query
            webbrowser.open("https://www.linkedin.com/feed/")    #opens linkedin in browser
            speak("What else you want me to do")  

        elif " track" in query:#if track in query(work for only one track you can also use your system music library to play different songs)
            webbrowser.open("https://www.youtube.com/watch?v=SmM0653YvXU") #start the notepad
            speak("What else you want me to do")

        elif "time" in query:#if time in query
            strTime = datetime.datetime.now().strftime("%H:%M:%S")#it tells current time and strftime formats the time in H:M:S
            speak(f"Boss,The Time is {strTime}")#will speak time
            speak("What else you want me to do")

        elif " vs code" in query:#if vs code in query
            os.startfile("C:\\Users\\vasu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe") #start the vs code 
            speak("What else you want me to do")    
    
         elif 'remember that' in query:#if remember in query 
            speak("what should i remember sir")#it teakes the note ypu speak and save
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')#it give you the note you tell it remember
            speak("you said me to remember that" + remember.read())

        
        elif "leave" or "exit"  in query:#if leave or exit in query
            speak("Cool!I am leaving Boss!Good Bye!... ")
            break #breaks the loops and code is exited
