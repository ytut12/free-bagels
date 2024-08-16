from gettingemail import email_data
import requests

x = email_data()[1]
print(x)

def check_email(x, seq):
    response = requests.get(API_URL, params={
        'f': 'check_email',
        'sid_token': x,
        'seq': seq
    })