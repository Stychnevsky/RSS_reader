## RSS_reader by Stychnevsky Anton
This packege will help you to manage news in RSS format: take them from websites, print in different easy-to-read formats, cach and so on.

## Requirement
You need to have Python >= 3.7 and Linux OS to use this package.
Also program need to some external libraries:
-feedparser
-argparse
-bs4

They will be installed automaticly using "install_requires" argument in setup.py file


## Package instalation
1) Clone this repository (https://github.com/Stychnevsky/RSS_reader/) for your computer

2) change folder to RSS_reader: 
    cd RSS_reader
    
3) setup package:
    python setup.py sdist
    
4) dist packeg will be created:
    cd dist
    
5) install package using pip 
    pip install rss_reader-1.0.tar.gz

Soo, know you install RSS_parser!

## Usage 
Usage: rss_reader.py [-h] [--version] [--json] [-v][--verbose] [-l][--limit LIMIT] [-d][--date]
                     source
Positional arguments:
'sourse' - URL to parse feed

Optional reguments:
'-h', '--help' - Pring information about package and exit program
'--version' - Print version of program and exit program. It will change after every usage of programe
'--json' - News will be printed in json format
'--verbose' - Turn on outputing verbose statuse messages
'--limit LIMIT - - limit number of news from sourse if this parametr provided
'date DATE''- prints cached news starting out for some date. If source provided, it will print only news from this sourse, another way. 


JSON structure (1 JSON = 1 Feed, not Feeds list):
{
    'access_time': 01.01.1900 00:00:00,
    'feed_url': example.com/rss,
    'published': 01.01.2019 00:00:00,
    'source': , example.com,
    'feed_description': self.feed_title.description,
    'entries':
    [
        {
            'title': 'News title',
            'link': 'example.com/news1.html',
            'description': 'News summary',
            'img_links:':
                [
                    img_saver.com/1234.png,
                    ...
                ],
            'published': 01.01.2018 00:00:00,
        },
        {
            ...
        }
     ]
}
        

# Examples
rss_reader.py https://onliner.by/feed --json -l5
Print 5 latest news from onliner.by i json format

rss_reader.py 'https://news.yahoo.com/rss/' -v 
Print all news from yahoo and output verbosr status messages

rss_reader.py --date 20101210 
Print all news from cache file, which are loaded not later than 10.12.2010
