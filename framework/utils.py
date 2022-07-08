from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait



class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.5)
        self.actions = webdriver.ActionChains(driver)
        
    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            "css": By.CSS_SELECTOR,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "id": By.ID,
            "link_text": By.LINK_TEXT,
            "name": By.NAME,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "tag_name": By.TAG_NAME,
        }
        return locating[find_by]

    def __find_if_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(
            ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def __find_if_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM"""
        return self.__wait.until(
            ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def __find_if_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Wait on element until it disappears"""
        return self.__wait.until(
            ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def __find_are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible"""
        return self.__wait.until(
            ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def __are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM"""
        return self.__wait.until(
            ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name
        )

    def __get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        """The input should be a list of WebElements, where we read text from each element and Return a List[String]"""
        return [element.text for element in elements]

    def __get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        """The input should we a list of WebElements, from which we return a single WebElement found by it's name"""
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def __hover_cursor(self, element: WebElement) -> WebElement:
        """This method moves the mouse to the middle of the element. The element is also scrolled into the view on performing this action."""
        return self.actions.move_to_element(element).perform()

    def __window_scroll_To(self, width: int, height: int):
        """The function scrolls the page to the specified height"""
        return self.driver.execute_script(f"window.scrollTo({width}, {height})")

    def __delete_cookie(self, cookie_name: str) -> None:
        '''Delete a cookie by a name.'''
        self.driver.delete_cookie(cookie_name)
        
    def __element_is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        """Check if the element from provided location is clickable."""
        return self.__wait.until(
            ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name
            )
        