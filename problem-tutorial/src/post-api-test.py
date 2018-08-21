from urllib import request, parse

url = 'http://....'

data = {
    'userName': 'tangguike',
    'serverList': [{'ip': '10.136.200.3', 'weight': 1}],
}

data = parse.urlencode(data).encode('utf-8')
req = request.Request(url, data=data, method='POST')
page = request.urlopen(req).read()
page = page.decode('utf-8')
print(page)
