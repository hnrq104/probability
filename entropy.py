import math

''' exercise 10.1 '''
def calc_entropy(k:int, alpha:float):
    S = 0
    sum_log = 0
    for i in range(1,k+1):
        power = i**alpha
        S += 1/(power)
        sum_log += math.log2(i)/power
    return math.log2(S) + alpha*sum_log/S

# as expected, entropy decreases !
values = [(10,2),(10,3),(10,10)]
for (k,a) in values:
    print(f"Entropy of X_{a}: {calc_entropy(k,a)}")