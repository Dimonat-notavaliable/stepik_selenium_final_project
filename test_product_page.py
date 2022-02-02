import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time

product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_page_link}/?promo=offer{number}" for number in range(10)]
urls[7] = pytest.param(f"{product_page_link}/?promo=offer7", marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_basket()
    page.should_be_correct_name()
    page.should_be_correct_price()
