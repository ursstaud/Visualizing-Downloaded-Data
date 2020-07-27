import csv
import matplotlib.pyplot as plt 
from datetime import datetime


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)


	date, highs, lows = [], [], []
	for index, column_header in enumerate(header_row):
		if index == 6 and column_header == 'TOBS':
			for row in reader:
				station_name = row[1] 
				current_date = datetime.strptime(row[2], '%Y-%m-%d')
				try:
					high = int(row[4])
					low = int(row[5])
				except ValueError:
					print(f"Missing data for {current_date}!")
				else:
					date.append(current_date)
					highs.append(high)
					lows.append(low)

		if index == 6 and column_header == 'TMIN':
			for row in reader:
				station_name = row[1] 
				current_date = datetime.strptime(row[2], '%Y-%m-%d')
				try:
					high = int(row[5])
					low = int(row[6])
				except ValueError:
					print(f"Missing data for {current_date}!")
				else:
					date.append(current_date)
					highs.append(high)
					lows.append(low)

#setup
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(date, lows, color = 'blue', alpha = 0.8)
ax.plot(date, highs, color = 'red', alpha = 0.8)

#format
title = f"HIGH/LOW TEMPERATURES RECORDED AT {station_name}, 2018"
plt.title(title, fontsize = 15)
plt.xlabel("Dates", fontsize = 13)
plt.ylabel("Temperature", fontsize = 13)
fig.autofmt_xdate()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()