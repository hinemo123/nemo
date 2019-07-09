import nemo
import datetime 
import text as t
import os,random

def AImain():
	while True:	
		try:
			requiment=nemo.ask()
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
			elif "who are you" in requiment.lower():
				nemo.tts("I  am  nemo, your  assistant")
			elif 'who make you' in requiment.lower():
				nemo.tts('that  is  my  love')
			elif 'what are you' in requiment:
				nemo.tts('I  am  a  computer  program')
			elif 'open code' in requiment:
				os.startfile('C:\Program Files (x86)\Sublime Text 3\sublime_text.exe')
			elif 'search' in requiment:
				link=b.replace("open","")
				t.open_google(link)
			elif 'how old are you' in requiment:
				nemo.tts('i  dont  know, why  you ask me like  that')
			elif 'hi' in requiment or 'hello' in requiment or 'hey' in requiment:
				choise=['hi','hello sir','i am  here ,sir']
				data=str(random.choice(choise))
				nemo.tts(data)
			elif 'what is your name' in requiment:
				nemo.tts('my  name  is  nemo')
			elif "weather in" in requiment:
				data=' '.join(requiment.split()[2:])
				weather=nemo.get_weather(data)
				print(weather)
				nemo.tts(weather)
			elif 'film' in requiment:
				data=' '.join(requiment.split()[1:requiment.index('flim')])
				t.opem_flim(data)
			elif 'funny' in requiment and 'story' in requiment:
				data="""Khi tôi đi ăn trưa hôm nay, tôi nhận thấy một ông già ngồi trên ghế đá công viên khóc nức nở. Tôi dừng lại và hỏi anh ta có chuyện gì. Anh nói với tôi, 'Tôi có một người vợ 22 tuổi ở nhà. Cô ấy xoa lưng tôi mỗi sáng và sau đó thức dậy và làm cho tôi bánh kếp, xúc xích, trái cây tươi và cà phê mới xay. ' Tôi tiếp tục, 'Chà, vậy tại sao bạn khóc?' Anh nói thêm: 'Cô ấy làm cho tôi món súp tự làm cho bữa trưa và bánh quy yêu thích của tôi, dọn dẹp nhà cửa và sau đó xem TV thể thao với tôi trong phần còn lại của buổi chiều.' Tôi nói, 'Chà, tại sao bạn khóc?' Anh nói: 'Cho bữa tối, cô ấy làm cho tôi một bữa ăn ngon với rượu vang và món tráng miệng yêu thích của tôi và sau đó chúng tôi âu yếm nhau cho đến những giờ nhỏ.' Tôi hỏi, 'Vậy thì, tại sao trên thế giới bạn sẽ khóc?' Anh ấy trả lời, 'Tôi không thể nhớ nơi tôi sống.'"""
				nemo.tts_orther(data,'vi')
			elif 'can you hear me' in requiment:
				nemo.tts('altime,sir')
			elif 'can you talk' in requiment:
				nemo.tts("""yes sir,i have programmed to talk with you,but i don't clever to answer all your question""")
			elif 'how are you' in requiment:
				nemo.tts('I  am  fine  ,sir,and you? are you ok?')
			elif 'i am good' in requiment or 'okay' in requiment or 'i am okay' in requiment or 'i am fine' in requiment:
				nemo.tts('it is good to hear that')
			elif 'time' in requiment:
				time=str(datetime.datetime.now().hour)+" and "+str(datetime.datetime.now().minute)+' minute'
				nemo.tts_orther(time,'vi')
			if "goodbye" in requiment or 'bye' in requiment:
				nemo.goodbye()
				break
		except:
			print("say that again,please")
	
if __name__ == '__main__':
	nemo.Greeting()
	AImain()
