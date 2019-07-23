import urllib.request
response = urllib.request.urlopen('https://www.creditchina.gov.cn')
print(response.read().decode('utf-8'))
