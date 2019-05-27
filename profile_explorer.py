#!/usr/bin/env python3.5
"""Goes through all usernames and collects their information"""
import sys
from util.settings import Settings
from util.datasaver import Datasaver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options as Firefox_Options

from util.extractor import extract_information
from util.account import login
from util.chromedriver import init_chromedriver


chrome_options = Options()
chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2, 'disk-cache-size': 4096}
chromeOptions.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=en-US')
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})

capabilities = DesiredCapabilities.CHROME


def get_all_user_names_from_file():
    FILE_PATH = '../data/ids.txt'
    with open(FILE_PATH, 'r') as f:
        usernames = [name.strip() for name in f.readlines() if not name.startswith('#')]
        return usernames

try:
    browser = init_chromedriver(chrome_options, capabilities)
except Exception as exc:
    print(exc)
    sys.exit()


try:
    usernames = get_all_user_names_from_file()

    for username in usernames:
        print('Extracting information from ' + username)
        information = []
        user_commented_list = []
        # try:
        information, user_commented_list = extract_information(browser, username, Settings.limit_amount)
        # except:
        #     print("Error with user " + username)
        #     sys.exit(1)

        Datasaver.save_profile_json(username,information)


except KeyboardInterrupt:
    print('Aborted...')

finally:
    # browser.delete_all_cookies()
    browser.close()
