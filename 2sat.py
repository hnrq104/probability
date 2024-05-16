''' Chapter 7'''

import math,random,itertools
import random

m = 5
n = 4

variables = [False for _ in range(n)]

# I will begin with the clause in the book (x1 ∨ x2 ) ∧ (x1 ∨ x3 ) ∧ (x1 ∨ x2 ) ∧ (x4 ∨ x3 ) ∧ (x4 ∨ x1 )

# Clauses are of the form ((x1, bool), (x2,bool)) where the bool represents if it's not negated and 
# xi is the number representing the variable

clauses = [((0,True),(1,False)),
           ((0,False),(2,False)),
           ((0,True),(1,True)),
           ((3,True),(2,False)),
           ((3,True),(0,False))]


def satisfied(variables, clause):
    for x, cap in clause:
        if not (variables[x] ^ cap): return True
    return False

print(satisfied(variables,clauses[1]))

def sat2(n,clauses):
    '''
    n is the number of variables
    '''

    #   Start with an arbitrary truth assignment
    m = len(clauses)

    variables = [False for _ in range(n)]
    
    unsatisfied = []
    for i, clause in enumerate(clauses):
        if not satisfied(variables,clause): unsatisfied.append(i)

    #repeat up to 2mn² times. terminating if all clauses are satisfied
    for i in range(2*m*n*n):
        if len(unsatisfied) == 0:
            return True, variables

        #this is really bad :(!
        #choose an arbitrary not satisfied clause
        c_idx = random.choice(unsatisfied)
        bad_clause = clauses[c_idx]

        #pick a random variable from that clause to be flipped
        k = len(bad_clause) #this is just for readabilty
        var_idx, _ = bad_clause[random.randrange(k)]

        #flip it
        variables[var_idx] = not variables[var_idx]

        #really, really not optimized use a set later and preprocess stuff!
        #I can preprocess to check only for the clauses which we may have changed (but I will check all again)
        unsatisfied.clear()
        for i, clause in enumerate(clauses):
            if not satisfied(variables,clause): unsatisfied.append(i)
        
    if len(unsatisfied) == 0:
        return True, variables

    return False, None

print(sat2(4,clauses))

def modified_sat3(n,clauses):
    m = len(clauses)

    unsatisfied = []
    for i in range(3*m):
        #generate a random truth assignment
        variables = [True if random.random() <= 1/2 else False for _ in range(n)]
        
        for j in range(3*n):
            unsatisfied.clear()
            for i, clause in enumerate(clauses):
                if not satisfied(variables,clause): unsatisfied.append(i)
        
            if len(unsatisfied) == 0:
                return True, variables

            c_idx = random.choice(unsatisfied)
            bad_clause = clauses[c_idx]
            var_idx, _ = bad_clause[random.randrange(len(bad_clause))]
            variables[var_idx] = not variables[var_idx]

    if len(unsatisfied) == 0:
        return True, variables

    return False, None    


