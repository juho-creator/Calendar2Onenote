import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_credentials():
    creds = None

    # Specify the path to the credentials.json file relative to the current working directory
    credentials_path = os.path.join(os.getcwd(), 'OneNoteSyncScheduler', 'OneNoteScheduler', 'credentials.json')

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds



def retrieve_schedule(year):
    """Shows usage of the Google Calendar API to fetch events within a specified year."""
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    try:
        # Construct start and end dates for the specified year
        start_date = f"{year}-01-01"
        end_date = f"{year+1}-01-01"

        start_datetime = datetime.datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
        end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d').isoformat() + 'Z'

        print(f'Fetching events for the year {year}')
        events = {}
        page_token = None

        while True:
            events_result = service.events().list(calendarId='primary', timeMin=start_datetime,
                                                  timeMax=end_datetime, singleEvents=True,
                                                  orderBy='startTime', pageToken=page_token, maxResults=250).execute()
            current_page_events = events_result.get('items', [])

            if not current_page_events:
                break

            for event in current_page_events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                event_summary = event.get('summary', 'No summary available')

                if start not in events:
                    events[start] = []

                events[start].append(event_summary)

            page_token = events_result.get('nextPageToken')

            if not page_token:
                break

        if not events:
            print(f'No events found for the year {year}.')
            return {}

        return events

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    # Example usage:
    year = 2023
    events = retrieve_schedule(year)
    pprint(events)
