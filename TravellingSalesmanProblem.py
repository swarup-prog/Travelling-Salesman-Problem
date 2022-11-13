# Travelling Salesman Problem
import numpy as np 
import random

# g(i,s) = min(w(i,j)+g(j, [s-j]))
def tsp(graph, starting_point): 
    sp = starting_point
    # Keeping track of the visited node
    visited_node = []
    cost = 0
    # Making temporary graph
    graph_n = np.copy(graph).tolist()
    # Removing 0 from the graph
    for grph in graph_n:
        for element in grph:
            if element == 0:
                grph.remove(element)
        
    i = 0    
    while i < len(graph) - 1:
        # TempList to add the elements of the graph which haven't been visited
        temp_list = []
        for j in graph_n[sp]:
            # Checking if the nodes of the graph is visited or not
            if graph[sp].index(j) not in visited_node:
                temp_list.append(j)
            else:
                continue
        # Adding the present node to visited node
        visited_node.append(sp)
        # Finding the destination node with minimum cost from the present node
        min_value = min(temp_list)
        min_val_index = graph[sp].index(min_value)
        cost += min_value
        # Changing the destination node to present node
        sp =  min_val_index
        i += 1

    visited_node.append(sp)
    # Adding the cost from last visited node to starting node in total cost    
    cost += graph[sp][starting_point]
    print(f"The final shortest route is from {visited_node} and back to start with the total cost {cost}")

    

graph = [[0, 16, 11, 6, 17, 12, 7,8, 54, 13, 16, 21, 4, 9],
         [8, 0, 13, 16, 21, 4, 9,4, 7, 23, 9, 1, 10, 13],
         [4, 7, 0, 9, 1, 10, 13,5, 12, 2, 53, 9, 6, 21],
         [5, 12, 2, 0, 9, 6, 21,10, 3, 7, 6, 31, 5, 8],
         [10, 3, 7, 6, 0, 5, 8,11, 8, 4, 13, 19, 121, 6],
         [11, 8, 4, 13, 19, 0, 6,4, 6, 10, 5, 11, 15, 32],
         [4, 6, 10, 5, 11, 15, 12,0, 16, 11, 6, 17, 12, 7],
         [8, 76, 13, 16, 21, 4, 9, 0, 16, 11, 6, 17, 12, 7],
         [4, 7, 21, 9, 1, 10, 13,8, 0, 13, 16, 21, 4, 9],
         [5, 12, 2, 42, 9, 6, 21,4, 7, 0, 9, 1, 10, 13],
         [10, 3, 7, 6, 21, 5, 8,5, 12, 2, 0, 9, 6, 21],
         [11, 8, 4, 13, 19, 24, 6, 10, 3, 7, 6, 0, 5, 8],
         [4, 6, 10, 5, 11, 15, 33,11, 8, 4, 13, 19, 0, 6],
         [21, 16, 11, 6, 17, 12, 7,4, 6, 10, 5, 11, 15, 0]]



starting_point = 0
tsp(graph, starting_point)


    

    