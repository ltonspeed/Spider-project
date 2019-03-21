import urllib.request
import urllib.parse
import json

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent':'Mozilla/5.0'}
key = input('请输入要翻译的内容')

data = {'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15530400221044',
        'sign':'546e5c0146b69e189090e65784448c94',
        'ts':'1553040022104',
        'bv':'e2a78ed30c66e16a857c5b6486a1d326',
        'doctype':'json',
        'version':'2.1',
        'keyform':'fanyi.web',
        'action':'FY_BY_REALTlME',
        'typoResult':'false',
        }
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')

rDict = json.loads(html)

result = rDict['translateResult'][0][0]['tgt']
print(result)