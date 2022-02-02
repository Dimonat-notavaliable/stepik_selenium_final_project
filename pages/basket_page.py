from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


languages = {
    "ar": "سلة التسوق فارغة", "ca": "La seva cistella està buida.", "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.", "de": "Ihr Warenkorb ist leer.", "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.", "es": "Tu carrito esta vacío.", "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.", "it": "Il tuo carrello è vuoto.", "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg", "pl": "Twój koszyk jest pusty.", "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.", "ro": "Cosul tau este gol.", "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny", "uk": "Ваш кошик пустий.", "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert languages[language] in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text,\
            "Basket is not empty"

    def should_be_products_in_basket(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Basket is empty, but should not be"

    def should_be_appeared_products_in_basket(self):
        assert self.is_appeared(*BasketPageLocators.BASKET_PRODUCTS), \
            "Products in basket didn't appear, but should"

