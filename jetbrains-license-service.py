from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import sys

email = sys.argv[1]
#TestLine
#email = 'test-email'

password = sys.argv[2]
#TestLine
#password = 'test-pass'

url = 'https://account.jetbrains.com/login'

browser = webdriver.Chrome()
browser.get(url)

browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(email)
browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[3]/input').send_keys(password)
browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div[1]/form/div[5]/div[1]/button').click()

license_id = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[5]/div[1]/div/div/div[3]/div').text

print(license_id)

browser.quit()
