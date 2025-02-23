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
