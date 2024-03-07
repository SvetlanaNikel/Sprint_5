from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestClickPersonalAccount:
    def test_click_personal_account_from_main(self, driver, sign_in):
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.HISTORY_OF_ORDERS_URL))

    def test_click_personal_account_from_the_order_feed(self, driver, sign_in):
        driver.find_element(*My_locators.ORDERS_FEED_BUTTON).click()
        driver.find_element(*My_locators.PERSONAL_ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.HISTORY_OF_ORDERS_URL))

