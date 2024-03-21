import scrapy
import json

class YnSpider(scrapy.Spider):
    name = 'yn'
    #allowed_domains = ['ggzy.yn.gov.cn']
    start_urls = ['https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getTenserPlanList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getZbggList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getGzsxList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getPbbgList',

                  ]

    #获取所有类型第一个页面的信息
    def start_requests(self):
        data = {"pageNum":"1","pageSize":"10","cityId":"018","industryCode":"","childType":"","tradeType":"gcjs","title":"","startTime":"","endTime":""}
        for url in self.start_urls:
            #访问单个页面
            data = {"pageNum": "1", "pageSize": "10", "cityId": "018", "industryCode": "", "childType": "",
                    "tradeType": "gcjs", "title": "", "startTime": "", "endTime": ""}
            print(url)
            #返回了该类型下单个页面的信息
            yield  scrapy.Request(url, body=json.dumps(data), method='POST', headers={'Content-Type':'application/json;charset=UTF-8'},callback=self.jiexi)
            break

    # 用来获取单类型下所有页面Guid
    def jiexi(self, response):
        # 获取url
        url = response.url
        # print(url)
        # #获取单类型页面的页数
        a = json.loads(response.text)
        page = a["value"]["pages"]
        # page = int(page)
        # print(type(page))
        # 获取当前类型下所有页面的信息
        for i in range(page):
            data = {"pageNum": f"{i}", "pageSize": "10", "cityId": "018", "industryCode": "", "childType": "",
                    "tradeType": "gcjs", "title": "", "startTime": "", "endTime": ""}
            yield scrapy.Request(url, body=json.dumps(data), method='POST',
                                 headers={'Content-Type': 'application/json;charset=UTF-8'}, callback=self.dangyemian)
            break

     # 访问所有子页面的信息
    def dangyemian(self, response):
        url = response.url
        a = json.loads(response.text)
        for i in range(len(a["value"]["list"])):
            guid = a["value"]["list"][i]['guid']
            print(guid)
            if "TenserPlan" in url:
                url = url.replace("List", "") + "Detail?guid=" + guid
            else:
                url = url.replace("get", "find").replace("List", "") + "ByGuid?guid=" + guid

            yield scrapy.Request(url, callback=self.dangyemianparse)
            break

        # 处理子页面返回的信息
    def dangyemianparse(self, response):
        a = json.loads(response.text)
        biaoti = a["value"]["projectName"]
        shijian = a["value"]["publishTime"]
        content = a["value"]["content"]
        print(biaoti, shijian, content)


