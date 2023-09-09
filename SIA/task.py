import datetime

import speak
from speak import Say
import webbrowser as web
import time
import keyboard
from listen import listen
import pymysql
from AppOpener import open, close, mklist, give_appnames
from fuzzywuzzy import fuzz
import pygetwindow as gw
import pyautogui
# from os_module  import play_music
# from os_module import increase_volume
# from os_module import decrease_volume
# from os_module import mute_volume
# from  os_module import unmute
# from os_module import exit




def close_app_by_title(app_title):
    # Get a list of all open windows
    windows = gw.getWindowsWithTitle(app_title)

    # Close each window with the specified title
    for window in windows:
        window.close()

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def date():
    date = datetime.date.today()
    Say(date)

def whatsapp(number, message):
    numb = '+91' + str(number)  # Convert the number to a string
    open_chat = "https://web.whatsapp.com/send?phone=" + numb + "&text=" + message
    web.open(open_chat)
    time.sleep(10)
    keyboard.write(message)
    time.sleep(2)
    keyboard.press('enter')

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        date()

    elif "camera" in query:
        open("Camera")

        #---------
    elif "setting" in query:
        open("Settings")

    elif "clock" in query:
        open("Clock")

    elif "calculator" in query:
        open("Settings")

    elif "file_explorer" in query:
        open("File Explorer")

    elif "calendar" in query:
        open("Calendar")

    elif "notepad" in query:
        open("Notepad")

    elif "paint" in query:
        open("Paint")

    elif "photos" in query:
        open("Photos")

    elif "brave" in query:
        open("Brave")

    # elif "mail" in query:
    #     open("Mail")

    elif "voice_recorder" in query:
        open("Voice recorder")

    elif "terminal" in query:
        open("Terminal")

    elif "wordpad" in query:
        open("WordPad")

    elif "vlc" in query:
        open("VLC media player")

    elif "microsoft_edge" in query:
        open("Microsoft Edge")

    # elif "close_all" in query:
    #     close("Microsoft Edge","VLC media player","WordPad","Terminal")
    #     close( "Brave", "Photos", "Paint")
    #     close("Notepad","Calendar","File Explorer","Settings")
    #     close("Clock","Camera")





    # elif "data_create" in query:
    #     dbquery = "create database hackathon4"
    #     cursor.execute(dbquery)
    #     print("sucessfully created...")





def InputExecution(tag, query):

    if "wikipedia" in tag:
        name = str(query).replace("what is","").replace("who is","").replace("sia  kya hai","").replace("sia bata","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query=str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)

    elif "youtube" in tag:
        speak.Say("ok sir i found that")
        query = query.replace("sia", "")
        query = query.replace("youtube search", "")
        web1 = 'https://www.youtube.com/results?search_query=' + query
        web.open(web1)
        print("done sir")

    elif "data_create" in tag:
        query = query.replace("sia","")
        query = query.replace("make", "")
        query = query.replace("open kar", "")
        query = query.replace("database", "")
        query = query.replace("database bana", "")
        query = query.replace("create", "")
        db_name = query
        db_name = db_name.strip()

        query1 = f"CREATE DATABASE `{db_name}`"


    elif "close_all" in query:
        query = str(query).replace("close","")
        query = str(query).replace("kar", "")
        query = str(query).replace("band", "")
        query = str(query).replace("destroy ", "")
        query = str(query).replace("one","")
        query = str(query).replace("that", "")
        query = str(query).replace("kill", "")
        query = str(query).replace("sab", "")

        target_words = ["Terminal", "Notepad", "WordPad","Camera","Brave"]

        # Get user input
        user_input = query

        # Initialize variables to keep track of the best match
        best_match = None
        best_ratio = 0

        # Iterate through the list of target words
        for target_word in target_words:
            # Calculate the similarity ratio (0-100) between user input and the current target word
            similarity_ratio = fuzz.ratio(user_input.lower(), target_word.lower())

            # Check if the similarity ratio is greater than the best ratio
            if similarity_ratio > best_ratio:
                best_ratio = similarity_ratio
                best_match = target_word

        # Check if the best match ratio is greater than or equal to 80%
        if best_ratio >= 80:
            # Replace user input with the best match
            user_input = best_match

        print("Processed input:", user_input)
        close_app_by_title(user_input)















    elif "whatsapp" in tag:
        query = str(query).replace("whatsapp","")
        speak.Say("name of the person")


        user_name = listen()
        print(user_name)


        contact_list = [
            {"name": "time", "phone": "9294632129"},
            {"name": "samiksh", "phone": "8770874862"},
            {"name": "shekhar", "phone": "9340882673"},
        ]
        found_contact = None

        for contact in contact_list:
            if user_name == contact["name"].lower():
                found_contact = contact
                break
        if found_contact:
            whatsapp(found_contact["phone"], query)
            print(f"Message sent to {found_contact['name']} ({found_contact['phone']}): {query}")
        else:
            print(f"Contact '{user_name}' not found in your contact list.")

        # whatsapp(9575930725,query )         #"so rha hai"














# import datetime
# date = datetime.date.today()
# print(date)

    # elif "whatsapp" in tag:
    #     query = str(query).replace("whatsapp", "")
    #     whatsapp(9575930725, query)