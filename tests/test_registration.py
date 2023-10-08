from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc
from helpers import Helpers as Help


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Loc.INPUT_NAME).send_keys(Help.fake_data()[0])
        driver.find_element(*Loc.INPUT_MAIL).send_keys(Help.fake_data()[1])
        driver.find_element(*Loc.INPUT_PASS).send_keys(Help.fake_data()[2])
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.REG_BUTTON)).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))

    def test_registration_failure(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Loc.INPUT_NAME).send_keys(Help.fake_data()[0])
        driver.find_element(*Loc.INPUT_MAIL).send_keys(Help.fake_data()[1])
        driver.find_element(*Loc.INPUT_PASS).send_keys('12345')
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Loc.REG_BUTTON)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.PASSWORD_ERROR))


