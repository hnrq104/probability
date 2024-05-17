''' Exercise 8.25 '''
import random
import numpy as np
#feedback pr(next ball in bin1) = x^p/(x^p + y^p)

bins = [51,49]

def bnb_with_feedback(p, bins : list[int], treshold):
    new_bins = bins.copy()
    n = sum(new_bins)

    while max(new_bins) < treshold * n:
        xp = new_bins[0]**p
        yp = new_bins[1]**p
        
        # print(new_bins,xp,yp)

        n+=1
        if random.random() <= xp/(xp + yp):
            new_bins[0]+=1
        else : new_bins[1]+=1

    return n, (0 if new_bins[0] > new_bins[1] else 1)

numbers = [bnb_with_feedback(1.5,[51,49],0.6) for _ in range(100)]
# print(numbers)
#a) 
bin1_wins = 0
for (balls,victor) in numbers:
    if victor == 0:
        bin1_wins +=1

print(f"Avarage number of balls thrown: {np.average([x[0] for x in numbers])}")
print(f"How often bin 1 has the majority: {bin1_wins/100}")
