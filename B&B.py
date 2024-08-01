import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
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
oracle_path1 = " -> ".join(oracle_path)

# Initialize the priority queue (min-heap) to store partial paths
priority_queue = PriorityQueue()

# Add the initial path with cost 0 to the queue
priority_queue.put((0, ["P"]))

# Create an empty list to store nodes explored
explored_nodes = []

# Create an empty dictionary to store the best-known costs
best_known_costs = {}

# Initialize the plot
plt.figure(figsize=(12, 8))

while not priority_queue.empty():
    # Get the path with the lowest cost from the queue
    current_cost, path = priority_queue.get()
    
    # Get the last node in the current path
    current_node = path[-1]
    
    # Mark the current node as explored
    explored_nodes.append(current_node)
    
    # Create a copy of the original graph for visualization
    current_graph = copy.deepcopy(G)
    
    # Draw the graph with explored nodes in green and current node in yellow
    node_colors = ["green" if node in explored_nodes else "yellow" for node in current_graph.nodes()]
    edge_colors = ["red" if u == current_node else "gray" for u, v in current_graph.edges()]
    
    # Create a subgraph containing only the nodes and edges on the minimum cost path
    min_cost_path = path
    subgraph = current_graph.subgraph(min_cost_path)
    
    # Draw the graph
    pos = nx.spring_layout(current_graph, seed=42)  # You can change the layout algorithm
    nx.draw(current_graph, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12, font_color="black", edge_color=edge_colors)
    nx.draw(subgraph, pos, with_labels=True, node_size=500, node_color="red", font_size=12, font_color="white", width=2)
    
    # Update the plot
    plt.title("Branch and Bound Algorithm Visualization")
    plt.axis("off")
    plt.show()
    
    # If we have reached the end node, stop the algorithm
    if current_node == "S":
        break
    
    # Explore neighboring nodes
    for neighbor in current_graph[current_node]:
        neighbor_cost = current_graph[current_node][neighbor]['cost']
        if neighbor not in path:
            # Calculate the total cost of the new path
            total_cost = current_cost + neighbor_cost
            
            # Check if this path has a lower cost than the best-known cost for the neighbor
            if neighbor not in best_known_costs or total_cost < best_known_costs[neighbor]:
                best_known_costs[neighbor] = total_cost
                # Add the new path to the priority queue
                new_path = path + [neighbor]
                priority_queue.put((total_cost, new_path))

# Oracle: Print the final chosen path and its cost
if "S" in explored_nodes:
    final_path = path
    final_cost = current_cost  # The cost of the final path
    print("Final Chosen Path:", " -> ".join(final_path))
    print("Cost of the Path:", final_cost)
else:
    print("No path to the destination exists.")

# Oracle: Check if the algorithm's result matches the oracle path
if final_path == oracle_path:
    print("Algorithm matched the oracle path:", " -> ".join(path))
else:
    print("Algorithm did not match the oracle path.")

