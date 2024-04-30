'''
Refers to chapter 5.8 of Probability and Computing
'''
import random

class marked_tree:
    def __init__(self,n):
        self.N = (1<<n) - 1
        self.tree = [False for i in range(self.N)]
        self.marked = 0

    def mark(self,x):
        #already marked
        if self.tree[x]: return
        
        self.marked += 1
        self.tree[x] = True
        #0 has no sibling nor parent

        #up
        if (x != 0):    
            sibling = x - 1 if x%2 == 0 else x + 1
            parent = (x-1)//2
            if self.tree[sibling]: self.mark(parent)
            if self.tree[parent]: self.mark(sibling)

        #down
        left_child, right_child = 2*x + 1, 2*x + 2
        if(right_child < len(self.tree)):
            if self.tree[left_child]: self.mark(right_child)
            if self.tree[right_child]: self.mark(left_child)

#as we are dealing with complete trees, I can use an array to make it way faster!

#Process 1:
def process_1(n):
    my_tree = marked_tree(n)
    steps = 0
    x = 0
    while(my_tree.marked != my_tree.N):
        x = random.randrange(my_tree.N)
        my_tree.mark(x)
        steps +=1
    return steps,x #following the tip

def test_1():
    avarages = []
    for i in range(10,21):
        avarage = 0
        for j in range(10):
            steps,_ = process_1(i)
            avarage+=steps
        avarages.append(avarage/10)

    for (n,avg_steps) in zip(range(10,21),avarages):
        print(f"n = {n}, Avarage steps = {avg_steps}")


def process_2(n):
    my_tree = marked_tree(n)
    steps = 0
    my_ordering = random.sample(range(my_tree.N),k=my_tree.N)
    for a in my_ordering:
        steps+=1
        if my_tree.tree[a]: continue
        my_tree.mark(a)
        if my_tree.marked == my_tree.N: break

    return steps

def test_2():
    avarages = []
    for i in range(10,21):
        avarage = 0
        for j in range(10):
            steps = process_2(i)
            avarage+=steps
        avarages.append(avarage/10)

    for (n,avg_steps) in zip(range(10,21),avarages):
        print(f"n = {n}, Avarage steps = {avg_steps}")


def process_3(n):
    #I think I have a fast way of trying this
    my_tree = marked_tree(n)
    steps = 0
    my_ordering = random.sample(range(my_tree.N),k=my_tree.N)
    # print(my_ordering)
    for a in my_ordering:
        if my_tree.tree[a]: continue
        my_tree.mark(a)
        steps+=1
        if my_tree.marked == my_tree.N: break

    return steps

def test_3():
    avarages = []
    for i in range(10,21):
        avarage = 0
        for j in range(10):
            steps = process_3(i)
            avarage+=steps
        avarages.append(avarage/10)

    return zip(range(10,21),avarages)
        



''' Here I will test multiprocessing, as this is highly parallel!'''

from multiprocessing import Pool
import numpy
import time
def mp_test_3():
    avarages = []
    for i in range(10,21):
        steps = []
        with Pool(10) as p:
            steps = p.map(process_3, [i for j in range(10)])
        avarages.append(numpy.average(steps))
    return zip(range(10,21),avarages)
        

t = time.perf_counter()
res = mp_test_3()
elapsed_time = time.perf_counter() - t
print(f"mp_test_3() took {elapsed_time}s") 
for n,avg_steps in res:
    print(f"n = {n}, Avarage steps = {avg_steps}")
