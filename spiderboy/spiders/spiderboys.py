#coding=utf-8
import scrapy
from spiderboy.items import DmozItem
from scrapy.http.request import Request
import path
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

class DmozSpider(scrapy.Spider):
    
    name = "spiderboys"
    #allowed_domains = ["gk66.cn"]
    allowed_domains = ["localhost"]
    #start_urls must be a list, not a string type. Or you will get url scheme lost error
    #start_urls = ["http://localhost/test.html"]
    #start_urls = ['http://14wj.gk66.cn/wj/zy_dt.aspx?t=8399E7EE6905BD68950A8F30EED320971202344C90106D3E&zy=6B1DBCE229A56C06624A9CD2F0625D71&p=&n=E3A09360D2AA5594&w=E28304031B769A23&b=BE0F36FA13AD428A&zyids=6D9DCCEC714A0EE4&wc1=&wc2=&fs1=&fs2=']
    start_urls = path.getLocalUrl()

    def parse(self, response):
        
        print "Parse..."

        for sel in response.xpath('//table[@id="tablecloth"]/tbody/tr'):
            item = DmozItem()

            row = sel.xpath('td/a/text()').extract()
            if row:
                item['xx'] = row[0].encode('utf-8')
                item['zy'] = row[1].encode('utf-8')
            else:
                continue

            row = sel.xpath('td/text()').extract()
            if row:
                item['mc'] = row[0]
                item['fs'] = row[1]
                item['pc'] = row[2]
                item['bflqrs'] = row[3]
                item['bzylqrs'] = row[4]
                item['zgf'] = row[5]
                item['zgfmc'] = row[6]
                item['zdf'] = row[7]
                item['zdfmc']= row[8]
                item['pjf'] = row[9]
                item['pjfmc'] = row[10]

            yield item

    """def start_requests(self):

        cookies = exmodule.getCookies()
        for cookie in cookies:
            if cookie['name'] == 'gk66_guid':
                gk66_guid =  cookie['value']

            if cookie['name'] == 'gk66_userinfo':
                gk66_userinfo =  cookie['value']

        for url in self.start_urls:          
            yield Request(url, cookies={'gk66_guid': gk66_guid,
                'gk66_userinfo': gk66_userinfo,
                'gk66_login': 'remname=789449870&rempass=aV6GNNQ8RL8=&remcheck=on',
                'Hm_lpvt_25ae7b1484a52b8a6ffdff4555060aa4': '1461951623',
                'Hm_lvt_25ae7b1484a52b8a6ffdff4555060aa4': '1461685215'
                })"""
