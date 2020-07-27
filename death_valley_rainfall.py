import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	rainfall, dates = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		rain = float(row[3])
		rainfall.append(rain)
		dates.append(current_date)

#plot the rainfall
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c = 'blue')

#format
title = "Daily Rainfall in Death Valley 2018"
plt.title(title, fontsize=18)
plt.xlabel('', fontsize = 10)
plt.ylabel('Precipitation', fontsize=15)
fig.autofmt_xdate()
plt.tick_params(axis='both', which = 'major', labelsize =16)
plt.show()

