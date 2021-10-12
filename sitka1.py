import csv
import matplotlib.pyplot as plt

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)
    #use index to put number in front of header (to know what index you need to find info)

highs = []

for row in csv_file:
    highs.append(int(row[5]))
    #append adds to list

print(highs)

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

plt.plot(highs,c="red")

plt.show()