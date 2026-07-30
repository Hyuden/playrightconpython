import allure
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect


@allure.epic("Plataforma Retail E-Commerce")
@allure.feature("Arquitectura POM")
def test_compra_con_pom(page: Page):

    # Instanciamos nuestras páginas
    login_pg = LoginPage(page)
    inventory_pg = InventoryPage(page)

    with allure.step("1. Iniciar sesión en la tienda"):
        login_pg.navegar()
        login_pg.iniciar_sesion("standard_user", "secret_sauce")

        # Validación en la prueba
        expect(inventory_pg.titulo_pagina).to_be_visible()

    with allure.step("2. Filtrar por menor precio y agregar producto"):
        inventory_pg.ordenar_por_precio_menor_a_mayor()
        inventory_pg.agregar_primer_producto()

        # Validación en la prueba
        expect(inventory_pg.insignia_carrito).to_have_text("1")