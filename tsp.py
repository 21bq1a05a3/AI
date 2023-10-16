from itertools import permutations
import re

def tsp(graph, s):

    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    min_path_cost = float('inf')
    min_path = None
    next_permutation = permutations(vertex)
    all_paths = {}
    for i in next_permutation:
        current_path = tuple([s] + list(i) + [s])
        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        if min_path_cost > current_pathweight:
            min_path_cost = current_pathweight
            min_path = current_path

        all_paths[current_path] = current_pathweight

    all_paths.pop(min_path)

    return {min_path: min_path_cost}, all_paths


def get_user_input():
    num_nodes = int(input("Enter Number of nodes: "))
    print("Enter Adjacent nodes and weights.\nJust press Enter if there is no path.")
    distances = [[0] * num_nodes for _ in range(num_nodes)]

    for i in range(num_nodes):
        print(f"Node {i+1}: ")
        while True:
            user = input()
            if user == "": break
            n1, n2, weight = map(int, re.split(r"[-:]", user))
            distances[n1 - 1][n2 -1] = weight
            distances[n2 - 1][n1 -1] = weight

    start = int(input("Enter the starting node : ")) - 1

    return distances, start


def display_solution(min, rest):
    
    result = "Optimal Path :\n"
    result += " -> ".join([str(node + 1) for node in list(min.keys())[0]]) + "\t"
    result += "Cost : "+str(list(min.values())[0]) + "\n\n"

    result += "Other possible paths :\n"
    i=1
    for path in rest.items():
        result += str(i) + ") "+" -> ".join([str(node + 1) for node in path[0]]) + "  "
        result += "Cost : "+str(path[1]) + "\n"
        i+=1

    print(result)

display_solution(*tsp(*get_user_input()))