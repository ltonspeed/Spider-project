import urllib.request
import urllib.parse
import time

baseurl = 'http://tieba.baidu.com/f?'
headers = {'User-Agent':' User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
name = input('贴吧名称')
begin = int(input('起始'))
end = int(input('终止'))

kw = urllib.parse.urlencode({'kw':name})
for page in range(begin,end+1):
    pn=(page-1)*50
    url = baseurl+kw+'&ie=utf-8&pn='+str(pn)
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')

    filename = '第'+str(page)+'页.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)
        print('第%d页爬取成功'%page)
        time.sleep(0.1)