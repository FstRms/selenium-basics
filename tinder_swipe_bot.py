""" Bot that swipes Tinder accounts. The real deal."""
import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
)

load_dotenv()

FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

driver_path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button'
)
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'
)
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]'
)
allow_location_button.click()
notifications_button = driver.find_element_by_xpath(
    '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]'
)
notifications_button.click()
cookies = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div[2]/div/div/div[1]/button'
)
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        )
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
