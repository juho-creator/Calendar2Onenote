from OneNote import *
from G_OAuth import * 
import inflect
import calendar
from G_OAuth import retrieve_schedule
import webbrowser
from flask import Flask, request, render_template

# Setting up date tracker
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09','10', '11', '12']
p = inflect.engine()


# Authenticate Microsoft Account (for onenote)
creds = get_credentials()


# Open Webpage for user input
app = Flask(__name__, template_folder='../templates')
webbrowser.open("http://127.0.0.1:5000")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get Year Input from user
            year = request.form['year']

            # Retrieve all events for Year Input
            events = retrieve_schedule(int(year))

            # 1. Create Notebook
            notebook_id = CreateNoteBook(year)

            # 2. Create sections for month
            for month in months:
                # Creating {month}...

                # Get month name 
                month_name = calendar.month_name[int(month)]

                # Get Section
                section_id = CreateSection(month_name, notebook_id)

                # Caculate number of days in a month
                days = calendar.monthrange(year, int(month))[1]
                
                # Create page with events
                for day in range(1,days+1):

                    # Get day format
                    ordinal = p.ordinal(day)

                    # Create date format for checking
                    if day>9:  
                        date = f'{year}-{month}-{day}' 
                    else:
                        date = f'{year}-{month}-0{day}'
                    
                    # Create page 
                    page_log = CreatePage(ordinal,events,date,section_id)
                    pprint(page_log)

            # Created {month} : {section_id}
            
        except KeyError:
            return "Notebook Already exists"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
