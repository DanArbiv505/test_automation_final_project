from selenium.webdriver.common.by import By

slider_barr = (By.XPATH, "//h2[text()='Filter by Price']")
slider_bar_left = (By.XPATH, "//span[contains(@class,'ui-slider-handle')][1]")
slider_bar_right = (By.XPATH, "//span[contains(@class,'ui-slider-handle')][2]")
slider_bar = (By.XPATH, "//div[contains(@class,'ui-slider-range')]")
min_price_after_slider = (By.XPATH, "//span[@class='from']")
max_price_after_slider = (By.XPATH, "//span[@class='to']")

accessories = (By.XPATH, "//ul[@class='product-categories']/li[1]/a")
men = (By.XPATH, "//ul[@class='product-categories']/li[2]/a")
women = (By.XPATH, "//ul[@class='product-categories']/li[3]/a")
order_by_dropdown = (By.CSS_SELECTOR, ".orderby")
page_numbers = (By.XPATH, "//ul[@class='page-numbers']/li")
product_list = (By.XPATH, "//ul[@class='products columns-4']/li")
product_list_names = (By.XPATH, "//ul[@class='products columns-4']/li/div[2]/a/h2")
products_list_rating_in_page = (By.XPATH, "//ul[@class='products columns-4']/li/div[2]/div")
search_field = (By.ID, "wc-block-search__input-1")
search_button = (By.CSS_SELECTOR, "button[aria-label='Search']")
view_cart = (By.CSS_SELECTOR, "a[class='cart-container']")
view_cart_button = (By.XPATH, "//div[@id='ast-site-header-cart']/div[2]/div/div/p[2]/a[1]")



class MainStorePage:



    def __init__(self, driver):
        self.driver = driver

    # elements related to slider

    def slider_bar_txt(self):
        return self.driver.find_element(slider_barr[0], slider_barr[1])

    def slider_bar_action(self):
        return self.driver.find_element(slider_bar[0],slider_bar[1])

    def slider_bar_action_left(self):
        return self.driver.find_element(slider_bar_left[0],slider_bar_left[1])

    def slider_bar_action_right(self):
        return self.driver.find_element(slider_bar_right[0],slider_bar_right[1])

    def min_price_txt(self):
        return self.driver.find_element(min_price_after_slider[0], min_price_after_slider[1])

    def max_price_txt(self):
        return self.driver.find_element(max_price_after_slider[0], max_price_after_slider[1])

    # elements related to categories

    def get_left_accessories(self):
        return self.driver.find_element(accessories[0], accessories[1])

    def get_left_men(self):
        return self.driver.find_element(men[0], men[1])

    def get_left_women(self):
        return self.driver.find_element(women[0], women[1])

    def get_order_by_dropdown(self):
        return self.driver.find_element(order_by_dropdown[0], order_by_dropdown[1])

    def get_pages_numbers(self):
        return self.driver.find_elements(page_numbers[0], page_numbers[1])

    def get_products_list_rating_in_page(self):
        return self.driver.find_elements(products_list_rating_in_page[0], products_list_rating_in_page[1])

    def get_products_list(self):
        return self.driver.find_elements(product_list[0], product_list[1])

    def get_products_list_names(self):
        return self.driver.find_elements(product_list_names[0], product_list_names[1])

    def get_search_field(self):
        return self.driver.find_element(search_field[0],search_field[1])

    def get_search_button(self):
        return self.driver.find_element(search_button[0], search_button[1])

    def get_view_cart(self):
        return self.driver.find_element(view_cart[0], view_cart[1])

    def get_view_cart_button(self):
        return self.driver.find_element(view_cart_button[0], view_cart_button[1])