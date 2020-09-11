#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'me'
SITENAME = 'Pelican Test'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = 'en'

TYPOGRIFY = False

# Category settings

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Articles Path

ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('test-site', 'https://sol-finance.github.io/test-site'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './pelican-blue'


# Path to the folder containing the plugins
PLUGIN_PATHS = ['plugins']

MARKUP = ("md", "ipynb")

# Enabled plugins
from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]