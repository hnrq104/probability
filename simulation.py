''' Exercise 8.27  simulation for a bank of n M/M/1 FIFO queues'''

import numpy as np
import collections, heapq
from enum import Enum


''' ET refers to EVENT TYPE '''
class ET(Enum):
    ARRIVAL = 0
    FINISH = 1

class bank_queue:
    def __init__(self,rate_in = 1/2, service_mean = 1, constant_service = False) -> None:
        self.T = 0
        self.rate_in = rate_in
        self.service_mean = service_mean
        self.constant_service = constant_service

        self.served_customers = []
        self.event_queue = []
        self.true_queue = collections.deque()
        self.add_customer()

    def add_customer(self):
        ''' Adds a customer to event QUEUE '''

        arriving_time = self.T + np.random.exponential(1/self.rate_in)
        heapq.heappush(self.event_queue,(arriving_time,ET.ARRIVAL))

    def add_service(self):
        ''' Adds service finish to event queue '''
        finishing_time = self.T
        
        if self.constant_service: 
            finishing_time += self.service_mean
        else: 
            finishing_time += np.random.exponential(self.service_mean)
        
        heapq.heappush(self.event_queue,(finishing_time,ET.FINISH))

    def next_event(self):
        event = heapq.heappop(self.event_queue)
        self.T = event[0]

        if event[1] == ET.ARRIVAL:
            self.true_queue.appendleft(event[0]) #customer currently in bank_queue!
            #se ele for o primeiro da fila, adiciona o tempo de finalizar
            if len(self.true_queue) == 1:
                self.add_service()
            
            #calcula chegada do proximo cliente
            self.add_customer()

        if event[1] == ET.FINISH:
            finished_customer_arrival = self.true_queue.pop()
            self.served_customers.append((finished_customer_arrival,self.T))
            #Se a fila não estiver vazia, adiciona proximo tempo de finalizar

            if self.true_queue:
                self.add_service()
    

T = 10000
N = 100
SERVICE_TIME_MEAN = 1

for rate in [0.5,0.8,0.9,0.99]:
    time_per_customer = []
    for _ in range(N):
        bq = bank_queue(rate_in=rate,service_mean=SERVICE_TIME_MEAN,constant_service=True)
        while(bq.T < T):
            bq.next_event()
        time_per_customer += [(f-a) for a,f in bq.served_customers if f < T]

    print(f"T={T}\tN={N}\tLAMBDA={rate}\tservice_mean={SERVICE_TIME_MEAN}\tCONSTANT TIME = TRUE")
    print(np.average(time_per_customer))




