import random
import itertools
def monte_carlo_pi(n)->float:
    pi = 0
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            pi+=1
    return 4*pi/n

''' A very interesting DNF counting randomized algorithm! '''

#clauses are [[(1,true),(3,false)],[(13,true),(1,false),(2,true)..] ...]
def dnf_count(clauses:list, m):
    variables = dict()
    for c in clauses:
        for (v,_) in c:
            variables[v] = False

    sci_sizes = []
    n = len(variables)
    for c in clauses:
        sci_sizes.append(2**(n-len(c)))
    cumulative_prob = [s for s in itertools.accumulate(sci_sizes)]
    
    X = 0
    for _ in range(m):
        '''unoptimized generation of assignment but ok'''
        c_idx = random.choices(population=range(len(clauses)),cum_weights=cumulative_prob,k=1)[0]
        for key in variables.keys():
            variables[key] = random.choice([True,False])
        for (v,b) in clauses[c_idx]:
            variables[v] = b

        '''checks if our assignment is true for any previous clause'''
        #this here should be a function!
        in_S = True
        for j in range(c_idx):
            '''checks if a is in SC_j'''
            ok = False
            for (clause_var,bool_val) in clauses[j]: 
                if variables[clause_var] != bool_val:
                    ok = True
            if not ok:
                in_S = False
                break

        if in_S: X+=1

    return (X/m)*sum(sci_sizes)

def assignment_generator(n,m):
    assignment = []
    for _ in range(m):
        number_of_variables = random.randint(1,n)
        clause_var = random.sample(range(n),k=number_of_variables)
        clause = [(c,random.choice([True,False])) for c in clause_var]
        assignment.append(clause)
    return assignment

def dnf_bad_count(assignment):
    X = 0
    variables = dict()
    for clause in assignment:
        for (v,_) in clause:
            if v not in variables:
                variables[v] = len(variables)
    
    n = len(variables)
    for p in itertools.product([True,False],repeat=n):
        ok = False
        for clause in assignment:
            aceita = True
            for (var,bool_val) in clause:
                if p[variables[var]] is not bool_val:
                    aceita = False
            if aceita is True:
                ok = True
                break
        if ok:
            X+=1
    return X

import time
um_assignment = assignment_generator(20,1)
t = time.perf_counter()
x = dnf_count(um_assignment,1000)
t = time.perf_counter() - t
print(f"contei {x} demorei {t}s")

t = time.perf_counter()
x = dnf_bad_count(um_assignment)
t = time.perf_counter() - t
print(f"contei {x} demorei {t}s")
