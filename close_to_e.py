import math


i = 1
x = 2
while(abs(x-1/math.e)*math.e > 0.0000001):
    i+=1
    x = math.pow(1 - 1/i,i)
print(i)