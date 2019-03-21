import urllib.request
import re
import pymysql
import time
import warnings

class MaoyanSpider():
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/6?offset='
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.page = 1
        self.db = pymysql.connect('localhost','root','123456','mydb',charset='utf-8')
        self.cursor = self.db.cursor()

    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parsePage(html)

    def parsePage(self,html):
        p = re.compile('<div class="board-item-main">.*?title="(.*?)"',re.S)
        rList = p.findall(html)
        self.writeMysql(rList)

    def writeMysql(self,rList):
        warnings.filterwarnings('ignore')
        ins = 'insert into top100(name,star,time) values(%s,%s,%s)'
        for r in rList:
            print(r)
            L = [
                r[0].strip(),
                r[1].strip(),
                r[2].strip()[5:15]
            ]
            self.cursor.execute(ins,L)
            self.db.commit()

    def workOn(self):
        for pg in range(0,11,10):
            url = self.baseurl+str(pg)
            self.getPage(url)
            print('第%d页爬取成功'%self.page)
            time.sleep(3)
            self.page += 1
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.workOn()