# gettingemail.py

import requests
import html2text

API_URL = 'https://api.guerrillamail.com/ajax.php'

def check_email(sid, seq):
    response = requests.get(API_URL, params={
        'f': 'check_email',
        'sid_token': sid,
        'seq': seq
    })

    try:
        data = response.json()
        if data:
            return data
        else:
            return False
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON response")
        return False
def get_email_address(lang='en', sid_token=None, site='guerrillamail.com'):
    params = {
        'f': 'get_email_address',
        'lang': lang,
        'site': site
    }
    if sid_token:
        params['sid_token'] = sid_token

    response = requests.get(API_URL, params=params)
    data = response.json()
    return data

def fetch_email(sid_token, email_id):
    response = requests.get(API_URL, params={
        'f': 'fetch_email',
        'email_id': email_id,
        'sid_token': sid_token
    })

    data = response.json()
    return data

def email_data():
    email_data1 = get_email_address()
    sid_token = email_data1['sid_token']
    print(f"Your temporary email address: {email_data1['email_addr']}")
    return email_data1['email_addr'], sid_token
