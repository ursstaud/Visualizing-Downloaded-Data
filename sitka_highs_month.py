import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f: #assign resulting file to f
	reader = csv.reader(f) #call csv.reader() method and pass it f, which creates a reader object associated
	#with that file
	header_row = next(reader)#next() returns the next file of the file when passed the reader object
	#print(header_row) #stored in a list

	for index, column_header in enumerate(header_row): #this function returns the index and value of each item
		print(index, column_header)

	#get high temperatures for this file
	highs, dates = [], []
	for row in reader :
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5]) #printing each row from index 5 (tmax) and assign it to variable high
		dates.append(current_date)
		highs.append(high)
print(highs)

#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
plt.title("Daily High Temperatures, July 2018", fontsize=24)
plt.xlabel(' ', fontsize=10)
fig.autofmt_xdate() #draws the date labels diagonally to prevent overlap
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

