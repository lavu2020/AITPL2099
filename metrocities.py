#exercise:create csv file with state and capitals of india
import csv
with open('metrocities.csv')as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    for row in readcsv:
        print(row)

