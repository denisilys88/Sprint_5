import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1200,800')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*Loc.INPUT_MAIL).send_keys('dns88@mail.ru')
    driver.find_element(*Loc.INPUT_PASS).send_keys('123456')
    driver.find_element(*Loc.ENTER_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.MAKE_PURCHASE_BUTTON))
    return driver

