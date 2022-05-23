from click import option
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

option = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values":{"notifications":2}}
option.add_experimental_option("prefs",prefs)

chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome("chromedriver",options=option)
driver.get("https://www.facebook.com/")
driver.maximize_window()

#透過cookie登入
# for c in cookie:
#     driver.add_cookie(c)

# driver.refresh()

#登入前cookie
# cookie = driver.get_cookies()
# print(cookie)
# print("==============")


#登入後cookie
# cookie = driver.get_cookies()
# jsoncookie = json.dumps(cookie)
# with open("facebook.json","w") as f:
#     f.write(jsoncookie) 

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="email"]')))
username.clear()
username.send_keys("0966130683")

password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[id="pass"]')))
password.clear()
password.send_keys("zxc85246")


login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[name="login"]')))
login.click()

# n_scroll = 10
# for scrolltimes in range(1,n_scroll):
driver.execute_script("window,scrollTo(0,5000)")


# popcat遊戲
# login = WebDriverWait(driver,0.00000000000000001).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[class="cat-img p"]')))
# while True:
#     login.click()
# button = driver.find_element_by_class_name("cat-img p")
# button.click()


# time.sleep(15)
# login.close()