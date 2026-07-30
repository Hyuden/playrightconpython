from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.titulo_pagina = page.get_by_text("Products")
        self.filtro_orden = page.locator("[data-test='product-sort-container']")
        self.primer_boton_agregar = page.get_by_role(
            "button", name="Add to cart"
        ).first
        self.insignia_carrito = page.locator(".shopping_cart_badge")

    # Acciones
    def ordenar_por_precio_menor_a_mayor(self):
        self.filtro_orden.select_option("lohi")

    def agregar_primer_producto(self):
        self.primer_boton_agregar.click()