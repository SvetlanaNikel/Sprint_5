from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestExitFromAccount:
    def test_exit_from_account(self, driver, sign_in):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.EXIT_BUTTON_ACCOUNT)).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.SIGN_IN_BUTTON_AUTH))

        driver.quit()