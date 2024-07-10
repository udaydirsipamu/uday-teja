import requests
url='https://httpbin.org/post'
data={'empid':101}
response=requests.post(url,data=data)
print('Status code:',response.status_code)
print('JSON Date:',response.json())