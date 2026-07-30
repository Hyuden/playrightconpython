from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        # 1. Definimos los elementos (Locators)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    # 2. Definimos las acciones
    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def iniciar_sesion(self, usuario: str, clave: str):
        self.username_input.fill(usuario)
        self.password_input.fill(clave)
        self.login_button.click()