import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data/KNMI_20181231.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    station_number, date, average_temp, min_temp, max_temp = [], [], [], [], []

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
            if row[11].isspace():
                average_temp.append(0)
            else:
                average_temp.append(int(row[11]))
            if row[12].isspace():
                min_temp.append(0)
            else:
                min_temp.append(int(row[12]))
            if row[13].isspace():
                max_temp.append(0)
            else:
                max_temp.append(int(row[14]))
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
# show last data that was gathered of min_temp
ax.plot(date[-10:], min_temp[-10:], c='red')

# draws date label diagonally
fig.autofmt_xdate()

plt.show()
