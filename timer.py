from datetime import datetime, date
import csv
import mysql.connector
from mysql.connector import errorcode

timer_duration = 0

def main():
    request= input("Welcome. Press 0 for entry OR 1 for report!\n")
    if request == "0":
        create_timer_entry()
    elif request == "1":
        create_daily_report()
    else:
        print("Something gone wrong. Please restart.")

# Create an entry
def create_timer_entry():
    timer_entry_date = date.today()
    timer_entry_title = input("Enter title: ")
    timer_entry_start = input("Enter start time in 24hr [hh:mm] format e.g. 12:20: ")
    timer_entry_end = input("Enter end time in 24hr [hh.mm] format e.g. 12:50: ")

    timer_entry_duration = datetime.strptime(timer_entry_end, "%H:%M") - datetime.strptime(timer_entry_start, "%H:%M")

    print(f"This entry today {timer_entry_date} is about {timer_entry_title} in {timer_entry_duration} minutes")
    save_timer_entry(timer_entry_date, timer_entry_title, timer_entry_start, timer_entry_end, timer_entry_duration)    

# Write an entry into csv & db table
def save_timer_entry(entry_date, entry_title, entry_start, entry_end, entry_duration):
    with open('timer-entries.csv', 'a', newline='') as entries:
        entries_writer = csv.writer(entries, delimiter=",")
        entries_writer.writerow([entry_date, entry_title, entry_start, entry_end, entry_duration])

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

def create_daily_report():
    report_date = str(date.today())
    report_entries = []
    with open('timer-entries.csv', 'r') as entries:
        entries_reader = csv.reader(entries, delimiter=',')
        for row in entries_reader:
            if row[0] == report_date:
                report_entries.append(row)
            else:
                continue
    
    print(f"Your daily report for {report_date}")
    print(report_entries)


main()

