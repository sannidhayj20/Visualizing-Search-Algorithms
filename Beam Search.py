import networkx as nx
import matplotlib.pyplot as plt


def beam_search(graph, start, goal, beam_width):
    # Initialize the search with the start node
    initial_path = [start]
    beam = [(initial_path, 0)]  # Each element is a tuple (path, cost)

    while beam:
        # Generate new candidates by extending the paths
        candidates = []
        for path, cost in beam:
            current_node = path[-1]
            for neighbor in graph.neighbors(current_node):
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_cost = cost + graph[path[-1]][neighbor]['cost']
                    candidates.append((new_path, new_cost))
        
        # Sort the candidates by cost and select the top-k
        candidates.sort(key=lambda x: x[1])
        beam = candidates[:beam_width]
        
        # Check if the goal node is reached in any of the paths
        for path, cost in beam:
            if path[-1] == goal:
                return path, cost
    
    return None, float('inf')  # Return None if no path is found

# Define your graph
G = nx.DiGraph()
G.add_edge("P", "A", cost=4)
G.add_edge("P", "C", cost=4)
G.add_edge("P", "R", cost=4)
G.add_edge("A", "M", cost=3)
G.add_edge("M", "L", cost=2)
G.add_edge("L", "N", cost=5)
G.add_edge("N", "S", cost=6)
G.add_edge("R", "E", cost=5)
G.add_edge("E", "S", cost=1)
G.add_edge("C", "R", cost=2)
G.add_edge("C", "U", cost=3)
G.add_edge("C", "M", cost=4)
G.add_edge("U", "S", cost=4)
G.add_edge("U", "N", cost=5)
G.add_edge("N", "S", cost=6)
G.add_edge("E", "U", cost=5)
G.add_edge("M", "U", cost=5)

# Perform beam search (using the previous code)
start_node = "P"
goal_node = "S"
beam_width = 2
best_path, min_cost = beam_search(G, start_node, goal_node, beam_width)

# Create a layout for the nodes in the graph
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')

# Draw the best path found by the beam search
if best_path:
    path_edges = [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

best_path1 = " -> ".join(best_path)
# Label the nodes with their names
labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

# Display the graph, best path, and cost
if best_path:
    print(f"Best path from {start_node} to {goal_node}: {best_path1}")
    print(f"Minimum cost: {min_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")

plt.title(f"Beam Search from {start_node} to {goal_node} (Min Cost: {min_cost})")
plt.axis('off')
plt.show()
