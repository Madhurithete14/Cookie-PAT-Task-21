
#Cookie created before and after login

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://www.saucedemo.com/")

print("cookies before login")
for cookies in driver.get_cookies():
   print(cookies)

# Finding and interacting with elements
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()    # Click the login button



print(" cookies after login")
for cookies in driver.get_cookies():
   print(cookies)
  


driver.quit()


