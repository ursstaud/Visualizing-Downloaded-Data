import matplotlib.pyplot as plt 
import csv
from datetime import datetime

deathvalleyfile = 'data/death_valley_2018_simple.csv'
with open(deathvalleyfile) as dvf:
	dv_reader = csv.reader(dvf)
	dv_header_row = next(dv_reader)

	dv_dates, dv_highs, dv_lows = [], [], []
	for row in dv_reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f'Missing data for {current_date}')
		else:
			dv_dates.append(current_date)
			dv_highs.append(high)
			dv_lows.append(low)

sitkafile = 'data/sitka_weather_2018_simple.csv'
with open(sitkafile) as sf:
	s_reader = csv.reader(sf)
	s_header_row = next(s_reader)

	s_dates, s_highs, s_lows = [], [], []
	for row in s_reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		s_dates.append(current_date)
		s_highs.append(high)
		s_lows.append(low)	

sanfranciscofile = 'data/san_francisco_2018.csv'
with open(sanfranciscofile) as sff:
	sf_reader = csv.reader(sff)
	sf_header_row = next(sf_reader)

	sf_dates, sf_highs, sf_lows = [], [], []

	for row in sf_reader:
		#current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(f"Missing data for {current_date}.")
		else:
			#sf_dates.append(current_date)
			sf_highs.append(high)
			sf_lows.append(low)
		
#plot
title = 'High Temperature Comparisons in 2018'
plt.style.use('seaborn')
fig, ax1 = plt.subplots()
ax1.plot(s_dates, s_highs, color = 'green')
ax1.plot(s_dates, dv_highs, color = 'red')
ax1.plot(s_dates, sf_highs, color = 'grey')
ax1.set_xlabel('', fontsize=10)
ax1.set_ylabel('Temperature (F)')
plt.title(title, fontsize = 18)


plt.show()