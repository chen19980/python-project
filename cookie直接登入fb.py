import json
from click import option
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"notifications":2}}
option.add_experimental_option("prefs",prefs)

chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome("chromedriver",options=option)
driver.get("https://www.facebook.com/")
f1 = open("facebook.json")
cookie = json.loads(f1.read())
driver.maximize_window()

for c in cookie:
    driver.add_cookie(c)

driver.refresh()