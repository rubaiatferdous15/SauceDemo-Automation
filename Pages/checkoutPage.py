from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link      = page.locator("[data-test='shopping-cart-link']")
        self.checkout_btn   = page.locator("[data-test='checkout']")
        self.first_name_inp = page.locator("[data-test='firstName']")
        self.last_name_inp  = page.locator("[data-test='lastName']")
        self.postal_inp     = page.locator("[data-test='postalCode']")
        self.continue_btn   = page.locator("[data-test='continue']")
        self.finish_btn     = page.locator("[data-test='finish']")

    def complete_checkout(self, first_name, last_name, postal_code):
        self.cart_link.click()
        self.checkout_btn.click()

        self.first_name_inp.fill(first_name)
        self.last_name_inp.fill(last_name)
        self.postal_inp.fill(postal_code)
        self.continue_btn.click()

        # ⬇️ Finish order
        self.finish_btn.click()

