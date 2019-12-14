## RSS_reader by Stychnevsky Anton
This packege will help you to manage news in RSS format: take them from websites, print in different easy-to-read formats, cach and so on.

## Requirement
You need to have Python >= 3.7 and Linux OS to use this package.<br/>
Also program need to some external libraries:<br/>
-feedparser<br/>
-bs4<br/>

They will be installed automaticly using "install_requires" argument in setup.py file


## Package instalation
1) Clone this repository (https://github.com/Stychnevsky/RSS_reader/) for your computer

2) Please install wheel and setuptools if you dont have it:<br/>
    pip install wheel<br/>
    pip install setuptools

3) change folder to RSS_reader:<br/>
    cd RSS_reader
    
4) setup package:<br/>
    python setup.py bdist_wheel
    
5) dist package will be created:<br/>
    cd dist
    
6) install package using pip:<br/>
    pip install rss_reader-1.0.tar.gz
    
7) Go to rss_reader folder:<br/>
    cd ..<br/>
    cd RSS_reader

8) Soo, now you can use RSS_parser!<br/>
    python3 rss_reader.py https://news.yahoo.com/rss/<br/>

## Program improvment
Now you see 1.0 program version. In is ready-to-work, but, to tell the truth, no so good as it can be.<br/>
So, we want to anounce 2.0 version realise. It is expected on Decemver 15 or 16. It will inculde testing, many little improvments and, probably, ability to create fb2 document.
Hope you will give us a chance just to show it...


## Usage 
Usage: rss_reader.py [-h] [--version] [--json] [-v][--verbose] [-l][--limit LIMIT] [-d][--date]<br/>
                     source
Positional arguments:<br/>
'sourse' - URL to parse feed

Optional reguments:<br/>
'-h', '--help' - Pring information about package and exit program<br/>
'--version' - Print version of program and exit program. It will change after every usage of programe<br/>
'--json' - News will be printed in json format<br/>
'--verbose' - Turn on outputing verbose statuse messages<br/>
'--limit LIMIT - - limit number of news from sourse if this parametr provided<br/>
'date DATE''- prints cached feeds starting out for some date. If source provided, it will print only news from this sourse, another way.


JSON structure (1 JSON = 1 Feed, not Feeds list):<br/>
{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'access_time': 01.01.1900 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'feed_url': example.com/rss,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'published': 01.01.2019 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'source': , example.com,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'feed_description': self.feed_title.description,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;'entries':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;[<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'title': 'News title',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'link': 'example.com/news1.html',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'description': 'News summary',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'img_links:':<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'img_saver.com/1234.png',<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;']<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'published': 01.01.2018 00:00:00,<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
&nbsp;&nbsp;&nbsp;&nbsp;']<br/>
}<br/>
        

# Examples
rss_reader.py https://onliner.by/feed --json -l 5<br/>
Print 5 latest news from onliner.by i json format<br/>

rss_reader.py https://news.yahoo.com/rss/ -v <br/>
Print all news from yahoo and output verbosr status messages<br/>

rss_reader.py --date 20191210 <br/>
Print all news from cache file, which are loaded not later than 10.12.2019<br/>
