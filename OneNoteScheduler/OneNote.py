from office365.graph_client import GraphClient
from M_OAuth import generate_access_token

APP_ID = "98c8b6c2-6df4-4765-ac02-4c32cf868661"
SCOPES = [
    "Notes.Create",
    "Notes.Read",
    "Notes.Read.All",
    "Notes.ReadWrite",
    "Notes.ReadWrite.All",
    "Notes.ReadWrite.CreatedByApp"
]




from pprint import pprint
import os
import base64
import requests
from M_OAuth import generate_access_token

# SCOPES = ["User.Read","Notes.Read.All"]


def draft_attachment(file_path):
    if not os.path.exists(file_path):
        print('file is not found')
        return
    
    with open(file_path, 'rb') as upload:
        media_content = base64.b64encode(upload.read())
        
    data_body = {
        '@odata.type': '#microsoft.graph.fileAttachment',
        'contentBytes': media_content.decode('utf-8'),
        'name': os.path.basename(file_path)
    }
    return data_body



access_token = generate_access_token(APP_ID, SCOPES)


headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}


GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'

# Generate Notebook
notebook_endpoint = GRAPH_ENDPOINT + '/me/onenote/notebooks'
request_body = {
    "displayName": "por favor"
}

response = requests.post(notebook_endpoint, headers=headers, json=request_body)
notebook = response.json()
notebook_id = notebook["id"]



# # Generate Section
section_endpoint = GRAPH_ENDPOINT + f'/me/onenote/notebooks/{notebook_id}/sections'
response = requests.post(section_endpoint, headers=headers, json=request_body)
section = response.json()
section_id = notebook["id"]

# # Generate Page
page_endpoint = GRAPH_ENDPOINT + f'/me/onenote/sections/{section_id}/pages'

request_body = {
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>A page with a block of HTML</title>
    </head>
    <body>
        <p>This page contains some <i>formatted</i> <b>text</b>.</p>
    </body>
    </html>
    """
}

response = requests.post(page_endpoint, headers=headers, json=request_body)
pprint(response.text)


# if response.status_code == 202:
#     print('Success')
# else: 
#     print(response.reason)

# pprint(notebook.text)
# pprint(section.text)
# pprint(page.text)