from playwright.sync_api import Page

class SauceDemoLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator('[data-test="username"]')
        self.password_field = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.page.set_default_timeout(60000)

    def navigate_to_login_page(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
