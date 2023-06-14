# the gui for the timer, so it just looks fancier, 

import time
import tkinter as tk

def start_timer(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes, seconds = divmod(int(remaining_time), 60)
        hours, minutes = divmod(minutes, 60)
        timer_label['text'] = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        root.update()
        time.sleep(1)
    timer_label['text'] = "TIME'S UP!"

def start_event_timer():
    duration = int(event_timer_entry.get())
    start_timer(duration)

def start_screen_timer():
    duration = int(screen_timer_entry.get())
    start_timer(duration)

root = tk.Tk()
root.title("Timer App")

event_timer_label = tk.Label(root, text="Event Timer (seconds):")
event_timer_label.pack()
event_timer_entry = tk.Entry(root)
event_timer_entry.pack()

event_timer_button = tk.Button(root, text="Start Event Timer", command=start_event_timer)
event_timer_button.pack()

screen_timer_label = tk.Label(root, text="Screen Timer (seconds):")
screen_timer_label.pack()
screen_timer_entry = tk.Entry(root)
screen_timer_entry.pack()

screen_timer_button = tk.Button(root, text="Start Screen Timer", command=start_screen_timer)
screen_timer_button.pack()

timer_label = tk.Label(root, text="00:00:00", font=("Arial", 24), pady=10)
timer_label.pack()

root.mainloop()
