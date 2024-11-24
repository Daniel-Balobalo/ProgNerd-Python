import os
import datetime
import time
import keyboard

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_instructions(is_twelve_hour):
    clear()
    print()
    if is_twelve_hour:
        print("Press 'T' to switch to 24-hour format.\n")
    else:
        print("Press 'T' to switch to 12-hour format.\n")

def twelve_hour_format():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%I:%M:%S %p")  # Format: hours:minutes:seconds AM/PM (12-hour format)
        print("\r" + formatted_time, end="", flush=True)  # Print without newline
        time.sleep(1)

def twentyfour_hour_format():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")  # Format: hours:minutes:seconds (24-hour format)
        print("\r" + formatted_time, end="", flush=True)  # Print without newline
        time.sleep(1)

def on_key_event(event):
    global is_twelve_hour
    if event.name == 't' and event.event_type == keyboard.KEY_DOWN:
        is_twelve_hour = not is_twelve_hour

def main():
    global is_twelve_hour
    is_twelve_hour = True

    keyboard.on_press_key('t', on_key_event)

    while True:
        display_instructions(is_twelve_hour)
        
        if is_twelve_hour:
            twelve_hour_format()
        else:
            twentyfour_hour_format()

if __name__ == "__main__":
    main()