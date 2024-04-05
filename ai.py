import streamlit as st
import pyttsx3
import google.cloud.speech as speech 
import datetime  

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio) 
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number 
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like 
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	# This function is for when the assistant 
	# is called it will say hello and then 
	# take query
	speak("Hello sir I am your desktop assistant. /Tell me how may I help you")

option = st.selectbox(
    'Choose your option',
    ('How to Login?', 'How to use Data Visualisation', 'How to use Analysis', 'Day?', 'Time?', 'Exit')
)
if option == 'How to Login?':
			st.write("To Login Follow the following commands: 1. Open the data summarization tool. 2. Click on the Login Button visible on the top-right corner. 3. A login page will open. 4. Enter the username and password and click on the submit button.")
			speak("To Login Follow the following commands: 1. Open the data summarization tool. 2. Click on the Login Button visible on the top-right corner. 3. A login page will open. 4. Enter the username and password and click on the submit button.")
		
elif option == 'How to use Data Visualisation':
			st.write("To use Data Visualisation follow the following commands: 1. On the left side of the selection bar, choose data visualisation. 2. Now upload a dataset. 3. Choose the data visualisation chart from the options available.")
			speak("To use Data Visualisation follow the following commands: 1. On the left side of the selection bar, choose data visualisation. 2. Now upload a dataset. 3. Choose the data visualisation chart from the options available.")
		
elif option == 'How to use Analysis':
			st.write("To use Data Analysis follow the following commands: 1. On the left side of the selection bar, choose Analysis. 2. Now upload a dataset. 3. Choose the data analysis options from the options available.")
			speak("To use Data Analysis follow the following commands: 1. On the left side of the selection bar, choose Analysis. 2. Now upload a dataset. 3. Choose the data analysis options from the options available.")	
elif option == 'Day?':
			tellDay()
		
elif option == "Time?":
			tellTime()
				
		# this will exit and terminate the program
elif option == "Exit":
			speak("Exiting the application.")
			st.write('Exiting the application.')
			st.page_link("https://datavizsumtool.netlify.app/", label="Open New Window", icon="🏠")