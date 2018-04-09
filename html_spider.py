import urllib
import demjson

url = 'http://tianqi.2345.com/t/wea_history/js/201803/54511_201803.js'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
str = response.read().decode('gbk')

dict = demjson.decode(str[16: -1])

print(dict)

print(dict.get("city"))