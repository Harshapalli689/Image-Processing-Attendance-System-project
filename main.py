from AIBrain import ReplyBrain #Brain of the Automation Bot using chat_log txt and api to talk.
from Qna import QuestionsAnswer#To answer for the technical questions to that answered by the automation bot.
from Listen import MicExecution#This is used by the bot to MicExecution the words of the human or Voice Recognition.
from date_time import date,time#This is date & time function to know the date & time now.
from wikipedia import tell_me_about#This searchs the content from the webbrowser wikipedia for the user Data to know from the google.
from AppOpener import close,open#This will close and the applications that are running or installed in windows.
from youtube_search import Search#This will search the required videos for the user from the youtube.
from website_open import website_opener#This will opens the Google chrome and searchs what that the user required from the bot from google.
from sendmsgwhatsapp import send_whatsapp_message#This is used by the bot that the user need to send a specified message for the required user.
from google_calendar import get_date,get_events,authenticate_google
from loc import my_location,loc#This  is used to get the location of the user.
import pyjokes#To make jokes by bot
from system_stats import system_stats#System statistics of my windows.
import os#This is used by the bot to handle the os.
from systeminfo import sysinfo#To get the information of the System.
print(">> Starting The PC bot : Wait For Some Seconds.")
from Speak import speak#This is used by the bot to Speak.
import sys#This is to go offline of bot.
from time import*
from pygame import mixer #This is used to play the notification sound for the tasks speficied in the tasks file. 
from plyer import notification#This is used to notify the Tasks in the Tasks.txt file.
import pyautogui#This is used to Perform the tasks.
from tasks import task,show#This is used to set and show the task.
from Alaram import alarm# This is used to set the alarm.
from remember import remem,remembered #This is used to remember the things that the user told to pc.
from tkinter import*
from PIL import Image, ImageTk
import datetime
# Create the main window
root =Tk()

# Set the title of the window
root.title("Chatbot and GIF")
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

print(">> Starting The PC bot : Wait For Few Seconds More")
"""
I have to implement the tasks are :
1.Reading the news.
2.Telling the Cricket Score.
3.Calender and Events.
4.Fetch my Location.
"""
def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        text = "Good Morning sir. I am Your PC Bot. How can I Assist you?"
    elif 12 <= hour < 18:
        text = "Good Afternoon sir. I am Your PC Bot. How can I Assist you?"
    else:
        text = "Good Evening sir. I am Your PC Bot. How can I Assist you?"

def MainExecution():
    speak("Hello Sir")
    speak("I'm your PC bot, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data)
        from date_time import time,date
        if "time now" in Data:
            speak("Now the time is")
            speak(time())

        elif "date" in Data:
            speak("Todays date is")
            speak(date())


        elif "go to sleep" in Data:
            speak("Ok sir , You can call me anytime")
            break 

        elif "system info" in Data:
            speak("Your pc info is")
            sysinfo()
        
        elif "windows statistics" in Data:
            speak("your pc statistics are")
            speak(system_stats())
                
        elif "joke" in Data or "jokes" in Data or "pc joke" in Data:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

        elif "turn on the tv" in Data:# Specific COmmand
            speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            speak(Reply)

        elif ("search in chrome" in Data) or ("open chrome" in Data) or ("google" in Data):
            speak("Tell me What i have to search sir!..")
            D=MicExecution()
            print(D)
            speak("opening")
            speak(D)
            website_opener(D)

        elif "hide all files" in Data or "hide this folder" in Data:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

        elif "visible" in Data or "make files visible" in Data:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

        elif "tell me about" in Data:
            speak(tell_me_about(Data))

        elif "goodbye" in Data or "offline" in Data or "bye" in Data:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

        elif "where is" in Data:
                place = Data.split('where is ', 1)[1]
                current_loc, target_loc, distance =loc(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)
        elif "where i am" in Data or "current location" in Data or "where am i" in Data:
                try:
                    city, state, country = my_location()## I have to make Execute  ##
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

        elif ("calendar" in Data) or ("events" in Data) or ("days" in Data):
            speak("Tell me the date sir..")
            text=MicExecution()
            text=text.lower()
            service =authenticate_google()##I have to make execute ##
            date =get_date(text)
            if date:
                get_events(date, service)

        elif ("open WhatsApp" in Data) or ("WhatsApp" in Data) or ("message using whatsapp" in Data) or ("message" in Data):
            speak("Opening Whatsapp Sir!!")
            speak("What message i have to send Sir!!")
            quer=MicExecution()
            speak(f"Searching sir.")
            text=quer.lower()
            send_whatsapp_message(text)

        elif "search youtube" in Data or "youtube" in Data:
            speak("Opening Youtube Sir!!")
            speak("What i have to search Sir!!")
            quer=MicExecution()
            speak(f"Searching sir.")
            text=quer.lower()
            Search(text)

        elif "schedule my day" in Data:
            speak("Task is scheduling")
            task()

        elif "show my schedule" in Data:
                show()
        elif "internet speed" in Data:
                import speedtest
                wifi  = speedtest.Speedtest()
                upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                download_net = wifi.download()/1048576
                print("Wifi Upload Speed is", upload_net)
                print("Wifi download speed is ",download_net)
                speak(f"Wifi download speed is {download_net}")
                speak(f"Wifi Upload speed is {upload_net}")

        elif "ipl score" in Data:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
                    a = print(f"{team1} : {team1_score}")

                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
        elif "play a game" in Data:
                    from game import game_play
                    game_play()
        
        elif "screenshot" in Data:
            import pyautogui #pip install pyautogui
            im = pyautogui.screenshot()
            im.save("scrsht.jpg")
        
        elif "click my photo" in Data:
            import pyautogui
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif "one tab" in Data or "1 tab" in Data:
            speak("Closing,sir")
            import pyautogui
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")

        elif "2 tab" in Data:
            import pyautogui
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "3 tab" in Data:
            import pyautogui
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "4 tab" in Data:
            import pyautogui
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "5 tab" in Data:
            import pyautogui
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")

        elif "hello" in Data:
            speak("Hello sir, how are you ?")

        elif "i am fine" in Data:
            speak("that's great, sir")

        elif "how are you" in Data:
            speak("Perfect, sir")

        elif "thank you" in Data:
            speak("you are welcome, sir")

        elif "pause" in Data:
            import pyautogui
            pyautogui.press("k")
            speak("video paused")
        elif "play" in Data:
            import pyautogui
            pyautogui.press("k")
            speak("video played")
        elif "mute" in Data:
            import pyautogui
            pyautogui.press("m")
            speak("video muted")

        elif "news" in Data:
            from NewsRead import latestnews##Have to add apis
            latestnews()

        elif "temperature" in Data:
            import requests 
            from bs4 import BeautifulSoup
            search = "temperature in my place"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current temperature in your place is {temp}")

        elif "weather" in Data:
            import requests 
            search = "temperature in my place"
            from bs4 import BeautifulSoup
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current weather in your place is {temp}")

        elif "set an alarm" in Data:
            print("input time example:- 10 and 10 and 10")
            speak("input time example:- 10 and 10 and 10")
            speak("Set the time")
            speak("Please tell the time :- ")
            a=input("set the time by manual like 10and10and10")
            alarm(a)
            speak("Done,sir")
        
        elif "remember that" in Data:
            rememberMessage = Data.replace("remember that"," ")
            rememberMessage = Data.replace("pc" or "bot","")
            speak("You told me "+rememberMessage)
            remem(rememberMessage)
           

        elif "what do you remember" in Data:
            remembered()

        elif "volume up" in Data:
            from keyboard import volumeup
            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in Data:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()

        elif "shutdown system" in Data:
            speak("Are You sure you want to shutdown")
            shutdown = MicExecution()
            if shutdown == "yes":
                os.system("shutdown /s /t 1")

            elif shutdown == "no":
                break
        

        elif "open" in Data:#for opening windows apps
            app_name = Data.replace("open ","")
            speak("opening")
            speak(app_name)
            open(app_name, match_closest=True)

        elif "close" in Data:#closing the windows apps
            app_name = Data.replace("close ","").strip()
            speak("closing")
            speak(app_name)
            close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
        
        else:
            if Data!=""  and Data!=[]:
                Reply = ReplyBrain(Data)
                speak(Reply)
MainExecution() 

# 10% 
