from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
import re, scrapy

from tv_roulette_scraper.items import Video


class EpisodesSpider(Spider):
  name = "episodes"
  allowed_domains = ["couchtuner.eu/parks-and-recreation/"]
  start_urls = (
    "http://www.couchtuner.eu/2014/04/parks-and-recreation-season-6-episode-21-moving-up-part-1/",
    "http://www.couchtuner.eu/2014/04/parks-and-recreation-season-6-episode-20-one-in-8000/",
    "http://www.couchtuner.eu/2014/04/parks-and-recreation-season-6-episode-19-flu-season-2/",
    "http://www.couchtuner.eu/2014/04/parks-and-recreation-season-6-episode-18-prom/",
    "http://www.couchtuner.eu/2014/03/parks-and-recreation-season-6-episode-17-galentines-day/",
    "http://www.couchtuner.eu/2014/03/parks-and-recreation-season-6-episode-16-new-slogan/",
    "http://www.couchtuner.eu/2014/03/parks-and-recreation-season-6-episode-15-the-wall/",
    "http://www.couchtuner.eu/2014/02/parks-and-recreation-season-6-episode-14-anniversaries/",
    "http://www.couchtuner.eu/2014/01/parks-and-recreation-season-6-episode-13-ann-and-chris/",
    "http://www.couchtuner.eu/2014/01/parks-and-recreation-season-6-episode-12-farmers-market/",
    "http://www.couchtuner.eu/2014/01/parks-and-recreation-season-6-episode-11-new-beginnings/",
    "http://www.couchtuner.eu/2014/01/parks-and-recreation-season-6-episode-10-second-chunce/",
    "http://www.couchtuner.eu/2013/11/parks-and-recreation-season-6-episode-9-the-cones-of-dunshire/",
    "http://www.couchtuner.eu/2013/11/parks-and-recreation-season-6-episode-8-fluoride/",
    "http://www.couchtuner.eu/2013/11/parks-and-recreation-season-6-episode-7-recall-vote/",
    "http://www.couchtuner.eu/2013/11/parks-and-recreation-season-6-episode-6-filibuster/",
    "http://www.couchtuner.eu/2013/10/parks-and-recreation-season-6-episode-5-gin-it-up/",
    "http://www.couchtuner.eu/2013/10/parks-and-recreation-season-6-episode-4-doppelgangers/",
    "http://www.couchtuner.eu/2013/10/parks-and-recreation-season-6-episode-3-the-pawnee-eagleton-tip-off-classic/",
    "http://www.couchtuner.eu/2013/09/parks-and-recreation-season-6-episode-1-london-part-1/",
    "http://couchtuner.eu.com/2013/05/parks-and-recreation-s5-e22.html",
    "http://couchtuner.eu.com/2013/04/parks-and-recreation-s5-e21-swing-vote.html",
    "http://couchtuner.eu.com/2013/04/parks-and-recreation-s5-e20-jerrys-scrapbook.html",
    "http://couchtuner.eu.com/2013/04/parks-and-recreation-s5-e19-article-two.html",
    "http://couchtuner.eu.com/2013/04/parks-and-recreation-s5-e18-animal-control.html",
    "http://couchtuner.eu.com/2013/04/parks-and-recreation-s5-e17-emergency-responce.html",
    "http://couchtuner.eu.com/2013/03/parks-and-recreation-s5-e16-bailout.html",
    "http://couchtuner.eu.com/2013/02/parks-and-recreation-s5-e15-bailout.html",
    "http://couchtuner.eu.com/2013/02/parks-and-recreation-s5-e14-1-hr.html",
    "http://couchtuner.eu.com/2013/02/parks-and-recreation-s5-e13-emergency-response.html",
    "http://couchtuner.eu.com/2013/02/parks-and-recreation-s5-e12-anns-decision.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e11-women-in-garbage.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e10-two-parties.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e9-ron-and-diane.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e8-pawnee-commons.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e7-leslie-vs-april.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e6-bens-parents.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e5-halloween-surprise.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e4-sex-education.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e3-how-a-bill-becomes-a-law.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e2-soda-tax.html",
    "http://couchtuner.eu.com/2013/01/parks-and-recreation-s5-e1-ms-knope-goes-to-washington.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e22.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e21.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e20.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e19.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e18.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e17.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e16.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e15.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e14.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e13.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e12.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e11.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e10.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e9.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e8.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e7.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e6.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e5.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e4.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e3.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e2.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s4-e1.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e16.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e15.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e14.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e13.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e12.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e11.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e10.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e9.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e8.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e7.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e6.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e5.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e4.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e3.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e2.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s3-e1.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e24.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e23.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e22.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e21.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e20.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e19.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e18.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e17.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e16.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e15.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e14.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e13.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e12.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e11.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e10.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e9.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e8.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e7.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e6.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e5.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e4.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e3.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e2.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s2-e1.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e6.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e5.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e4.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e3.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e2.html",
    "http://couchtuner.eu.com/2013/09/parks-and-recreation-s1-e1.html"
  )

  def parse(self, response):
    sel = Selector(response)
    videos = sel.xpath('//div[@class="postTabs_divs"]')
    items = []

    for video in videos:
      item = Video()
      item['page'] = ((sel.xpath('//h2/text()').extract())[0]).encode('cp850"', 'replace').replace(' ? ', '')
      item['url'] = (video.xpath('iframe/@src').extract())[0]
      items.append(item)

    return items

  def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    return item

