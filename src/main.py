from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.colorado.edu/daily-health-form")

try:
    isLoaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Start Daily Student Health Form"))
    )
    isLoaded.click()
except:
    driver.quit()

#locate canvas username and password fields and fill them out

try:
    isLoaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
except:
    driver.quit()

username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

usr = os.environ.get("CANVAS_USER")
pas = os.environ.get("CANVAS_PASS")

username_field.send_keys(usr)
password_field.send_keys(pas)

#click submit

submit_button = driver.find_element_by_name("_eventId_proceed")
submit_button.click()

# On health form link now

#Can fill out form

time.sleep(60)

driver.close()

