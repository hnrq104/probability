import math, random, itertools, heapq

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
        edge_weight = random.randrange(10)
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


def Djikstra(source, vertices, my_edges):
    #initialize single source
    distance = [math.inf for _ in vertices]
    parent = [None for _ in vertices]
    found = [False for _ in vertices]

    #prepare adjecency list
    adj_list = [[] for _ in vertices]
    for u,v,w in my_edges:
        adj_list[u].append((v,w))

    distance[source] = 0
    H = []
    heapq.heappush(H,(0,source))

    while H:
        _,u = heapq.heappop(H)
        if found[u]: continue
        found[u] = True

        for v, w in adj_list[u]:
            #v was already found!
            if found[v]: continue

            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                heapq.heappush(H,(distance[v],v))
    
    return distance, parent


def floyd_warshal(vertices, my_edges):
    n = len(vertices)
    W = [[math.inf for _ in range(n)] for _ in range (n)] # my matrix
    for i in range(n):
        W[i][i] = 0
    for u,v,w in my_edges:
        W[u][v] = w
    #matrix ready
    D_prev = W
    for k in range(n):
        D_prev = [[min(D_prev[i][j], D_prev[i][k] + D_prev[k][j]) for j in range(n)] for i in range(n)]
    return D_prev

vtx = [0,1,2,3,4]
edges = set([(0,1,3), (0,2,8), (0,4,-4),
             (1,3,1),(1,4,7),
             (2,1,4),
             (3,0,2),(3,2,-5),
             (4,3,6)])

print(BellmanFord(0,my_vertex,my_edges))
print(Djikstra(0,my_vertex,my_edges))

print("Warshal!")
for dist in floyd_warshal(vtx,edges):
    print(dist)

