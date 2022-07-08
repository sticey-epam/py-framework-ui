import pytest
from framework.web_elements import WebPage
from framework.locators.main_page import MainPageLocators
from framework.locators.common import Common

@pytest.mark.usefixtures("setup")
class TestMainPage:

    def test_main_page(self):
        # Testing the presence of elements on the pagef
        
        browser = WebPage(self.driver)
        
        browser.page_is_opened(MainPageLocators.LINK)

        assert "Welcome to the-internet" in browser.find_element(*MainPageLocators.MAIN_HEADING).text
        assert "Available Examples" in browser.find_element(*MainPageLocators.SECOND_HEADING).text
        assert len(browser.find_elements(*MainPageLocators.LIST_OF_ALL_ELEMENTS)) != 0
        assert browser.element_is_clickable(*Common.FORK_ME_ON_GITHUB_IMAGE)
