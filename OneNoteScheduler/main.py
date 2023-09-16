from OneNote import *
from G_OAuth import * 
import inflect
import calendar
from G_OAuth import retrieve_schedule
import webbrowser
import os
from flask import Flask, request, render_template

# Setting up date tracker
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09','10', '11', '12']
p = inflect.engine()


creds = get_credentials()


# Webpage for user input
app = Flask(__name__)
webbrowser.open("http://127.0.0.1:5000")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            year = request.form['year']

            # Retrieve all events
            events = retrieve_schedule(int(year))
            pprint(events)

            
            # 1. Create Notebook
            notebook_id = CreateNoteBook(str(year))


            # 2. Create sections for month
            for month in months:
                month_name = calendar.month_name[int(month)]
                section_id = CreateSection(month_name, notebook_id)
                
                # Caculate number of days in a month
                days = calendar.monthrange(int(year), int(month))[1]
                
                # Create page with events
                for day in range(1,days+1):
                    ordinal = p.ordinal(day)
                    if day>9:  
                        date = f'{year}-{month}-{day}' # Create date format for checking
                    else:
                        date = f'{year}-{month}-0{day}' # Create date format for checking
                    page_id = CreatePage(ordinal,events,date,section_id)
                    pprint(page_id)
        except KeyError:
            return "Notebook Already exists"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
