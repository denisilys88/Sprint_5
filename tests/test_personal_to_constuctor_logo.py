from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators as Loc


class TestFromPersonalToConstructorToLogo:

    def test_go_from_personal_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Loc.CONSTR_LINK)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        driver.quit()

    def test_go_from_personal_to_logo(self, login):
        driver = login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Loc.LOGO)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.CONSTR))
        driver.quit()
