import requests
url="https://api.github.com"
username="user"
password="pass"
response=requests.get(url,auth=(username,password))
print("Status code:",response.status_code)
if response.status_code==200:
    print("You are able to access the site with the given credentials..")
else:
    print("Invalid credentials..")
