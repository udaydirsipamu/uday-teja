import requests
params={
    'userid':'Uday',
    'password':'Admin'
}
response=requests.get('http://example.com',params=params)
print('Status code:',response.status_code)
print('Response text:',response.text)
print('URL:',response.url)