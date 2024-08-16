import time
import random
import string
import re
import html2text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from gettingemail import email_data, check_email, fetch_email
for i in range(10):
    try:
        email_address, sid_token = email_data()

        webdriver_path = r'C:\Users\Ryan Zhou\Downloads\chromedriver.exe'
        url = 'https://www.the-spoke.ca/'

        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')


        browser = webdriver.Chrome(executable_path=webdriver_path, options=options)
        browser.get(url)

        vip_element_css_selector = 'a.jss173 > h2.MuiTypography-root.jss180.jss186.jss174.pm-img-overlay-text.pm-AH.pm-h4.MuiTypography-h5.MuiTypography-alignCenter'
        vip_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, vip_element_css_selector)))
        vip_element.click()
        time.sleep(random.uniform(2.5, 5.0))  # Random delay between actions
        time.sleep(random.uniform(2.5, 5.0))  # Random delay between actions

        email_input_id = 'pm-signup-email-input'
        email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, email_input_id)))
        email_input.send_keys(email_address)

        # Generate random name
        letter = ''
        for i in range(random.randint(8, 19)):
            letter += random.choice(string.ascii_letters)
        time.sleep(random.uniform(2.5, 5.0))  # Random delay between actions

        name_input_id = 'pm-signup-name-input'
        name_input = WebDriverWait(browser, (random.randint(5,15))).until(EC.presence_of_element_located((By.ID, name_input_id)))
        name_input.send_keys(letter)

        # Generate random phone number
        number = ''
        for i in range(10):
            x = random.randint(0, 10)
            x = str(x)
            number += x

        phone_input_id = 'pm-signup-phone-input'
        phone_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, phone_input_id)))
        phone_input.send_keys(number)
        time.sleep(random.uniform(2.5, 5.0))  # Random delay between actions


        # Locate the dropdown menu and select an option
        dropdown_input_id = 'react-select-2-input'
        dropdown_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dropdown_input_id)))

        # Send the desired value to the dropdown input, for example, 'January'
        listofbday = ["January","Febuary", "March", "April", "May", "June", "July", "August","September","October","November", "December"]
        dropdown_input.send_keys(listofbday[(random.randint(0,11))])
        dropdown_input.send_keys(u'\ue007')  # Press the 'Enter' key to confirm the selection

        # Locate the dropdown menu and select an option
        dropdown_input_id = 'react-select-3-input'
        dropdown_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dropdown_input_id)))

        # Send the desired value to the dropdown input, for example, 'January'
        poop = random.randint(1,30)
        dropdown_input.send_keys(str(poop))

        time.sleep(random.uniform(2.5, 5.0))  # Random delay between actions

        dropdown_input.send_keys(u'\ue007')  # Press the 'Enter' key to confirm the selection
        # Locate the dropdown menu and select an option
        dropdown_input_id = 'react-select-2-input'
        dropdown_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dropdown_input_id)))

        # Send the desired value to the dropdown input, for example, 'January'
        listofbday = ["January","Febuary", "March", "April", "May", "June", "July", "August","September","October","November", "December"]
        dropdown_input.send_keys(listofbday[(random.randint(0,11))])

        dropdown_input.send_keys(u'\ue007')  # Press the 'Enter' key to confirm the selection
        dropdown_input_id = 'react-select-4-input'
        dropdown_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, dropdown_input_id)))

        # Send the desired value to the dropdown input, for example, 'January'
        dropdown_input.send_keys('Western University')
        dropdown_input.send_keys(u'\ue007')  # Press the 'Enter' key to confirm the selection

        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cy="submit"]'))
        )

        # Click the button
        button.click()
        time.sleep(5)
        browser.quit()
        # magic_link_button_xpath = '//button[span[contains(text(), "Email me a Magic Link")]]'
        # magic_link_button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, magic_link_button_xpath)))
        #
        # magic_link_button.click()

        time.sleep(9)
        for i in range(5):
            # Check for new emails
            seq = 0
            checked_emails = check_email(sid_token, seq)
            print("Checking for new emails...")

            if int(checked_emails['count']) > 0:
                for email in checked_emails['list']:
                    fetched_email = fetch_email(sid_token, email['mail_id'])
                    if fetched_email:
                        html_content = fetched_email['mail_body']
                        text_content = html2text.html2text(html_content)
                        print(text_content)
                        url_pattern = re.compile(r'\[Redeem Offer\s*Now!\]\s*\((http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)\)')
                        url = re.search(url_pattern, text_content)

                        if url:
                            extracted_url = url.group(1)
                            with open("hehe.txt", "a") as f:
                                f.write(extracted_url + "\n")
                            print(f'The extracted URL is: {extracted_url}')
                        else:
                            print('No URL found in the text.')

                    seq = max(seq, int(email['mail_id'])) + 1

            time.sleep(6)

        #browser.quit()
        print('poop')
    except Exception as e:
        print(f"Error on iteration {i}: {e}")
        browser.quit()
        continue
        #open and read the file after the appending:


browser.quit()