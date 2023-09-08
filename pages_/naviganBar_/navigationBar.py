from selenium.webdriver.common.by import By
from pages_.basePage_ import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.__userNameLocator = (By.ID, "nav-link-accountList-nav-line-1")

    def get_user_name(self):
        # userNameElement = self.driver.find_element(*self.__userNameLocator)
        userNameElement = self._find_element(self.__userNameLocator)
        return (userNameElement.text.split(" "))[1]
