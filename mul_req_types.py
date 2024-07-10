import requests
url="https://jsonplaceholder.typicode.com/posts/1"
try:
    response=requests.get(url)
    response.raise_for_status()
    content_type=response.headers.get('Content-Type')
    if 'application.json' in content_type:
        data=response.json()
    elif 'text' in content_type:
        data=response.text
    else:
        data=response.content
    print('Response Data:',data)
except requests.exceptions.HTTPError as errh:
    print("HTTP Error occured:",errh)
except requests.exceptions.ConnectionError as errc:
    print("HTTP Error occured:",errc)
except requests.exceptions.Timeout as errt:
    print("HTTP Error occured:",errt)
except requests.exceptions.RequestException as errr:
    print("HTTP Error occured:",errr)