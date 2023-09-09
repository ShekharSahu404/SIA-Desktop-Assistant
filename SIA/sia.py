import random
import json
import torch
from brain import NeuralNet
from NeuralNetwork import bag_of_words ,tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data= torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size , output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-------------------
Name = "sia"
from listen import listen
from speak import Say
from task import NonInputExecution ,InputExecution
# from task import

def Main():
    sentence =listen()

    result = str(sentence)

    if sentence == "bye":
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tags"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date"in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply,result)

                elif "google" in reply:
                    InputExecution(reply,result)

                elif "whatsapp" in reply:
                    InputExecution(reply, result)

                elif "youtube" in reply:
                    InputExecution(reply,result)

                elif "data_create"  in reply:
                    InputExecution(reply,result)

                elif "camera" in reply:
                    NonInputExecution(reply)

                    #---------------------
                elif "setting" in reply:
                    NonInputExecution(reply)
                elif "clock" in reply:
                    NonInputExecution(reply)

                elif "calculator" in reply:
                    NonInputExecution(reply)

                elif "file_explorer" in reply:
                    NonInputExecution(reply)

                elif "calendar" in reply:
                    NonInputExecution(reply)

                elif "notepad" in reply:
                    NonInputExecution(reply)

                elif "paint" in reply:
                    NonInputExecution(reply)

                elif "photos" in reply:
                    NonInputExecution(reply)

                elif "brave" in reply:
                    NonInputExecution(reply)

                # elif "mail" in reply:
                #     NonInputExecution(reply)

                elif "voice_recorder" in reply:
                    NonInputExecution(reply)

                elif "terminal" in reply:
                    NonInputExecution(reply)

                elif "wordpad" in reply:
                    NonInputExecution(reply)

                elif "vlc" in reply:
                    NonInputExecution(reply)

                elif "microsoft_edge" in reply:
                    NonInputExecution(reply)

                elif "close_all" in reply:
                    InputExecution(reply,result)



                else:
                    Say(reply)




while True:
    Main()

