from selenium.webdriver.common.by import By # call for the selenium driver

class LoginPageLocators:

    USER_NAME_TEXT_BOX = (By.NAME, "userName")  # call for the xpath of the locators
    PASSWORD_TEXT_BOX = (By.NAME, "password")
    SUBMIT_BUTTON = (By.NAME,"submit")

