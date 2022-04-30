# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):

	Job_title = scrapy.Field()

	Job_description = scrapy.Field()

	Company_name = scrapy.Field()

	Company_Indeed_URL = scrapy.Field()

	URL_to_job_listing = scrapy.Field()

	Company_size = scrapy.Field()

	Company_industry = scrapy.Field()

	Company_description = scrapy.Field()

	Company_URL = scrapy.Field()

	Job_Type = scrapy.Field()

	helpful = scrapy.Field()

	helpless = scrapy.Field()

	work_life_rating = scrapy.Field()

	benefits_rating = scrapy.Field()

	security_rating = scrapy.Field()

	management_rating = scrapy.Field()

	culture_rating = scrapy.Field()