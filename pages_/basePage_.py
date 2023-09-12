from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_ import customLogger

class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout, 0.3).until(EC.visibility_of_element_located(locator))
            return element
        except:
            # import datetime
            # now = datetime.datetime.now()
            # print("Exception Of find element", now.strftime("%H:%M:%S"))
            customLogger.loger("ERROR", "ELEMENT NOT FOUND")
            exit(5)
