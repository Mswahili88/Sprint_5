from locators import BurgerLocators
from data import BurgerTestData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings

class TestExitAccount:
    def test_exit_account(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        personal_account_enter = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        personal_account_enter.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'account/profile'))
        button_exit = driver.find_element(*BurgerLocators.BUTTON_EXIT)
        button_exit.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(settings.URL + 'login'))
        login_title = driver.find_element(*BurgerLocators.TITLE_ENTER)
        assert login_title.is_displayed() and login_title.text == 'Вход'