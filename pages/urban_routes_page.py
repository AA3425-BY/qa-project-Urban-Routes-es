import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils import helpers



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR,'.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_click_area = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//button[contains(@class, "button") and contains(text(), "Siguiente")]')
    phone_code_field =(By.ID, 'code')
    confirm_button = (By.XPATH, '//button[@type="submit" and contains(text(), "Confirmar")]')
    payment_method_area =(By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    add_card_button =(By.CSS_SELECTOR, 'img.pp-plus')
    card_number_field =(By.ID, 'number')
    cvv_field = (By.NAME, 'code')
    link_button =(By.XPATH, '//button[@type="submit" and contains(text(), "Agregar")]')
    close_button= (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    checked_button= (By.ID, 'card-1')
    driver_message_field =(By.ID, "comment")
    switches_locator = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CSS_SELECTOR, '.switch input')
    overlay_locator = (By.CLASS_NAME, 'overlay')
    ice_cream_plus_button = (By.CSS_SELECTOR, "div.counter-plus")  # botón '+'
    ice_cream_quantity = (By.CSS_SELECTOR, "div.counter-value")

    order_taxi_button =(By.CLASS_NAME,'smart-button')
    order_taxi_modal =(By.XPATH, '//div[@class="order-header-title" and contains(text(), "Buscar automóvil")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)
    #2
    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_icon))

    def click_on_comfort_icon(self):
        self.get_comfort_icon().click()
   #3
    def click_phone_area(self):
        self.wait.until(EC.element_to_be_clickable(self.phone_click_area)).click()

    def set_phone(self, phone_number):
        self.wait.until(EC.presence_of_element_located(self.phone_field)).send_keys(phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()

    def get_phone_code_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_code_field))

    def set_phone_code(self, driver):
        code = helpers.retrieve_phone_code(driver)
        self.get_phone_code_field().send_keys(code)

    def click_confirm_button(self):
        self.wait.until(EC.element_to_be_clickable(self.confirm_button)).click()



    #4
    def click_payment_method_area(self):
        self.wait.until(EC.element_to_be_clickable(self.payment_method_area)).click()

    def click_add_card_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_card_button)).click()


    def set_card_number(self, card_number):
        self.wait.until(EC.presence_of_element_located(self.card_number_field)).send_keys(card_number)

    def click_card_number_field(self):
        self.wait.until(EC.element_to_be_clickable(self.card_number_field)).click()

    def set_cvv(self, card_code):
        cvv = self.wait.until(EC.visibility_of_element_located(self.cvv_field))
        cvv.click()
        cvv.send_keys(card_code)
        cvv.send_keys(Keys.TAB)

    def click_link_button(self):
        self.wait.until(EC.visibility_of_element_located(self.link_button)).click()

    def click_close_button(self):
        close_button = self.wait.until(EC.element_to_be_clickable(self.close_button))
        close_button.click()


    #5
    def set_driver_message(self, message):
        field = self.wait.until(EC.presence_of_element_located(self.driver_message_field))
        field.send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.driver_message_field).get_attribute('value')


    #6
    def click_en_mantas_y_panuelos_option(self):
        self.wait.until(EC.invisibility_of_element_located(self.overlay_locator))
        switches = self.wait.until(EC.presence_of_all_elements_located(self.switches_locator))
        switches[0].click()

    def get_mantas_y_panuelos_option_checked(self):
       inputs = self.wait.until(EC.presence_of_all_elements_located(self.option_switches_inputs))
       return inputs[0].is_selected()

    #7
    def click_ice_cream_plus(self):
        plus_button = self.wait.until(EC.element_to_be_clickable(self.ice_cream_plus_button))
        plus_button.click()

    def get_ice_cream_quantity(self):
        quantity_element = self.wait.until(EC.visibility_of_element_located(self.ice_cream_quantity))
        return int(quantity_element.text)

    #8
    def click_order_taxi(self):
        boton = self.wait.until(EC.element_to_be_clickable(self.order_taxi_button))
        boton.click()

    def is_order_taxi_modal_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.order_taxi_modal)).is_displayed()