from Google import Create_Service
from pprint import pprint

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events.readonly',
    'https://www.googleapis.com/auth/calendar.events'
]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def get_events(calendar_id):
    events = service.events().list(calendarId=calendar_id).execute()['items']
    entire_schedule = {}
    
    for event in events:
        start_time = event['start'].get('dateTime', event['start'].get('date'))[:10]
        
        if start_time not in entire_schedule:
            entire_schedule[start_time] = []
            
        entire_schedule[start_time].append(event['summary'])
    
    return entire_schedule

events = get_events("primary")

sorted_dates = sorted(events.keys())
for date in sorted_dates:
    print(f"Date: {date}")
    for event in events[date]:
        print(f"- {event}")
    print()

def check_recurrence(schedule):
    try:
        recurrence_rule = schedule['recurrence'][0][10:]
        
        if "MONTHLY" in recurrence_rule:
            return "MONTHLY"
        elif "YEARLY" in recurrence_rule:
            return "YEARLY" 
        elif "DAILY" in recurrence_rule:
            return "DAILY"
            
    except KeyError:
        pass
