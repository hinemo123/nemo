from gtts import gTTS 
import pyglet
import time,os
import speech_recognition as sr 
from selenium import webdriver
import webbrowser
from urllib.parse import quote


def tts(text,lang="en"):
	file=gTTS(text=text,lang=lang)
	fileName='temp.mp3'
	file.save(fileName)
	music=pyglet.media.load(fileName,streaming=False)
	music.play()
	time.sleep(music.duration)
	os.remove(fileName)

def Greeting():
	text="""hello sir,
	welcome back
	do you need some help"""
	tts(text)
	"""a=text.split(",")
	for i in a:
		tts(i)"""

def ask():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
	try:
		text=r.recognize_google(audio)
		print("you mean:"+text)
		tts(text)
		return text
	except Exception as e:
		print(e)

