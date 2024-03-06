from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestFromPersonalAccountInConstructor:
    def test_click_from_personal_account_on_constructor(self, driver, sign_in):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*My_locators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.COLLECT_BURGER_HEADER))

    def test_click_from_personal_account_on_logo(self, driver, sign_in):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*My_locators.LOGO_HEADER).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.COLLECT_BURGER_HEADER))

        driver.quit()