from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys

email = sys.argv[1]
#TestLine
#email = 'email'

password = sys.argv[2]
#TestLine
#password = 'pass'

url = 'https://account.jetbrains.com/login'

browser = webdriver.Firefox()
browser.get(url)

userInput = browser.find_element(By.XPATH, '//*[@id="username"]')
passwordInput = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[3]/input')
submitButton = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[5]/div[1]/button')
submitButtonClickable = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[5]/div[1]/button')

actions = ActionChains(browser)
actions.send_keys_to_element(userInput, email)\
    .send_keys_to_element(passwordInput, password)\
    .move_to_element(browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[5]/div[1]/button'))\
    .click(submitButtonClickable)\
    .perform()

wait = WebDriverWait(browser, 10)
licenseId = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'id'))).text

print(licenseId)

browser.quit()