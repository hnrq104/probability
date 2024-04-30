import itertools
import random

#I will generate a random graph with probability p
n = 100 #number of vertices
my_vtx = [i for i in range(0,n)]


p_edge = 0.5
my_edges = []
for e in itertools.combinations(my_vtx,2):
    if random.random() <= p_edge:
        my_edges.append(e)


p = 0.5
vtx_set = [0 for i in range(len(my_vtx))] #represents A,B
for u in my_vtx:
    if random.random() <= p:
        vtx_set[u] = 1

e_AB = 0
for (u,v) in my_edges:
    if vtx_set[u] != vtx_set[v]: e_AB+=1

print(f"|V(G)|: {n}; |e(G)|: {len(my_edges)}; |e_AB|: {e_AB}")



## greedy aproach
# take a random order of the vertices!

def greedy_take(my_vtx, my_edges) -> int:
    ''' Greedy approach, return number of edges in e_AB '''
    
    order = random.sample(my_vtx,len(my_vtx))
    #this is a preprocessing to fasten things up!
    adjecency_list = [[] for i in range(len(my_vtx))]
    for (u,v) in my_edges:
        adjecency_list[u].append(v)
        adjecency_list[v].append(u)

    vtx_set = [0 for i in range(len(my_vtx))]
    e_AB = 0
    for i in range(len(order)):
        a_neighbors = 0
        b_neighbors = 0
        for neighbor in adjecency_list[i]:
            if neighbor < i:
                if vtx_set[neighbor] == 1:
                    a_neighbors+=1
                else: b_neighbors+=1
        
        if b_neighbors > a_neighbors:
            vtx_set[i] = 1
            e_AB += b_neighbors
        else: e_AB += a_neighbors
    
    return e_AB

print(f"|V(G)|: {n}; |e(G)|: {len(my_edges)}; Greedy |e_AB|: {greedy_take(my_vtx,my_edges)}")








