""" Bot to follow instagram accounts from a 'base' instagram account."""
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv

load_dotenv()

DRIVER_PATH = os.environ.get("DRIVER_PATH")
# Account you want to take followers from
BASE_ACCOUNT = os.environ.get("BASE_ACCOUNT")
# Your Instagram credentials
USERNAME = os.environ.get("INSTAGRAM_USER")
PASSWORD = os.environ.get("INSTAGRAM_PASS")


class InstagramFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(7)

        username_box = self.driver.find_element_by_name("_box")
        password_box = self.driver.find_element_by_name("password")

        username_box.send_keys(USERNAME)
        password_box.send_keys(PASSWORD)

        time.sleep(2)
        password_box.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(7)
        self.driver.get(f"https://www.instagram.com/{BASE_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers.click()

        time.sleep(2)
        scroller = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scroller
            )
            time.sleep(2)

    def new_follow(self):
        buttons = self.driver.find_elements_by_css_selector("li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()


instagram_follower = InstagramFollower(DRIVER_PATH)
instagram_follower.login()
instagram_follower.find_followers()
instagram_follower.new_follow()
