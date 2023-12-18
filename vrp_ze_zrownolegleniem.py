import random
import networkx as nx
from vrpy import VehicleRoutingProblem
import time
import multiprocessing

def generate_random_edges(G, num_cities, start, end):
    for i in range(start, end):
        G.add_node(i)

        G.add_edge("Source", i, cost=random.randint(1, 10), time=random.randint(1, 10))
        G.add_edge(i, "Sink", cost=random.randint(1, 10), time=random.randint(1, 10))

        for j in range(1, num_cities + 1):
            if i != j:
                G.add_edge(i, j, cost=random.randint(1, 10), time=random.randint(1, 10))

def main():
    num_cities = 30
    start = time.time()

    G = nx.DiGraph()

    G.add_node("Source")
    for i in range(1, num_cities + 1):
        G.add_edge("Source", i, cost=random.randint(1, 10), time=random.randint(1, 10))

    G.add_node("Sink")
    for i in range(1, num_cities + 1):
        G.add_edge(i, "Sink", cost=random.randint(1, 10), time=random.randint(1, 10))

    processes = []

    num_processes = multiprocessing.cpu_count()
    chunk_size = num_cities // num_processes

    for i in range(num_processes):
        start_idx = i * chunk_size + 1
        end_idx = start_idx + chunk_size if i != num_processes - 1 else num_cities + 1

        process = multiprocessing.Process(target=generate_random_edges, args=(G, num_cities, start_idx, end_idx))   # zrownoleglony proces dodawania wierzcholkow i krawedzi w grafie
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Nodes in the graph:", G.nodes)

    prob = VehicleRoutingProblem(G, load_capacity=10, duration=170) # rozwiązanie problemu vrp przy uzyciu wbudowanej biblioteki
    prob.solve()

    end = time.time()
    print("Computing duration: ", end - start)
    print(prob.best_value)
    print(prob.best_routes)

if __name__ == "__main__":
    main()
