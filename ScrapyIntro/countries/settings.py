# -*- coding: utf-8 -*-

# Scrapy settings for amazon project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import os
import sys

BOT_NAME = 'countries'

# Set default 'robots.txt' parser
script_dir = os.path.dirname(__file__)
sys.path.append(script_dir)
import robots_parser

ROBOTSTXT_PARSER = 'robots_parser.Latin1_utf8RobotsParser.Latin1_utf8RobotsParser'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'

SPIDER_MODULES = ['countries.spiders']
NEWSPIDER_MODULE = 'countries.spiders'

#CSV IMPORTACION
ITEM_PIPELINES = {
    'countries.pipelines.CountriesPipeline': 500,
    'countries.pipelines.CountriesImagenesPipeline': 600, 
    }

# Images directory
IMAGES_STORE = 'flags'

# Allow redirection to download images
MEDIA_ALLOW_REDIRECTS = True

# The amount of time (in secs) that the downloader should wait before downloading
#     consecutive pages from the same website
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True # This is by default

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Retry attempts
RETRY_TIMES = 5

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enable and configure HTTP caching (disabled by default). Helps to avoid banning!
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3_600 # One hour
HTTPCACHE_DIR = 'httpcache'

# Enabling logging to a file
LOG_ENABLED = True
LOG_FILE = 'scrapy.log'