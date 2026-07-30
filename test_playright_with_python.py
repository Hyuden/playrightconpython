from playwright.sync_api import Page, expect

def test_agregar_tarea(page: Page):
    # 1. Abrir la página
    page.goto("https://demo.playwright.dev/todomvc")

    # 2. Escribir una tarea y presionar Enter
    input_tarea = page.get_by_placeholder("What needs to be done?")
    input_tarea.fill("Aprender Playwright con Python")
    input_tarea.press("Enter")

    # 3. Validar que la tarea aparezca en la pantalla
    item = page.locator(".todo-list li")
    expect(item).to_have_text("Aprender Playwright con Python")