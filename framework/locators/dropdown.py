from selenium.webdriver.common.by import By

class Dropdown:
    
    LINK = "https://the-internet.herokuapp.com/dropdown"
    MAIN_HEADING = (By.XPATH, "//div[@class='example']/h3")
    
    DROPDOWN = (By.XPATH, "//select[@id='dropdown']")
    
    DISABLED = (By.XPATH, "//*[@id='dropdown']/option[1]")
    OPTION1 = (By.XPATH, "//option[@value='1']")
    OPTION2 = (By.XPATH, "//option[@value='2']")
    