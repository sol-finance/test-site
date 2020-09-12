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



# Enabled plugins

# Path to the folder containing the plugins

PLUGIN_PATHS = ['/pelican-plugins']

# from pelican_jupyter import markup as nb_markup

# MARKUP = ("md")

MARKUP = ("md", "ipynb")

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    # 'liquid_tags',
    # 'liquid_tags.youtube',
    # 'liquid_tags.include_code',
    'render_math',
    'tipue_search',
    'pelican_jupyter.markup'
    ]

# for pelican_jupyter Plugin

IGNORE_FILES = [".ipynb_checkpoints"]

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# THEMES

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'