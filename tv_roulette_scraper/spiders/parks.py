from scrapy.spider import Spider
from scrapy.selector import Selector
import re, unidecode

from tv_roulette_scraper.items import Episodes


class ParksSpider(Spider):
    name = "parks"
    allowed_domains = ["couchtuner.eu/parks-and-recreation/"]
    start_urls = (
        'http://couchtuner.eu/parks-and-recreation//',
    )

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li/strong')
        items = []

        for site in sites:
            item = Episodes()
            item['name'] = 'Parks & Recreation'
            item['season'] = (filter(None, (re.findall('S(\d+)|Season\ (\d+)', (site.xpath('a/text()').extract())[0]))[0]))[0]
            item['episode'] = (re.findall('Episode\ (\d+)', txt))[0]
            item['url'] = (site.xpath('a/@href').extract())[0]
            item['title'] = ((site.xpath('text()').extract())[0]).encode('cp850"', 'replace').replace(' ? ', '')
            items.append(item)

        return items