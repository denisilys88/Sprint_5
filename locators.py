from selenium.webdriver.common.by import By


class Locators:

    # input fields for name, email, password
    INPUT_NAME = (By.XPATH, ".//label[text()='Имя']/../input[@value]")
    INPUT_MAIL = (By.XPATH, ".//label[text()='Email']/../input[@value]")
    INPUT_PASS = (By.XPATH, ".//label[text()='Пароль']/../input[@value]")

    # private area link
    REGISTR_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    REGISTR_LINK_ENTER = (By.XPATH, ".//a[text()='Войти']")
    RESTORE_PASS_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    PROFILE = (By.XPATH, ".//a[text()='Профиль']")

    # buttons on private
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    ENTER_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # error with wrong registration
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # buttons on main
    ENTER_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    MAKE_PURCHASE_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    PRIVATE_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']")

    # logo
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    # constructor
    CONSTR_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    CONSTR = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # constructor buttons
    SAUCES = (By.XPATH, ".//span[text()='Соусы']")
    BUNCHES = (By.XPATH, ".//span[text()='Булки']")
    INNERS = (By.XPATH, ".//span[text()='Начинки']")
    # constructor taps
    TAP_SAUCES = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Соусы']")
    TAP_BUNCHES = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Булки']")
    TAP_INNERS = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]/span[text()='Начинки']")



