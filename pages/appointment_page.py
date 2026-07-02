"""
Appointment Page Object for CURA Healthcare Service
"""
from pages.base_page import BasePage


class AppointmentPage(BasePage):
    # Locators
    FACILITY_DROPDOWN = "id=combo_facility"
    READMISSION_CHECKBOX = "id=chk_hospotal_readmission"
    HEALTHCARE_PROGRAM_MEDICARE = "input[value='Medicare']"
    VISIT_DATE_INPUT = "id=txt_visit_date"
    COMMENT_TEXTAREA = "id=txt_comment"
    BOOK_APPOINTMENT_BTN = "id=btn-book-appointment"

    def is_facility_dropdown_visible(self) -> bool:
        """Check if Facility dropdown is visible"""
        return self.is_visible(self.FACILITY_DROPDOWN)

    def is_healthcare_program_visible(self) -> bool:
        """Check if Healthcare Program options are visible"""
        # Check if any radio button for healthcare program is visible
        return self.is_visible("input[name='programs']") or self.is_visible(self.HEALTHCARE_PROGRAM_MEDICARE)

    def select_facility(self, facility: str):
        """Select facility from dropdown"""
        self.select_option(self.FACILITY_DROPDOWN, facility)

    def is_readmission_checkbox_visible(self) -> bool:
        """Check if Hospital Readmission checkbox is visible"""
        return self.is_visible(self.READMISSION_CHECKBOX)

    def check_readmission(self):
        """Check Hospital Readmission checkbox"""
        self.check(self.READMISSION_CHECKBOX)

    def is_readmission_checked(self) -> bool:
        """Check if Hospital Readmission is checked"""
        return self.is_checked(self.READMISSION_CHECKBOX)

    def select_healthcare_program(self, program: str):
        """Select Healthcare Program"""
        self.page.check(f"input[value='{program}']")

    def is_healthcare_program_selected(self, program: str) -> bool:
        """Check if Healthcare Program is selected"""
        return self.page.is_checked(f"input[value='{program}']")

    def enter_visit_date(self, date: str):
        """Enter visit date (format: dd/mm/yyyy)"""
        self.fill(self.VISIT_DATE_INPUT, date)
        # Wait for calendar to appear
        self.page.wait_for_timeout(500)
        # Click on the date in the calendar (e.g., "30" for 30/06/2026)
        day = date.split('/')[0].lstrip('0')  # Remove leading zero
        try:
            # Try to find and click the calendar date
            date_cell = self.page.locator(f"td:has-text('{day}')")
            if date_cell.count() > 0:
                date_cell.first.click()
        except:
            # If calendar click fails, just proceed - the field might be filled
            pass

    def is_visit_date_filled(self, expected_date: str) -> bool:
        """Check if visit date is filled correctly"""
        return self.page.input_value(self.VISIT_DATE_INPUT) == expected_date

    def enter_comment(self, comment: str):
        """Enter comment"""
        self.fill(self.COMMENT_TEXTAREA, comment)

    def is_comment_filled(self, expected_comment: str) -> bool:
        """Check if comment is filled correctly"""
        return self.page.input_value(self.COMMENT_TEXTAREA) == expected_comment

    def click_book_appointment(self):
        """Click Book Appointment button"""
        # Ensure the button is visible and clickable
        self.page.wait_for_selector(self.BOOK_APPOINTMENT_BTN, state="visible", timeout=10000)
        self.page.wait_for_timeout(500)  # Brief pause to ensure page is ready
        
        # Get button element
        button = self.page.locator(self.BOOK_APPOINTMENT_BTN)
        button.scroll_into_view_if_needed()
        
        # Click with force to ensure it works
        button.click(force=True)
        
        # Wait a bit for the page to process
        self.page.wait_for_timeout(2000)
        
        # Check if we're on confirmation page by checking page content
        page_content = self.page.content()
        max_attempts = 5
        attempts = 0
        
        while "Appointment Confirmation" not in page_content and attempts < max_attempts:
            self.page.wait_for_timeout(2000)
            page_content = self.page.content()
            attempts += 1
        
        if "Appointment Confirmation" not in page_content:
            # Log debug info
            print(f"[DEBUG] Current URL: {self.page.url}")
            print(f"[DEBUG] Page title: {self.page.title()}")
            raise Exception("Confirmation page not reached after clicking Book Appointment")
