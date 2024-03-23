import scrapy
import json
from yunnan.items import YunnanItem
import time
class YnSpider(scrapy.Spider):
    name = 'yn'
    #allowed_domains = ['ggzy.yn.gov.cn']

    start_urls = ['https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getTenserPlanList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getZbggList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getGzsxList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getPbbgList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getZbJgGgList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getContractList',
                  'https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getZbycList'
                  ]

    #获取所有类型第一个页面的信息
    def start_requests(self):
        data = {"pageNum":"1","pageSize":"10","cityId":"018","industryCode":"","childType":"","tradeType":"gcjs","title":"","startTime":"","endTime":""}
        for url in self.start_urls:
            #访问单个页面
            data = {"pageNum": "1", "pageSize": "10", "cityId": "018", "industryCode": "", "childType": "",
                    "tradeType": "gcjs", "title": "", "startTime": "", "endTime": ""}
            # print(url)
            #返回了该类型下单个页面的信息
            yield  scrapy.Request(url, body=json.dumps(data), method='POST', headers={'Content-Type':'application/json;charset=UTF-8'},callback=self.parse)
            # break

    # 用来获取单类型下所有页面Guid
    def parse(self, response):
        # 获取url
        url = response.url
        # time.sleep(3)
        # print(response,"正在执行")
        # #获取单类型页面的页数
        a = json.loads(response.text)
        page = a["value"]["pages"]
        # page = int(page)
        print(page)
        # 获取当前类型下所有页面的信息
        for i in range(1):
            # print()
            data = {"pageNum": f"{i}", "pageSize": "10", "cityId": "018", "industryCode": "", "childType": "",
                    "tradeType": "gcjs", "title": "", "startTime": "", "endTime": ""}
            yield scrapy.Request(url, body=json.dumps(data), method='POST',
                                 headers={'Content-Type': 'application/json;charset=UTF-8'},callback=self.parse_two)


     # 访问所有子页面的信息
    def parse_two(self, response):
        url = response.url
        # print(url)
        a = json.loads(response.text)
        for i in range(len(a["value"]["list"])):
            guid = a["value"]["list"][i]['guid']
            # print(guid)
            if "TenserPlan" in url:
                url_two = url.replace("List", "") + "Detail?guid=" + guid
            elif "Contract" in url:
                url_two = " https://ggzy.yn.gov.cn/ynggfwpt-home-api/jyzyCenter/jyInfo/gcjs/getGcjsContractDetail?guid=" + guid

            else:
                url_two = url.replace("get", "find").replace("List", "") + "ByGuid?guid=" + guid
            # print(url_two)
            yield scrapy.Request(url_two, callback=self.dangyemianparse)


        # 处理子页面返回的信息
    def dangyemianparse(self, response):
        url=response.url
        a = json.loads(response.text)

        if "Gzsx" in url:
            biaoti = a["value"]["changetitle"]
            shijian = a["value"]["fabutime"]
            content = a["value"]["changecontent"]
            guid = a["value"]["guid"]
            leix="15"
        elif  "TenserPlan" in url:
            biaoti = a["value"]["projectName"]
            shijian = a["value"]["publishTime"]
            content = a["value"]["content"]
            guid = a["value"]["guid"]
            leix = "15"
        elif "Zbgg" in url:
            biaoti = a["value"]["bulletinname"]
            shijian = a["value"]["bulletinissuetime"]
            content = a["value"]["bulletinname"]
            guid = a["value"]["guid"]
            leix = "15"
        elif "Pbbg" in url:
            biaoti = a["value"]["publicityname"]
            shijian = a["value"]["publicitystarttime"]
            content = a["value"]["publicitycontent"]
            guid = a["value"]["guid"]
            leix = "16"
        elif "ZbJgGg" in url:
            biaoti = a["value"]["tenderprojectname"]
            shijian = a["value"]["bulletinissuetime"]
            content = a["value"]["bulletincontent"]
            guid = a["value"]["guid"]
            leix = "16"
        elif "Contract" in url:
            biaoti = a["value"]["contractName"]
            shijian = a["value"]["gongshiTime"]
            content = a["value"]["contractContent"]
            guid = a["value"]["guid"]
            leix = "16"

        elif "Zbyc" in url:
            biaoti = a["value"]["exceptionName"]
            shijian = a["value"]["dateTimeStamp"]
            content = a["value"]["exceptionInfor"]
            guid = a["value"]["guid"]
            leix = "16"



        if "TenserPlan" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=招标计划&from=jiaoYi"
        elif "Zbgg" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=招标公告&from=jiaoYi"
        elif "Gzsx" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=变更通知&from=jiaoYi"
        elif "Pbbg" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=中标候选人公示&from=jiaoYi"
        elif "ZbJgGg" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=中标结果公示&from=jiaoYi"
        elif "Contract" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=合同及履约公示&from=jiaoYi"
        elif "Zbyc" in url:
            url =  f"https://ggzy.yn.gov.cn/tradeHall/tradeDetail?guid={guid}&colCode=1&rowCode=异常公告&from=jiaoYi"


        print("标题："+biaoti)
        print("时间：" + shijian)
        print("类型：" + leix)
        print("url：" + url)
        # print("html内容："+content)

        itemm = YunnanItem()
        itemm['biaoti'] = biaoti
        itemm['shijian'] = shijian
        itemm['leix'] =leix
        itemm['url'] = url
        itemm['content'] = content
        yield itemm


