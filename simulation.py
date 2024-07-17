''' Exercise 8.27  simulation for a bank of n M/M/1 FIFO queues'''
import numpy as np
import collections, heapq
from enum import Enum

''' 
    Comentario: 12/Jul 
    Revisitei o código depois que o professor passou como trabalho. 
    A primeira iteração - bank_queue, foi feita a 2 meses atrás quando vi o problema pela primeira vez.
    A segunda (e possíveis posteriores) - bank_queue2, foi feita hoje.
    '''

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



class bank_queue2:
    ''' Após seguir a dica do Professor Gusmão
        bank_queue2 simula o mesmo processo sem usar nenhuma estrutura complicada, tornando-o bem mais rápido.
        tentar fazer sem uma deque '''
    
    def __init__(self,rate_in = 1/2, service_mean = 1, constant_service = False) -> None:
        self.rate_in = rate_in
        self.service_mean = service_mean
        self.constant_service = constant_service

        #nessa fila sempre haverá alguém no serviço, eu sempre pularei o estado 0
        self.T = np.random.exponential(1/self.rate_in)
        self.in_service = self.T
        self.next_in_line = self.T + np.random.exponential(1/self.rate_in)
        self.served_customers = []
    
    def finish_service(self):
        service_time = self.service_mean if self.constant_service else np.random.exponential(self.service_mean)
        
        self.served_customers.append((self.in_service, self.T + service_time))
        if self.T + service_time < self.next_in_line:
            self.T = self.next_in_line
        else:
            self.T = self.T + service_time

        self.in_service = self.next_in_line
        self.next_in_line = self.in_service + np.random.exponential(1/self.rate_in)



''' simulation part!'''
T = 10000
N = 100

# servidos_bq = 0
# servidos_bq2 = 0
# for i in range(N):
#     bq = bank_queue(rate_in=0.8,service_mean=1)
#     bq2 = bank_queue2(rate_in=0.8,service_mean=1)
#     while(bq.T < 10000):
#         bq.next_event()
#     while(bq2.T < 10000):
#         bq2.finish_service()
#     servidos_bq += len(bq.served_customers)
#     servidos_bq2 += len(bq2.served_customers)

# print("sanity check")
# print(f"# de clientes servidos bq: {servidos_bq/N}")
# print(f"# de clientes servidos bq2: {servidos_bq2/N}")

''' Perceba que no problema original, como as filas são independentes, podemos simplesmente
considerar a variável tempo como única a cada fila. E podemos simular cada uma sequencialmente 
para obter o resultado.'''

SERVICE_TIME_MEAN = 1
print("BQ2")
for rate in [0.5,0.8,0.99]:
    time_per_customer = []
    for _ in range(N):
        bq = bank_queue2(rate_in=rate,service_mean=SERVICE_TIME_MEAN,constant_service=True)
        while(bq.T < T):
            bq.finish_service()
        time_per_customer += [(f-a) for a,f in bq.served_customers if f < T]

    print(f"T={T}\tN={N}\tLAMBDA={rate}\tservice_mean={SERVICE_TIME_MEAN}")
    print(np.average(time_per_customer))


'''
Nota de adendo:
Fiquei devendo implementar algumas outras políticas que poderiam ser interessante:
- Diferença entre escolher a menor fila e escolher aleatóriamente
- Se escolher a menor fila, escolher por numero de jobs ou por tempo somado de jobs na fila (ver a diferença)
- Outras políticas de escalonamento, talvez SRTF ou Round-Robin.
Todas ideias são interessantes e me arrependo até de não ter feito.

Adoeci e tive um leve burnout esse final de período (toca Não Creio em Mais Nada - Paulo Sérgio).
Espero que isso melhore depois.
'''

