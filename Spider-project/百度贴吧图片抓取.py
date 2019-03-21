import requests
from lxml import etree

class BaiduSpider():
    def __init__(self):
        self.baseurl = 'http://tieba.baidu.com/f?'
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    def getPageUrl(self,params):
        res = requests.get(self.baseurl,params=params,headers = self.headers)
        html = res.text
        parseHtml = etree.HTML(html)
        rList = parseHtml.xpath('//div[@class = "t_con cleafix"]/div/div/div/a/@href')

        for t in rList:
            tLink = 'http://tieba.baidu.com'+t
            print(t)
            self.getImgUrl(tLink)
    def getImgUrl(self,tLink):
        res = requests.get(tLink,headers = self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parseHtml = etree.HTML(html)
        imgList = parseHtml.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')
        for imgLink in imgList:
            print(imgLink)
            self.writeImg(imgLink)
    def writeImg(self,imgLink):
        res = requests.get(imgLink,headers = self.headers)
        res.encoding = 'utf-8'
        html = res.content
        filename = imgLink[-10:]
        with open(filename,'wb') as f:
            f.write(html)
            print('下载成功')
    def Main(self):
        name=input('请输入贴吧名称：')
        begin=int(input('起始页：'))
        end=int(input('终止页：'))
        for i in range(begin,end+1):
            pn = (i-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.getPageUrl(params)

if __name__ == '__main__':

    x = BaiduSpider()
    x.Main()