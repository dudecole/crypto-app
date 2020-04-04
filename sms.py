from selenium import webdriver
from bs4 import BeautifulSoup
import time

EMAIL = ''
PASSWORD = ''
CHROMEPATH = '.\chromedriver.exe'


login_url = 'https://www.google.com/accounts/Login'

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
browser = webdriver.Chrome(CHROMEPATH, options=chrome_options);
browser.set_window_position(0, 0)
browser.get(login_url)
time.sleep(2)
browser.find_element_by_id("identifierId").send_keys(EMAIL)
browser.find_element_by_id("identifierNext").click()
time.sleep(5)
browser.find_element_by_name("password").send_keys(PASSWORD)
browser.find_element_by_id("passwordNext").click()
time.sleep(10)

soup = BeautifulSoup(browser.page_source, 'html.parser')
