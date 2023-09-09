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


APP_ID = "98c8b6c2-6df4-4765-ac02-4c32cf868661"
SCOPES = ['Mail.Send', 'Mail.ReadWrite']
# SCOPES =  ['User.Read']



access_token = generate_access_token(APP_ID, SCOPES)


headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}


GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'
endpoint = GRAPH_ENDPOINT + '/me/sendMail'

for i in range(1,101):
    request_body = {
        'message': {
            # recipient list
            'toRecipients': [
                {
                    'emailAddress': {
                        'address': 'kjuho2021@gmail.com'
                    }
                }
            ],
            # email subject
            'subject': 'You got an email',
            'importance': 'normal',
            'body': {
                'contentType': 'HTML',
                'content': '<b> I am sending mail Number {}</b>'.format(i)
            },
            # # include attachments
            # 'attachments': [
            #     # draft_attachment('hello.txt'),
            #     draft_attachment('image.png')
            # ]
        }
    }

    response = requests.post(endpoint, headers=headers, json=request_body)
    if response.status_code == 202:
        print('Email sent')
    else:
        print(response.reason)