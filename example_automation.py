""" Basic commands and practice of Selenium library."""
import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

chrome_driver_path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# # Scrapping data from wikipedia and searching something

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # Getting article count
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# # Visit the link
# article_count.click()

# # Locate search bar and send data
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)


# Web page Automatic registration

driver.get("http://secure-retreat-92358.herokuapp.com/")

# Get the input boxes
first_box = driver.find_element_by_name("fName")
second_box = driver.find_element_by_name("lName")
third_box = driver.find_element_by_name("email")

# Populate data
first_box.send_keys("Agapito")
second_box.send_keys("Ramirez")
third_box.send_keys("agapito_ram@gmail.com")
time.sleep(3)
# Find button and send data
send_button = driver.find_element_by_css_selector(".form-signin button")
send_button.click()
time.sleep(4)
driver.quit()
