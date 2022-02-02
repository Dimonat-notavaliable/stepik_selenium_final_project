from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form[id = 'login_form']")
    REGISTER_FORM = (By.CSS_SELECTOR, "form[id = 'register_form']")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket_summary")
