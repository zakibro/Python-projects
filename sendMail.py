#!python 3

from selenium import webdriver
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

#Podaj argumenty kolejno - twój email, hasło, treść maila


if len(sys.argv) < 4:
    print('Not enough data!')
else:
    browser = webdriver.Firefox()
    browser.get('https://accounts.google.com/AccountChooser/identifier?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AddSession')
    #login
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys(sys.argv[1])
    GoButton = browser.find_element_by_css_selector('.RveJvd')
    GoButton.click()
    #password
    time.sleep(2)
    passElem = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input')
    passElem.send_keys(sys.argv[2])
    GoButton2 = browser.find_element_by_css_selector('#passwordNext > content:nth-child(3)')
    GoButton2.click()
    #write new email
    newMailElem = browser.find_element_by_css_selector('.T-I-KE')
    newMailElem.click()
    time.sleep(6)
    recipient = browser.find_element_by_name('to')
    recipient.send_keys('pawelmazur835@gmail.com')
    subject = browser.find_element_by_name('subjectbox')
    subject.send_keys('Subject')
    message = ' '.join(sys.argv[3:])
    subject.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)













