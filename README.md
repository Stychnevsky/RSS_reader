## RSS_reader by Stychnevsky Anton
This packege will help you to manage news in RSS format: take them from websites, print in different easy-to-read formats, cach and so on.

## Requirement
You need to have Python >= 3.7 and Linux OS to use this package.<br/>
Also program need to some external libraries:<br/>
-feedparser<br/>
-bs4<br/>
-httplib2<br/>
-requests<br/>

They will be installed automaticly using "install_requires" argument in setup.py file


## Package instalation

1) Please install wheel and setuptools if you dont have it:<br/>
    pip3 install wheel<br/>
    pip3 install setuptools

2) Install RSS reader:<br/>
    pip install git+https://github.com/Stychnevsky/RSS_reader
    
3) Now you can use CLI ("rss-parser" command)<br/>
    rss-reader https://news.yahoo.com/rss/ #example<br/>


## Usage 
Usage: rss_reader.py [-h] [--version] [--json] [-v][--verbose] [-l][--limit LIMIT]<br/>
                           [-d][--date DATE] [--output-path OUTPUT_PATH]<br/>
                          [--to-epub] [--to-html]<br/>
                         [url]<br/>
Positional arguments:<br/>
'sourse' - URL to parse feed<br/><br/>

Optional reguments:<br/>
 '-h', '--help' -            show this help message and exit<br/>
  '--version' -             Print version info and exit program. Version changed
                        after every program launch<br/>
  '--json' -                 Print result as JSON<br/>
  '-v', '--verbose' -          Outputs verbose status messages<br/>
  '--limit LIMIT', '-l LIMIT' - 
                        Limit news number if this parameter provided<br/>
  '--date DATE', '-d DATE' -   Print all feeds from cache from appropriate date and
                        appropriate source<br/>
  '--output-path OUTPUT_PATH' - 
                        In this argument you can set path to save epub and
                        html files. Home directory is default<br/>
  '--to-epub' -              Generate epub file with news. Use --output-path to
                        select directory to save it. Defalault filename is feed title + date<br/>
  '--to-html' -             Generate html file, which include only. Use --output-
                        path arg to select directory to save<br/>



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
rss-reader https://onliner.by/feed --json -l 5<br/>
Print 5 latest news from onliner.by i json format<br/>

rss-reader https://news.tut.by/rss -l6 --to-epub --output-path /home/your_user_name/Downloads<br/>
Create in folder epub-file with 6 entries from tut.by<br/>

rss-reader https://news.yahoo.com/rss/ -v <br/>
Print all news from yahoo and output verbosr status messages<br/>

rss-reader --date 20191225 <br/>
Print all news from cache file, which are loaded not later than 25.12.2019<br/>
