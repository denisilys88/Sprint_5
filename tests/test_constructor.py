import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc


class TestConstructor:

    @pytest.mark.parametrize('for_click,for_presence', [[Loc.SAUCES, Loc.TAP_SAUCES], [Loc.BUNCHES, Loc.TAP_BUNCHES],
                                                         [Loc.INNERS, Loc.TAP_INNERS]])
    def test_constructor(self, login, for_click, for_presence):
        driver = login
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        if for_click != Loc.BUNCHES:
            driver.find_element(*for_click).click()
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(for_presence))

