def bellman_ford(vertices, edges, source): 

    distance = [float('inf')] * vertices 
    distance[source] = 0 
    loop_range = vertices - 1
    for _ in range(loop_range):

        for u, v, weight in edges: 
            if distance[u] != float('inf') and distance[u]+ weight < distance[v] : 
                distance[v] = distance[u] + weight 

        
    for u, v, weight in edges: 
        if distance[u] != float('inf') and distance[u] + weight < distance[v]: 
            print('negative cycle is detected ') 
            return True 

    print('no negative cycle is have ') 
    return False 
# Example usage
vertices = 4  # Number of nodes
# (u, v, weight): Edge from node u to node v with given weight
edges = [
    (0, 1, 1),
    (1, 2, -2),
    (2, 3, -1),
    (3, 1, -1)
]

# Starting from source node 0
has_negative_cycle = bellman_ford(vertices, edges, 0)
    
