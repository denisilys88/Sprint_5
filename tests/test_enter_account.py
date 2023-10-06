from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc


class TestEnterAccount:

    def test_enter_account_from_main(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))
        driver.find_element(*Loc.INPUT_MAIL).send_keys('dns88@mail.ru')
        driver.find_element(*Loc.INPUT_PASS).send_keys('123456')
        driver.find_element(*Loc.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.MAKE_PURCHASE_BUTTON))

    def test_enter_account_from_private_area(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.PRIVATE_AREA)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))
        driver.find_element(*Loc.INPUT_MAIL).send_keys('dns88@mail.ru')
        driver.find_element(*Loc.INPUT_PASS).send_keys('123456')
        driver.find_element(*Loc.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.MAKE_PURCHASE_BUTTON))

    def test_enter_account_from_registr_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.REGISTR_LINK)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.REGISTR_LINK_ENTER)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))
        driver.find_element(*Loc.INPUT_MAIL).send_keys('dns88@mail.ru')
        driver.find_element(*Loc.INPUT_PASS).send_keys('123456')
        driver.find_element(*Loc.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.MAKE_PURCHASE_BUTTON))

    def test_enter_account_from_password_restore(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.RESTORE_PASS_LINK)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.REGISTR_LINK_ENTER)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))
        driver.find_element(*Loc.INPUT_MAIL).send_keys('dns88@mail.ru')
        driver.find_element(*Loc.INPUT_PASS).send_keys('123456')
        driver.find_element(*Loc.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.MAKE_PURCHASE_BUTTON))
