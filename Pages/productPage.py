from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    def add_product_by_name(self, product_name: str):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_card.locator("button:has-text('Add to cart')").click()

    def remove_product_by_name(self, product_name: str):
        product_card = self.page.locator(".inventory_item").filter(has_text=product_name)
        product_card.locator("button:has-text('Remove')").click()
