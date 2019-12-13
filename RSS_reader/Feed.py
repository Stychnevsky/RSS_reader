import feedparser
import html
from FeedTitle import FeedTitle
from Entry import Entry
import json
import time
import logging
import datetime


class Feed:

    feed_url = ""

    def __init__(self, url, limit):
        self.feed_url = url
        the_feed = feedparser.parse(self.feed_url)
        self.feed_title = FeedTitle(the_feed)
        self.entries = []

        # number_of_entries = limit  if limit else len(the_feed.entries) #может быть  len>limit!!!!
        n = 1
        #while n < number_of_entries and n < len(the_feed.entries):  # better use generators!!!!!
        #    self.entries.append(Entry(the_feed.entries[n]))
        #    n += 1
        #    print(n)
        for entry in the_feed.entries: #лимит лучше вот тут пропиши, в слайсе. или все же нет??
            if limit and n > limit:
                break
            self.entries.append(Entry(entry))
            n += 1

        self.json_data = {
            'access_time': str(datetime.datetime.now()),
            'feed_url': self.feed_url,
            'published': self.feed_title.published,
            'source': self.feed_title.title,
            'feed_description': self.feed_title.description,
            'entries': [entry.output_to_json() for entry in self.entries]
        }


    def print(self):  # возможно лучше в классе нормально задать метод __str__
        end_of_feed_title = '\n==================\n'
        end_of_entry = '\n__________________\n'
        print(*self.feed_title.output(), sep='\n', end=end_of_feed_title)
        for entry in self.entries:
            print(*entry.output(), sep='\n', end=end_of_entry)

    def print_json(self):
        pass

    def caching(self):
        with open ('cache.txt','a') as cache_file:
            cache_file.write(json.dumps(self.json_data) + '\n')
            #json.dump(self.json_data, cache_file)



