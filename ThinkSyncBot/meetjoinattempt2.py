from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

class Bot:
    load_dotenv()
    def Glogin(self, driver, mail_address, password):
        driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
        
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@type="email"]'))
        )
        email_field.send_keys(mail_address)
        driver.find_element(By.ID, "identifierNext").click()

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
        )
        password_field.send_keys(password)
        driver.find_element(By.ID, "passwordNext").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        driver.get('https://google.com/')

    def turnOffMicCam(self,driver):
        mic_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-label, "Turn off microphone")]'))
        )
        mic_button.click()

        cam_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(@aria-label, "Turn off camera")]'))
        )
        cam_button.click()

    def joinMeeting(self, driver):
        try:
            ask_join_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Ask to join")]'))
            )
            ask_join_button.click()
            print("Clicked 'Ask to join'.")
        except Exception:
            try:
                join_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Join now")]'))
                )
                join_button.click()
                print("Clicked 'Join now'.")
            except Exception as e:
                print(f"Error while trying to join the meeting: {e}")



    def runBot(self, meet_link) :
        mail_address = os.getenv('EMAIL_ID')
        password = os.getenv('EMAIL_PASSWORD')
        print("running")
        print(mail_address)

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

        self.Glogin(driver, mail_address, password)

        driver.get(meet_link)
        self.turnOffMicCam(driver)

        self.joinMeeting(driver)
        time.sleep(5) 
        driver.quit()


