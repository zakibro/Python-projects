"""Simple script that "plays" the 2048"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

browser.get('https://play2048.co')
htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
