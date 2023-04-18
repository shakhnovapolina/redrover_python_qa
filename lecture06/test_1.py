from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def open_page():
#browser.get('http://suninjuly.github.io/xpath_examples')
    browser.get('http://suninjuly.github.io/cats.html')
    #time.sleep(5)
    #bullet_cat = browser.find_element(By.XPATH,"//*[contains(text(), 'Bullet cat')]")
    #print(bullet_cat.text)
    view_buttons = browser.find_elements(By.XPATH,"//*[contains(text(), 'View')]")
    assert len(view_buttons) == 6, 'wrong length'

def find_gold_button():
    browser.get('http://suninjuly.github.io/xpath_examples')
    gold_button = browser.find_element(By.XPATH, "//div[2]/button[last()-1]")
    assert gold_button.text =='Gold', 'Gold button not found'

def find_fully_charged_cat():
    browser.get('http://suninjuly.github.io/cats.html')
    charged_cat = browser.find_element(By.XPATH, "/html/body/main/div/div/div/div[5]/div/div/p")
    assert charged_cat.text =='Fully charged cat', 'Fully charged cat not found'

def test_open_page():
    open_page()

def test_find_gold_button():
    find_gold_button()

def test_find_charged_cat():
    find_fully_charged_cat()