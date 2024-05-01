import math, random, itertools

''' In this script, I will create a random directed weighted graph and run Bellman Ford on it to check 
distances from the vertex 0 '''

n = 10
my_vertex = [i for i in range(10)]

p_edge = 1/2

my_edges = set()
for u,v in itertools.permutations(my_vertex,2):
    if random.random() <= p_edge:
        #the edge exists!
        #I will start with a random uniform weight distribution
        edge_weight = random.uniform(-10,10)
        my_edges.add((u,v,edge_weight))

adjecency_list = [[] for _ in range(n)]
for u,v,w in my_edges:
    adjecency_list[u].append((v,w))



def BellmanFord(source, vertices, edges):
    dist = [math.inf for _ in vertices]
    parents = [None for _ in vertices]

    dist[source] = 0

    def relax(d,p, edge):
        u,v,w = edge
        if d[u] + w < d[v]:
            d[v] = d[u] + w
            p[v] = u
            return True
        return False


    for _ in range(len(vertices)):
        for e in edges:
            relax(dist,parents,e)

    for e in edges:
        if relax(dist,parents,e):
            return False,None,None
    
    return True, dist, parents


print(BellmanFord(0,my_vertex,my_edges))
