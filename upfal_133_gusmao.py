'''
GUSMÃO!
Refers to chapter 5.8 of Probability and Computing
'''
import random, time

class sampleable_int_set():
    def __init__(self, n):
        self.pos_by_element = {x : x for x in range(n)}
        self.elements = list(range(n))

    def add(self, x):
        if x in self.pos_by_element:
            return
        self.elements.append(x)
        self.pos_by_element[x] = len(self.elements)-1

    def remove(self, x):
        position = self.pos_by_element.pop(x)
        last = self.elements.pop()
        if position != len(self.elements):
            self.elements[position] = last
            self.pos_by_element[last] = position

    def pick_random_element(self):
        return random.choice(self.elements)

class marked_tree:
    def __init__(self, h, support_unmarked_choice=False):
        self.N = (1 << h) - 1
        self.tree = [False for i in range(self.N)]
        self.unmarked_set = sampleable_int_set(self.N) if support_unmarked_choice else None
        self.marked = 0

    def mark(self, x):
        #already marked
        if self.tree[x]: return
        
        self.marked += 1
        self.tree[x] = True
        if self.unmarked_set is not None: self.unmarked_set.remove(x)

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
def process_1(h):
    my_tree = marked_tree(h)
    steps = 0
    x = 0
    while(my_tree.marked != my_tree.N):
        x = random.randrange(my_tree.N)
        my_tree.mark(x)
        steps +=1
    return steps, x #following the tip

#Process 2:
def process_2(h):
    my_tree = marked_tree(h)
    steps = 0
    my_ordering = random.sample(range(my_tree.N), k=my_tree.N)
    for x in my_ordering:
        steps += 1
        if my_tree.tree[x]: continue
        my_tree.mark(x)
        if my_tree.marked == my_tree.N: break

    return steps, x

#Process 3:
def process_3(h):
    my_tree = marked_tree(h, True)
    steps = 0
    while my_tree.marked < my_tree.N:
        x = my_tree.unmarked_set.pick_random_element()
        my_tree.mark(x)
        steps += 1
    return steps, x

def test(process, min_depth, max_depth, repetitions):
    for h in range(min_depth, max_depth + 1):
        total_steps = 0
        start = time.time()
        for _ in range(repetitions):
            steps,_ = process(h)
            total_steps += steps
        elapsed = time.time() - start
        print("h = %2d,   avg steps = %7d,   avg duration (millis) = %4d" % (h, total_steps/repetitions, 1000*elapsed/repetitions))

# Tests all processes
for process in [process_1, process_2, process_3]:
    print(process.__name__)
    test(process, 10, 20, 10)
    print()

