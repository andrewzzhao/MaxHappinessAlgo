import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from operator import itemgetter
import sys
def merge(G, n1, n2):
    
    neighbors = nx.common_neighbors(G, n1, n2)
    # Create the new node with combined name ---- list(<iterator>), or iterator.next
    name = str(n1) + ' ' + str(n2)


    G.add_node(name)

    #nx.set_node_attributes(G, values, name=None)
    G.nodes[name]["happiness"] = G.nodes[n1].get("happiness", 0) + G.nodes[n2].get("happiness", 0) + G.edges[n1, n2]["happiness"]
    G.nodes[name]["stress"] = G.nodes[n1].get("stress", 0) + G.nodes[n2].get("stress", 0) + G.edges[n1, n2]["stress"]


    for p in neighbors:
        G.add_edge(p,name)
        G[p][name]["happiness"] = G[p][n1]["happiness"] + G[p][n2]["happiness"]
        G[p][name]["stress"] = G[p][n1]["stress"] + G[p][n2]["stress"]
       
    # Remove old nodes
    G.remove_nodes_from([n1, n2])

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k = solve(G, s)


  
