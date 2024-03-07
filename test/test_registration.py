import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestRegistration:
    def test_registration_valid_values_successful_registration(self, driver):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.REGISTER_URL_AUTH)).click()
        driver.find_element(*My_locators.NAME_INPUT_FIELD_REG).send_keys('Sveta')
        random_email = f'svetlana_nikel_6_{random.randint(100, 999)}'
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_REG).send_keys(random_email)
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_REG).send_keys(123458)
        driver.find_element(*My_locators.REGISTRATION_BUTTON_REG).click()

    def test_registration_invalid_values_error_response(self, driver):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.REGISTER_URL_AUTH)).click()
        driver.find_element(*My_locators.NAME_INPUT_FIELD_REG).send_keys('Sveta')
        random_email = f'svetlana_nikel_6_{random.randint(100, 999)}'
        driver.find_element(*My_locators.EMAIL_INPUT_FIELD_REG).send_keys(random_email)
        driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_REG).send_keys(12345)
        driver.find_element(*My_locators.REGISTRATION_BUTTON_REG).click()
        assert driver.find_element(*My_locators.INCORRECT_PASSWORD_ERROR_REG)

