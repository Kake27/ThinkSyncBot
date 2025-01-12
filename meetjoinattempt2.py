# Import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv


def Glogin(mail_address, password):
    # Navigate to Google Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
    
    # Input Gmail ID
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_field.send_keys(mail_address)
    driver.find_element(By.ID, "identifierNext").click()

    # Wait for password field and input password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    password_field.send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()

    # Wait until the page loads and navigate to Google Home
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    driver.get('https://google.com/')

def turnOffMicCam():
    # Turn off Microphone using aria-label
    mic_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-label, "Turn off microphone")]'))
    )
    mic_button.click()

    # Turn off Camera using aria-label
    cam_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-label, "Turn off camera")]'))
    )
    cam_button.click()

def joinMeeting():
    try:
        # Try to find and click "Ask to join" button
        ask_join_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ask to join")]'))
        )
        ask_join_button.click()
        print("Clicked 'Ask to join'.")
    except Exception:
        try:
            # If "Ask to join" is not found, try "Join now"
            join_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Join now")]'))
            )
            join_button.click()
            print("Clicked 'Join now'.")
        except Exception as e:
            print(f"Error while trying to join the meeting: {e}")

def checkParticipants():
    try:
        # Check the number of participants in the meeting
        participants_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MKVSQd"))
        )
        participants_count = participants_element.text.strip()  # Get participant count as a string
        return int(participants_count)  # Return as integer for comparison
    except Exception as e:
        print(f"Error while checking participants: {e}")
        return 0

def keepMeetingAlive():
    # Continue running the script as long as the participants count is greater than 1
    while checkParticipants() > 1:
        print("More than 1 participant in the meeting. Waiting...")
        time.sleep(10)  # Check every 10 seconds
    print("Only 1 participant remaining. Leaving the meeting.")
    driver.quit()  # Exit the browser gracefully

# Assign email ID and password
mail_address = os.getenv('EMAIL_ID')
password = os.getenv('EMAIL_PASSWORD')

# Create Chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

# Login to Google account
Glogin(mail_address, password)
meet_link=os.getenv('MEET_LINK')
# Navigate to Google Meet
driver.get(meet_link)

# Turn off mic and camera
turnOffMicCam()

# Join the meeting
joinMeeting()

# Monitor the meeting and leave when only one participant is left
keepMeetingAlive()

# Close the driver after usage
time.sleep(5)  # Wait before closing the browser to observe actions
driver.quit()
