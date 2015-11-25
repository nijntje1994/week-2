import csv
import random
import string
from datetime import date

##csv.register_dialect("pk",delimiter=';')
fin = open("ding.csv", 'rt')
fout = open("ding2.csv", 'wt',newline='')
try:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    klantnr= 0
    for row in reader:
        print(row)
        if (row[0] == 'naam'):
            row.append('Leeftijd')
            row.append('Password')
            row.append('Klantnummer')
            row.append('Username')
        else:
            row.append(date.today().year - int(row[1]))
            row.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
            row.append(klantnr)
            klantnr += 1
            row.append(row[0] + row[1])
            print(row)
            writer.writerow(row)
finally:
    fin.close()
    fout.close()