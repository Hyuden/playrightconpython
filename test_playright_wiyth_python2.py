from playwright.sync_api import Page, expect

def test_agregar_tarea(page: Page):
    # 1. Abrir la página
    page.goto("https://www.qa-practice.com/elements/input/simple")
    # 2. buscar un boton 
    boton_inputs = page.get_by_role("button", name="inputs").click
    # 3. luego ingresar un texto.
    page.get_by_placeholder("Submit Me").fill("Hola Mundo")
    # 4. presioanr boton requeriments
    boton_requirements = page.get_by_text("Requirements:").click()   
