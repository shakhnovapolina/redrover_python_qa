from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert "openweathermap" in driver.current_url
    print(driver.current_url)

def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys("New York")
    time.sleep(5)
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class = 'button-round dark']")))
    search_button.click()
    driver.implicitly_wait(20)
    search_option = driver.find_element(By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_option.click()
    time.sleep(5)
    expected_city = "New York City, US"
    displayed_city = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')))
    displayed_city_text = displayed_city.text
    assert displayed_city_text == expected_city, 'Displayed city not New York City'


def test_open_market(driver):
    driver.get("https://home.openweathermap.org/marketplace")
    assert "marketplace" in driver.current_url

def test_open_market_from_menu(driver):
    driver.get("https://home.openweathermap.org")
    market_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#desktop-menu > ul > li:nth-child(4) > a")))
    market_link.click()
    assert "marketplace" in driver.current_url

def test_available_bundles(driver):
    driver.get("https://home.openweathermap.org/marketplace")
    products  = WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product")))
    print(products)
    assert products, 'some products are here'

'''
def test_default_cityname():
    cityname = driver.find_element(By.XPATH, "//h2[contains(text(), 'London, GB')]")
    assert cityname.text == 'London, GB', 'Default city is not London'


def test_date():
    date = driver.find_element(By.XPATH, "//*[@id='weather-widget']/div[2]/div[1]/div[1]/div[1]/span")
    assert datetime.date in date.text, 'Date is correct and visible'
'''