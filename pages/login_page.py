"""
Login Page Object for CURA Healthcare Service
"""
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "id=txt-username"
    PASSWORD_INPUT = "id=txt-password"
    LOGIN_BTN = "id=btn-login"

    def is_username_field_visible(self) -> bool:
        """Check if Username field is visible"""
        return self.is_visible(self.USERNAME_INPUT)

    def is_password_field_visible(self) -> bool:
        """Check if Password field is visible"""
        return self.is_visible(self.PASSWORD_INPUT)

    def is_login_button_visible(self) -> bool:
        """Check if Login button is visible"""
        return self.is_visible(self.LOGIN_BTN)

    def enter_username(self, username: str):
        """Enter username"""
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """Enter password"""
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click Login button"""
        self.click(self.LOGIN_BTN)
        self.wait_for_load_state()
