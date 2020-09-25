#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3


# In[ ]:


dir(pyttsx3)


# In[ ]:


engine = pyttsx3.init()
engine.say("welcome to linux world")
engine.runAndWait()


# In[ ]:





# In[ ]:


import speech_recognition  as sr


# In[ ]:


mic =  sr.Microphone()


# In[ ]:


rec = sr.Recognizer()


# In[ ]:


with mic as source:
    print("say :")
    audio = rec.listen(source)
    text = rec.recognize_google(audio)
    print(text)


# In[ ]:


import socket


# In[ ]:


s = socket.socket()


# In[ ]:


s.connect( ("192.168.100.122" , 1234) )


# In[ ]:


engine = pyttsx3.init()
engine.say("enter your command")
engine.runAndWait()


# In[ ]:


with mic as source:
    print("say :")
    audio = rec.listen(source)
    text = rec.recognize_google(audio)
    print(text)

if "date" and "run" in text  or "date" and "execute" in text:
    cmd = "date"
    cmd = cmd.encode()
    s.send(cmd)
    print(s.recv(100).decode())


# In[ ]:


cmd


# In[ ]:





# In[ ]:




