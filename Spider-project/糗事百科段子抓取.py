import requests
from lxml import etree
import pymongo

url = 'https://www.qiushibaike.com/text/'
headers ={'User-Agent':'Mozilla/5.0'}

conn = pymongo.MongoClient('localhost',28184)
db = conn['Database']
set = db['baike']

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text

parseHtml = etree.HTML(html)
baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
for x in baseList:
    name = x.xpath('./div/a/h2')
    if not name:
        name = '匿名用户'
    else:
        name = name[0].text.strip()
    #段子内容
    content = x.xpath('.//div[@class = "content"]/span')[0].text.strip()
    number = x.xpath('.//i[@class = "number"]')[0].text.strip()
    number2 = x.xpath('.//i[@class = "number"]')[1].text
    print('用户名称:',name)
    print('段子内容:',content)
    print('觉得好笑的人数:',number)
    print('评论人数:',number2)
    print('------------------------------')