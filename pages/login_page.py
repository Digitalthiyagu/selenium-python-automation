class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_btn = "button[type='submit']"

    def login(self, username, password):
        self.driver.get("https://example.com/login")
        self.driver.find_element("css selector", self.username_input).send_keys(username)
        self.driver.find_element("css selector", self.password_input).send_keys(password)
        self.driver.find_element("css selector", self.login_btn).click()
