from gettingemail import get_email_address, sid_token, API_URL, fetch_email
import requests
import html2text
import time
import re

def check_email(sid_token, seq):
    response = requests.get(API_URL, params={
        'f': 'check_email',
        'sid_token': sid_token,
        'seq': seq
    })

    #print("Check email response text:", response.text)  # Add this line to print the response text

    try:
        data = response.json()
        if data:
            return data
        else:
            return False
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON response")
        return False

for i in range(2):

    # Check for new emails
    seq = 0
    checked_emails = check_email(sid_token, seq)
    print("Checking for new emails...")

    if int(checked_emails['count']) > 0:
        #print("New emails found:")
        for email in checked_emails['list']:
            #print(f"From: {email['mail_from']}, Subject: {email['mail_subject']}")

            # Fetch the email using its mail_id
            fetched_email = fetch_email(sid_token, email['mail_id'])
            if fetched_email:
                # Extract the email content and convert HTML to plain text
                html_content = fetched_email['mail_body']
                text_content = html2text.html2text(html_content)
                print(text_content)

                url_pattern = re.compile(r'\[Redeem Offer\s*Now!\]\s*\((http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)\)')
                url = re.search(url_pattern, text_content)

                if url:
                    extracted_url = url.group(1)
                    print(f'The extracted URL is: {extracted_url}')
                else:
                    print('No URL found in the text.')



            seq = max(seq, int(email['mail_id'])) + 1

    # else:
    #     print("No new emails found.")

    time.sleep(5)