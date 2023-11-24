from multiprocessing import process
import sys

print(sys.executable)
print(sys.path)

import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes                     #For some really bad jokes
from playsound import playsound    #To playsound
import keyboard                    #To get keyboard
import asyncio
import threading

def lazy_load_libraries():
    global engine, voices
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

lazy_load_libraries()

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()
    
def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait() 


def wishMe():

  hour=datetime.datetime.now().hour

  if hour >= 6 and hour < 12:

      speak("Hello,Good Morning")
 
  elif hour >= 12 and hour < 17:

      speak("Hello,Good Afternoon")

  else:

      speak("Hello,Good Evening")


def get_audio(): 

    r = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 

        print("Listening") 
        playsound("assistant_on.wav")
        audio = r.listen(source, phrase_time_limit = 3) 
        playsound("assistant_off.wav")
        print("Stop.") 
        
    try: 
        text = r.recognize_google(audio, language ='en-US') 
        print('You: ' + ': ' + text)
        return text


    except:

        return "None"
    
def note_async(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    def write_note():
        with open(file_name, "w") as f:
            f.write(text)

    thread = threading.Thread(target=write_note)
    thread.start()

    subprocess.Popen(["notepad.exe", file_name])


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

wishMe()

async def async_wikipedia_search(statement):
    try:
        speak('Searching Wikipedia...')
        statement = statement.replace("wikipedia", "")
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(None, lambda: wikipedia.summary(statement, sentences=3))
        speak("According to Wikipedia")
        wikipedia_screen(results)
    except:
        speak("Error")
        
def Process_audio():

    run = 1
    if __name__=='__main__':
        while run==1:

            app_string = ["open word", "open excel", "open discord","open notepad",  "open chrome"]
            app_link = [r'\Word.lnk', r'\Excel.lnk', r'\Discord.lnk', r'\Notepad.lnk', r'\Google Chrome.lnk']
            app_dest = [r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs']

            statement = get_audio().lower()
            results = ''
            run +=1

            if "hello" in statement or "hi" in statement:

              wishMe()               


            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant ' + name_assistant +' is shutting down, Good bye')
                screen.destroy()
                break

            if 'wikipedia' in statement:
                asyncio.run(async_wikipedia_search(statement))


            if 'joke' in statement:
              speak(pyjokes.get_joke())    
     
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)


            if 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)


            if 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Google Mail open now")
                    time.sleep(5)

            if 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Netflix open now")


            if 'open prime video' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")
                    time.sleep(5)

            if app_string[0] in statement:
                os.startfile(app_dest[0] + app_link[0])

                speak("Microsoft office Word is opening now")


            if app_string[1] in statement:
                os.startfile(app_dest[0] + app_link[1])
                speak("Microsoft office Excel is opening now")
        
            if app_string[2] in statement:

                os.startfile(app_dest[0] + app_link[2])
                speak("Discord is opening now")


            if app_string[3] in statement:
                os.startfile(app_dest[0] + app_link[3])
                speak("Notepad is opening now")
        
            if app_string[4] in statement:
                os.startfile(app_dest[0] + app_link[4])
                speak("Google chrome is opening now")
                       

            if 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/Delhi")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            if 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in statement:
                date()

            if 'who are you' in statement or 'what can you do' in statement:
                    speak('I am '+name_assistant+' your personal assistant. I am programmed to perform minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra') 


            if 'who made you' in statement or 'who created you' in statement or 'who discovered you' in statement:
                speak('I was built by Jahnvi Jain')

            
            if 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note_async(statement)


            if 'note this' in statement:    
                statement = statement.replace("note this", "")
                note_async(statement)    

            speak(results)


def change_name():

  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()


def change_name_window():
    
      global settings_screen
      global name


      settings_screen = Toplevel(screen)
      settings_screen.title("Settings")
      settings_screen.geometry("300x300")
      settings_screen.iconbitmap('app_icon.ico')

      
      name = StringVar()

      current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
      current_label.pack()

      enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
      enter_label.pack(pady=10)   
      

      Name_label = Label(settings_screen, text = "Name")
      Name_label.pack(pady=10)
     
      name_entry = Entry(settings_screen, textvariable = name)
      name_entry.pack()


      change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
      change_name_button.pack(pady=10)


def info():

  info_screen = Toplevel(screen)
  info_screen.title("Info")
  info_screen.iconbitmap('app_icon.ico')

  creator_label = Label(info_screen,text = "Created by Jahnvi Jain")
  creator_label.pack()

  for_label = Label(info_screen, text = "as a CPT Project!")
  for_label.pack()

keyboard.add_hotkey("F4", Process_audio)


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(screen)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icon.ico')
  wikipedia_screen.geometry("250x250")

  message = Message(wikipedia_screen, text= text)
  message.pack()



def main_screen():

      global screen
      screen = Tk()
      screen.title(name_assistant)
      screen.geometry("220x250")
      screen.iconbitmap('app_icon.ico')


      name_label = Label(text = name_assistant,width = 400, bg = "black", fg="white", font = ("Calibri", 14))
      name_label.pack()


      microphone_photo = PhotoImage(file = "assistant_logo.png")
      microphone_button = Button(image=microphone_photo, command = Process_audio)
      microphone_button.pack(pady=15)

      settings_photo = PhotoImage(file = "settings.png")
      settings_button = Button(image=settings_photo, command = change_name_window)
      settings_button.pack(pady=10)
       
      info_button = Button(text ="Info", command = info, font = ("Calibri", 12))
      info_button.pack(pady=10)

      screen.mainloop()


main_screen()
