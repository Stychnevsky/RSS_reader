import argparse

import logging
import json
import time
from Feed import Feed
import sys


def display_cache(url_to_show, date_to_show):
    try:
        date_to_show = time.strptime(date_to_show, '%Y%m%d')
    except ValueError:
        logging.error('Date format Error! Please input data in yyyymmdd format!')
    except Exception:
        logging.info('??????') #тут еще может быть тайп еррор которая в итоге окажется внизу в ифе!!
        raise #тут типо тайп еррор по идее. мл ждали стринг а нам дали дату или инт
    with open('cache.txt') as cache_file:
        for line in cache_file:
            feed_json = json.loads(line)
            feed_access_date = time.strptime(feed_json['access_time'], '%Y-%m-%d %H:%M:%S.%f')
            url = feed_json['feed_url']
            if feed_access_date < date_to_show and (not url_to_show or url == url_to_show):
                print(json.dumps(feed_json, indent=2))

"""logging.basicConfig(format='# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    filename=u'logs.log')
"""
"""
#root = logging.getLogger()
root=logging.FileHandler('logs.log')
root.setLevel(logging.INFO)


handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
"""



def main():
    args_parser = argparse.ArgumentParser(prog='Stychnevsky RSS Reader',
                                          description='Help to read RSS',
                                          epilog='end of help, thank for using')

    args_parser.add_argument('url', nargs='?', action="store", help=' ')
    # args_parser.add_argument('--version', action="version", version='1.0', help='Print version info')
    args_parser.add_argument('--version', action="store_true", help='Print version info')
    args_parser.add_argument('--json', action="store_true", help='Print result as JSON in stdout')
    args_parser.add_argument('-v', '--verbose',  action="store_true",
                             help='Outputs verbose status messages')
    args_parser.add_argument('--limit', '-l', action="store",
                             type=int,
                             help='Limit news topics if this parameter provided')
    args_parser.add_argument('--short', action="store_true", help='???? shor_ver>?')
    args_parser.add_argument('--date', '-d', action="store", help='??????')

    cl_args = args_parser.parse_args()

    log = logging.getLogger('main_logger')
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler('logs.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    if cl_args.verbose:
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        log.addHandler(ch)

    log.info(u'Program started')

    with open('version.txt', 'r+') as ver_file:
        prev_version = ver_file.readline()
        try:
            main_version, sub_version = prev_version.split('.')
        except ValueError:
            logging.error(u'Error during parsing version.txt. ValueError in spliting version data.')
            print("Version Error. Wrong Data in version.txt. Version has not been changed")
        new_version = main_version + '.' + str(int(sub_version) + 1)
        ver_file.seek(0)
        ver_file.write(new_version)
        if cl_args.version:
            print('Current version of program: ', prev_version)
            log.info(u'Program ended after Show Version mode')
            return

    if cl_args.date:
        display_cache(cl_args.url, cl_args.date)
        return

    #args = vars(args_parser.parse_args())
    #feed = RSSParser(**args)
    feed = Feed(cl_args.url, cl_args.limit)
    feed.print()
    feed.caching()
    """
    if cl_args.verbose:
        with open('logs.log', 'r') as logs_file:
            for line in logs_file.readlines():
                print(line, end='')
    """

    log.info(u'Program ended')


if __name__ == '__main__':
    main()

