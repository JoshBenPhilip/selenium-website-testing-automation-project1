# Test Case
# -----------------
# pause_time. open web browser (Chrome/firefox/Edge).
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin)
# 4. Enter Password (adminpause_time23)
# 5. Click on Login
# 6. Capture the title of the homepage. (actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# 8. close browser

# Test Case
# -----------------
# pause_time. open web browser (Chrome/firefox/Edge).
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin)
# 4. Enter Password (adminpause_time23)
# 5. Click on Login
# 6. Capture the title of the homepage. (actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# at it's core this problem is title = OrangeHRM ? if true test = success else if false test = failure
# 8. close browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

pause_time = 1.5

driver=webdriver.Chrome("/Users/joshbenphilip/Drivers/chromedriver")


driver.get("https://www.saucedemo.com/")

driver.maximize_window() # For maximizing window
time.sleep(pause_time)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(pause_time)
driver.find_element(By.ID, "login-button").click()
time.sleep(pause_time)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(pause_time)
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(pause_time)
driver.find_element(By.ID,"checkout").click()
time.sleep(pause_time)
driver.find_element(By.ID,"first-name").send_keys("TomTest")
driver.find_element(By.ID,"last-name").send_keys("Testerson")
driver.find_element(By.ID,"postal-code").send_keys("33427")
time.sleep(pause_time)
driver.find_element(By.ID,"continue").click()
time.sleep(pause_time)
driver.find_element(By.ID, "finish").send_keys("down")
time.sleep(pause_time)
driver.find_element(By.ID, "finish").click()
#
exp_result=driver.find_element(By.ID,"checkout_complete_container")
# image_shown=driver.find_element(By.ID,"checkout_complete_container").img.src="/static/media/pony-express.46394a5d.png"
#
#
#
#
if exp_result:
    print ("Test Success")
else:
    print ("Test Failure")

time.sleep(pause_time)
driver.close()

