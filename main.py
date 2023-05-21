import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:\Development\chromedriver.exe"   # Your own browser driver path
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

LOGIN = os.getenv("twitter_login")
PASSWORD = os.getenv("twitter_password")
USERNAME = os.getenv("twitter_username")

class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.real_down = 0
        self.real_up = 0
        self.provider_twitter_username = "Orange_Polska"
        self.declared_down = 600
        self.declared_up = 100

    def get_internet_speed(self):

        driver.get("https://www.highspeedinternet.com/tools/speed-test")

        start = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "start-button-text")))
        start.click()

        if wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "speed-download"), "Mbps")):

            self.real_down = float(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "speed-download"))).text.split()[0])
            print(f"Your download speed is: {self.real_down} Mbps")

        if wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "speed-upload "), "Mbps")):

            self.real_up = float(wait.until(EC.presence_of_element_located((By.CLASS_NAME, "speed-upload "))).text.split()[0])
            print(f"Your upload speed is: {self.real_up} Mbps")

    def log_into_twitter(self):

        driver.get("https://twitter.com/i/flow/login")
        driver.refresh()

        login_fill = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'r-30o5oe')))
        login_fill.send_keys(LOGIN)
        login_fill.send_keys(Keys.ENTER)
        
        # In some cases, if the user is logging too often it will be needed to enter username before the password as addidtional verification
        try:    
            password_fill = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
            password_fill.send_keys(PASSWORD)
            password_fill.send_keys(Keys.ENTER)
        except TimeoutException:
            username_fill = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")))
            username_fill.send_keys(USERNAME)
            username_fill.send_keys(Keys.ENTER)

            password_fill = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")))
            password_fill.send_keys(PASSWORD)
            password_fill.send_keys(Keys.ENTER)

        time.sleep(3)

    def send_tweet(self):
  
        tweet = f"@{self.provider_twitter_username}\nWhy is my internet speed {self.real_down} down/{self.real_up} up when I pay for {self.declared_down} down/{self.declared_up} up?\nIt is not nice!"

        driver.get("https://twitter.com/compose/tweet")

        post = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        post.send_keys(tweet)

        send = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')))
        send.click()


bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()
if (bot.declared_down > bot.real_down) or (bot.declared_up > bot.real_up):
    bot.log_into_twitter()
    bot.send_tweet()

input("To finish press 'Enter'")
