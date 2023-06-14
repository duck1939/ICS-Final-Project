# the gui for the timer, so it just looks fancier, 

import time
import tkinter as tk

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.end_time = None
        self.timer_running = False
    
    def start(self):
        self.end_time = time.time() + self.duration
        self.timer_running = True
    
    def stop(self):
        self.timer_running = False
    
    def update(self):
        if self.timer_running:
            remaining_time = self.end_time - time.time()
            if remaining_time <= 0:
                self.timer_running = False
                return "TIME'S UP!"
            minutes, seconds = divmod(int(remaining_time), 60)
            hours, minutes = divmod(minutes, 60)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return "00:00:00"

event_timer = Timer(0)
screen_timer = Timer(0)
# starting the timers
def start_event_timer():
    duration = int(event_timer_entry.get())
    event_timer.duration = duration
    event_timer.start()

def start_screen_timer():
    duration = int(screen_timer_entry.get())
    screen_timer.duration = duration
    screen_timer.start()
# stoping the timers 
def stop_event_timer():
    event_timer.stop()

def stop_screen_timer():
    screen_timer.stop()

def update_timers():
    event_timer_label['text'] = event_timer.update()
    screen_timer_label['text'] = screen_timer.update()
    root.after(1000, update_timers)

root = tk.Tk()
root.title("Timer Pro v2 App")

event_timer_label = tk.Label(root, text="00:00:00", font=("Arial", 24), pady=10)
event_timer_label.pack()

event_timer_entry = tk.Entry(root)
event_timer_entry.pack()

event_timer_button = tk.Button(root, text="Start Event Timer", command=start_event_timer)
event_timer_button.pack()

event_timer_stop_button = tk.Button(root, text="Stop Event Timer", command=stop_event_timer)
event_timer_stop_button.pack()

screen_timer_label = tk.Label(root, text="00:00:00", font=("Arial", 24), pady=10)
screen_timer_label.pack()

screen_timer_entry = tk.Entry(root)
screen_timer_entry.pack()

screen_timer_button = tk.Button(root, text="Start Screen Timer", command=start_screen_timer)
screen_timer_button.pack()

screen_timer_stop_button = tk.Button(root, text="Stop Screen Timer", command=stop_screen_timer)
screen_timer_stop_button.pack()

update_timers()

root.mainloop()
