import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import time
import numpy
import tflearn
import tensorflow 
import random
import json
import pickle
import nemo
import text as t
import os,datetime
with open("intents.json") as file:
    data = json.load(file)


"""try:
    with open("data.pickle","rb") as f:
        words,labels,training,output=pickle.load
except:"""
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = numpy.array(training)
output = numpy.array(output)
"""with open("data.pickle","wb") as f:
    pickle.dump((words,labels,training,output),f)"""
tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

#try:
#    model.load("model.tflearn")
#except:
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_word(s,words):
    bag=[0 for _ in range(len(words))]

    s_words=nltk.word_tokenize(s)
    s_words=[stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i ,w in enumerate(words):
            if w==se:
                bag[i]=1
    return numpy.array(bag)

def AImain(requiment):
    
    try:
        #requiment=nemo.ask()
        if "open Facebook" in requiment:
            t.open_facebook()
        elif "open Gmail" in requiment:
            t.open_gmail()
        elif "open GitHub" in requiment:
            t.open_github()
        elif "open Wiki" in requiment:
            t.open_wiki()
        elif "song" in requiment and "YouTube" in requiment:
            song=requiment.split()
            song=song[1:requiment.index("song")]
            song="".join(song)
            t.open_video_on_youtube(song)
        elif "open YouTube" in requiment:
            t.open_youtube()
            
        elif 'open code' in requiment:
            os.startfile(r'C:\Program Files (x86)\Sublime Text 3\sublime_text.exe')
        elif 'search' in requiment:
            link=b.replace("open","")
            t.open_google(link)
        elif "weather in" in requiment:
            data=' '.join(requiment.split()[2:])
            weather=nemo.get_weather(data)
            print(weather)
            nemo.tts(weather)
        elif 'film' in requiment:
            data=' '.join(requiment.split()[1:requiment.index('flim')])
            t.opem_flim(data)
        elif 'time' in requiment:
            time=str(datetime.datetime.now().hour)+" and "+str(datetime.datetime.now().minute)+' minute'
            nemo.tts_orther(time,'vi')
    except:
        pass
    
def chat():
    print("Start talking with Nemo!...")
    time.sleep(3)
    while True:
        try:
            you_talk=nemo.ask()
            print(f"you:{you_talk}")
            stop=["quit","exit"]
            if you_talk.lower() in stop:
                break
            results=model.predict([bag_of_word(you_talk,words)])
            max_index=numpy.argmax(results)
            tag=labels[max_index]
            for t in data['intents']:
                if tag==t["tag"]:
                    rep=random.choice(t["responses"])
                    print(f"bot:{rep}")
                    nemo.tts(rep)
            AImain(you_talk)

        except:
            print("say that again,sir")
            nemo.tts("say that again,sir")


chat()
