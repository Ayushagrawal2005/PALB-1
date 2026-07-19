import win32com.client as wincl

# Dispatch the Windows SAPI Speech Voice
speaker = wincl.Dispatch("SAPI.SpVoice")

names =["Rahul","Aayush","Rohit","Saurabh","Ankit"]
for name in names:
    speaker.speak(f"Shoutouts to {name} ") 
# speaker.Speak("Hello world! This requires zero third-party audio player engines.")
