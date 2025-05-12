from pages.login_page import LoginPage
from utils.browser_setup import setup_browser

def test_valid_login():
    driver = setup_browser()
    login = LoginPage(driver)
    login.login("user@example.com", "password123")
    assert "Dashboard" in driver.title
    driver.quit()
