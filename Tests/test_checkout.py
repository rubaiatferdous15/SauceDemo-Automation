from playwright.sync_api import Page, expect
from Pages.checkoutPage import CheckoutPage
from Pages.Login import SauceDemoLoginPage
from Pages.productPage import ProductPage

def test_checkout_flow(page: Page, login_credentials, checkout_info, product_names):
    # Login
    login = SauceDemoLoginPage(page)
    login.navigate_to_login_page()
    login.login(**login_credentials)

    # Add products
    product_page = ProductPage(page)
    for product in product_names:
        product_page.add_product_by_name(product)

    # Checkout
    checkout = CheckoutPage(page)
    checkout.complete_checkout(**checkout_info)

    # ✅ Assertion – order success banner is visible
    expect(page.locator("h2[data-test='complete-header']")).to_have_text("Thank you for your order!")

