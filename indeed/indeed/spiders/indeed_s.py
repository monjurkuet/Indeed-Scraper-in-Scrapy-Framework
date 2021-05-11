# -*- coding: utf-8 -*-
import scrapy
from indeed.items import IndeedItem
import pandas as pd

urls = pd.read_csv("C:/Users/MXX/Desktop/cleaned_company_list.csv") #change the path and file name
urls = urls['indeed_url']

class IndeedSSpider(scrapy.Spider):
    name = 'indeed_s'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/cmp/Amazon.com/reviews?fcountry=US&lang=en']

    def parse(self, response):
        for url in urls:
            yield scrapy.Request("https://www.indeed.com" + url + "/reviews?fcountry=CN",callback = self.parse_single)
            #change the country code

    def parse_single(self, response):

        reviews = response.xpath('//div[@class = "cmp-Review"]')

        company = response.xpath('//div[@class = "cmp-CompactHeaderLayout-nameContainer"]//text()').extract_first()

        for review in reviews:

            item = IndeedItem()

            item['company'] = company

            item['rating'] = review.xpath(".//div[@class = 'cmp-ReviewRating-text']/text()").extract_first()

            item['date'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[last()]").extract_first()

            item['content'] = review.xpath(".//span[@itemprop = 'reviewBody']//span[@class = 'cmp-NewLineToBr-text']/text()").extract()

            item['position'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']//meta[@itemprop='name']/@content").extract_first()

            if len(review.xpath(".//div[@class = 'cmp-Review-title']/text()")):
                item['title'] = review.xpath(".//div[@class = 'cmp-Review-title']/text()").extract_first()
            else:
                item['title'] = review.xpath(".//a[@class = 'cmp-Review-titleLink']/text()").extract_first()


            if len(review.xpath(".//a[@class = 'cmp-ReviewAuthor-link']")) == 2 :
                item['location'] = review.xpath(".//a[@class = 'cmp-ReviewAuthor-link'][2]/text()").extract_first()
                item['status'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[2]").extract_first()

            elif len(review.xpath(".//a[@class = 'cmp-ReviewAuthor-link']")) == 1:
                if review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[last()-2]").extract_first() != ' - ':
                    item['location'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[last()-2]").extract_first()
                    item['status'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[last()-4]").extract_first()
                else:
                    item['location'] = review.xpath(".//a[@class = 'cmp-ReviewAuthor-link'][1]/text()").extract_first()
                    item['status'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[3]").extract_first()
            else:
                item['location'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[5]").extract_first()
                item['status'] = review.xpath(".//span[@class = 'cmp-ReviewAuthor']/text()[3]").extract_first()


            subrating = review.xpath(".//div[@class = 'cmp-SubRating']//div[@class = 'cmp-RatingStars-starsFilled']/@style").extract()

            item['work_life_rating'] = subrating[0]

            item['benefits_rating'] = subrating[1]

            item['security_rating'] = subrating[2]

            item['management_rating'] = subrating[3]

            item['culture_rating'] = subrating[4]
            # 3px=0
            # 15px=1
            # 27px=2
            # 39px=3
            # 51px=4
            # 63px=5

            if len(review.xpath(".//div[@class = 'cmp-ReviewProsCons-prosText']//span[@class = 'cmp-NewLineToBr-text']/text()")):
                item['Pros'] = review.xpath(".//div[@class = 'cmp-ReviewProsCons-prosText']//span[@class = 'cmp-NewLineToBr-text']/text()").extract_first()
            else:
                item['Pros'] = 'NaN'

            if len(review.xpath(".//div[@class = 'cmp-ReviewProsCons-consText']//span[@class = 'cmp-NewLineToBr-text']/text()")):
                item['Cons'] = review.xpath(".//div[@class = 'cmp-ReviewProsCons-consText']//span[@class = 'cmp-NewLineToBr-text']/text()").extract_first()
            else:
                item['Cons'] = 'NaN'

            if len(review.xpath(".//span[text()='Yes']//span[@class = 'cmp-StatelessReviewFeedbackButtons-count']/text()")):
                item['helpful'] = review.xpath(".//span[text()='Yes']//span[@class = 'cmp-StatelessReviewFeedbackButtons-count']/text()").extract_first()
            else:
                item['helpful'] = 0
            
            if len(review.xpath(".//span[text()='No']//span[@class = 'cmp-StatelessReviewFeedbackButtons-count']/text()")):
                item['helpless'] = review.xpath(".//span[text()='No']//span[@class = 'cmp-StatelessReviewFeedbackButtons-count']/text()").extract_first()
            else:
                item['helpless'] = 0

            yield item

        if len(response.xpath("//a[@data-tn-element = 'next-page']/@href")):
            next_url = response.xpath("//a[@data-tn-element = 'next-page']/@href").extract_first()

            yield scrapy.Request("https://www.indeed.com" + next_url ,callback = self.parse_single)














