#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = ''
# SITENAME = 'experience'
SITENAME = ''
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Contacts', 'pages/contact.html'),)


# Social widget
SOCIAL = (('You can add links in your config file', '#'), ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
THEME = 'pelicanyan'
GA_ACCOUNT = 'UA-12344321-1'
# TWITTER_ACCOUNT = 'getpelican'  
# TWITTER_ACCOUNT = ''  
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'sitemap', 'robots', 'humans')
DISPLAY_PAGES_ON_MENU = True
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'

DEFAULT_LANG = 'en'
DATE_FORMATS = { 'en': '%B %d, %Y', }
STATIC_PATHS = ['images', 'favicon.ico']
# SITEDESCRIPTION = 'sample blog'
TYPOGRIFY=True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
