import csv
f = open("osdinge.csv", 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print (row[0])
        print (row[2])
finally:
    f.close()


plt.plot([1,4,9,16],'r')    # bcgkmrwy
plt.plot([1,2,3,4], 'v')    # .,ov etc.
plt.plot([2,3,4,5], '--')   # - -- -. :
plt.plot([4,5,6,7], 'k-.v') # all
plt.show()