import requests
link = 'https://fast.com/'
response = requests.get(link)
print(response.ok)
