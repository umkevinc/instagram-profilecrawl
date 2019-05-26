import os
import sys
import datetime
from sys import platform as p_os
import importlib

thismodule = sys.modules[__name__]


TODAY_STR = datetime.datetime.now().strftime("%Y-%m-%d")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OS_ENV = "windows" if p_os == "win32" else "osx" if p_os == "darwin" else "linux"

SETTING_NAME = os.getenv('SETTING', 'DailyInfoSetting')


class AccountCrawlerSettings:
    profile_location = os.path.join(BASE_DIR, 'NDATA', 'account', TODAY_STR)
    limit_amount = 0
    max_user_depth = 10000
    scrape_posts_infos = False
    scrape_posts_likers = False
    scrape_follower = False
    output_comments = False
    sleep_time_between_post_scroll = 1
    sleep_time_between_comment_loading = 1
    mentions = False

    log_output_toconsole = True
    log_output_tofile = True
    log_file_per_run = False
    log_location = os.path.join(BASE_DIR, 'logs')

    #from Instpy
    # Set a logger cache outside object to avoid re-instantiation issues
    loggers = {}

    login_username = ''
    login_password = ''

    #chromedriver
    chromedriver_min_version = 2.36
    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')


class BackfillSettings:
    profile_location = os.path.join(BASE_DIR, 'NDATA', 'profiles', TODAY_STR)
    profile_commentors_location = os.path.join(BASE_DIR, 'NDATA', 'profiles', TODAY_STR)
    profile_file_with_timestamp = True
    profile_commentors_file_with_timestamp = True
    limit_amount = 800
    scrape_posts_infos = True
    scrape_posts_likers = False
    scrape_follower = False
    output_comments = False
    sleep_time_between_post_scroll = 2
    sleep_time_between_comment_loading = 1
    mentions = True

    log_output_toconsole = True
    log_output_tofile = True
    log_file_per_run = False
    log_location = os.path.join(BASE_DIR, 'logs')

    #from Instpy
    # Set a logger cache outside object to avoid re-instantiation issues
    loggers = {}

    login_username = ''
    login_password = ''

    #chromedriver
    chromedriver_min_version = 2.36
    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')


class DailyInfoSetting:
    profile_location = os.path.join(BASE_DIR, 'NDATA', 'dailyInfo', TODAY_STR)
    profile_commentors_location = os.path.join(BASE_DIR, 'NDATA', 'dailyInfo', TODAY_STR)
    profile_file_with_timestamp = True
    profile_commentors_file_with_timestamp = True
    limit_amount = 2 # Max 5 post for daily
    scrape_posts_infos = True
    scrape_posts_likers = True
    max_likers_per_post = 500
    scrape_follower = False
    output_comments = True
    sleep_time_between_post_scroll = 1
    sleep_time_between_comment_loading = 1
    mentions = True

    log_output_toconsole = True
    log_output_tofile = True
    log_file_per_run = False
    log_location = os.path.join(BASE_DIR, 'logs')

    #from Instpy
    # Set a logger cache outside object to avoid re-instantiation issues
    loggers = {}

    login_username = ''
    login_password = ''

    #chromedriver
    chromedriver_min_version = 2.36
    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')


class FastStatsSetting:
    profile_location = os.path.join(BASE_DIR, 'NDATA', 'fastStats', TODAY_STR)
    profile_commentors_location = os.path.join(BASE_DIR, 'NDATA', 'fastStats', TODAY_STR)
    profile_file_with_timestamp = True
    profile_commentors_file_with_timestamp = True
    limit_amount = 5 # Max 5 post for daily
    scrape_posts_infos = True
    scrape_posts_likers = False
    max_likers_per_post = 500
    scrape_follower = False
    output_comments = False
    sleep_time_between_post_scroll = 1
    sleep_time_between_comment_loading = 1
    mentions = True

    log_output_toconsole = True
    log_output_tofile = True
    log_file_per_run = False
    log_location = os.path.join(BASE_DIR, 'logs')

    #from Instpy
    # Set a logger cache outside object to avoid re-instantiation issues
    loggers = {}

    login_username = ''
    login_password = ''

    #chromedriver
    chromedriver_min_version = 2.36
    specific_chromedriver = "chromedriver_{}".format(OS_ENV)
    chromedriver_location = os.path.join(BASE_DIR, "assets", specific_chromedriver)

    if not os.path.exists(chromedriver_location):
        chromedriver_location = os.path.join(BASE_DIR, 'assets', 'chromedriver')


Settings = getattr(thismodule, SETTING_NAME)