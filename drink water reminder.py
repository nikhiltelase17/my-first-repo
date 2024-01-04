import time
from plyer import notification
import win32com.client

engine = win32com.client.Dispatch("SAPI.SpVoice")
# Set reminder interval in minutes
print("---------drink water reminder---------\n".upper().center(50))
try:
    interval = int(input("Enter reminder interval in minutes (e.g., 60 for hourly).\n>>> ".title()))
    print(f"Ok, i remind you to after {interval} minutes".title())
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="hey Nikhil, it's time to drink water ",
            app_name="Water Reminder",
            timeout=10  # Optional: Set notification timeout in seconds
        )
        engine.Speak("hey Nikhil, It's time to drink water")
        time.sleep(interval)

except ValueError:
    print("Invalid interval")
