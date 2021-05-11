# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):

	company = scrapy.Field()

	rating = scrapy.Field()

	title = scrapy.Field()

	position = scrapy.Field()

	status = scrapy.Field()

	location = scrapy.Field()

	content = scrapy.Field()

	date = scrapy.Field()

	Pros = scrapy.Field()

	Cons = scrapy.Field()

	helpful = scrapy.Field()

	helpless = scrapy.Field()

	work_life_rating = scrapy.Field()

	benefits_rating = scrapy.Field()

	security_rating = scrapy.Field()

	management_rating = scrapy.Field()

	culture_rating = scrapy.Field()