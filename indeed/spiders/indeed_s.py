# -*- coding: utf-8 -*-
import scrapy
import re

class IndeedSSpider(scrapy.Spider):
    name = 'indeedjobspider'
    allowed_domains = ['indeed.com']
    start_urls = ['https://www.indeed.com/jobs?radius=25&l=Los%20Angeles%2C%20CA&limit=50&sort=date&q=customer%20support&start=0']

    def parse(self, response):

       job_post_baseurl='https://www.indeed.com/viewjob?jk=' 

       job_posts = response.xpath('//a[@data-jk]/@data-jk').getall()
 
       print(job_posts)
       for job_post in job_posts:
           URL_to_job_listing=job_post_baseurl+job_post
           yield scrapy.Request(URL_to_job_listing,callback = self.parse_jobpost)

       next_page_url='https://www.indeed.com'+response.xpath('//li/a[@aria-label="Next"]/@href').get()   
       if len(next_page_url)!=0:
           print(next_page_url)
           yield scrapy.Request(next_page_url, self.parse)  

    def parse_jobpost(self, response):
        try:
            Job_title=response.xpath('//h1/text()').get()  
            Job_description=response.xpath('//div[@id="jobDescriptionText"]//text()').getall()
            Job_description=('\n'.join(x.strip() for x in Job_description)).strip()    # pretty data
            Company_name=response.xpath('//div[@class="jobsearch-CompanyInfoContainer"]//a/text()').get()  
            Company_Indeed_URL=response.xpath('//div[@class="jobsearch-CompanyInfoContainer"]//a/@href').get().split('?')[0]  
            URL_to_job_listing=response.request.url 
            Job_Type=response.xpath('//div[text()="Job Type"]/following::*/text()').get()  
             
            jobpost_data = {
							"Job_title":Job_title,
							"Job_description":Job_description,
							"Company_name":Company_name,
							"URL_to_job_listing":URL_to_job_listing,
							"Job_Type":Job_Type,
                            "Company_Indeed_URL":Company_Indeed_URL
							}
            
            data = {'jobpost_data': jobpost_data}

            #print(jobpost_data)

            yield scrapy.Request(Company_Indeed_URL, meta=data, callback=self.parse_Company_Indeed_URL)
        except:
            pass
    def parse_Company_Indeed_URL(self, response):

            data = response.meta['jobpost_data']
            
            Company_industry=Company_size=Company_founded=Company_URL=None
            try:
             Company_industry=response.xpath('//li[@data-testid="companyInfo-industry"]//div[text()="Industry"]/following::*/text()').get()  
            except:
             pass   
            try:
             Company_size=response.xpath('//li[@data-testid="companyInfo-employee"]//text()').getall()[-1]
            except:
             pass 
            try:
             Company_founded=response.xpath('//div[text()="Founded"]/following-sibling::*/text()').get()  
            except:
             pass    
            try:
             Company_URL=response.xpath('//li[@data-testid="companyInfo-companyWebsite"]//a/@href').get()  
            except:
             pass   
           
            data['Company_industry']=Company_industry
            data['Company_size']=Company_size
            data['Company_founded']=Company_founded
            data['Company_URL']=Company_URL

            #print(data)       

            yield data 
