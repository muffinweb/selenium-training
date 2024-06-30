from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import sys

url = sys.argv[1]

browser = webdriver.Firefox()
browser.get(url)

clickable = browser.find_element(By.XPATH, "//*[@id=\"quick-index-nav\"]/li[2]/a")
ActionChains(browser).click(clickable).perform()

print(browser.title)