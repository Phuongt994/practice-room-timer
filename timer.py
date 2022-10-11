from datetime import datetime 

timer_duration = 0

timer_entry_title = input("Enter title: ")
timer_entry_start = input("Enter start time in 24hr [hh:mm] format e.g. 12:20: ")
timer_entry_end = input("Enter end time in 24hr [hh.mm] format e.g. 12:50: ")

timer_entry_duration = datetime.strptime(timer_entry_end, "%H:%M") - datetime.strptime(timer_entry_start, "%H:%M") 

# timer_entry_duration = time(int(timer_entry_end[0]), int(timer_entry_end[1])) - time(int(timer_entry_start[0]), int(timer_entry_start[1])) 

print(f"This entry is for {timer_entry_title} in {timer_entry_duration} minutes")
