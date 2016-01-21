import urllib2, base64

url = 'https://atctrailers.leankit.com/kanban/api/board/199063443/Archive'
username = 'aaronc@aluminumtrailer.com'
password = '8v!Wr2S'


request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)

data = result.read()
print data

