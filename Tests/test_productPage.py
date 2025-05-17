from playwright.sync_api import Page, expect
from Pages.Login import SauceDemoLoginPage
from Pages.productPage import ProductPage

def test_add_and_remove_products(page: Page, login_credentials, product_names):
    login_page = SauceDemoLoginPage(page)
    product_page = ProductPage(page)

    # Navigate & Login
    login_page.navigate_to_login_page()
    login_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"]
    )

    # Add all products
    for product in product_names:
        product_page.add_product_by_name(product)
    
    
    expect(page.locator("[data-test='shopping-cart-badge']")).to_have_text(str(len(product_names)))


    # Remove all products
    for product in product_names:
        product_page.remove_product_by_name(product)
    
    
    expect(page.locator("[data-test='shopping-cart-badge']")).not_to_be_attached()


  
        


