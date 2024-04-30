import random
# Exercise 5.21 Probability and Computing

class disjoint_set():
    def __init__(self,number):
        self.n = number
        self.size = 1
        self.rep = number

def find_rep(ds, a):
    if (ds[a].rep == a) :
        return a
    else:
        ds[a].rep = find_rep(ds,ds[a].rep)
        return ds[a].rep

def union(ds,a,b):
    arep = find_rep(ds,a)
    brep = find_rep(ds,b)

    if(arep == brep): return 

    if(ds[arep].size > ds[brep].size):
        ds[arep].size += ds[brep].size
        ds[brep].rep = arep
    else:
        ds[brep].size += ds[arep].size
        ds[arep].rep = brep    


# n is number of vertices
# adds edges randomly until graph is connected, return number of edges added
# as of exercise b will also return number of edges added until there are no more isolated vertices
def edges_until_connected(n):
    comp = n
    isolated = n
    lonely_guys = True
    isolated_edges = 0
    ds = [disjoint_set(i) for i in range(n)]
    edge_set = set()
    while(comp != 1):
        a,b = random.randrange(n), random.randrange(n)
        if a == b: continue
        
        a,b = min(a,b),max(a,b)
        if (a,b) in edge_set:
            continue
    
        edge_set.add((a,b))
        arep, brep = find_rep(ds,a), find_rep(ds,b)
        
        if ds[arep].size == 1: #exercise 5.21 b
                isolated -=1
        if ds[brep].size == 1:
                isolated -=1
        
        if lonely_guys and isolated == 0:
            lonely_guys = False
            isolated_edges = len(edge_set)

        if  arep != brep:
            comp -=1
            union(ds,a,b)
    
    return len(edge_set), isolated_edges


experiment_trials = 100
experiment_sizes = [100*i for i in range(1,11)]

avarages = []
for size in experiment_sizes:
    avarage = [0,0]
    for trial in range(experiment_trials):
        con,isol = edges_until_connected(size)
        avarage[0] += con
        avarage[1] += isol
    avarage[0] /= experiment_trials
    avarage[1] /= experiment_trials
    avarages.append(avarage)

#this is taking too long, it would be way faster in c or go (and it is easily made parallel)

for n,(con,iso) in zip(experiment_sizes,avarages):
    print(f"N={n}, Avarage edges till connected:{con:>.2f}, Avarage edges till no one is isolated:{iso:>.2f}")

#this is crazy and seems really wrong!







