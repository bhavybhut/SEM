from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = None

def setup_module(module):
    global browser
    browser = webdriver.Firefox(executable_path="C:/automation/geckodriver.exe")
    browser.get("http://www.amazon.com")

def teardown_module(module):
    time.sleep(10)
    if browser:
        browser.close()

def test_amazonConnection():
    assert "Amazon" in browser.title

def test_blender():
    id = "twotabsearchtextbox"
    searchbox = browser.find_element_by_id(id)
    searchbox.clear()
    searchbox.send_keys("blender")
    searchbox.send_keys(Keys.RETURN)
    time.sleep(5)
    id="s-results-list-atf"
    result_list = browser.find_element_by_id(id)
    result_text = result_list.text
    assert ("Oster" in result_text or "Hamilton Beach" in result_text)