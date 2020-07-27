import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

#readable_file = 'data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
#	json.dump(all_eq_data, f, indent =4)

all_eq_dicts = all_eq_data['features'] #taking the data associated with 'features'
#print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	hover_texts.append(eq_dict['properties']['title'])

#print(mags[:10])
#print(lons[:5])
#print(lats[:5])


#map the earthquakes
data = [{
	'type': 'scattergeo',
	'lon': lons, 
	'lat': lats,
	'text': hover_texts,
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Electric',
		'reversescale': True,
		'colorbar': {'title': 'Magnitude'}
	},
}]

graph_tile = all_eq_data['metadata']['title']

my_layout = Layout(title=graph_tile)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
