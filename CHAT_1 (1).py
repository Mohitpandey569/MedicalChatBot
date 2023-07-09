import nltk
from textblob import TextBlob 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from PIL import Image , ImageTk
from keras.models import load_model
model = load_model('TRIAL_MODEL.h5')
import json
import random
import sqlite3
import tkinter as tk
import pyttsx3 
import PIL.Image
import speech_recognition as sr

converter = pyttsx3.init() 

converter.setProperty('rate', 150) 

converter.setProperty('volume', 1.0) 

intents = json.loads(open('intents2.json').read())


words = pickle.load(open('WORDS.pkl','rb'))
classes = pickle.load(open('CLASSES.pkl','rb'))


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    if 'CHICKEN POX' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='CHICKEN POX'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'FEVER' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='FEVER'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COUGH' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COUGH'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COLD' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COLD'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Contact Dermatitis' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Contact Dermatitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Eye Allergies' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eye Allergies'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Sinus Infection' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Sinus Infection'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Allergic Rhinitis' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Allergic Rhinitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Food Allergy' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Food Allergy'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Anaphylaxis' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Anaphylaxis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Acne' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Acne'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
     
    if 'Eczema' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eczema'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'hives' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='hives'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dark circles' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dark circles'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Blackheads' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Blackheads'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'psoriasis' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='psoriasis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dry, cracked skin' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dry, cracked skin'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    
    if 'ulcers' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ulcers'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'rosacea' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='rosacea'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'open sores or lesions' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='open sores or lesions'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'ringworm' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ringworm'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d   
    else:
        print(res)
        return res 

#Creating GUI with tkinter
import tkinter
from tkinter import *


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: \n" + str(res) + '\n')
        
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
from translate import Translator 
def To_English():
    global file
    pass_text = detect_text()
    en_blob = TextBlob(str(pass_text))
    translated = (en_blob.translate(to='en'))
    print(translated)
    To_English_label = tk.Label(root,text=str(translated),font=('Times New Roman',12,'italic'),width=47,height=30,bg='green4',fg='white')
    To_English_label.place(x=905,y=50)
def SPEECH():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        
        import time
            #language = 'mr'
            #Lang1=c.get()
            #translator= Translator(from_lang=Lang1,to_lang=language)
            #translation = translator.translate(text)
        global file
            
            #en_blob = TextBlob(str(text))
            #translated = (en_blob.translate(to='en'))
            #print(translated)
        time.sleep(1)
        translator= Translator(from_lang="English",to_lang="English")
        translation = translator.translate(text)
        print(translation)
        print(type(translation))
        print('You Said : {}'.format(translation))
        # en_blob = TextBlob(str(translation))
        # translated = (en_blob.translate(to='en'))
        # translated = str(translated)
        # print(str(translated))
        # print(type(translated))
       
     
        
        
       
        
    #msg = listen()
    # print(msg)
    # en_blob = TextBlob(str(msg))
    # translated = (en_blob.translate(to='en'))
    # print(translated)
    language = 'mr'
    # Lang1=c.get()
    # translator= Translator(from_lang=Lang1,to_lang='en-US')
    # translation = translator.translate(msg)
    # print(translation)
    EntryBox.delete("0.0",END)

    if translation != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + translation + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(translation)
        ChatLog.insert(END, "Bot:\n " + "\n"+ str(res)+ '\n\n')
        converter.say(str(res)) 
        converter.runAndWait() 

            
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
def eng_mr():
        import speech_recognition as sr
        from googletrans import Translator
        from translate import Translator as trans
        #from customer.chat import get_response,bot_name
        from gtts import gTTS
        import os

        r = sr.Recognizer()
        print("Please talk")
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=10)
            print("Recognizing...")
                                            # convert speech to text
            text = r.recognize_google(audio_data)
            print("Recognised Speech:" + text)
            a=text
            translator = Translator()
            source_lan = "mr"
            translated_to= "hi"
            translated_text = translator.translate(text, src=source_lan, dest = translated_to)
            res1=translated_text.text
            print(translated_text.text)
            translator1 = Translator()
            source_lan1 = "hi"
            translated_to1= "en"
            translated_text1 = translator1.translate(res1, src=source_lan1, dest = translated_to1)
                                   
            print(translated_text1.text)
            a_res=translated_text1.text
                                            #translator5 = trans(from_lang="en", to_lang="hi")
                                            #data3 = translator5.translate(text)
            result=chatbot_response(a_res)
            #result="hello i am robot"
            print(result)
            translator2 = Translator()
            source_lan2 = "en"
            translated_to2= "mr"
            translated_text2 = translator2.translate(result, src=source_lan2, dest = translated_to2)
                                   
            print(translated_text2.text)
            final=translated_text2.text
                                           
            #print(r)
            context={"user":res1,"bot":final}
            print(context)
            TTS = gTTS(text=str(final))
            TTS.save("voice.mp4")
            os.system("voice.mp4")
            EntryBox.delete("0.0",END)

            if res1 != '':
                ChatLog.configure(state=NORMAL)
                ChatLog.insert(END, "You: " + res1 + '\n\n')
                ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
           
                #res = chatbot_response(a_res)
                ChatLog.insert(END, "Bot:\n " + "\n"+ str(final)+ '\n\n')
                converter.say(str(final)) 
                converter.runAndWait() 

                   
                   
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
    
    
def eng_hi():
        import speech_recognition as sr
        from googletrans import Translator
        from translate import Translator as trans
        #from customer.chat import get_response,bot_name
        from gtts import gTTS
        import os

        r = sr.Recognizer()
        print("Please talk")
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=10)
            print("Recognizing...")
                                            # convert speech to text
            text = r.recognize_google(audio_data)
            print("Recognised Speech:" + text)
            a=text
            # translator = Translator()
            # source_lan = "mr"
            # translated_to= "hi"
            # translated_text = translator.translate(text, src=source_lan, dest = translated_to)
            # res=translated_text.text
            # print(translated_text.text)
            translator1 = Translator()
            source_lan1 = "hi"
            translated_to1= "en"
            translated_text1 = translator1.translate(text, src=source_lan1, dest = translated_to1)
                                    
            print(translated_text1.text)
            a_res=translated_text1.text
            translator5 = trans(from_lang="en", to_lang="hi")
            data3 = translator5.translate(text)
            result=chatbot_response(a_res)
            #result="hello i am robot"
            print(result)
            translator2 = Translator()
            source_lan2 = "en"
            translated_to2= "hi"
            translated_text2 = translator2.translate(result, src=source_lan2, dest = translated_to2)
                                    
            print(translated_text2.text)
            final=translated_text2.text
                                            
            #print(r)
            context={"user":data3,"bot":final}
            print(context)
            TTS = gTTS(text=str(final))
            TTS.save("voice.mp4")
            os.system("voice.mp4")
            
            if data3 != '':
                ChatLog.configure(state=NORMAL)
                ChatLog.insert(END, "You: " + data3 + '\n\n')
                ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
            
                #res = chatbot_response(a_res)
                ChatLog.insert(END, "Bot:\n " + "\n"+ str(final)+ '\n\n')
                converter.say(str(final)) 
                converter.runAndWait() 

                    
                    
                ChatLog.config(state=DISABLED)
                ChatLog.yview(END)
                 

        
    
base = tk.Toplevel()
base.title("Medical Chat bot")

base.configure(background="#A9A9A9")
#base.geometry("600x600")
base.resizable(width=tk.TRUE, height=tk.TRUE)
w, h = base.winfo_screenwidth(), base.winfo_screenheight()
base.geometry("%dx%d+0+0" % (w, h))
load_bg = PIL.Image.open(r"img1.jpg")
load_bg = load_bg.resize((900,805))
render_bg = ImageTk.PhotoImage(load_bg)
bg = tk.Label(base, image = render_bg)
bg.image = render_bg
bg.place(x=880,y=20)

# head_icon=ImageTk.PhotoImage(file="D:/icon1.jpg")
# #Create Chat window
ChatLog = tk.Text(base, bd=2, bg="white",fg="black", height="15", width="150", font="Arial",)

#ChatLog.config(state=DISABLED)
# scrollbar = Scrollbar(ChatLog)
# (scrollbar.pack( side = RIGHT, fill = Y))
#Bind scrollbar to Chat window
# scrollbar = tk.Scrollbar(base, command=ChatLog.yview, cursor="heart")
# ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = tk.Button(base, font=("Verdana",12,'bold'), text="Send", width="15", 
                    bd=0, bg="#6495ED", activebackground="green",fg='#ffffff',
                    command= send)

#Create the box to enter message
EntryBox = tk.Text(base, bd=1, bg="pink",width="100", height="1", font=("Arial",15))
#EntryBox.bind("<Return>", send)

c=StringVar()
#Place all components on the screen
head = tk.Label(base,width=70,text="Voice Based Medical Assistant ChatBot",font=("times",30,'bold',"italic"),bg="#8B0A50",fg="White",height=2)
head.place(x=0,y=0)
#scrollbar.place(x=850,y=20, height=900)
ChatLog.place(x=0,y=100, height=500, width=880)
SendButton.place(x=200, y=700, height=80)
EntryBox.place(x=0, y=600, height=100, width=880)


head = tk.Label(base,width=20,text="Voice Communication",font=("times",25,"italic"),bg="black",fg="white")
head.place(x=1020,y=300)


list1 = ['English','Marathi','Hindi'];

droplist=OptionMenu(base,c, *list1)
droplist.config(height=2,width=20)
c.set('Select language') 
droplist.place(x=1140,y=350)
#Button(frame_alpr1, text='After Selecting Language... Press Button and Talk....',height=5,width=50,font=('times', 14, ' bold '),bg='brown',fg='white',command=translate_text).place(x=30,y=180)

button2 = tk.Button(base,text="... Press Button and Talk eng....",command=SPEECH,font=('Times New Roman',15,'bold'),width=20,bg='green',fg='white')
button2.place(x=900,y=500)

button2 = tk.Button(base,text="... Press Button and Tal Hindi...",command=eng_hi,font=('Times New Roman',15,'bold'),width=20,bg='green',fg='white')
button2.place(x=1250,y=500)

button2 = tk.Button(base,text="... Press Button and Tal marathi...",command=eng_mr,font=('Times New Roman',15,'bold'),width=20,bg='green',fg='white')
button2.place(x=1100,y=600)


import tkinter as tk





        

# def prediction_emotion():
#     #clear_img()
#     #update_label("Model Training Start...............")

#     start = time.time()

#     result = validate.files_count()
#     #validate.files_count()
#     end = time.time()
#     #print("---" + result)
    

#     msg = '\n' + str(result) + '\n'

#     update_label(msg)
#################################################################################################################
def window():
    root.destroy()



# button3 = tk.Button(base, text="Face Recognise",command=evaluation,width=12, height=1,font=('times', 15, ' bold '), bg="brown4", fg="white")
# button3.place(x=1300, y=450)

# button4 = tk.Button(base, text="Prediction",command=prediction_emotion, width=12, height=1, bg="brown4", fg="white",font=('times', 15, ' bold '))
# button4.place(x=1400, y=400)

base.mainloop()

