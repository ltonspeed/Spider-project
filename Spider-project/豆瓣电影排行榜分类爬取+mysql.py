import requests
import pymysql
import json
import time

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.db = pymysql.connect('127.0.0.1',
                                  'root','123456',
                                   'mydb',
                                   charset = 'utf8')
        self.cursor = self.db.cursor()
    def getPage(self,params):
        res = requests.get(self.url,params=params,headers=self.headers)
        res.encoding = 'utf-8'
        html=res.text
        self.parsePage(html)

    def parsePage(self,html):
        hList = json.loads(html)
        for h in hList:
            name = h['title']
            score = h['score']
            actors = h['actors']
            L = [name,float(score.strip()),'&'.join(actors[0:8])]
            self.writeMysql(L)

    def writeMysql(self,L):
        ins = 'insert into film(name,score,actors)values(%s,%s,%s)'
        self.cursor.execute(ins,L)
        self.db.commit()
    def workOn(self):
        print('*****************************************************')
        print('  |剧情|喜剧|爱情|动作|科幻|动画|悬疑|惊悚|恐怖|纪录片  ')
        print('*****************************************************')
        kinds = ['剧情','喜剧','爱情','动作','科幻','动画','悬疑','惊悚','恐怖','纪录片']
        kind = input('请输入电影类型:')
        kDict = {'剧情':'11','喜剧':'24','爱情':'13','动作':'5','科幻':'17','动画':'25','悬疑':'10','恐怖':'20','纪录片':'1'}
        if kind in kinds:
            n=input('请输入要爬取的电影数量:')
            params = {
                'type':kDict[kind],
                'interval_id':'100:90',
                'action':"",
                'start': '0',
                'limit':n
            }
            self.getPage(params)
            print('爬取成功,数量:%s'%n)
        else:
            print('类型不存在')

if __name__ == '__main__':
    start = time.time()
    spider = DoubanSpider()
    spider.workOn()
    end=time.time()
    print('执行时间:%.2f'%(end-start))