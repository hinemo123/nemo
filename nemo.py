from gtts import gTTS 
import pyglet
import pyttsx3
import time,os
import speech_recognition as sr 
from selenium import webdriver
import webbrowser
from urllib.parse import quote
import datetime,requests

engien=pyttsx3.init('sapi5')
voices=engien.getProperty('voices')
engien.setProperty('voice',voices[0].id)
engien.setProperty('rate',150)
def tts(text):
	engien.say(text)
	engien.runAndWait()

def Greeting():
	hour=int(datetime.datetime.now().hour)
	session=''
	if hour<11 and hour>=0:
		session="Moring"
	elif hour>=12 and hour<=18:
		session='Afternoon'
	else:
		session='Evening'
	text="""good %s sir,
	welcome back
	do you need some help""" %session
	tts(text)
	"""a=text.split(",")
	for i in a:
		tts(i)"""

def ask():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print('listening...')
		r.pause_threshold=1
		audio=r.listen(source)
	try:
		print('Recognizing...')
		text=r.recognize_google(audio)
		print("you mean:"+text)
		return text
	except Exception as e:
		#print(e)
		print('i cant hear you')
def goodbye():
	text="""goodbye sir,
	have a nice day,
	I hope you enjoy me!!"""
	tts(text)
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	return format_response(weather)
def tts_orther(text,lang):
	file=gTTS(text=text,lang=lang)
	fileName='temp.mp3'
	file.save(fileName)
	music=pyglet.media.load(fileName,streaming=False)
	music.play()
	time.sleep(music.duration)
	os.remove(fileName)
