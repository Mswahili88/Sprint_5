from locators import BurgerLocators
from data import BurgerTestData
import time

class TestConstructionSections:
    def test_construction_sections(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()
        time.sleep(1)

        driver.find_element(*BurgerLocators.SAUCE_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.SAUCE_IN_FOCUS)
        driver.find_element(*BurgerLocators.TOPPING_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.TOPPING_IN_FOCUS)
        time.sleep(1)
        driver.find_element(*BurgerLocators.BREAD_UNFOCUSED).click()
        assert driver.find_element(*BurgerLocators.BREAD_IN_FOCUS)






