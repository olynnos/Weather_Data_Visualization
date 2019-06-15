import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/KNMI_20181231.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    station_number, date, average_temp, min_temp, max_temp, missing_data = [], [], [], [], [], []

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    for row in reader:
        # remove empty lines otherwise it will cause list index out of range error
        if not row:
            continue

        if int(row[0]) == 344:
            station_number.append(int(row[0]))
            # date.append(row[1])
            datetm = "-".join([row[1][:4], row[1][4:6], row[1][6:]])
            date_formatted = datetime.strptime(datetm, '%Y-%m-%d')
            date.append(date_formatted)
            # using a try except else block to handle missing data error
            try:
                average_temp.append(int(row[11])*0.1)
                min_temp.append(int(row[12]) * 0.1)
                max_temp.append(int(row[14]) * 0.1)
            except ValueError as e:
                missing_data.append(str(e))
                # print(f"Missing data from {date_formatted}")
            else:
                average_temp.append(int(row[11]) * 0.1)
                min_temp.append(int(row[12]) * 0.1)
                max_temp.append(int(row[14]) * 0.1)

            # another way of handling error from missing data
            # if row[11].isspace():
            #     average_temp.append(0)
            # else:
            #     average_temp.append(int(row[11])*0.1)
            # if row[12].isspace():
            #     min_temp.append(0)
            # else:
            #     min_temp.append(int(row[12])*0.1)
            # if row[13].isspace():
            #     max_temp.append(0)
            # else:
            #     max_temp.append(int(row[14])*0.1)
        else:
            continue

    # rotterdam_data = dict(zip(station_number, date, min_temp, max_temp, average_temp))

    rotterdam_data = {date: {'stn_nmbr': station_number, 'min_temp': min_temp, 'max_temp': max_temp, 'avg_temp':
        average_temp } for date, station_number, min_temp, max_temp, average_temp in zip(date, station_number, min_temp,
                                                                                         max_temp, average_temp)}

# print(rotterdam_data.get("20181231"))
# print(len(min_temp))

plt.style.use('seaborn')
fig, ax = plt.subplots()

plt.title('Min and max temp of the last 100 readings', fontsize=20)
plt.ylabel("Temperature in (C)", fontsize=10)
plt.xlabel("Day of recorded temp", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=10)

# show last data that was gathered of min_temp
ax.plot(date[-100:], min_temp[-100:], c='blue')
ax.plot(date[-100:], max_temp[-100:], c='red')
plt.fill_between(date[-100:], max_temp[-100:], min_temp[-100:], facecolor="grey", alpha=0.1)

# draws date label diagonally
fig.autofmt_xdate()

print(len(missing_data))

plt.show()
