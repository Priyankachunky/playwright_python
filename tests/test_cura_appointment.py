"""
CURA Healthcare Service - End-to-End Test
Single test executed across three concurrent Chrome browser instances.
"""

from playwright.sync_api import sync_playwright

from config.settings import BASE_URL, DEFAULT_TIMEOUT, HEADLESS
from pages.appointment_page import AppointmentPage
from pages.confirmation_page import ConfirmationPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


def run_browser_flow(browser_index: int) -> bool:
    """Run the appointment workflow on a single browser page."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        context = browser.new_context(base_url=BASE_URL, ignore_https_errors=True)
        page = context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        page.set_default_navigation_timeout(DEFAULT_TIMEOUT)

        home_page = HomePage(page)
        login_page = LoginPage(page)
        appointment_page = AppointmentPage(page)
        confirmation_page = ConfirmationPage(page)

        home_page.navigate(BASE_URL)
        home_page.wait_for_load_state()
        print(f"[Browser {browser_index}] Navigated to {BASE_URL}")

        home_page.verify_page_title()
        print(f"[Browser {browser_index}] Page title verified")

        assert home_page.is_make_appointment_button_visible(), "Make Appointment button not visible"
        home_page.click_make_appointment()
        print(f"[Browser {browser_index}] Clicked Make Appointment")

        assert login_page.is_username_field_visible(), "Username field not visible"
        assert login_page.is_password_field_visible(), "Password field not visible"
        assert login_page.is_login_button_visible(), "Login button not visible"
        login_page.enter_username("John Doe")
        login_page.enter_password("ThisIsNotAPassword")
        login_page.click_login()
        print(f"[Browser {browser_index}] Logged in")

        appointment_page.wait_for_selector(appointment_page.FACILITY_DROPDOWN, timeout=10000)
        assert appointment_page.is_facility_dropdown_visible(), "Facility dropdown not visible"
        assert appointment_page.is_healthcare_program_visible(), "Healthcare Program options not visible"
        appointment_page.select_facility("Tokyo CURA Healthcare Center")
        page.wait_for_timeout(500)
        appointment_page.check_readmission()
        assert appointment_page.is_readmission_checked(), "Hospital Readmission checkbox not checked"
        appointment_page.select_healthcare_program("Medicare")
        assert appointment_page.is_healthcare_program_selected("Medicare"), "Medicare option not selected"
        appointment_page.enter_visit_date("30/06/2026")
        assert appointment_page.is_visit_date_filled("30/06/2026"), "Visit date not filled correctly"
        comment_text = "Patient experiencing fever, headache and body pain for 3 days."
        appointment_page.enter_comment(comment_text)
        assert appointment_page.is_comment_filled(comment_text), "Comment not filled correctly"
        appointment_page.click_book_appointment()
        print(f"[Browser {browser_index}] Book Appointment clicked")

        page.wait_for_url("**/appointment.php*", timeout=15000)
        confirmation_page.verify_confirmation_heading()
        assert confirmation_page.verify_facility_value("Tokyo CURA Healthcare Center"), "Facility value mismatch"
        assert confirmation_page.verify_readmission_value("Yes"), "Hospital Readmission value mismatch"
        assert confirmation_page.verify_healthcare_program_value("Medicare"), "Healthcare Program value mismatch"
        assert confirmation_page.verify_visit_date_value("30/06/2026"), "Visit Date value mismatch"
        assert confirmation_page.verify_comment_value(comment_text), "Comment value mismatch"
        assert confirmation_page.verify_all_details(
            facility="Tokyo CURA Healthcare Center",
            readmission="Yes",
            program="Medicare",
            date="30/06/2026",
            comment=comment_text,
        ), "Not all appointment details match"
        print(f"[Browser {browser_index}] Confirmation verified")

        home_page.open_navigation_menu()
        assert home_page.is_home_menu_visible(), "Home menu option not visible"
        assert home_page.is_history_menu_visible(), "History menu option not visible"
        assert home_page.is_profile_menu_visible(), "Profile menu option not visible"
        assert home_page.is_logout_menu_visible(), "Logout menu option not visible"
        home_page.click_logout_menu()
        home_page.wait_for_load_state()
        assert home_page.is_make_appointment_button_visible(), "Make Appointment button not visible after logout"
        home_page.verify_page_title()
        print(f"[Browser {browser_index}] Logout completed")

        page.close()
        context.close()
        browser.close()

        return True


class TestCURAAppointment:
    """Test class for CURA appointment booking workflow"""

    def test_complete_appointment_workflow(self):
        """Single test case executed on one Chrome browser."""
        assert run_browser_flow(1), "Single test case failed on the browser"
        print("\nSingle test case completed successfully on a single Chrome browser.")
