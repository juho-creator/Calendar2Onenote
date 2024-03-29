[![Return to mainpage](https://img.shields.io/badge/Return_to_mainpage-blueviolet.svg)](https://github.com/juho-creator/Calendar2Onenote/blob/main/README.md)


# Calendar2Onenote

**Overview:** Calendar2Onenote is a program designed to create schedules in OneNote based on Google Calendar events.
<br><br>

## Demonstration Video (Without GUI)
[![Watch the Demonstration Video](https://img.youtube.com/vi/kQ-CY51pwEo/0.jpg)](https://www.youtube.com/watch?v=kQ-CY51pwEo)

<!-- Add demonstration content here if applicable -->
<br><br>

## Usage

### First-time Setup

1. **Download**: Get Calendar2Onenote and Credentials.json from the [Download link](https://github.com/juho-creator/OneNoteSyncScheduler/releases) and place them in the same folder.

2. **Run**: After downloading, double-click the Calendar2Onenote application to run it.

3. **Microsoft Login**: Paste the automatically copied code and log in with your Microsoft account

4. **Sync OneNote**: Authorize access to OneNote.

5. **Google Login**: Sign in to your Google account.

6. **Sync Google Calendar**: Authorize access to fetch Google Calendar events.

7. **Generate Scheduler**: Input the target year in the terminal to create a OneNote notebook with 12 monthly sections, automatically organizing events. This takes 5-10 minutes.
<br>

### Subsequent Use (When logged in)

1. **Run**: Double-click the Calendar2Onenote executable.

2. **Generate Scheduler**: Enter the target year to create a OneNote notebook with 12 monthly sections. Events will be automatically organized by date in the respective sections.
<br><br>

## Authentication and API Flow Diagrams
### Step 1. Google OAuth2.0 & Google Calendar API (G_OAuth.py)
- **Documentation**: [Google OAuth2.0 Documentation](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google Calendar API Documentation](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br>![Google OAuth2.0 Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **Process**:
  - Google OAuth2.0 authenticates Google account users without Calendar2Onenote having to need user credentials. (using **token.json**)
  - Once user authorize access to their Google Calendar events, Calendar2Onenote can fetch user calendar events using the Google Calendar API. <br><br><br><br>






### Step 2. Microsoft OAuth2.0 & Microsoft Graph API (M_OAuth.py, OneNote.py)
- **Documentation**: [Microsoft Account Authentication & Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)
<br>![Microsoft Account Authentication & Microsoft Graph API Flow Diagram](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- **Process**:
  - Microsoft OAuth2.0 authenticates Microsoft(Onenote) account users without Calendar2Onenote having to need user credentials (using **api_token_access.json**)
  - Once user authorize access to their Onenote, Calendar2Onenote is given permission to create a Onenote Notebook.
  - Calendar2Onenote is now ready to use Microsoft Graph API <br><br><br><br>
    


### Step 3. OneNote API development stack <br>
- **Documentation**: [OneNote REST API Documentation](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0) <br>
![image](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)
- After the authentication & authorization process, Calendar2Onenote creates a OneNote Notebook with google calendar events using Onenote API which is a part of Microsoft Graph API. <br>
<br><br>

## Technologies Used 
  
- **Google Calendar API**: 
  - **Documentation**: [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **Module**: `G_OAuth.py`
  - **Function**: Authenticates Google account for fetching user calendar events.
  
- **Microsoft Authentication Library (MSAL)**: 
  - **Documentation**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **Modules**: `M_OAuth.py`
  - **Function**: Authenticates Microsoft account for Onenote.


  
- **Microsoft Graph API**: 
  - **Tutorial**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **Module**: `OneNote.py`
  - **Function**: Creates a OneNote notebook with google calendar events.

<br><br>

## Reference

### Getting Started with Google APIs
- Video Tutorial: [Watch Here](https://www.youtube.com/watch?v=I5ili_1G0Vk)

### Google Calendar API
- Tutorial Series: [Watch Here](https://www.youtube.com/watch?v=1JkKtGFnua8&list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on)
- Documentation: [Read Here](https://developers.google.com/calendar/api/quickstart/python)

### Microsoft Azure
- Tutorial Series: [Watch Here](https://www.youtube.com/watch?v=BErur8WwAsg&list=PL3JVwFmb_BnQ8zwvN4OmP-fYpwJXg47Z6)

### Microsoft Graph API
- Tutorial Series: [Watch Here](https://www.youtube.com/watch?v=7ywUs54eGBo&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx)
- Try out Microsoft Graph : [Here](https://developer.microsoft.com/en-us/graph/graph-explorer)

### Onenote API Testing with Microsoft Graph Explorer
- Tutorial: [Watch Here](https://www.youtube.com/watch?v=VXd4OeQU1ek)

### Onenote API Documentation
- [Learn More](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0)

