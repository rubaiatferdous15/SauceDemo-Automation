from playwright.sync_api import Page, expect
from Pages.Login import SauceDemoLoginPage

def test_login_valid_credentials(page: Page, login_credentials):
    login_page = SauceDemoLoginPage(page)
    login_page.navigate_to_login_page()
    login_page.login(
        username=login_credentials["username"],
        password=login_credentials["password"]
    )

  
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
  


