# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):

    def __init__(self, guid, title, subject, summary, link):

        self.guid = str(guid)
        self.title = str(title)
        self.subject = str(subject)
        self.summary = str(summary)
        self.link = str(link)

    def get_guid(self):
        #Gets GUID
        return self.guid

    def get_title(self):
        #Gets Title
        return self.title

    def get_subject(self):
        #Gets Subject
        return self.subject

    def get_summary(self):
        #Gets Summary
        return self.summary

    def get_link(self):
        #Gets Link
        return self.link
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

class WordTrigger(Trigger):

    def __init__(self, word):

        self.word = str(word.lower())
        

    def is_word_in(self, text):

        for i in text:

            if i in string.punctuation:
                

                text = text.replace(i, ' ')

        list_of_words = text.lower().split()
        print list_of_words

        return self.word in list_of_words

    
            
# TODO: TitleTrigger

class TitleTrigger(WordTrigger):

    def __init__(self, word):

        WordTrigger.__init__(self,word)
        print type(super(TitleTrigger,self))

    def evaluate(self, story):
        #Evaluates title to see if alert is needed
        assert type(story) == NewsStory
        return self.is_word_in(story.title)

koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
soda      = NewsStory('', 'Soft drinks are great', '', '', '')
pink      = NewsStory('', "Soft's the new pink!", '', '', '')
football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
caps      = NewsStory('', 'soft things are soft', '', '', '')

s1 = TitleTrigger('SOFT')
s2  = TitleTrigger('soft')

for trig in [s1, s2]:
    
    print trig.evaluate(koala), "TitleTrigger failed to fire when the word appeared in the title"
    print trig.evaluate(pillow), "TitleTrigger failed to fire when the word had punctuation on it"
    print trig.evaluate(soda), "TitleTrigger failed to fire when the case was different"
    print trig.evaluate(pink), "TitleTrigger failed to fire when the word had an apostrophe on it"
    print trig.evaluate(football), "TitleTrigger failed to fire in the presence of lots of punctuation"
    print trig.evaluate(caps), "TitleTrigger is case-sensitive and shouldn't be"
            
    print trig.evaluate(microsoft), "TitleTrigger fired when the word was present, but not as its own word (e.g. 'soft' and 'Microsoft)'"
    print trig.evaluate(nothing), "TitleTrigger fired when the word wasn't really present in the title"

