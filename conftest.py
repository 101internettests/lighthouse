import os
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture
def driver():
    options = ChromeOptions()
    if os.getenv("HEADLESS") == "True":
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    yield driver
    driver.quit()