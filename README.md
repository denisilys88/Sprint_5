Проект содержит тесты на сайт https://stellarburgers.nomoreparties.site/

Locators.py содержит класс с константами локаторов, используемых в тестах

conftest.py содержит фикстуры:
driver - инициализирует драйвер Chrome
login - инициализирует вход в учетную запись
fake_data - возвращает список с генерируемыми значениями для полей name, email, password


[test_registration.py] содержит тесты на регистрацию
TestRegistration::test_registration_success - тест на успешную регистрацию
TestRegistration::test_registration_failure - тест на регистрацию с ошибкой

[test_personal_to_constuctor_logo.py] содержит тесты на переход в конструктор
TestFromPersonalToConstructorToLogo::test_go_from_personal_to_constructor - тест на 
переход в конструктор через кнопку конструктор
TestFromPersonalToConstructorToLogo::test_go_from_personal_to_logo - тест на 
переход в конструктор через логотип

[test_go_to_personal_area.py] содержит тест на вход в личный кабинет 
TestGoToPersonalArea::test_go_to_personal_area - тест на успешный вход в личный кабинет

[test_exit.py] содержит тест на выход из учетной записи
TestExit::test_exit_off_account - тест на успешный выход из учетной записи

[test_constructor.py] содержит тест на переходы по разделам конструктора
TestConstructor::test_constructor - параметризованный тест на успешный переход 
по вкладкам конструктора

[test_enter_account.py] содержит тесты на успешную авторизацию
TestEnterAccount::test_enter_account_from_main - тест на успешную авторизацию с главной страницы
TestEnterAccount::test_enter_account_from_private_area - тест на успешную авторизацию из личного кабинета
TestEnterAccount::test_enter_account_from_registr_form - тест на успешную авторизацию со страницы регистрации
TestEnterAccount::test_enter_account_from_password_restore - тест на успешную авторизацию со страницы восстановаления пароля