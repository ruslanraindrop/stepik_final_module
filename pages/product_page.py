from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def should_be_correct_product_added(self):
        self.should_be_correct_message()
        self.should_be_correct_price()

    def should_be_correct_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_message = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE).text
        print(f"product_name={product_name}, added_name={added_product_message}")
        assert product_name == added_product_message, \
            f"This message is wrong: added {product_name}, not a {added_product_message}"

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        print(f"product_price={product_price}, added_price={added_product_price}")
        assert product_price == added_product_price, \
            f"This price is wrong: added product for a price {product_price}, not a {added_product_price}"
