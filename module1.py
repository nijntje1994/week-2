import csv


f = open("ding.csv", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print (row[0])
        print (row[2])
finally:
    f.close()