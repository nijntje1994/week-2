import matplotlib.pyplot as plt
import csv
import numpy as np

file = open("osdinge.csv", 'rt')

data = csv.reader(file)

lijst = []
for i,line in enumerate(data):
    lijst.append(line)

lnaam = lijst[0][1:8]
l2011 = lijst[1][1:8]
l2012 = lijst[2][1:8]
l2013 = lijst[3][1:8]
l2014 = lijst[4][1:8]

Win7 = [l2011[0],l2012[0],l2013[0],l2014[0]]
WinXP = [l2011[1],l2012[1],l2013[1],l2014[1]]
WinVista = [l2011[2],l2012[2],l2013[2],l2014[2]]
OSX = [l2011[3],l2012[3],l2013[3],l2014[3]]
Win8 = [l2011[4],l2012[4],l2013[4],l2014[4]]
Win81 = [l2011[5],l2012[5],l2013[5],l2014[5]]
Linux = [l2011[6],l2012[6],l2013[6],l2014[6]]

plt.plot(Win7, label=lnaam[0])
plt.plot(WinXP, label=lnaam[1])
plt.plot(WinVista, label=lnaam[2])
plt.plot(OSX, label=lnaam[3])
plt.plot(Win8, label=lnaam[4])
plt.plot(Win81, label=lnaam[5])
plt.plot(Linux, label=lnaam[6])
plt.title('Top 7 Besturingssystemen')
plt.xlabel('Jaar')
plt.ylabel('Procent')
plt.xticks( np.arange(4),('2011','2012','2013','2014'))
plt.legend(loc='upper left')
plt.show()

##print(lnaam)
##print(l2011)
##print(l2012)
##print(l2013)
##print(l2014)