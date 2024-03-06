from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import My_locators

class TestSectionsInConstructor:
    def test_section_in_constructor_buns(self, driver):
        section = driver.find_element(*My_locators.FILLINGS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", section)
        driver.find_element(*My_locators.BUNS_TAB).click
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.BUNS_HEADER))

    def test_section_in_constructor_sauces(self, driver):
        driver.find_element(*My_locators.SAUCES_TAB).click
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.SAUCES_HEADER))

    def test_section_in_constructor_fillings(self, driver):
        driver.find_element(*My_locators.FILLINGS_TAB).click
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(My_locators.FILLINGS_HEADER))

        driver.quit()