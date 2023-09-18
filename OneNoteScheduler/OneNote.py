from M_OAuth import generate_access_token
from pprint import pprint
import requests
import bleach

# Setup for Azure AD
APP_ID = "98c8b6c2-6df4-4765-ac02-4c32cf868661"
SCOPES = [
    "Notes.Create",
    "Notes.ReadWrite"
]



# Generate access token
access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

# Base Graph Endpoint
GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'


# Generate Notebook
def CreateNoteBook(year):
    # Request for creating Notebook
    notebook_endpoint = GRAPH_ENDPOINT + '/me/onenote/notebooks'
    request_body = {
        "displayName": year
    }
    response = requests.post(notebook_endpoint, headers=headers, json=request_body)

    # Extract Notebook ID
    notebook = response.json()
    notebook_id = notebook["id"]

    # Return Notebook ID
    return notebook_id


# Generate Section
def CreateSection(month,notebook_id):
    # Request for creating Section
    section_endpoint = GRAPH_ENDPOINT + f'/me/onenote/notebooks/{notebook_id}/sections'
    request_body = {
        "displayName": month
    }
    response = requests.post(section_endpoint, headers=headers, json=request_body)

    # Extract Section ID
    section = response.json()
    section_id = section["id"]

    #  Return Section ID
    return section_id



# Generate Page
def CreatePage(day, events, date, section_id):
    # Request for creating Page
    headers = {
        'Authorization': 'Bearer ' + access_token['access_token'],
        'Content-type': 'text/html; charset=utf-8'  # Set charset to UTF-8
    }

    # Get page endpoint
    page_endpoint = GRAPH_ENDPOINT + f'/me/onenote/sections/{section_id}/pages'

    # Check for matching values
    matching_values = [bleach.clean(event) for key, value in events.items() for event in value if date in key]
    print(date,matching_values)

    if matching_values:
        value_html = "".join([f"<p data-tag='to-do'>{value}</p>" for value in matching_values])

        # Encode the HTML data as UTF-8
        html = f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{day}</title></head><body>{value_html}</body></html>'
        html_encoded = html.encode('utf-8')
    else:
        html_encoded = f'<!DOCTYPE html><html><head><meta charset="UTF-8"><title>{day}</title></head><body></body></html>'.encode('utf-8')

    response = requests.post(page_endpoint, headers=headers, data=html_encoded)
    page = response.json()
    pprint(page)
