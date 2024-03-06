from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestSignIn:
    def test_sign_in_account_button_on_the_main_page(self, driver):
        driver.find_element(*My_locators.SIGN_IN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_AUTH).send_keys("svetlana_nikel_6_123@yandex.ru")
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(123456)
        driver.find_element(*My_locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.MAKE_AN_ORDER_BUTTON))

    def test_sign_in_account_button_on_the_personal_account_button(self, driver):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_AUTH).send_keys("svetlana_nikel_6_123@yandex.ru")
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(123456)
        driver.find_element(*My_locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.MAKE_AN_ORDER_BUTTON))

    def test_sign_in_account_button_on_the_registration_form(self, driver):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.SIGN_IN_BUTTON_REG)).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_AUTH).send_keys("svetlana_nikel_6_123@yandex.ru")
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(123456)
        driver.find_element(*My_locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.MAKE_AN_ORDER_BUTTON))

    def test_sign_in_account_button_password_recovery_button(self, driver):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.RECOVERY_PASSWORD_BUTTON_AUTH)).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.SIGN_IN_BUTTON_PASSWORD_RECOVERY)).click()
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_AUTH).send_keys("svetlana_nikel_6_123@yandex.ru")
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(123456)
        driver.find_element(*My_locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.MAKE_AN_ORDER_BUTTON))

        driver.quit()