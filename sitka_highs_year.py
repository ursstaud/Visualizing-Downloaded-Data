import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f: #assign resulting file to f
	reader = csv.reader(f) 
	header_row = next(reader)

	for index, column_header in enumerate(header_row): #this function returns the index and value of each item
		print(index, column_header)

	#get high temperatures for this file
	highs, dates, lows = [], [], []
	for row in reader :
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5]) 
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)


#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
#format plot
plt.title("Daily High & Low Temperatures 2018", fontsize=24)
plt.xlabel(' ', fontsize=10)
fig.autofmt_xdate() #draws the date labels diagonally to prevent overlap
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

