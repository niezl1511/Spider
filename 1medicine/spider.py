# -*- coding:utf-8 -*-
import json
import re
import time

import requests
from common_spider import Common_Spider
from lxml import etree

class Medicine1(Common_Spider):
    #https://www.111.com.cn/categories/953710?tp=10-1
    def __init__(self):
        self.list_url = 'https://www.111.com.cn/categories/953783-j1.html'
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.111.com.cn/categories/953783-j2.html',
            'Cookie':'locateCityName=%E4%B8%8A%E6%B5%B7; locateProvinceName=%E4%B8%8A%E6%B5%B7; locateProvinceId=1; UUID=6BEc6DAD-7d7B-4e7-9DDA-DDDeebBAAeA; Hm_lvt_4674a7b9bc5deca972145cfd7f6cb592=1564534688; cartKey=5f7e11336acde1595b918f7ce300e7a0; demandItemCount=0; NTKF_T2D_CLIENTID=guest4557BD20-6345-AF6C-3637-4588CD0A3A5E; provinceId=20; healthGiftTanStatus=0; nTalk_CACHE_DATA={uid:yy_1000_ISME9754_guest4557BD20-6345-AF,tid:1564565880056860}; locateProvinceId=20; locateProvinceName=%E5%B9%BF%E4%B8%9C; locateCityName=%E5%B9%BF%E5%B7%9E; cityName=%E5%B9%BF%E5%B7%9E; history=51217629%2C%20%E5%90%8C%E4%BB%81%E5%A0%82%20%E9%87%91%E5%8C%AE%E8%82%BE%E6%B0%94%E4%B8%B8%200.2g*360%E7%B2%92%20%20*4%E4%BB%B6%3B%2050708962%2C%20%E5%AE%AB%E5%AE%9D%20%E8%83%9A%E5%AE%9D%E8%83%B6%E5%9B%8A%200.3g*30%E7%B2%92%3B%2050148671%2C%20%E4%BD%9B%E6%85%88%20%E7%9F%A5%E6%9F%8F%E5%9C%B0%E9%BB%84%E4%B8%B8%20360%E4%B8%B8%3B%2050169581%2C%20%E5%90%8C%E4%BB%81%E5%A0%82%20%E5%B7%A6%E5%BD%92%E4%B8%B8%2054g%2F%E7%93%B6%3B%2050981144%2C%20%E5%90%8C%E4%BB%81%E5%A0%82%20%E9%94%81%E9%98%B3%E5%9B%BA%E7%B2%BE%E4%B8%B8%209g*10%E4%B8%B8*12%E4%BB%B6%3B%20; JSESSIONID=9C908B6183A198434D2605CBFB80E011; cururl=https%3A%2F%2Fwww.111.com.cn%2Fcategories%2F953784-a0-b0-c21-d0-e0-f0-g1-h0-i0-j1.html; Hm_lpvt_4674a7b9bc5deca972145cfd7f6cb592=1564573251'
        }
        self.page = 1
        self.final_item = []
    def get_target_url(self):
        #//h3[@class="no_bd_b"]/a[2]/text()
        cate_list = []
        response = requests.get(self.list_url,headers=self.headers)
        content = response.text
        html = etree.HTML(content)
        category = html.xpath('//h3[@class="no_bd_b"]/a[2]/text()')
        for i in category:
            i = re.sub("\s",'',i)
            cate_list.append(i)
        print(cate_list)
        ul_s = html.xpath('//ul[@class="list_ul"]')
        with open('category_item.jsonlines','a') as f:
            for index,ul in enumerate(ul_s):
                item = {}
                list_urls = ul.xpath('.//li/a/@href')
                sub_categorys = ul.xpath('.//li/a/text()')
                # print(sub_categorys)
                for index2,sub_category in enumerate(sub_categorys[::2]):
                    sub_category = re.sub('\s','',sub_category)
                    if sub_category:
                        item['list_url'] = 'https:' + list_urls[index2] if list_urls[index2] else None
                        item['sub_category'] = sub_category if sub_category else None
                        item['category'] = cate_list[index]
                        json.dump(item,f,ensure_ascii=False)
                        f.write('\n')
                        print(item)


    def get_data_by_url(self,item):
        list = []
        print('开始第{}页'.format(self.page))
        url = item['page_url'].format(self.page)
        print(url)
        response = requests.get(url,headers=self.headers)
        time.sleep(1)
        content = response.text
        html = etree.HTML(content)
        lis = html.xpath('//ul[@id="itemSearchList"]/li')
        print(len(lis))
        for li in lis:
            result = {}
            result['category'] = item['category']
            result['sub_category'] = item['sub_category']
            url = li.xpath('.//div[@class="itemSearchResultCon"]/a/@href')
            result['detail_url'] = ('https:' + url[0]) if len(url) != 0 else None
            # price = li.xpath('.//div[@class="itemSearchResultCon"]/p/span/text()')
            prices = li.xpath('.//div[@class="itemSearchResultCon none"]/p[@class="price"]/span/text()')
            if len(prices) == 0:
                price = li.xpath('.//div[@class="itemSearchResultCon"]/p[@class="price"]//span/text()')[0]
                price = price.replace('\n', '')
                price = price.replace(' ', '')
            else:
                price = prices[0]
                li1 = price.replace('\n', '')
                price = li1.replace(' ', '')
            result['price'] = price
            # print(price)
            comment = li.xpath('.//div[@class="itemSearchResultCon"]//span[@class="comment comment_right"]//em/text()')
            result['comment'] = comment[0] if len(comment) != 0 else 0
            print(result)
            list.append(result)
        if len(list) != 0:
            self.page += 1
            with open('detail_url2','a') as f:
                for i in list:
                    json.dump(i,f,ensure_ascii=False)
                    f.write('\n')
            self.get_data_by_url(item)

    def parse_detail_url(self,item):
        try:
            url = item['detail_url']
            response = requests.get(url, headers=self.headers)
            time.sleep(0.5)
            content = response.text
            html = etree.HTML(content)

            info = html.xpath('//div[@class="middle_property"]//span[@class="red giftRed"]/text()')

            item['info'] = info[0] if len(info) != 0 else None
            name = html.xpath('//th[contains(text(),"通用名称 : ")]/following-sibling::td[1]/text()')
            # 商品名称  品牌  产品类型 说明 价格 评论
            item['name'] = name[0] if len(name) != 0 else None
            brand = html.xpath('//th[contains(text(),"品　　牌：")]/following-sibling::td[1]/text()')
            item['brand'] = brand[0] if len(brand) != 0 else None
            pro_type = html.xpath('//th[contains(text(),"产品类型：")]/following-sibling::td[1]/text()')
            item['pro_type'] = re.sub('\s','',pro_type[0]) if len(pro_type) != 0 else None
            print(item)
            # self.final_item.append(item)
            with open('final_rst.jsonlines2', 'a') as f:
                # for item in self.final_item:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')

        except:
            print('error')
    def run(self):
        #爬取详情item
        # with open('category_item.jsonlines','r') as f:
        #     rst = f.readlines()
        # for i in rst:
        #     self.page = 1
        #     item = i.replace('\n', '')
        #     item = json.loads(item)
        #     print(item['sub_category'],"：开始爬取")
        #     item['page_url'] = item['list_url'] + '-a0-b0-c21-d0-e0-f0-g1-h0-i0-j{}.html'
        #     self.get_data_by_url(item)
        # self.get_target_url()
        #解析详情页
        with open('detail_url3','r') as f:
            rst = f.readlines()
        for i in rst:
            item = i.replace('\n', '')
            item = json.loads(item)
            self.parse_detail_url(item)

if __name__ == '__main__':
    medicine = Medicine1()
    medicine.run()