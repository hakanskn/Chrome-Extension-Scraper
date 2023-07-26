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
from ExtensionEntity import *

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
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        #option.add_argument("accept-language=en-US")
        #option.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        #chrome_locale = 'he-IL'
        #option.add_argument("--lang={}".format(chrome_locale))
        #option.add_argument("--lang=en-US")
        # prefs = {
        #     "translate_whitelists": {"your native language": "en"},
        #     "translate": {"enabled": "False"}
        # }
        # option.add_experimental_option("prefs", prefs)


        option.add_argument('--headless')

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        # browser = webdriver.Chrome(executable_path="chromedriver.exe", options=option)
        browser.get(ext_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 30)

        soup = BeautifulSoup(browser.page_source, 'html.parser')

        extTemp = ExtensionItem()

        extTemp.scrape_url = ext_url

        # title
        extTemp.title = soup.find("h1", attrs = {"class": "e-f-w"}).text.strip()

        # web_site
        try:
            extTemp.web_site = soup.find("a", attrs = {"class": "e-f-y"}).get("href").strip()
        except:
            extTemp.web_site = ""


        # vote_count
        try:
            extTemp.vote_count = soup.find("span", attrs = {"class": "e-f-Sa-L"}).text.replace("(", "").replace(")", "").strip()
        except:
            extTemp.vote_count = ""

        # vote_score
        try:
            temp1 = soup.find("div", attrs = {"class": "rsw-stars"}).get("title")
            extTemp.vote_score = temp1[:temp1.find("yıldız")].replace("Ortalama oy: ", "").strip()
        except:
            extTemp.vote_score = ""


        # user_count
        try:
            extTemp.user_count = soup.find("span", attrs = {"class": "e-f-ih"}).text.replace("users", "").replace("kullanıcı", "").strip()
        except:
            extTemp.user_count = ""


        # category
        try:
            #extTemp.category = soup.find('a', attrs={"class":"e-f-y","aria-label": True}).text.strip()
            extTemp.category = browser.find_elements(By.CLASS_NAME, "e-f-y")[1].get_attribute("aria-label").replace("Category:", "").replace("Kategori:", "").strip()
        except:
            extTemp.category = ""


        # lang
        try:
            extTemp.lang = soup.find('span', attrs = {"class":"C-b-p-D-Xe h-C-b-p-D-Ba"}).text.strip()
        except:
            extTemp.lang = ""


        # size
        try:
            extTemp.size = soup.find('span', attrs = {"class":"C-b-p-D-Xe h-C-b-p-D-za"}).text.strip()
        except:
            extTemp.size = ""

        # updated_date
        try:
            extTemp.updated_date = soup.find('span', attrs = {"class":"C-b-p-D-Xe h-C-b-p-D-xh-hh"}).text.strip()
        except:
            extTemp.updated_date = ""


        # version
        try:
            extTemp.version = soup.find('span', attrs = {"class":"C-b-p-D-Xe h-C-b-p-D-md"}).text.strip()
        except:
            extTemp.version = ""


        # developer_contact
        try:
            extTemp.developer_contact = soup.find('a', attrs = {"class":"C-b-p-rc-D-R"}).get("href").replace("mailto:", "").strip()
        except:
            extTemp.developer_contact = ""


        # desc
        try:
            extTemp.desc = soup.find('div', attrs = {"class":"C-b-p-j-D Ka-Ia-j C-b-p-j-D-gi"}).text.strip()
        except:
            extTemp.desc = ""


        # image_urls
        try:
            tmp1 = soup.find_all("img",
                                 attrs={"class": "h-A-Ce-ze-Yf A-Ce-ze-Yf", "aria-hidden": "true", "height": "400px"})
            tmp2 = [x.get("src") for x in tmp1]
            tmp3 = list(set(tmp2))
            extTemp.image_urls = tmp3
        except:
            extTemp.image_urls = []


        browser.close()
        return extTemp