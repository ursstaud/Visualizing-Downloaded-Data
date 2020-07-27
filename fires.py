import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_7_day.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#for index, column_header in enumerate(header_row):
	#	print(index, column_header)

	frps, lats, lons = [], [], []
	row_num = 0
	row_limit = 7000
	for row in reader:
		lats.append(row[0])
		lons.append(row[1])
		try:
			frp = float(row[11])
		except ValueError:
			print(f"There is no data for the location at {lat}, {lon}.")
		else:
			frps.append(frp)
		row_num += 1
		if row_num>= row_limit:
			break

data = [{
	'type': 'scattergeo',
	'lon': lons, 
	'lat': lats,
	'marker': {
		'size': [0.05*frp for frp in frps],
		'color': frps,
		'colorscale': 'Viridis',
		'reversescale': True,
		'colorbar': {'title': 'Fire Radiative Power'}
	},
}]

title = 'Fires Around the World for 7 Days and their Radiative Power'
my_layout = Layout(title = title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_fires.html')
