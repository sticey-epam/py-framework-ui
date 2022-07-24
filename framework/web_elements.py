from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

from framework.utils import SeleniumBase


class WebPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def page_is_opened(self, link: str) -> str:
        return self.driver.get(link)

    def find_element(self, find_by: str, locator: str) -> WebElement:
        return self._SeleniumBase__find_if_visible(find_by, locator)

    def find_elements(self, find_by, locator) -> List[WebElement]:
        return self._SeleniumBase__find_are_visible(find_by, locator)

    def element_is_present(self, find_by: str, locator: str) -> WebElement:
        return self._SeleniumBase__find_if_present(find_by, locator)

    def element_is_not_present(self, find_by: str, locator: str) -> WebElement:
        return self._SeleniumBase__find_if_not_present(find_by, locator)

    def hover_over_element(self, element: WebElement) -> WebElement:
        return self._SeleniumBase__hover_cursor(element)

    def get_txt_of_navigation_links(self, links) -> str:
        """Return all nav links text. Return format is a String with comma separated values"""
        nav_links_text = self._SeleniumBase__get_text_from_webelements(links)
        return ",".join(nav_links_text)

    def scroll_to(self, width: int, height: int):
        """The function scrolls the page to the specified height"""
        return self._SeleniumBase__window_scroll_To(width, height)
    
    def element_is_clickable(self, find_by: str, locator: str) -> WebElement:
        return self._SeleniumBase__element_is_clickable(find_by, locator)
    
    def click_on(self, find_by: str, locator: str) -> WebElement:
        element = self._SeleniumBase__find_if_visible(find_by, locator)
        return element.click()
    
    def select(self, find_by: str, locator: str, value: str) -> WebElement:
        element = Select(self._SeleniumBase__find_if_visible(find_by, locator))
        return element.select_by_visible_text(value)
    
    def deselect(self, find_by: str, locator: str, value: str) -> WebElement:
        element = Select(self._SeleniumBase__find_if_visible(find_by, locator))
        return element.deselect_by_visible_text(value)
    
    def get_background_colour(self, find_by: str, locator: str):
        """Find the colour of an element to compare it."""
        element = self._SeleniumBase__find_if_visible(find_by, locator)
        rgb_colour = element.value_of_css_property('background-color')
        return Color.from_string(rgb_colour).hex

    
    
    
    
