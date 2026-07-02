"""
Home Page Object for CURA Healthcare Service
"""
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    MAKE_APPOINTMENT_BTN = "id=btn-make-appointment"
    MENU_BUTTON = "a[href='#']"  # The hamburger menu link
    HOME_MENU = "a:has-text('Home')"
    HISTORY_MENU = "a:has-text('History')"
    PROFILE_MENU = "a:has-text('Profile')"
    LOGOUT_MENU = "a:has-text('Logout')"

    def verify_page_title(self):
        """Verify page title contains CURA Healthcare Service"""
        title = self.get_title()
        assert "CURA Healthcare Service" in title, f"Expected 'CURA Healthcare Service' in title, got: {title}"
        return True

    def is_make_appointment_button_visible(self) -> bool:
        """Check if Make Appointment button is visible"""
        return self.is_visible(self.MAKE_APPOINTMENT_BTN)

    def click_make_appointment(self):
        """Click on Make Appointment button"""
        self.click(self.MAKE_APPOINTMENT_BTN)

    def open_navigation_menu(self):
        """Open the navigation menu"""
        # Try to find and click the navbar toggle button
        try:
            # First, check if menu items are already visible
            if self.page.is_visible("a:has-text('Logout')"):
                # Menu is already visible, no need to click toggle
                self.page.wait_for_timeout(300)
                return
        except:
            pass
        
        # Try various selectors for the toggle button
        toggle_selectors = [
            "button.navbar-toggle",
            "a[href='#']:first-child",
            ".navbar-toggle",
            "[aria-label*='menu']"
        ]
        
        for selector in toggle_selectors:
            try:
                if self.page.is_visible(selector):
                    self.click(selector)
                    self.page.wait_for_timeout(500)  # Wait for menu animation
                    return
            except:
                continue
        
        # If we reach here, menu items might already be visible
        self.page.wait_for_timeout(300)

    def is_home_menu_visible(self) -> bool:
        """Check if Home menu option is visible"""
        return self.is_visible("a:has-text('Home')")

    def is_history_menu_visible(self) -> bool:
        """Check if History menu option is visible"""
        return self.is_visible("a:has-text('History')")

    def is_profile_menu_visible(self) -> bool:
        """Check if Profile menu option is visible"""
        return self.is_visible("a:has-text('Profile')")

    def is_logout_menu_visible(self) -> bool:
        """Check if Logout menu option is visible"""
        return self.is_visible("a:has-text('Logout')")

    def click_logout_menu(self):
        """Click on Logout menu option"""
        # Use JavaScript to click the logout link to bypass pointer event issues
        self.page.evaluate("document.querySelector('a[href*=logout]').click()")
        # Wait for redirect to home page (URL will be just the domain or /index.php)
        self.page.wait_for_url("**/", timeout=15000)
        self.wait_for_load_state()
