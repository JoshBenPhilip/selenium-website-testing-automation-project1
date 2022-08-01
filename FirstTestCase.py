# Test Case
# -----------------
# 1. open web browser (Chrome/firefox/Edge).
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin)
# 4. Enter Password (admin123)
# 5. Click on Login
# 6. Capture the title of the homepage. (actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# 8. close browser

# Test Case
# -----------------
# 1. open web browser (Chrome/firefox/Edge).
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin)
# 4. Enter Password (admin123)
# 5. Click on Login
# 6. Capture the title of the homepage. (actual title)
# 7. Verify title of the page: OrangeHRM (Expected)
# at it's core this problem is title = OrangeHRM ? if true test = success else if false test = failure
# 8. close browser



from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("/Users/joshbenphilip/Drivers/chromedriver")


driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
act_title=driver.title

exp_title="OrangeHRM"


if act_title == exp_title:
    print ("Test Success")
else:
    print ("Test Failure")

