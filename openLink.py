from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote

executable_path=r"C:\Users\ASUS\Documents\python\tacke\chromedriver_1.exe"
browser = webdriver.Chrome(executable_path=executable_path)
def open_facebook():
	url="https://www.facebook.com/"
	browser.get(url)
	element=browser.find_element_by_id("email")
	element.send_keys("")
	element=browser.find_element_by_id("pass")
	element.send_keys("")
	element.send_keys(Keys.RETURN)

def open_gmail():
	url="https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
	browser.get(url)
	element=browser.find_element_by_id("identifierId")
	element.send_keys("")
	element.send_keys(Keys.ENTER)
	#tim tag name=password trong truong input
	element=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
	element.send_keys("")
	element.send_keys(Keys.RETURN)

def open_github():
	url="https://github.com"
	browser.get(url)

def open_wiki():
	url="https://vi.wikipedia.org"
	browser.get(url)

def open_youtube():
	url="https://www.youtube.com"
	browser.get(url)

def open_video_on_youtube(video_name):
	url="https://www.youtube.com/results?search_query="+quote(video_name)
	browser.get(url)
def open_google(text):
	url="https://www.google.com/search?q="+quote(text)
	browser.get(url)