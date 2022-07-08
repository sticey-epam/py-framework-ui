import pytest
from framework.web_elements import WebPage
from framework.locators.add_remove import AddRemove
from framework.locators.common import Common


@pytest.mark.usefixtures("setup")
class TestAddRemove:
    
    def test_add_element(self):
        # Testing that the element is added when the button is clicked.
        
        browser = WebPage(self.driver)
        
        
        browser.page_is_opened(AddRemove.LINK)
        
        assert browser.element_is_present(*AddRemove.MAIN_HEADING)
    
        assert browser.element_is_present(*AddRemove.ADD_ELEMENT) and browser.element_is_clickable(*AddRemove.ADD_ELEMENT)
        assert browser.element_is_not_present(*AddRemove.added_element(1))
        
        browser.click_on(*AddRemove.ADD_ELEMENT)
        assert browser.element_is_present(*AddRemove.added_element(1))
        browser.click_on(*AddRemove.added_element(1))
        assert browser.element_is_not_present(*AddRemove.added_element(1))