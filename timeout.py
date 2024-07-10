import requests
try:
    response=requests.get("https://example.com",timeout=0.1)
    print(("Status code:",response.status_code))
    print("Response text:",response.text)
except requests.exceptions.Timeout as errt:
    print(f'Unable to connect to server with the time frame: {errt}')
