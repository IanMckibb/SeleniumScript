from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.colorado.edu/living/dining/dining-centers/village-center-dining")
print(driver.title)

content = driver.find_element_by_class_name("content-grid-container")
locations = content.find_elements_by_class_name("content-grid-item")
for location in locations:
    name = location.find_element_by_class_name("feature-callout-title")
    print(name.text)

time.sleep(5)

driver.close()

