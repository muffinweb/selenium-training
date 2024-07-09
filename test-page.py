from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.get('http://localhost:8000/test-page.php')

wait = WebDriverWait(browser, 10)
elementWaitedFor = wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="license-key"]')))

print(elementWaitedFor.text)

browser.quit()