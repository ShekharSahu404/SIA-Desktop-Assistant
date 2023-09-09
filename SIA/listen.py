import speech_recognition as sr

# def listen():
#     r= sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print("Listeninng...")
#         r.pause_threshold = 1
#         audio = r.listen(source,0,4)
#
#     try:
#         print("Recogninzing..")
#         query = r.recognize_google(audio , language="en-in")
#         print(f"you said : {query}")
#
#     except:
#         return  ""
#
#     query = str(query)
#     return  query.lower()
#
#
# listen()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # print(f"Using {sr.Microphone.list_microphone_names()[1]} as the default microphone.")
        print("Listeninng...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recogninzing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"you said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()



listen()







# Replace 'your_microphone_index' with the index of your earphones' microphone
# with sr.Microphone(device_index=1) as source:
#     print(f"Using {sr.Microphone.list_microphone_names()[1]} as the default microphone.")

# try:
#     with sr.Microphone(device_index=1) as source:
#         print("Please speak something...")
#         audio = recognizer.listen(source)
#
#     # Perform speech recognition on the captured audio
#     text = recognizer.recognize_google(audio)
#     print(f"You said: {text}")
#
# except sr.RequestError as e:
#     print(f"Could not request results; {e}")
# except sr.UnknownValueError:
#     print("Could not understand audio")
