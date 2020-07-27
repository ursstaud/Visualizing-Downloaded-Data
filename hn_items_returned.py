import json
import requests


def top_items_returned():
	url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
	r = requests.get(url)
	submission_ids = r.json()
	submission_dicts = []
	count = 0

	for submission_id in submission_ids:
	#make separate api call for each submission
		count += 1

	return count