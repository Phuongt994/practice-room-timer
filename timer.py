timer_duration = 0

timer_entry_title = input("Enter title: ")
timer_entry_start = float(input("Enter start time in 24hr [hh.mm] format e.g. 12.20: "))
timer_entry_end = float(input("Enter end time in 24hr [hh.mm] format e.g. 12.50: "))

timer_entry_duration = int((timer_entry_end - timer_entry_start) * 100)

print(f"This entry is for {timer_entry_title} in {timer_entry_duration} minutes")
