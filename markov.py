import math
import numpy as np


''' 7.1 '''
linear_system = np.array(
    [[-10,1,1,9],
     [3,-9,7,1],
     [1,7,-9,0],
     [1,1,1,1]])

x = np.linalg.solve(linear_system,np.array([0,0,0,1]))

P = np.matrix([[0,3/10,1/10,3/5],
              [1/10,1/10,7/10,1/10],
              [1/10,7/10,1/10,1/10],
              [9/10,1/10,0,0]])

''' x should be the stationary distribution'''
print(f"a) resolving the linear system x = {x}, x*P = {x*P}")

''' We found the eigenvector! (b)'''
res = np.array([1,0,0,0]) * np.linalg.matrix_power(P,32)
print(f"b) (1,0,0,0) * P^32 = {res}, P(0,3)^32 = {res[0,3]}")

''' (c) '''
start = np.ones(4)/4
res = start * np.linalg.matrix_power(P,128)
print(f"c) after 128 steps = {res}, P(0,3)^128 = {res[0,3]}")

'''(d) this is interesting'''
small_t = 0
values = [0.01,0.001]
val_t = []
for d in values:
    small_t = 0
    while True:
        Pt = np.linalg.matrix_power(P,small_t)
        diff = np.abs(x - Pt[0,])
        if diff.max() < 0.01:
            val_t.append(small_t)
            break
        small_t+=1

print(f"d) maxs <= {values[0]} : t = {val_t[0]}")
print(f"d) maxs <= {values[1]} : t = {val_t[1]}")



