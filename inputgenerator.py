import random
import networkx as nx
from parse import write_input_file

maxStress = 99.69
numPeople = 10
'''
inputs = [[-1 for _ in range(numPeople)] for _ in range(numPeople)]

sums = [random.uniform(30, 250) for _ in range(numRooms)]

constraints = [random.uniform(40, 200) for _ in range(numRooms)]
'''
G = nx.complete_graph(numPeople)

for i in range(numPeople):
    for j in range(i+1, numPeople):
        """
        prev_edge = list(G.edges)[i]
        print(prev_edge)
        """
        G[i][j]["happiness"] = round(random.uniform(20,100), 3)
        G[i][j]["stress"] = round(random.uniform(10,70), 3)
        
write_input_file(G, maxStress, "backup/10.in")
