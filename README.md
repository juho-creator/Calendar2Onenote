# OneNote Scheduler

**Overview:** OneNote Scheduler is a program designed to create schedules in OneNote based on Google Calendar events.
<br><br>

## Demonstration
[Demonstration video](https://www.youtube.com/watch?v=kQ-CY51pwEo)
<!-- Add demonstration content here if applicable -->
<br>

## Usage

### First-time Setup

1. **Download**: Get OneNoteScheduler and Credentials.json from the [Download link](https://github.com/juho-creator/OneNoteSyncScheduler/releases) and place them in the same folder.

2. **Run**: After downloading, double-click the OneNoteScheduler application to run it.

3. **Microsoft Login**: Paste the automatically copied code and log in with your Microsoft account

4. **Sync OneNote**: Authorize access to OneNote.

5. **Google Login**: Sign in to your Google account.

6. **Sync Google Calendar**: Authorize access to fetch Google Calendar events.

7. **Generate Scheduler**: Input the target year in the terminal to create a OneNote notebook with 12 monthly sections, automatically organizing events. This takes 5-10 minutes.
<br>

### Subsequent Use (When logged in)

1. **Run**: Double-click the OneNoteScheduler executable.

2. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.
<br>

## Authentication and API Flow Diagrams

### Microsoft OAuth2.0 & Microsoft Graph API (M_OAuth.py, OneNote.py)
- **Documentation**: [Microsoft Account Authentication & Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)
<br>![Microsoft Account Authentication & Microsoft Graph API Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- **Process**:
  - Microsoft OAuth2.0 authenticates Microsoft(Onenote) users without OneNoteScheduler having to need user credentials (using **api_token_access.json** created)
  - Once user authorize access to their Onenote, OneNoteScheduler(3rd-party app) is able to create Onenote Notebook. <br>
    

### Google OAuth2.0 & Google Calendar API (G_OAuth.py)
- **Documentation**: [Google OAuth2.0 Documentation](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google Calendar API Documentation](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br>![Google OAuth2.0 Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **Process**:
  - Google OAuth2.0 authenticates Google account users without OneNoteScheduler having to need user credentials. (using **token.json** created)
  - Once user authorize access to their Google Calendar events, OneNoteScheduler(3rd-party app) can fetch user calendar events using the Google Calendar API. <br>


### OneNote API development stack <br>
- **Documentation**: [OneNote REST API Documentation](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0) <br>
![image](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)
- After the authentication & authorization process, OneNoteScheduler is ready to create onenote page with all the google calendar events usin microsoft graph api that includes onenote api. <br>



## Technologies Used 
- **Google Calendar API**: 
  - **Documentation**: [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **Module**: `G_OAuth.py`
  - **Function**: Authenticates Google account and fetches calendar events.
  
- **Microsoft Authentication Library (MSAL)**: 
  - **Documentation**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **Modules**: `M_OAuth.py`
  - **Function**: Authenticates Microsoft account.
  
- **Microsoft Graph API**: 
  - **Tutorial**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **Module**: `OneNote.py`
  - **Function**: Creates a OneNote notebook with calendar events.


## Reference
**Google Console Cloud** :
**Google Calendar API** : 
**Microsoft Azure** : 
**Microsoft Graph API** : 
**Onenote API** :
