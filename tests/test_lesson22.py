import time

import pytest
from selenium.webdriver.common import actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from framework.web_elements import WebPage


@pytest.mark.usefixtures("setup")
class TestPages:

    def test_demo_guru99(self):

        browser = WebPage(self.driver)
        browser.page_is_opened("https://demo.guru99.com/test/newtours/register.php")

        registration_txt = browser.find_element("xpath", "//p//font[@face='Arial, Helvetica, sans-serif'][@size='2']")
        assert (
            "To create your account, we'll need some basic information about you. This information will be used to send reservation confirmation emails, mail tickets when needed and contact you if your travel arrangements change. Please fill in the form completely."
            in registration_txt.text
        )

        first_name = browser.find_element("xpath", "//input[@name='firstName']")
        first_name.send_keys("Dale")
        assert "Dale" in first_name.get_attribute("value")

        last_name = browser.find_element("xpath", "//input[@name='lastName']")
        last_name.send_keys("Cooper")
        assert "Cooper" in last_name.get_attribute("value")

        phone = browser.find_element("xpath", "//input[@name='phone']")
        phone.send_keys("+995599804331")

        email = browser.find_element("xpath", "//input[@name='userName']")
        email.send_keys("duck@duck.com")

        address = browser.find_element("xpath", "//input[@name='address1']")
        address.send_keys("Brest, Masherova avenue 94")

        city = browser.find_element("xpath", "//input[@name='city']")
        city.send_keys("Brest")

        state = browser.find_element("xpath", "//input[@name='state']")
        state.send_keys("Brest")

        postal_code = browser.find_element("xpath", "//input[@name='postalCode']")
        postal_code.send_keys("225903")

        country_dropdown = Select(browser.find_element("xpath", "//select[@name='country']"))
        country_dropdown.select_by_value("BELARUS")

        user_name = browser.find_element("xpath", "//input[@id='email']")
        user_name.send_keys("NewUser")
        assert "NewUser" in user_name.get_attribute("value")

        password = browser.find_element("xpath", "//input[@name='password']")
        password.send_keys("87654321")
        assert "87654321" in password.get_attribute("value")

        confirm_password = browser.find_element("xpath", "//input[@name='confirmPassword']")
        confirm_password.send_keys("87654321")

        submit_button = browser.find_element("xpath", "//input[@type='submit']")
        submit_button.click()

    def test_herokuapp(self):
        browser = WebPage(self.driver)
        browser.page_is_opened("https://the-internet.herokuapp.com")
        
        hovers_link = browser.find_element("xpath", '//a[@href="/hovers"]')
        hovers_link.click()

        hovers_title = browser.find_element("xpath", "//div[@class='example']/h3")
        assert "Hovers" in hovers_title.text

        first_img = browser.find_element("xpath", "//div[@class='figure'][1]/img")
        first_img.is_displayed()
        time.sleep(2)

        browser.hover_over_element(first_img)

        time.sleep(1)
        first_img_caption = browser.element_is_present("xpath", "//h5[text()='name: user1']")
        assert "name: user1" in first_img_caption.text

       
