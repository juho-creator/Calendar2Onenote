# DISCLAIMER 
# !! FOllOWING PROGRAM (v1.0, v2.0) IS OLD VERSION, WITH UPDATED PROGRAM WITHOUT KEYBOARD AUTOMATION UNDER DEVELOPMENT !!

# OneNote Scheduler

**Overview:** OneNote Scheduler is a program designed to create schedules in OneNote based on Google Calendar events.

## Demonstration

<!-- Add demonstration content here if applicable -->

## Usage

### First-time Setup

1. **Download**: Obtain OneNoteScheduler from the [Download link].

2. **Installation**: After downloading, double-click the OneNoteScheduler application to install it.

3. **Google Login**: Sign in to your Google account.

4. **Sync Google Calendar**: Authorize access to fetch Google Calendar events.

5. **Microsoft Login**: Log in using your Microsoft account.

6. **Sync OneNote**: Authorize access to OneNote.

7. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.

### Subsequent Use (When logged in)

1. **Run**: Double-click the OneNoteScheduler executable.

2. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.

## Authentication and API Flow Diagrams

### Google OAuth2.0 & Google Calendar API (G_OAuth.py)
- **Documentation**: [Google OAuth2.0 Documentation](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google Calendar API Documentation](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br> ![Google OAuth2.0 Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **Process**:
  - Google OAuth2.0 authenticates Google account users without the need for their credentials.
  - It also authorizes OneNoteScheduler, a 3rd-party app, to access Google Calendar information using the Google Calendar API. <br>

### Microsoft OAuth2.0 & Microsoft Graph API (M_OAuth.py, OneNote.py)
- **Documentation**: [Microsoft Account Authentication & Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)

<br> ![Microsoft Account Authentication & Microsoft Graph API Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

### OneNote API development stack <br> ![image](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)



- **Process**:
  - MSAL utilizes OAuth 2.0 for authenticating Microsoft account users, eliminating the need for their credentials.
  - Additionally, it grants authorization to OneNoteScheduler, a 3rd-party app, allowing it to write Google Calendar events to OneNote using the Microsoft Graph API.

## Technologies Used 

- **Google Calendar API**: 
  - **Documentation**: [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **Module**: `G_OAuth.py`
  - **Function**: Authenticates Google accounts and fetches calendar events.
  
- **Microsoft Authentication Library (MSAL)**: 
  - **Documentation**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **Modules**: `M_OAuth.py`
  - **Function**: Authenticates Microsoft accounts.
  
- **Microsoft Graph API**: 
  - **Documentation**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **Module**: `OneNote.py`
  - **Function**: Creates a OneNote notebook with calendar events.
 
