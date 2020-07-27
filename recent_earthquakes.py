import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/big_magnitude_earthquake.json'
with open(filename) as f:
	recent_data = json.load(f)

features_recent_data = recent_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for data in features_recent_data:
	mags.append(data['properties']['mag'])
	lons.append(data['geometry']['coordinates'][0])
	lats.append(data['geometry']['coordinates'][1])
	hover_texts.append(data['properties']['title'])

#map the quakes
data = [{
	'type': 'scattergeo',
	'lon': lons, 
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	},
}]
title = recent_data['metadata']['title']
my_layout = Layout(title = title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'recent_earthquakes.html')