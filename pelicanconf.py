#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lev Maximov'
SITENAME = u'axil\'s blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Novosibirsk'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
#THEME = "D:/Documents/python/pelican-themes/pelican-simplegrey"
THEME = "./pelican-elegant"

DEFAULT_DATE = 'fs'
LOCALE = 'usa'
STATIC_PATHS = 'css', 'img'
GOOGLE_ANALYTICS = 'UA-63331443-1'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

DISQUS_SITENAME = "axil"

RST_GLOBAL_INCLUDES = [ "include/globals.rst" ]
