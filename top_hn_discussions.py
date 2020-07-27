import requests
from operator import itemgetter
import json
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
r = requests.get(url)
#print(f"Status code: {r.status_code}")

#pull in and process information about each top submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids:
	#make separate api call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	#build a dictionary for each article
	submission_dict = {
		'title': response_dict['title'],
		'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
		'comments':  response_dict.get('descendants',0),
		}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts[:30]:
	print({submission_dict['title']})
	print({submission_dict['hn_link']})
	print({submission_dict['comments']})


#process results
article_names, comments, links, embedded_links = [], [], [], []
for submission_dict in submission_dicts[:30]:
	article_names.append(submission_dict['title'])
	comments.append(submission_dict['comments'])
	links.append(submission_dict['hn_link'])
	embedded_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
	embedded_links.append(embedded_link)

#plot results
data = [{
	'type': 'bar',
	'x': embedded_links,
	'y': comments,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
		},
	'opacity': 0.6,
	}]

my_layout = {
	'title': 'Most Commented On Articles in Hacker News',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Article Name',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
		},
	'yaxis': {
		'title': 'Comments',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
		},
	}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'top_hn_discussions.html')