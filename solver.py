import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
from operator import itemgetter
import sys


def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!

    G_checker = G.copy()
    best_D_so_far = {}
    best_k_so_far = 1
    best_H_so_far = 0.0
    n = nx.number_of_nodes(G)
    for k in range(1, n + 1):
        curr_D = {}
        while len(curr_D) < n:  
            # sort edges by decreasing happiness
            G_happy = G.copy()
            sorted_happiness = sorted(G_happy.edges(data=True), key=itemgetter(0), reverse=True)
            #need to merge nodes A and B
            a, b = sorted_happiness[0]


        
        if is_valid_solution(curr_D, G_checker, s, k):
            if calculate_happiness(curr_D, G_checker) > best_H_so_far:
                best_D_so_far = curr_D
                best_k_so_far = k

        


            #
    # pass
    return best_D_so_far, best_k_so_far

def merge(G, n1, n2):
    # Get all predecessors and successors of two node
    neighbors = nx.common_neighbors(G, n1, n2)
    # Create the new node with combined name ---- list(<iterator>), or iterator.next
    name = str(n1) + '/' + str(n2)
    G.add_node(name)
    G.nodes[name]["happiness"] = (G.nodes[n1].get("happiness", 0) + G.nodes[n2].get("happiness", 0))
    G.nodes[name]["stress"] = (G.nodes[n1].get("stress", 0) + G.nodes[n2].get("stress", 0))



    G.add_edges([(p, name) for p in neighbors])
    for p in neighbors:
        G[p][name]["happiness"] = G[p][n1]["happiness"] + G[p][n2]["happiness"]
        G[p][name]["stress"] = G[p][n1]["stress"] + G[p][n2]["stress"]
       
    # Remove old nodes
    G.remove_nodes_from([n1, n2])











    #my.pp[name] = "big"
    #len(pp.extend(simp.get("Andrew")) = 1 
    #len(simp.get("Andrew").pp) == -1 * sys.maxint -> TRUE
    #print("gimmeee one.. gimme twooo seconds" + "- kdrama simp")
    #\   ^__^
    # \  (oo)\_______
    #    (__)\       )\/\
    #        ||----w |
    #        ||     ||


    #neeenerrrrrrneeeneeerrruihuhuihuihu
    

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G, s = read_input_file(path)
#     D, k = solve(G, s)
#     assert is_valid_solution(D, G, s, k)
#     print("Total Happiness: {}".format(calculate_happiness(D, G)))
#     write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('file_path/inputs/*')
#     for input_path in inputs:
#         output_path = 'file_path/outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path, 100)
#         D, k = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         cost_t = calculate_happiness(T)
#         write_output_file(D, output_path)
