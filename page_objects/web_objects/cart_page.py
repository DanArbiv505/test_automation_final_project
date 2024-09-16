from selenium.webdriver.common.by import By

total_list = (By.XPATH, "//table/tbody/tr/td[6]")
sub_total_price = (By.CSS_SELECTOR, ".cart-subtotal>td>span>bdi")
free_shipping = (By.XPATH, "//ul[@id='shipping_method']/li[1]")
local_pickup = (By.XPATH, "//ul[@id='shipping_method']/li[2]")
delivery_express = (By.XPATH, "//ul[@id='shipping_method']/li[3]")
registered_mail = (By.XPATH, "//ul[@id='shipping_method']/li[4]")
total = (By.XPATH, "//td[@data-title='Total']/strong/span/bdi")
item_in_cart = (By.XPATH, "//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']/tbody/tr")
quantity_of_item_in_cart = (By.XPATH, "//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']/tbody/tr/td[5]/div/input")
remove_item_button = (By.XPATH, "//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']/tbody/tr/td[1]/a")
names_of_item_in_cart = (By.XPATH, "//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']/tbody/tr/td[3]")
price_of_single_item_in_cart = (By.XPATH, "//table[@class='shop_table shop_table_responsive cart woocommerce-cart-form__contents']/tbody/tr/td[4]")
update_carte = (By.NAME, "update_cart")
alert = (By.XPATH, "//div[@role='alert']")

class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_total_list(self):
        return self.driver.find_elements(total_list[0], total_list[1])

    def get_sub_total_price(self):
        return self.driver.find_element(sub_total_price[0], sub_total_price[1])

    def get_free_shipping(self):
        return self.driver.find_element(free_shipping[0], free_shipping[1])

    def get_local_pickup(self):
        return self.driver.find_element(local_pickup[0], local_pickup[1])

    def get_delivery_express(self):
        return self.driver.find_element(delivery_express[0], delivery_express[1])

    def get_registered_mail(self):
        return self.driver.find_element(registered_mail[0], registered_mail[1])

    def get_total(self):
        return self.driver.find_element(total[0], total[1])

    def get_item_in_cart(self):
        return self.driver.find_elements(item_in_cart[0], item_in_cart[1])

    def get_quantity_of_item_in_cart(self):
        return self.driver.find_elements(quantity_of_item_in_cart[0], quantity_of_item_in_cart[1])

    def get_names_of_item_in_cart(self):
        return self.driver.find_elements(names_of_item_in_cart[0], names_of_item_in_cart[1])

    def get_update_carte(self):
        return self.driver.find_element(update_carte[0], update_carte[1])

    def get_alert(self):
        return self.driver.find_element(alert[0], alert[1])

    def get_remove_item_button(self):
        return self.driver.find_elements(remove_item_button[0], remove_item_button[1])

    def get_price_of_single_item_in_cart(self):
        return self.driver.find_elements(price_of_single_item_in_cart[0], price_of_single_item_in_cart[1])