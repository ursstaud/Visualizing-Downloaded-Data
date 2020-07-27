import matplotlib.pyplot as plt
import csv
from datetime import datetime

deathvalleyfile = 'data/death_valley_2018_simple.csv'
with open(deathvalleyfile) as dvf:
	dvreader = csv.reader(dvf)
	header_row = next(dvreader) #need to specify this

	dvdate, dvhighs, dvlows = [], [], []
	for row in dvreader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}.")
		else:
			dvdate.append(current_date)
			dvhighs.append(high)
			dvlows.append(low)



sitkafilename = 'data/sitka_weather_2018_simple.csv'
with open(sitkafilename) as sf:
	sreader = csv.reader(sf)
	header_row = next(sreader) #need to specify

	sdate, shighs, slows = [], [], []
	for row in sreader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		sdate.append(current_date)
		shighs.append(high)
		slows.append(low)

#highs
plt.style.use('seaborn')
fig, ax1 = plt.subplots()
ax1.set_xlabel('', fontsize=10)
ax1.set_ylabel("Sitka and Death Valley Highs in 2018\n(Sitka in Green)", fontsize=12)
ax1.plot(sdate, shighs, color='green')
ax1.plot(sdate, dvhighs, color = 'red')
ax1.tick_params(axis='both', which = 'major', labelsize =16)

#lows
plt.style.use('seaborn')
fig, ax2 = plt.subplots()
ax2.set_xlabel('', fontsize=10)
ax2.set_ylabel("Sitka and Death Valley Lows in 2018\n(Sitka in Green)", fontsize=12)
ax2.plot(sdate, slows, color='green')
ax2.plot(sdate, dvlows, color = 'red')
ax2.tick_params(axis='both', which = 'major', labelsize =16)

plt.show()
