import csv

# assign file to a variable
filename = "data/knmi_stations_2018.csv"

# open the file
with open(filename) as f:
    # Read content of file
    reader = csv.reader(f, delimiter=";")
    # Get the first row of the file. Usually the header
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get the station number and name
    station_number = []
    station_name = []
    for row in reader:
        number = int(row[0])
        station_number.append(number)

        name = str(row[4])
        station_name.append(name)

    # Create dictionary with station number and name
    station_dictionary = dict(zip(station_number, station_name))

# Print the station dictionary value by using get() and passing in the key, in this case key 344 have value of Rotterdam
print(station_dictionary.get(344))
