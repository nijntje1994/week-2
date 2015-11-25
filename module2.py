import csv
import sys
import random

f = open("test.csv", 'wt',newline='')
try:
    writer = csv.writer(f)
    writer.writerow( ('nummers', 'gegen') )
    for i in range(100):
        writer.writerow( (i+1, random.randint(1,10000)) )
finally:
    f.close()
