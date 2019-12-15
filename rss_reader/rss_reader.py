import argparse
import logging
import json
import time
from rss_reader.Feed import Feed
import os


def display_cache(url_to_show, date_to_show):
    try:
        date_to_show = time.strptime(date_to_show, '%Y%m%d')
    except ValueError:
        logging.error('Date format Error! Please input data in yyyymmdd format!')
        raise ValueError('Wrong date type')
    with open('rss_reader/cache.txt') as cache_file:
        for line in cache_file:
            feed_json = json.loads(line)
            feed_access_date = time.strptime(feed_json['access_time'], '%Y-%m-%d %H:%M:%S.%f')
            url = feed_json['feed_url']
            if feed_access_date > date_to_show and (not url_to_show or url == url_to_show):
                feed_json = json.dumps(feed_json, indent=2)
                print(json.loads(feed_json))


def rss_reader():
    args_parser = argparse.ArgumentParser(prog='Stychnevsky RSS Reader',
                                          description='Reader to parse RSS and output news',
                                          epilog='RSS Reader 2019')

    args_parser.add_argument('url', nargs='?', action="store", help=' ')
    args_parser.add_argument('--version', action="store_true", help='Print version info and exit program')
    args_parser.add_argument('--json', action="store_true", help='Print result as JSON')
    args_parser.add_argument('-v', '--verbose',  action="store_true",
                             help='Outputs verbose status messages')
    args_parser.add_argument('--limit', '-l', action="store",
                             type=int,
                             help='Limit news number if this parameter provided')
    args_parser.add_argument('--date', '-d', action="store",
                             help='Print all feeds from cache from appropriate date and appropriate source')

    cl_args = args_parser.parse_args()

    log = logging.getLogger('main_logger')
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('rss_reader/logs.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    if cl_args.verbose:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        log.addHandler(ch)

    log.info('Program started')
    with open('rss_reader/version.txt', 'r+') as ver_file:
        prev_version = ver_file.readline()
        try:
            main_version, sub_version = prev_version.split('.')
        except ValueError:
            logging.error('Error during parsing version.txt. ValueError in spliting version data.')
            print("Version Error. Wrong Data in version.txt. Version has not been changed")
        new_version = main_version + '.' + str(int(sub_version) + 1)
        ver_file.seek(0)
        ver_file.write(new_version)
        if cl_args.version:
            print('Current version of program: ', prev_version)
            log.info('Program ended after Show Version mode')
            return

    if cl_args.date:
        display_cache(cl_args.url, cl_args.date)
        log.info('Program ended after Show Cache mode')
        return

    feed = Feed(cl_args.url, cl_args.limit)
    log.info('Feed object created')
    if cl_args.json:
        feed.print_json()
        log.info('Feed object printed as JSON')
    else:
        feed.print()
        log.info('Feed object printed')

    feed.caching()
    log.info('Program ended')

