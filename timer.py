from datetime import datetime 
import csv
import mysql.connector
from mysql.connector import errorcode

timer_duration = 0

timer_entry_title = input("Enter title: ")
timer_entry_start = input("Enter start time in 24hr [hh:mm] format e.g. 12:20: ")
timer_entry_end = input("Enter end time in 24hr [hh.mm] format e.g. 12:50: ")

timer_entry_duration = datetime.strptime(timer_entry_end, "%H:%M") - datetime.strptime(timer_entry_start, "%H:%M") 

# timer_entry_duration = time(int(timer_entry_end[0]), int(timer_entry_end[1])) - time(int(timer_entry_start[0]), int(timer_entry_start[1])) 

print(f"This entry is for {timer_entry_title} in {timer_entry_duration} minutes")

# Write entries to a .csv file
with open('timer-entries.csv', 'a') as entries:
    entries_writer = csv.writer(entries, delimiter=",")
    entries_writer.writerow([timer_entry_title, timer_entry_start, timer_entry_end, timer_entry_duration])

# Write entries to mySQL
try:
    db_connect = mysql.connector.connect(user="root", password="karakara13", host="0.0.0.0", database="timer")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Your credentials were rejected.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DB not exist.")
    else:
        print(err)
else:
    db_connect.close()

