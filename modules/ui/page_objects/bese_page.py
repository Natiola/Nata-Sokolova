from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePege:
    PATH = r"C:\Users\Natiola\Nata-Sokolova"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePege.PATH + BasePege.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
        