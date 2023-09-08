# OneNote Scheduler

This program creates a OneNote scheduler with Google Calendar events.

## Demonstration of OneNote Scheduler

<!-- Add demonstration content here if applicable -->

## How to Use the Program

### First-time Setup

1. **Download**: Obtain OneNoteScheduler from the [Download link].

2. **Run**: After installation, double-click the OneNoteScheduler application.

3. **Google Login**: Sign in with your Google account.

4. **Sync Google Calendar**: Authorize access to fetch Google Calendar events.

5. **Microsoft Login**: Log in using your Microsoft account.

6. **Sync OneNote**: Authorize access to OneNote.

7. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.

### Subsequent Use (When logged in)

1. **Run**: Double-click the OneNoteScheduler executable.

2. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.



## Authentication and API Flow Diagrams

### Google OAuth2.0 (G_OAuth.py)
[Google OAuth2.0 Documentation](https://developers.google.com/workspace/guides/auth-overview?hl=ko)

![Google OAuth2.0 Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- Google OAuth2.0 authenticates Google account users without the need for their credentials.
- It also authorizes OneNoteScheduler, a 3rd-party app, to access Google Calendar information using the Google Calendar API.

### Microsoft OAuth2.0 & Microsoft Graph API (M_OAuth.py,OneNote.py)
[Microsoft Account Authentication & Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)

![Microsoft Account Authentication & Microsoft Graph API Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- MSAL utilizes OAuth 2.0 for authenticating Microsoft account users, eliminating the need for their credentials.
- Additionally, it grants authorization to OneNoteScheduler, a 3rd-party app, allowing it to write Google Calendar events to OneNote using the Microsoft Graph API.




## Technologies Used 

- [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=ko): 
  - `G_OAuth.py` - Authenticates Google accounts and fetches calendar events.
  
- [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python): 
  - `M_OAuth.py` - Authenticates Microsoft accounts.
  
- [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2): 
  - `OneNote.py` - Creates a OneNote notebook with calendar events.
