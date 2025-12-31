# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
