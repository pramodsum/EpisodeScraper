from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import re, scrapy

from tv_roulette_scraper.items import Episodes

class PsychSpider(Spider):
    name = "psych"
    allowed_domains = ["couchtuner.eu/psych/"]
    start_urls = (
        'http://couchtuner.eu/psych/',
    )

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li/strong')
        items = []

        for site in sites:
            item = Episodes()
            item['name'] = 'Psych'
            link = site.xpath('a')

            if len(link.xpath('text()').extract()) > 0:
                item['page'] = (link.xpath('text()').extract())[0]
                item['season'] = (filter(None, (re.findall('S(\d+)|Season\ (\d+)', item['page']))[0]))[0]
                item['episode'] = (re.findall('Episode\ (\d+)', item['page']))[0]
                item['link'] = (link.xpath('@href').extract())[0]
            else: 
                item['page'] = ''
                item['season'] = ''
                item['episode'] = ''
                item['link'] = ''

            if len(site.xpath('text()').extract()) > 0:
                item['title'] = ((site.xpath('text()').extract())[0]).encode('cp850"', 'replace').replace(' ? ', '')
            else: 
                item['title'] = ''
            item['url'] = ''
            items.append(item)

        return items