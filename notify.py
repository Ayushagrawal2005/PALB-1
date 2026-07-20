import time
import threading
import pyttsx3
from plyer import notification

# Configuration
INTERVAL_SECONDS = 5  # Set your desired interval here (e.g., 600 for 10 minutes)
TITLE = "Reminder Alert"
MESSAGE = "This is your recurring notification."

def speak_text(text):
    # Running the speech engine in an isolated function prevents looping freezes
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def trigger_notification():
    while True:
        # 1. Show the desktop popup
        notification.notify(
            title=TITLE,
            message=MESSAGE,
            app_name='Python Notifier',
            timeout=5
        )
        
        # 2. Speak the message in a background thread so it doesn't block the timer
        voice_thread = threading.Thread(target=speak_text, args=(MESSAGE,))
        voice_thread.start()
        
        # 3. Wait for the next interval
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    print(f"Notification loop started. Running every {INTERVAL_SECONDS} seconds...")
    print("Press Ctrl+C in the terminal to stop.")
    
    # Start the loop
    trigger_notification()
