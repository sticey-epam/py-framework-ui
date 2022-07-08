from selenium.webdriver.common.by import By

class AddRemove:
    
    LINK = "https://the-internet.herokuapp.com/add_remove_elements/"
    MAIN_HEADING = (By.XPATH, "//div[@id='content']/h3")
    ADD_ELEMENT = (By.XPATH, "//div[@class='example']/button")
    FOOTER = (By.XPATH, "//div[@class='large-4 large-centered columns']/div")
    
    def added_element(number):
        ADDED_ELEMENT = (By.XPATH, f"//button[@class='added-manually'][{number}]")
        return ADDED_ELEMENT
    
   
        
    
    