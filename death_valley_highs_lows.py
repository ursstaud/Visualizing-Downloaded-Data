import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	#get high temperatures for this file
	highs, dates, lows = [], [], []
	for row in reader :
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4]) 
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
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
title = "Daily High and Low Temperatures in 2018\nDeath Valley, California"
plt.title(title, fontsize=18)
plt.xlabel(' ', fontsize=10)
fig.autofmt_xdate() #draws the date labels diagonally to prevent overlap
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

