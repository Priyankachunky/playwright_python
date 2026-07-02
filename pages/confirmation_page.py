"""
Confirmation Page Object for CURA Healthcare Service
"""
from pages.base_page import BasePage


class ConfirmationPage(BasePage):
    # Locators - Based on actual page structure
    CONFIRMATION_HEADING = "h2:has-text('Appointment Confirmation')"
    FACILITY_LABEL = "text=Facility"
    FACILITY_VALUE = "text=Tokyo CURA Healthcare Center"
    READMISSION_LABEL = "text=Apply for hospital readmission"
    READMISSION_VALUE = "text=Yes"
    HEALTHCARE_PROGRAM_LABEL = "text=Healthcare Program"
    HEALTHCARE_PROGRAM_VALUE = "text=Medicare"
    VISIT_DATE_LABEL = "text=Visit Date"
    VISIT_DATE_VALUE = "text=30/06/2026"
    COMMENT_LABEL = "text=Comment"
    COMMENT_VALUE = "text=Patient experiencing fever, headache and body pain for 3 days."

    def is_on_confirmation_page(self) -> bool:
        """Check if we're on the confirmation page by URL"""
        return "appointment.php" in self.page.url and "#summary" in self.page.url

    def verify_confirmation_heading(self):
        """Verify Appointment Confirmation heading"""
        # Look for the h2 with "Appointment Confirmation" text
        heading = self.page.locator("h2").first
        heading_text = heading.text_content()
        assert "Appointment Confirmation" in heading_text, \
            f"Expected 'Appointment Confirmation' heading, got: {heading_text}"
        return True

    def verify_facility_value(self, expected_facility: str) -> bool:
        """Verify Facility value"""
        page_content = self.page.content()
        return expected_facility in page_content and "Tokyo CURA" in page_content

    def verify_readmission_value(self, expected_value: str) -> bool:
        """Verify Hospital Readmission value"""
        page_content = self.page.content()
        return "readmission" in page_content.lower() and expected_value in page_content

    def verify_healthcare_program_value(self, expected_program: str) -> bool:
        """Verify Healthcare Program value"""
        page_content = self.page.content()
        return "Healthcare Program" in page_content and expected_program in page_content

    def verify_visit_date_value(self, expected_date: str) -> bool:
        """Verify Visit Date value"""
        page_content = self.page.content()
        return "Visit Date" in page_content and expected_date in page_content

    def verify_comment_value(self, expected_comment: str) -> bool:
        """Verify Comment value"""
        page_content = self.page.content()
        return expected_comment in page_content

    def verify_all_details(self, facility: str, readmission: str, program: str, date: str, comment: str) -> bool:
        """Verify all appointment details"""
        page_content = self.page.content()
        required_values = [facility, readmission, program, date, comment]
        
        for value in required_values:
            if value not in page_content:
                print(f"[DEBUG] Missing value in confirmation: {value}")
                return False
        return True
