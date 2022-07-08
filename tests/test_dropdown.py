import pytest
from framework.web_elements import WebPage
from framework.locators.common import Common
from framework.locators.dropdown import Dropdown


@pytest.mark.usefixtures("setup")
class TestDropdown:
    
    def test_select_element(self):
        # Testing selection of the elements from the dropdown
        
        browser = WebPage(self.driver)
        
        browser.page_is_opened(Dropdown.LINK)
        
        assert browser.element_is_present(*Dropdown.MAIN_HEADING)
        assert "Dropdown List" in browser.find_element(*Dropdown.MAIN_HEADING).text
        
        assert browser.element_is_present(*Dropdown.DROPDOWN)
        browser.click_on(*Dropdown.DROPDOWN)
        
        browser.select(*Dropdown.DROPDOWN, "Option 1")
        assert "Please select an option" in browser.find_element(*Dropdown.DISABLED).text
        # browser.select(*Dropdown.DISABLED, "Please select an option") #Disabled option is not selectable.