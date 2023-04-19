import requests

url = "https://www.instagram.com/p/CrJVzgWrHlp/?igshid=YmMyMTA2M2Y="

payload={}
headers = {}

response = requests.get( url, stream=True,timeout=111,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0', 'accept-language': 'en-US,en;q=0.5', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})

print(response.text)
