import time

x = "TIMER PRO v2".center(64)
y = "".center(64)
hour_time_screen = 0
minute_time_screen = 0
second_time_screen = 0

hour_time_event = 0
minute_time_event = 0
second_time_event = 0
# killswitch
choice_exit = input("Exit Program[y or n]?: ")

while choice_exit != "y":
    print("------------------------------------------------------------------")
    print(f"|{x}|")
    print(f"|{y}|")
    print("|1. Create a timer for an event                                  |")
    print("|2. Set a limit on screen time                                   |")
    print(f"|{y}|")
    print("------------------------------------------------------------------")
    choice = int(input("What do you need assistance in[1-2]?: "))

    if choice == 1:
        countdown_1 = int(input("How many seconds until event?: "))
        start_time = time.time()
        end_time = start_time + countdown_1


        # creating the actual timer for the event
        while time.time() < end_time:
            remaining_time = end_time - time.time()
            # gets the formating part, so if minutes or seconds exceed 60 they add one minute or hour corresponding to which one is over 60
            minutes, seconds = divmod(int(remaining_time), 60)
            hours, minutes = divmod(minutes, 60)
            print(f"Remaining time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        print("\nTIME TO GO!")
        choice = int(input("What do you need assistance in[1-5]?: "))

    elif choice == 2:
        countdown_2 = int(input("How many seconds?: "))
        start_time = time.time()
        end_time = start_time + countdown_2

        # creating the actual timer for screen time limit.
        while time.time() < end_time:
            remaining_time = end_time - time.time()
            # gets the formating part, so if minutes or seconds exceed 60 they add one minute or hour corresponding to which one is over 60
            minutes, seconds = divmod(int(remaining_time), 60)
            hours, minutes = divmod(minutes, 60)
            print(f"Remaining time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
            time.sleep(1)

        print("\nTIME TO STOP!")\
    # exit condition
    choice_exit = input("Exit Program[y or n]?: ")
    if choice_exit == "y":
        break
