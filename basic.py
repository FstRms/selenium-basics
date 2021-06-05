""" Basic commands and practice of Selenium library."""
import os

from dotenv import load_dotenv
from pprint import pprint
from selenium import webdriver

load_dotenv()
# Specify chromedriver path and initialize object
chrome_driver_path = os.environ.get("DRIVER_PATH")
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Testing simple find methods
driver.get("https://www.python.org/")

print("\nTesting simple find methods")
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(f"Size of the logo is: {logo.size}")

doc_link = driver.find_element_by_css_selector(".documentation-widget a")
print(f"Link: {doc_link.text}")

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(f"Bug Link: {bug_link.text}")

# Example 1 Scrapping conference events in python org

print("\nScrapping conference events in python org")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
event_dict = {}

for ev in range(len(event_times)):
    event_dict[ev] = {
        "date": event_times[ev].text,
        "name": event_names[ev].text,
    }
pprint(event_dict)


driver.close()
driver.quit()
