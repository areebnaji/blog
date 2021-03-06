#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Savvas Tjortjoglou'
SITENAME = 'Savvas Tjortjoglou'
SITEURL = 'http://savvastjortjoglou.com'
# SITEURL = ''


TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = "UA-50819746-2"
DISQUS_SITENAME = "savvasblog"


DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
THEME = "/home/savvas/repos/blog_env/pelican-themes/pelican-bootstrap3"

# Bootswatch THEME
BOOTSTRAP_THEME = 'cosmo'

# Set to blue version of creative which is based on yeti
BOOTSTRAP_NAVBAR_INVERSE = False

# Hide the side bar
HIDE_SIDEBAR = True

MARKUP = ('md', 'ipynb')

#Plugins
PLUGIN_PATHS = ['/home/savvas/repos/blog_env/pelican-plugins']
PLUGINS = ['ipynb.markup', 
            'liquid_tags.img', 
            'liquid_tags.video',
           'liquid_tags.youtube', 
           'liquid_tags.vimeo',
           'liquid_tags.include_code', 
           'summary']


# Pygments 
PYGMENTS_STYLE = 'bw'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'code', 'extra/CNAME']

# # Shift the installed location of a file
# Used for custom domain name
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

SHARIFF = True
SHARIFF_LANG = True

# Use ummary from Sumary section of ipynb-meta
IPYNB_USE_META_SUMMARY = True