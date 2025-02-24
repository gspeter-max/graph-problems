from collections import deque

def color_find(graph, colors):
    colors_marking = {}
    
    for node in graph:
        used_color = []  
        print(f'nodes printing : {node}')
      
        for neighbor in graph[node]:
            print(f'neighbors printing : {neighbor}')
            if neighbor in colors_marking:
                used_color.append(colors_marking[neighbor])
                print(f'used colors printing : {used_color}')
        
        available_colors = [color for color in colors if color not in used_color]
        print(f'remaining colors available : {available_colors}')
        
  
        colors_marking[node] = available_colors[0]
        print(f'final color assignment: {colors_marking}')
        print("-------------------------------------------------------------------------------------------------------\n --------------------------------------------------------------------------------")
    
    return colors_marking
  
Graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
result = color_find(Graph, colors)
print("Final Coloring Result:", result)


''' 2nd solution ''' 
vertices = 4
connection_matrix = [
    [0, 1, 1, 0], 
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

ab_list = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D'
}


def find_hamiltonian_path(path, visited):
    if len(path) == vertices:
        return path  

    last_vertex = path[-1]

    for next_vertex in range(vertices):
        if connection_matrix[last_vertex][next_vertex] == 1 and next_vertex not in visited:
            visited.add(next_vertex)
            result = find_hamiltonian_path(path + [next_vertex], visited)
            if result:
                return result  
            visited.remove(next_vertex)  

    return None  

for start_vertex in range(vertices):
    path = find_hamiltonian_path([start_vertex], {start_vertex})
    if path:
        readable_path = ' -> '.join(ab_list[v] for v in path)
        print("Hamiltonian Path Found:", readable_path)
        break
else:
    print("No Hamiltonian Path exists.")

