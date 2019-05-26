# simple module for reading crawled profile information and logging the stats
import json
import datetime
import csv
import argparse
from util.settings import Settings
import glob
import os
import shutil
import sys
from pytz import timezone
import pytz
import dateutil.parser



INPUT_DIR = './NDATA/fastStats/*/'

def move_file_to_done(profile_filename):
    check_done_folder()
    profile_folder_done = Settings.profile_location + '/done/'
    try:
        shutil.move(profile_filename, profile_folder_done)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # raise


def write_stats(profile):
    timestamp = profile['scraped']
    username = profile['username']
    print('Reading crawled profile info of {}'.format(username))
    #print(profile)


    post_info = []
    for post in profile['posts']:
        post_date = (dateutil.parser.parse(post['date'])
            .astimezone(timezone('US/Pacific'))
            .strftime('%Y-%m-%d %H:%M:%S'))

        stats = {
            'url': post['url'],
            'tags': ' '.join(post['tags']),
            'likes': post['likes']['count'],
            'comments': post['comments']['count'],
            'preview_img': post['preview_img'],
            #'caption': post['caption'],
            'post_date': post_date
        }
        post_info.append(stats)

    print(timestamp)
    if 'T' in timestamp:
        timestamp = (dateutil.parser.parse(timestamp)
            .astimezone(timezone('US/Pacific'))
            .strftime('%Y-%m-%d %H:%M:%S'))
        print(timestamp)

    global_info = {
        'ts': timestamp,
        'username': profile['username'],
        'followers': profile['followers']['count'],
        'following': profile['following']['count'],
        'num_of_posts': profile['num_of_posts']
    }
    # append collected stats to stats.csv
    with open('stats.json', 'a', encoding='utf-8') as f_stats:
        for stats in post_info:
            stats.update(global_info)
            f_stats.write(json.dumps(stats)+'\n')
            # print('Added stats to stats.csv')


def log_stats(username=None):
    profile_folder = INPUT_DIR
    searchFiles = profile_folder + '*.json'

    list_of_files = glob.glob(searchFiles)  # * means all if need specific format then *.csv
    for profile_filename in list_of_files:
        print(profile_filename)
        with open(profile_filename, 'r') as f_profile:
            profile = json.load(f_profile)
            write_stats(profile)

    # while list_of_files != []:
    #     profile_filename = min(list_of_files, key=os.path.getctime)
    #     print(profile_filename)
    #     with open(profile_filename, 'r') as f_profile:
    #         profile = json.load(f_profile)
    #         #write_stats(profile)

    #     # move_file_to_done(profile_filename)

    #     try:
    #         list_of_files = glob.glob(searchFiles)  # * means all if need specific format then *.csv
    #     except:
    #         print("Unexpected error:", sys.exc_info()[0])
    #         # raise


def check_done_folder():
    profile_folder_done = Settings.profile_location + '/done/'
    try:
        os.stat(profile_folder_done)
    except:
        os.mkdir(profile_folder_done)


def parse_args():
    parser = argparse.ArgumentParser(description="Read and log collected stats from crawled profiles")
    parser.add_argument("-u", "--user", help="Username", required=False, default=None, dest="user")
    return parser.parse_args()


if __name__ == '__main__':
    log_stats()
