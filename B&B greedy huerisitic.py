import networkx as nx
import matplotlib.pyplot as plt
import copy
from queue import PriorityQueue
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

# Define a heuristic function (straight-line distance)
def calculate_heuristic(node, goal):
    heuristic_values = {
        "P": 10,
        "R": 8,
        "A": 11,
        "C": 6,
        "M": 9,
        "U": 4,
        "E": 3,
        "L": 9,
        "N": 6,
        "S": 0
    }
    return heuristic_values[node]

# Initialize the plot
plt.figure(figsize=(12, 8))

class PathNode:
    def __init__(self, node, path, cost, heuristic):
        self.node = node
        self.path = path
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        # Compare based on the sum of cost and heuristic (greedy strategy)
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def branch_and_bound_greedy(graph, start, goal):
    # Initialize priority queue (min-heap) to store partial paths
    priority_queue = PriorityQueue()
    
    # Add the initial path to the queue with cost and heuristic
    initial_heuristic = calculate_heuristic(start, goal)
    initial_path_node = PathNode(start, [start], 0, initial_heuristic)
    priority_queue.put(initial_path_node)
    
    while not priority_queue.empty():
        # Get the path with the lowest cost and heuristic from the queue
        current_path_node = priority_queue.get()
        
        current_node = current_path_node.node
        current_path = current_path_node.path
        current_cost = current_path_node.cost
        
        # If we have reached the goal node, stop the algorithm
        if current_node == goal:
            return current_path, current_cost
        
        # Explore neighboring nodes
        for neighbor in graph[current_node]:
            neighbor_cost = graph[current_node][neighbor]['cost']
            
            # Calculate the total cost of the new path
            total_cost = current_cost + neighbor_cost
            
            # Calculate the heuristic for the neighbor
            neighbor_heuristic = calculate_heuristic(neighbor, goal)
            
            # Create a new path node for the neighbor
            new_path_node = PathNode(neighbor, current_path + [neighbor], total_cost, neighbor_heuristic)
            
            # Add the new path node to the priority queue
            priority_queue.put(new_path_node)
    
    # If no path to the destination exists
    return [], float('inf')

# Find the optimal path using Branch and Bound with greedy heuristics
optimal_path, optimal_cost = branch_and_bound_greedy(G, "P", "S")

# Print the optimal path and cost
if not optimal_path:
    print("No path to the destination exists.")
else:
    print("Optimal Path:", " -> ".join(optimal_path))
    print("Optimal Cost:", optimal_cost)

# Check if the algorithm's result matches the oracle path
if optimal_path == oracle_path:
    print("Algorithm found the oracle path:", optimal_path)
else:
    print("Algorithm did not find the oracle path.")

# Visualize the final path
final_graph = copy.deepcopy(G)
node_colors = ["green" if node in optimal_path else "yellow" for node in final_graph.nodes()]
edge_colors = ["red" if u in optimal_path and v in optimal_path else "gray" for u, v in final_graph.edges()]

pos = nx.spring_layout(final_graph, seed=42)
nx.draw(final_graph, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12,
        font_color="black", edge_color=edge_colors)
plt.title("Branch and Bound Algorithm Visualization (Optimal Path)")
plt.axis("off")
plt.show()
