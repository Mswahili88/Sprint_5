from selenium.webdriver.common.by import By

class BurgerLocators:
    BUTTON_ACCOUNT = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]")
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_SMALL_ENTER = (By.XPATH, "//*[contains(@class, 'Auth_link__1fOlj')]")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//*[contains(@href,'/forgot-password')]")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_REGISTRATE = (By.XPATH, "//*[contains(@href,'/register')]")
    BUTTON_FINAL_REGISTRATE = (By.XPATH, "//button[text()='Зарегистрироваться']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']")

    SAUCE_UNFOCUSED = (By.XPATH, "//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    SAUCE_IN_FOCUS = (By.XPATH, "//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_UNFOCUSED = (By.XPATH, "//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_IN_FOCUS = (By.XPATH, "//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    BREAD_UNFOCUSED = (By.XPATH, "//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    BREAD_IN_FOCUS = (By.XPATH, "//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")

    TITLE_ENTER = (By.XPATH, "//h2[text()='Вход']")
    TITLE_PROFILE = (By.XPATH, "//a[text()='Профиль']")
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")

    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")
    FORM_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")