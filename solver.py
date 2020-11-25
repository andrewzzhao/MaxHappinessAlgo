import networkx as nx
import numpy as np
import random
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_happiness, convert_dictionary
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
    best_D_so_far = {}
    best_k_so_far = 1
    best_H_so_far = 0.0
    n = nx.number_of_nodes(G)
    
    for k in range(1, n + 1):
        curr_D = {}
        smax = s/k
        G_stress = G.copy()
        while nx.number_of_nodes(G_stress) > k:  
            # sort edges by decreasing happiness
            sorted_stress = sorted(G_stress.edges(data=True), key=lambda y: (y[2]["stress"], -y[2]["happiness"]), reverse=False)
            if len(sorted_stress) == 0:
                break
            #need to merge nodes A and B
            n1, n2, _ = sorted_stress[0]
            if G_stress.nodes[n1].get("stress", 0) + G_stress.nodes[n2].get("stress", 0) + G_stress.edges[n1, n2]["stress"] <= smax:
                merge(G_stress, n1, n2)
                
            else:
                G_stress.remove_edge(n1,n2)
                

        if nx.number_of_nodes(G_stress) == k:
            room = 0
            for node in list(G_stress.nodes):
                if isinstance(node, int):
                    temp = [node]
                else:
                    temp = node.split(' ')
                    temp = [int(x) for x in temp]
                curr_D[room] = temp
                room += 1
            curr_D = convert_dictionary(curr_D)
            
        else:
            continue
       
        if is_valid_solution(curr_D, G, s, k):
            if calculate_happiness(curr_D, G) > best_H_so_far:
                best_D_so_far = curr_D
                best_k_so_far = k
                best_H_so_far = calculate_happiness(curr_D, G)
            #
    # pass
    return best_D_so_far, best_k_so_far

def solve_kinda(G,s,n=10):
    curMax = 0
    dMax, kMax = 0,0
    for i in range(n):
        print("ITERATION", i)
        d1, k1 = solve_happy(G,s)
        d2, k2 = solve_stress(G,s)
        h1 = calculate_happiness(d1, G)
        h2 = calculate_happiness(d2, G)
        if max(h1, h2) >  curMax:
            print("NEW MAX YEY", max(h1, h2))
            if h1 > h2:
                curMax = h1
                dMax, kMax = d1, k1 
            else:
                print("WOWOWOWOWOWOWOWOWOWOWWOW")
                curMax = h2 
                dMax, kMax = d2, k2
    return dMax, kMax




def solve_happy(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    best_D_so_far = {}
    best_k_so_far = 1
    best_H_so_far = 0.0
    n = nx.number_of_nodes(G)
    
    for k in range(1, n + 1):
        curr_D = {}
        smax = s/k
        G_happy = G.copy()
        while nx.number_of_nodes(G_happy) > k:  
            i = np.random.geometric(p=0.10, size = 1).item(0)
            # sort edges by decreasing happiness
            sorted_happiness = sorted(G_happy.edges(data=True), key=lambda y: (y[2]["happiness"], -y[2]["stress"]), reverse=True)
            #i = random.randint(0, len(sorted_happiness))
            if len(sorted_happiness) == 0:
                break
            #need to merge nodes A and B
            i = i % len(sorted_happiness)
            n1, n2, _ = sorted_happiness[i]
            if G_happy.nodes[n1].get("stress", 0) + G_happy.nodes[n2].get("stress", 0) + G_happy.edges[n1, n2]["stress"] <= smax:
                merge(G_happy, n1, n2)
                
            else:
                G_happy.remove_edge(n1,n2)
                

        if nx.number_of_nodes(G_happy) == k:
            room = 0
            for node in list(G_happy.nodes):
                if isinstance(node, int):
                    temp = [node]
                else:
                    temp = node.split(' ')
                    temp = [int(x) for x in temp]
                curr_D[room] = temp
                room += 1
            curr_D = convert_dictionary(curr_D)
            
        else:
            continue
       
        if is_valid_solution(curr_D, G, s, k):
            if calculate_happiness(curr_D, G) > best_H_so_far:
                best_D_so_far = curr_D
                best_k_so_far = k
                best_H_so_far = calculate_happiness(curr_D, G)
            #
    # pass
    return best_D_so_far, best_k_so_far

def solve_stress(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    best_D_so_far = {}
    best_k_so_far = 1
    best_H_so_far = 0.0
    n = nx.number_of_nodes(G)
    
    for k in range(1, n + 1):
        curr_D = {}
        smax = s/k
        G_stress = G.copy()
        while nx.number_of_nodes(G_stress) > k:  
            # sort edges by decreasing happiness
            i = np.random.geometric(p=0.2, size = 1).item(0)
            sorted_stress = sorted(G_stress.edges(data=True), key=lambda y: (y[2]["stress"], -y[2]["happiness"]), reverse=False)
            if len(sorted_stress) == 0:
                break
            #need to merge nodes A and B
            i = i % len(sorted_stress)
            n1, n2, _ = sorted_stress[i]
            if G_stress.nodes[n1].get("stress", 0) + G_stress.nodes[n2].get("stress", 0) + G_stress.edges[n1, n2]["stress"] <= smax:
                merge(G_stress, n1, n2)
                
            else:
                G_stress.remove_edge(n1,n2)
                

        if nx.number_of_nodes(G_stress) == k:
            room = 0
            for node in list(G_stress.nodes):
                if isinstance(node, int):
                    temp = [node]
                else:
                    temp = node.split(' ')
                    temp = [int(x) for x in temp]
                curr_D[room] = temp
                room += 1
            curr_D = convert_dictionary(curr_D)
            
        else:
            continue
       
        if is_valid_solution(curr_D, G, s, k):
            if calculate_happiness(curr_D, G) > best_H_so_far:
                best_D_so_far = curr_D
                best_k_so_far = k
                best_H_so_far = calculate_happiness(curr_D, G)
            #
    # pass
    return best_D_so_far, best_k_so_far

def merge(G, n1, n2):
    
    neighbors = nx.common_neighbors(G, n1, n2)
    # Create the new node with combined name
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











    #name = "Andrew"
    #my.pp[name] = "smol compared to eiffel tower big compared to a water bottle made for ants that are 6 feet tall"
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

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k = solve_kinda(G, s, 100)
    assert is_valid_solution(D, G, s, k)
    print(D)
    print(k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    write_output_file(D, 'backup/50.out')


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
