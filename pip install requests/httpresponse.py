import requests
response=requests.get('https://w3schools.com/python/demopage.htm')
print('Status code:',response.status_code)
print('Text data server is returning',response.text)
print('Headers:',response.headers)