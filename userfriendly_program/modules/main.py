from modules.OneNote import *
from modules.G_OAuth import * 
import inflect
import calendar
from modules.G_OAuth import retrieve_schedule
import tkinter as tk
import time
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))
    
# Setting up date tracker
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09','10', '11', '12']
p = inflect.engine()


def create_schedule(year, next_window, headers, access_token):
    try:
        # Retrieve all events
        all_events = retrieve_schedule(int(year))

        # 1. Create Notebook
        notebook_url,notebook_id = CreateNoteBook(str(year), headers)

        # 2. Create sections for month
        for month in months:
            month_name = calendar.month_name[int(month)]
            # Display
            label = tk.Label(next_window, text=f"Creating {month_name}...")
            label.pack()
            next_window.update()
            section_id = CreateSection(month_name, notebook_id, headers)

            # Caculate number of days in a month
            days = calendar.monthrange(int(year), int(month))[1]
            
            # Create page with events
            for day in range(1,days+1):
                ordinal = p.ordinal(day)
                if day>9:  
                    date = f'{year}-{month}-{day}' # Create date format for checking
                else:
                    date = f'{year}-{month}-0{day}' # Create date format for checking
                
                # Find matching events
                try:
                    events = all_events[date]
                except:
                    events = ""
                page = CreatePage(ordinal,events,section_id, headers, access_token)


        label = tk.Label(next_window, text="Notebook has been successfully created!")
        label.pack()
        next_window.update()

        lbl = tk.Label(next_window, text=notebook_url, fg="blue", cursor="hand2")
        lbl.pack()
        lbl.bind("<Button-1>", callback)

    except Exception as e:
        lbl = tk.Label(next_window, text=e, fg="blue", cursor="hand2")
        lbl.pack()
        next_window.update()

