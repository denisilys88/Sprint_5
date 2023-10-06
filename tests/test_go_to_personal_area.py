from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators as Loc


class TestGoToPersonalArea:

    def test_go_to_personal_area(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.PRIVATE_AREA)).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Loc.PROFILE))

