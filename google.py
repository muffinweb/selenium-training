from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.google.com')

client_location = browser.find(By.CLASS_NAME, 'uU7dJb').text

print(client_location)