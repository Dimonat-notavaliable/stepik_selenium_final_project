from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_basket_button()
        self.should_be_product_url()

    def should_be_product_url(self):
        assert "?promo=offer" in self.browser.current_url, "Wrong url for product"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message button didn't disappear, but should"

    def should_be_correct_name(self):
        assert self.browser.find_element_by_css_selector("#messages>.alert:nth-child(1) strong").text == \
               self.browser.find_element_by_css_selector(".product_main h1").text, "Wrong name!"

    def should_be_correct_price(self):
        assert self.browser.find_element_by_css_selector("#messages>.alert:nth-child(3) strong").text == \
               self.browser.find_element_by_css_selector(".product_main .price_color").text, "Wrong price!"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_button.click()
        # self.solve_quiz_and_get_code()
