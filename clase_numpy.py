import numpy as np
import time

n = 1000000

#Lista en python


l1 = list(range(n))
l2 = list(range(n))

start = time.time()
l3 = [] 

for x in range(len(l1)):
    l3.append(l1[x]+l2[x])
print('Total segundos Lista: ',((time.time() - start)*1000))


#Lista en numpy

n1 = np.arange(n)
n2 = np.arange(n)

start = time.time()

n3 = n1 + n2 

print('Total segundos Numpy: ',((time.time() - start)*1000))

