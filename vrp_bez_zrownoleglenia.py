import random
from networkx import DiGraph
from vrpy import VehicleRoutingProblem
import time

G = DiGraph()   # do korzystania z vrpy nalezy stworzyc graf skierowany

num_cities = 30  # wpisywana liczba miast
start = time.time()


# generowanie losowych wartości odległości między miastami (w następnym kroku wzbogacenie o zapisywanie danych do pliku w celu powtarzalności)
for i in range(1, num_cities + 1):
    G.add_edge("Source", i, cost=random.randint(1, 10), time=random.randint(1, 10))  
    G.add_edge(i, "Sink", cost=random.randint(1, 10), time=random.randint(1, 10)) 

    for j in range(1, num_cities + 1):
        if i != j:
            G.add_edge(i, j, cost=random.randint(1, 10), time=random.randint(1, 10)) 

# określenie zapotrzebowania klientów
for node in range(1, num_cities + 1):
    G.nodes[node]["demand"] = random.randint(1, 10) 


prob = VehicleRoutingProblem(G, load_capacity=10, duration=170)

prob.solve()
end = time.time()
print("Computing duration: ", end-start)
print(prob.best_value)
print(prob.best_routes)
