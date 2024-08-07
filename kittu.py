import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import operator
import urllib.parse


def takeCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			
			print("sir you said.", Query)

		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(audio)
	engine.runAndWait()

def tellDay():
	
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir.")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir.")

    else:
        speak("Good Evening sir.")

    speak("i am, kittu, how can i help you")
    Take_query()

def tellTime():
	
	time = str(datetime.datetime.now())
	
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is sir" + hour + "Hours and" + min + "Minutes")	

def Take_query():
	
	while(True):
		
		query = takeCommand().lower()

		if "open youtube" in query:
			speak("sir what should i search in youtube")
			query = takeCommand().lower()
			query_url = urllib.parse.quote(query)
			search_url = "https://www.youtube.com/results?search_query=" + query_url
			webbrowser.open(search_url)
			continue
		
		elif "open google" in query:
			speak("sir what should i search in google")
			cm=takeCommand().lower()
			webbrowser.open(f"{cm}")
			continue
		
		elif "twitter" in query:
			speak("opening twitter")
			webbrowser.open("www.twitter.com")
			continue


		elif 'search' in query:
    			query = query.replace("search", "")
    			query_url = urllib.parse.quote(query)
    			search_url = "https://www.youtube.com/results?search_query=" + query_url
    			webbrowser.open(search_url)

		elif "gmail" in query:
			speak("opening gmail")
			webbrowser.open("https://mail.google.com/mail")
			continue

		elif "open facebook" in query:
			speak("opening facebook")
			webbrowser.open("www.facebook.com")
			continue

		elif "instagram" in query:
			speak("opening instagram")
			webbrowser.open("www.instagram.com")
			continue

		elif "notepad" in query:
			speak("opening notpad")
			np="C:\\Windows\\System32\\notepad.exe"
			os.startfile(np)
			continue

		elif "open cmd" in query:
			speak("opening Command Prompt")
			np="C:\\Windows\\System32\\cmd.exe"
			os.startfile(np)
			continue

		elif "close" and "cmd" in query:				
				os.system("taskkill /im WindowsTerminal.exe")
				speak("closing Command Prompt")
				continue

		elif "open photoshop" in query:
			speak("opening photoshop")
			ps="C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
			os.startfile(ps)
			continue

		elif "close" and "photoshop" in query:
			os.system("taskkill /im Photoshop.exe")
			speak("closing photoshop")
			continue

		elif "close" and "browser" in query:				
				os.system("taskkill /im chrome.exe")
				speak("closing google chrome")
				continue

		elif "close" and "chrome" in query:				
				os.system("taskkill /im chrome.exe")
				speak("closing google chrome")
				continue

		elif "results" in query:
			webbrowser.open("https://www.pdilipvenkatesh.in/try/")
			speak("opening GEC Results")
			continue

		elif "day" in query:
			tellDay()
			continue
		
		elif "time" in query:
			tellTime()
			continue

		elif "calculate" in query:

				def get_operator_fn(op):
					return {
						'+': operator.add,
						'-': operator.sub,
						'x': operator.mul,
						'/': operator.truediv,
					}[op]

				def eval_binary_expr(op1, oper, op2):
					op1, op2 = int(op1), int(op2)
					return get_operator_fn(oper)(op1, op2)

				if "calculate" in query:
					r = sr.Recognizer()
					with sr.Microphone() as source:
						speak("ready")
						print("Listening...")
						r.adjust_for_ambient_noise(source)
						audio = r.listen(source)
					my_string = r.recognize_google(audio)
					print(my_string)
					speak("your result is" )
					speak(eval_binary_expr(*(my_string.split())))
					print("your result is", eval_binary_expr(*(my_string.split())))



		elif "shutdown" in query:
    			os.system("shutdown /s /t 5")

		elif "restart" in query:
    			os.system("shutdown /r /t 5")
		
		elif "lock" in query:
    			os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



		
		elif "bye" in query:
			speak("Bye sir. ")
			exit()
		
		elif 'song' in query:
				music_dir = 'D:\\songs'
				songs = os.listdir(music_dir)
				n=random.randint(0,len(songs))
				print("playing...",songs[n])
				os.startfile(os.path.join(music_dir, songs[n]))

		elif 'music' in query:
				music_dir = 'D:\\songs'
				songs = os.listdir(music_dir)
				n=random.randint(0,len(songs))
				print("playing...",songs[n])
				os.startfile(os.path.join(music_dir, songs[n]))
		
		elif "wikipedia" in query:
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "what" in query:	
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "who" in query:	
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			print(result)
			speak(result)
			continue

		elif "email" in query:
			# create message object instance
			msg = MIMEMultipart()

			speak("tell me the message")
							
			message =takeCommand()
			
			# setup the parameters of the message
			
			password = "pssword"
			msg['From'] = "bhargavgandhi71@gmail.com"
			msg['To'] = "bhargavgandhi79@gmail.com"
			speak("tell me the subject")
			msg['Subject'] = takeCommand()
			
			# add in the message body
			msg.attach(MIMEText(message, 'plain'))
			
			#create server
			server = smtplib.SMTP('smtp.gmail.com: 587')
			
			server.starttls()
			
			# Login Credentials for sending the mail
			server.login(msg['From'], password)
			
			
			# send the message via the server.
			server.sendmail(msg['From'], msg['To'], msg.as_string())
			
			server.quit()
			
			print("successfully sent email to %s:" % (msg['To']))
				
		elif "tell me your name" in query:
			speak("I am, kittu. Your deskstop Assistant")


		elif "how are you" in query:
    			speak("i am fine sir. what about you")

if __name__ == '__main__':

    wishMe()
	
exit()
