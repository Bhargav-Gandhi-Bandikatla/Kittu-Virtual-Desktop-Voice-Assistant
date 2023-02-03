import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#import pyjokes
import random


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
			speak("opening youtube")
			webbrowser.open("www.youtube.com")
			continue

		if "joke" in query:
			My_joke = pyjokes.get_joke(language="en", category="neutral")
			print(My_joke)
			speak(My_joke)
			continue
		
		elif "google" in query:
			speak("sir what should i search in google")
			cm=takeCommand().lower()
			webbrowser.open(f"{cm}")
			continue
		
		elif "twitter" in query:
			speak("opening twitter")
			webbrowser.open("www.twitter.com")
			continue
		
		elif "gmail" in query:
			speak("opening gmail")
			webbrowser.open("https://mail.google.com/mail")
			continue

		elif "facebook" in query:
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

		elif "cmd" in query:
			speak("opening Command Prompt")
			np="C:\\Windows\\System32\\cmd.exe"
			os.startfile(np)
			continue

		elif "photoshop" in query:
			speak("opening photoshop")
			ps="C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe"
			os.startfile(ps)
			continue

		elif "day" in query:
			tellDay()
			continue
		
		elif "time" in query:
			tellTime()
			continue
		
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
		
		elif "wikipedia" or "about" in query:
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
			
			password = "idzjdiuvdnnqhugi"
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