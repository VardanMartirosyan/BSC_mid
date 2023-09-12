from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_ import customLogger

class CustomListener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver) -> None:
        pass

    def after_navigate_to(self, url: str, driver) -> None:
        pass

    def before_navigate_back(self, driver) -> None:
        pass

    def after_navigate_back(self, driver) -> None:
        pass

    def before_navigate_forward(self, driver) -> None:
        pass

    def after_navigate_forward(self, driver) -> None:
        pass

    def before_find(self, by, value, driver) -> None:
        customLogger.loger("INFO", f"Trying to find element by {by} and value {value}")

    def after_find(self, by, value, driver) -> None:
        customLogger.loger("INFO", f"Founded element by {by} and value {value}")

    def before_click(self, element, driver) -> None:
        pass

    def after_click(self, element, driver) -> None:
        pass

    def before_change_value_of(self, element, driver) -> None:
        pass

    def after_change_value_of(self, element, driver) -> None:
        pass

    def before_execute_script(self, script, driver) -> None:
        pass

    def after_execute_script(self, script, driver) -> None:
        pass

    def before_close(self, driver) -> None:
        pass

    def after_close(self, driver) -> None:
        pass

    def before_quit(self, driver) -> None:
        pass

    def after_quit(self, driver) -> None:
        pass

    def on_exception(self, exception, driver) -> None:
        pass
