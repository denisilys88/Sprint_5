import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc


class TestConstructor:

    def test_constructor_go_sauces(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        driver.find_element(*Loc.SAUCES).click()
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Loc.TAP_SAUCES))

    def test_constructor_go_inners(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        driver.find_element(*Loc.INNERS).click()
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Loc.TAP_INNERS))

    def test_constructor_go_bunches(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        driver.find_element(*Loc.SAUCES).click()
        driver.find_element(*Loc.BUNCHES).click()
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Loc.TAP_BUNCHES))

