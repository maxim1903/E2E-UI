import sys
import os
import pytest
from selenium import webdriver
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_purchase_flow(driver):
    driver.get("https://www.saucedemo.com/")
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    product_page = ProductPage(driver)
    product_page.add_product_to_cart()
    product_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_information("Maxim", "Dashkevich", "12345")
    checkout_page.finish_checkout()

    checkout_complete_page = CheckoutCompletePage(driver)
    assert checkout_complete_page.verify_order_complete(), "Order completion failed"
