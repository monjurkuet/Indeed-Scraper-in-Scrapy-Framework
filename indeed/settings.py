# -*- coding: utf-8 -*-

BOT_NAME = 'indeed'
SPIDER_MODULES = ['indeed.spiders']
NEWSPIDER_MODULE = 'indeed.spiders'
FEED_EXPORT_ENCODING = 'utf-8-sig'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4
DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 600
COOKIES_ENABLED = False
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
#
ITEM_PIPELINES = {'indeed.pipelines.ValidateItemPipeline': 100,
					'indeed.pipelines.WriteItemPipeline': 200}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'tor_ip_rotator.middlewares.TorProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
TOR_IPROTATOR_ENABLED = True
TOR_IPROTATOR_CHANGE_AFTER = 2
RETRY_TIMES=10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 429]