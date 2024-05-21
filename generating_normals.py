import math
import random

def random_standard_normal():
    """
        Returns two samples from a standard normal RV
        mean =  0, standart deviation = 1
    """    
    U,V = random.random(),random.random()
    Theta = 2*math.pi*U
    Radius = math.sqrt(-2*(math.log(V)))
    return Radius*math.cos(Theta), Radius*math.sin(Theta)

def standard_normal_without_trig():
    "Same as before without trignometric functions!"
    U,V = random.random(), random.random()
    while(U**2 + V**2 > 1): U,V = random.random(), random.random()
    S = U**2 + V**2

    X = U*(math.sqrt(-2*math.log(S)/S))
    Y = V*(math.sqrt(-2*math.log(S)/S))
    return (X,Y)


from time import perf_counter
foos = [random_standard_normal,standard_normal_without_trig]
n = 100
for f in foos:
    t = perf_counter()
    a = [f() for _ in range(n)]
    elapsed = perf_counter() - t
    print(f"{n} * {f.__name__} took {elapsed}")
