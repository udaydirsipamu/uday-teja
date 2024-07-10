import requests
url="https://httpbin.org/post"
payload={
    "name":"Uday",
    "age":23
}
headers={
    'Content-Type':'application/json',
    'Accept':'application/json'
}
response=requests.post(url,json=payload,headers=headers)
if response.status_code==200:
    print("Data sent successfully")
    print("Recieved data is:",response.json())
else:
    print(f'failed to send data.. {response.status_code}')