from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen('https://www.example.com')
body = http_response.read()
html = body.decode("utf-8")
print(html)

# POST
data = {
    'id': 'raspy',
    'pw': '1234'
}
data = urlencode(data).encode('utf-8')

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_response = urlopen(request)
body = http_response.read()
html = body.decode("utf-8")
print(html)





print(html)




