import matplotlib.pyplot as plt
import numpy as np


plt.plot([1,2,4,9,16,25,36,1])
plt.show()


plt.plot([7,8,9,10,11,12,13,14,15,16,17,18],[10, 10, 10, 30, 20, 25,30, 35, 70, 75, 80, 10])
plt.axis([7, 18, 0, 100])
plt.title('dingen')
plt.xlabel('tijd')
plt.ylabel('Procent')
plt.grid(True)
plt.annotate('hier gebeuren dingen', xy=(17,80), xytext=(15,80),arrowprops=dict(facecolor='black'))

x = np.arange(1, 5)
plt.plot(x, x*1.5, label='vandaag')
plt.legend(loc='upper left') # best / upper/lower/left/right
plt.show()



