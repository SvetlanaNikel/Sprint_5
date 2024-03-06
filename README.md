Описание проверок:

Фикстуры:
1. driver инициализирует браузер
2. sign_in тестовые данные для авторизации

В файле test_registration.py содержатся проверки:
1. Успешная регистрация test_registration_valid_values_successful_registration
2. Регистрация при введении некорректного пароля test_registration_invalid_values_error_response

В файле test_sign_in.py содержатся проверки:
1. Вход по кнопке "Войти в аккаунт" на главной test_sign_in_account_button_on_the_main_page
2. Вход через кнопку «Личный кабинет» test_sign_in_account_button_on_the_personal_account_button
3. Вход через кнопку в форме регистрации test_sign_in_account_button_on_the_registration_form
4. Вход через кнопку в форме восстановления пароля test_sign_in_account_button_password_recovery_button

В файле test_click_personal_account.py содержатся проверки:
1. Переход по клику "Личный кабинет" с главной страницы test_click_personal_account_from_main
2. Переход по клику "Личный кабинет" из ленты заказов test_click_personal_account_from_the_order_feed

В файле test_from_personal_account_in_constructor.py содержатся проверки:
1. Переход из личного кабинета в конструктор по клику на кнопку "Конструктор" test_click_from_personal_account_on_constructor
2. Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers

В файле test_exit_from_account.py содержатся проверки:
1. Выход по кнопке «Выйти» в личном кабинете test_exit_from_account

В файле test_section_in_constructor.py содержатся проверки перехода в разделе "Конструктор":
1. Во вкладку "Булки" test_section_in_constructor_buns
2. Во вкладку "Соусы" test_section_in_constructor_sauces
3. Во вкладку "Начинки" test_section_in_constructor_fillings