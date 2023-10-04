from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators as Loc


class TestExit:

    def test_exit_off_account(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.PRIVATE_AREA)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Loc.EXIT_BUTTON)).click()
        assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Loc.ENTER_BUTTON))
        driver.quit()
