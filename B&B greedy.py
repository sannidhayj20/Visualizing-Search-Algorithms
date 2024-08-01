import networkx as nx
import matplotlib.pyplot as plt
import copy

# Create a directed graph
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

# Define the oracle path
oracle_path = ["P", "R", "E", "S"]

# Initialize the plot
plt.figure(figsize=(12, 8))

current_node = "P"  # Start from node "P"
explored_nodes = [current_node]
total_cost = 0
final_path = [current_node]

while current_node != "S":
    # Get neighboring nodes and their costs
    neighbors = G[current_node]
    min_cost = float('inf')
    min_cost_neighbor = None

    for neighbor, data in neighbors.items():
        neighbor_cost = data['cost']
        if neighbor not in explored_nodes:
            if neighbor_cost < min_cost:
                min_cost = neighbor_cost
                min_cost_neighbor = neighbor

    if min_cost_neighbor is None:
        print("No path to the destination exists.")
        break

    # Move to the neighbor with the lowest cost
    current_node = min_cost_neighbor
    explored_nodes.append(current_node)
    total_cost += min_cost
    final_path.append(current_node)

    # Draw the graph
    current_graph = copy.deepcopy(G)
    node_colors = ["green" if node in explored_nodes else "yellow" for node in current_graph.nodes()]
    edge_colors = ["red" if u == current_node else "gray" for u, v in current_graph.edges()]

    pos = nx.spring_layout(current_graph, seed=42)
    nx.draw(current_graph, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12,
            font_color="black", edge_color=edge_colors)
    plt.title("Greedy Branch and Bound Algorithm Visualization")
    plt.axis("off")
    plt.show()

# Print the final chosen path and its cost
if current_node == "S":
    print("Final Chosen Path:", " -> ".join(final_path))
    print("Cost of the Path:", total_cost)

# Check if the algorithm's result matches the oracle path
if final_path == oracle_path:
    print("Algorithm Matched the oracle path:", final_path)
else:
    print("Algorithm did not find the oracle path.")
