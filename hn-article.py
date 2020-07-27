import requests
import json

#make API call, store response
url = 'https://hacker-news.firebaseio.com/v0/item/23603866.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#explore data structure
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
	json.dump(response_dict, f, indent = 4)