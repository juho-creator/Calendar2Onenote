

import os
import webbrowser
import msal


# APP_ID = "98c8b6c2-6df4-4765-ac02-4c32cf868661"
# CLIENT_SECRET = "iqd8Q~S-4NVAndMGfea5Yf4ww6M1Oz36hMhwbb4q"
# authority_url = "https://login.microsoftonline.com/consumers/"
# base_url = "https://graph.microsoft.com/v1.0/"
# SCOPES = ["User.Read","Notes.Read.All"]

def generate_access_token(app_id,scopes):

    access_token_cache = msal.SerializableTokenCache()
    
    # read the token files
    if os.path.exists('api_token_access.json'):
        access_token_cache.deserialize(open('api_token_access.json','r').read())


    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

    # get all accounts
    accounts = client.get_accounts()
    if accounts: # if there is an account
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else: # if there's no account
        flow = client.initiate_device_flow(scopes) 
        print('user code: '+ flow['user_code']) 
        webbrowser.open(flow['verification_uri'])
        token_response = client.acquire_token_by_device_flow(flow)

    with open('api_token_access.json', 'w') as _f: 
        _f.write(access_token_cache.serialize())
    return token_response

if __name__ == '__main__':
    APP_ID = '98c8b6c2-6df4-4765-ac02-4c32cf868661' 
    SCOPES =  ['User.Read']

    token_response = generate_access_token(APP_ID,SCOPES)
    print(token_response['access_token'])
