from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )

        username_field.clear()
        username_field.send_keys(username)
    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
        login_button.click()


    def is_login_successful(self):
        WebDriverWait(self.driver, 10).until(
        EC.url_to_be("https://practicetestautomation.com/logged-in-successfully/")
    )
        return self.driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"


    
    def is_error_displayed(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        return error_message.is_displayed()
    
