import time

from selenium.webdriver import Keys

from data import data
from pages import urban_routes_page as urp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.helpers import retrieve_phone_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability(name="goog:loggingPrefs", value={'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort(self):
        #Hacer clic en el botón "Pedir taxi"
        self.routes_page.click_on_request_taxi_button()
        #Seleccionar la opción de tarifa "Comfort"
        self.routes_page.click_on_comfort_icon()
        #Verificar que el icono "Comfort" esté visible
        assert self.routes_page.get_comfort_icon().is_displayed()

    def test_fill_phone(self):
        phone_number = data.phone_number
        #Clic en la casilla para abrir el campo de teléfono
        self.routes_page.click_phone_area()
        #Escribir el número
        self.routes_page.set_phone(phone_number)
        self.routes_page.click_next_button()  #hacer clic en el botón "Siguiente"
        self.routes_page.set_phone_code(self.driver)  #código recibido y escribirlo en el campo del código
        time.sleep(1)
        self.routes_page.click_confirm_button()  # Hacer clic en el botón "Confirmar"
        assert self.routes_page.get_phone() == data.phone_number


    def test_add_credit_card(self):
        card_number = data.card_number
        card_code = data.card_code
        #Clic en la casilla "Metodo de pago"
        self.routes_page.click_payment_method_area()
        #hacer clic en el boton "Agregar tarjeta"
        self.routes_page.click_add_card_button()
        #Ingresar el número de tarjeta
        self.routes_page.set_card_number(card_number)
        # Escribir el código CVV y TAB
        self.routes_page.set_cvv(card_code)
        #Clic en el botón "Agregar"
        self.routes_page.click_link_button()
        self.routes_page.click_close_button()#Cerrar el modal
        #Validar la seleccion de la tarjeta
        checked_box = self.driver.find_element(*self.routes_page.checked_button)
        assert checked_box.is_selected()


    def test_set_driver_message(self):
        #obtiene mensaje desde el archivo data
        message = data.message_for_driver
        #escribe el mensaje
        self.routes_page.set_driver_message(message)
        #verifica que el texto se haya escrito
        assert self.routes_page.get_driver_message() == message

    def test_toggle_blanket_and_tissues_switch(self):
        self.routes_page.click_en_mantas_y_panuelos_option()
        assert self.routes_page.get_mantas_y_panuelos_option_checked() == True #verifica que fue seleccionada

    def test_order_two_ice_creams(self):
        self.routes_page.click_ice_cream_plus()  # clic para sumar uno
        self.routes_page.click_ice_cream_plus()  # clic para sumar otro
        quantity = self.routes_page.get_ice_cream_quantity()
        assert quantity == 2 #verifica que se agregaron los dos helados

    def test_modal_buscar_automovil(self):
        self.routes_page.click_order_taxi()
        assert self.routes_page.is_order_taxi_modal_visible()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()