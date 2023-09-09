import pyttsx3


# def Say(Text):
#     engine.setProperty("rate", 160)
#     engine.setProperty("volume", 0.4)
#     # voices = engine.getProperty("voices")
#     # engine.setProperty("voices" , voices[1].id)
#     print("     ")
#     print(f"AI : {Text}")
#     engine.say(text = Text)
#     engine.runAndWait()
#     print("     ")

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 160)
    print("   ")
    print(f"SAI : {Text}")
    engine.say(text = Text)
    engine.runAndWait()
    print("     ")

Say("hello")



