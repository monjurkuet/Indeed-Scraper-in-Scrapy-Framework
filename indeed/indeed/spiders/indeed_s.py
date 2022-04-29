# -*- coding: utf-8 -*-
import scrapy
from indeed.items import IndeedItem

class IndeedSSpider(scrapy.Spider):
    name = 'indeedjobspider'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=customer%20support&l=Los%20Angeles%2C%20CA']

    def parse(self, response):

       job_post_baseurl='https://www.indeed.com/viewjob?jk=' 

       job_posts = response.xpath('//a[@data-jk]/@data-jk').getall()
 
       print(job_posts)
       for job_post in job_posts:
           URL_to_job_listing=job_post_baseurl+job_post
           #yield scrapy.Request(URL_to_job_listing,callback = self.parse_single)
            #change the country code

       next_page_url='https://www.indeed.com'+response.xpath('//li/a[@aria-label="Next"]/@href').get()   
       if len(next_page_url)!=0:
           print(next_page_url)
           yield scrapy.Request(next_page_url, self.parse)  

    # def parse_single(self, response):

    #     job_posts = response.xpath('//a[@data-jk]')

    #     for job_post in job_posts:

    #         item = IndeedItem()

    #         item['company'] = company

    #         item['rating'] = review.xpath(".//div[@class = 'cmp-ReviewRating-text']/text()").extract_first()

    #         item['date'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[last()]").extract_first()

    #         item['content'] = review.xpath(".//span[@itemprop = 'reviewBody']//span[@class = 'cmp-NewLineToBr-text']/text()").extract()

    #         item['position'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']//meta[@itemprop='name']/@content").extract_first()

    #         yield item

    #     if len(response.xpath("//a[@data-tn-element = 'next-page']/@href")):
    #         next_url = response.xpath("//a[@data-tn-element = 'next-page']/@href").extract_first()

    #         yield scrapy.Request("https://www.indeed.com" + next_url ,callback = self.parse_single)














