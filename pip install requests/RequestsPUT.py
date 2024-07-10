import requests
import json
url='https://jsonplaceholder.typicode.com/posts/1'
data={'id':101, 'title':'Introduction to python'}
headers={'content-type':'application/json;charset-UTG-8'}
response=requests.put(url,data=json.dumps(data),headers=headers)
print("Status code:",response.status_code)
print("Text response:",response.text)
print("URL:",response.url)
print("content type:",response.headers['content-type'])