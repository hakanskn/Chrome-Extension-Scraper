import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.remote.webelement import WebElement
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import pandas as pd
import random
from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager
from Entity import *

class ExtensionProvider(object):

    @staticmethod
    def GetExtensionUrls(visit_url):

        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        #option.add_argument('--headless')

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        # browser = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
        browser.get(visit_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 30)

        for i in range(70):
            print(str(i+1))
            browser.execute_script("window.scrollTo(0, 100000000000000)")
            time.sleep(3)

        soup = BeautifulSoup(browser.page_source, 'html.parser')
        list1 = soup.find_all("a", attrs={"class": "a-u"})
        list2 = [x.get("href") for x in list1]

        browser.close()

        return list2


    @staticmethod
    def GetExtensionDetails(ext_url):

        pass