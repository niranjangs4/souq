from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
launch_config = dict(souq=r'https://saudi.souq.com/sa-en/',
                     menu='fi-menu',
                     categories_id="panel12-label",
                     Perfumes_Fragrances="Perfume",
                     implicit=150)

# print(launch_config.get('souq'))
interval = 10


def advance(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("% {} %".format(argument))
            result = function(*args, **kwargs)
            print("% {} %".format(argument))
            return result

        return wrapper

    return real_decorator
