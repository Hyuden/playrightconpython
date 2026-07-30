import allure
import pytest
from playwright.sync_api import Page, expect


@allure.epic("Plataforma Retail E-Commerce")
@allure.feature("Módulo de Checkout y Compras")
@allure.story("Flujo End-to-End exitoso de compra con ordenamiento de catálogo")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Este test verifica el flujo transaccional completo de un cliente: autenticación, "
    "ordenamiento de productos por menor precio, adición al carrito, llenado de datos "
    "de despacho y validación del mensaje final de confirmación."
)
def test_flujo_compra_retail_allure(page: Page):

    with allure.step("1. Navegar a la tienda e iniciar sesión"):
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Validación de ingreso exitoso a la pantalla de productos
        expect(page.get_by_text("Products")).to_be_visible()

    with allure.step(
        "2. Aplicar filtro de catálogo por precio (Menor a Mayor)"
    ):
        page.locator("[data-test='product-sort-container']").select_option(
            "lohi"
        )

    with allure.step("3. Seleccionar el primer producto y agregarlo al carrito"):
        page.get_by_role("button", name="Add to cart").first.click()

        # Validar que el contador del carrito se actualice a 1
        insignia_carrito = page.locator(".shopping_cart_badge")
        expect(insignia_carrito).to_have_text("1")

    with allure.step("4. Ir al carrito de compras y proceder al Checkout"):
        page.locator(".shopping_cart_link").click()
        expect(page.get_by_text("Your Cart")).to_be_visible()
        page.get_by_role("button", name="Checkout").click()

    with allure.step("5. Completar el formulario de despacho del cliente"):
        page.get_by_placeholder("First Name").fill("Christian")
        page.get_by_placeholder("Last Name").fill("QA")
        page.get_by_placeholder("Zip/Postal Code").fill("8320000")
        page.get_by_role("button", name="Continue").click()

    with allure.step("6. Revisar la pantalla de resumen (Overview) y finalizar"):
        expect(page.get_by_text("Checkout: Overview")).to_be_visible()
        page.get_by_role("button", name="Finish").click()

    with allure.step("7. Validar la orden completada y adjuntar evidencia"):
        mensaje_exito = page.get_by_role(
            "heading", name="Thank you for your order!"
        )
        expect(mensaje_exito).to_be_visible()

        # Adjuntar captura de pantalla de confirmación directamente dentro del reporte Allure
        allure.attach(
            page.screenshot(full_page=True),
            name="Evidencia_Confirmacion_Orden",
            attachment_type=allure.attachment_type.PNG,
        )