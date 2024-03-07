import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def sign_in(driver):
    driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.EMAIL_INPUT_FIELD_AUTH))
    driver.find_element(*My_locators.EMAIL_INPUT_FIELD_AUTH).send_keys("svetlana_nikel_6_123@yandex.ru")
    driver.find_element(*My_locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(123456)
    driver.find_element(*My_locators.SIGN_IN_BUTTON_AUTH).click()