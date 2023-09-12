import time
import unittest
from selenium import webdriver

from pages_.logIn_.logInPage import LogIn
from pages_.naviganBar_.navigationBar import NavigationBar
from common_.utilities_ import customLogger

from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import CustomListener

from tests_.testData_.testData import validClientUser, invalidClientUser, signInURL

class LogInTest(unittest.TestCase):
    def setUp(self) -> None:
        customLogger.loger("INFO", "Test Started")
        self.coreDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.coreDriver, CustomListener())
        self.driver.implicitly_wait(6)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInURL)

    def test_invalid_login(self):
        loginPageObj = LogIn(self.driver)

        loginPageObj.fill_login_field(invalidClientUser.login)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(invalidClientUser.password)
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()

    def test_valid_login(self):
        loginPageObj = LogIn(self.driver)

        loginPageObj.fill_login_field(validClientUser.login)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validClientUser.password)
        time.sleep(5)
        loginPageObj.click_to_sign_in_button()

        #Assertion
        navigationBarObj = NavigationBar(self.driver)
        self.assertEqual(navigationBarObj.get_user_name(), validClientUser.name)

    def tearDown(self) -> None:
        time.sleep(17)
        self.driver.close()
        customLogger.loger("INFO", "Test Finished")

