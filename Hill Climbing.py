import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
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


# Define the heuristic function with updated values
def heuristic(node):
    heuristic_values = {  
        'A': 11,   
        'C': 6,
        'R': 8,
        'M': 9,
        'U': 4,
        'E': 3,
        'L': 9,
        'N': 6,
        'S': 0,
    }
    return heuristic_values.get(node, 0)

# Define the hill climbing function with updated heuristic
def hill_climbing_with_heuristic(graph, start_node, goal_node):
    current_node = start_node
    path = [current_node]
    total_cost = 0
    canceled_nodes = []

    while current_node != goal_node:
        neighbors = list(graph.neighbors(current_node))
        min_cost = float('inf')
        next_node = None

        for neighbor in neighbors:
            edge_cost = graph[current_node][neighbor].get('cost', 0)
            neighbor_heuristic = heuristic(neighbor)
            if neighbor not in path and (edge_cost + neighbor_heuristic) < min_cost:
                min_cost = edge_cost + neighbor_heuristic
                next_node = neighbor

        if next_node is None:
            canceled_nodes.append(current_node)
            break

        path.append(next_node)

        current_node = next_node

    # After reaching the goal node 'G', add its heuristic value to the total cost
    

    return path,canceled_nodes

# Specify the start and goal nodes
start_node = 'P'
goal_node = 'S'

# Find the path, total cost, and canceled nodes using hill climbing with updated heuristic
path, canceled_nodes = hill_climbing_with_heuristic(G, start_node, goal_node)
final_path = " -> ".join(path)

# Create a new graph highlighting explored, canceled, and unexplored nodes
new_G = G.copy()
node_colors = ['g' if node in path else 'r' if node in canceled_nodes else 'b' for node in new_G.nodes()]
edge_colors = ['r' if edge in zip(path, path[1:]) else 'k' for edge in new_G.edges()]

# Visualization
pos = nx.spring_layout(new_G)

plt.figure(figsize=(10, 6))
nx.draw(new_G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=800, font_size=12, font_color='white')
edge_labels = nx.get_edge_attributes(new_G, 'cost')
nx.draw_networkx_edge_labels(new_G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.4)

plt.title(f'Hill Climbing Path from {start_node} to {goal_node}')
plt.show()

# Print the results
print(f"Path from {start_node} to {goal_node}: {final_path}")
