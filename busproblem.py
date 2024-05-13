import math,itertools,random
import numpy as np

# (ui,ti)
# buses = [(1,2),(1.1,2),(3,4),(0.5,15),(10,1),(3.3,4.1)]

buses = [(random.random()*10 + 1 ,random.random()*50 + 1) for _ in range(10)]

def calc_expectation(buses):
    thetas = np.array([1/u for u,_ in buses])
    times = np.array([t for _,t in buses])
    
    return (1 + np.dot(thetas,times))/thetas.sum()

print(calc_expectation(buses))


min_value = None
min_comb = None
for k in range(1,len(buses) + 1):
    for c in itertools.combinations(buses,k):
        e = calc_expectation(c)
        if min_value is None or e < min_value:
            min_value = e
            min_comb = c
        # print(k,c,f"\tExpected time = ",calc_expectation(c))

print(f"Min Expected time = {min_value}\t",min_comb)


random.shuffle(buses)
previous_best = []
for i in range(1,len(buses)):
    current_best = previous_best.copy()
    c = math.inf if not current_best else calc_expectation(current_best)

    for bus in buses:
        if bus in previous_best: continue
        expectation = calc_expectation(previous_best + [bus])
        if expectation < c:
            c = expectation
            current_best = previous_best + [bus]
    
    if not previous_best or c < calc_expectation(previous_best):
        previous_best = current_best

print(current_best)    
    