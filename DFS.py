import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
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



def dfs_path(graph, start, end, path=[], visited_nodes=[]):
    path = path + [start]
    visited_nodes.append(start)
    if start == end:
        return path, visited_nodes
    if start not in graph:
        return None, visited_nodes
    shortest_path = None
    for neighbor in graph[start]:
        neighbor_name = neighbor
        if neighbor_name not in path:
            new_path, visited_nodes = dfs_path(graph, neighbor_name, end, path, visited_nodes)
            if new_path:
                if shortest_path is None or (new_path < shortest_path):
                    shortest_path = new_path
    return shortest_path, visited_nodes

start_node = "P"
end_node = "S"

shortest_path, visited_nodes = dfs_path(G, start_node, end_node)

if shortest_path:
    print("DFS path from {} to {}:".format(start_node, end_node))
    print(" -> ".join(shortest_path))
else:
    print("No path found from {} to {}.".format(start_node, end_node))

# Create a list of edges in the DFS path for visualization
if shortest_path:
    edges_in_dfs_path = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]

# Draw the graph with labels
pos = nx.spring_layout(G)

# Highlight visited nodes
visited_nodes_set = set(visited_nodes)
unvisited_nodes = [node for node in G.nodes() if node not in visited_nodes_set]

# Draw the visited nodes in light green and unvisited nodes in light gray
nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=500)
nx.draw_networkx_nodes(G, pos, nodelist=unvisited_nodes, node_color='lightgray', node_size=500)

# Draw the edges in blue dotted lines for non-DFS path edges
for edge in G.edges():
    if edge not in edges_in_dfs_path:
        nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color='blue', width=1, style='dotted')

# Highlight the DFS path in red
nx.draw_networkx_edges(G, pos, edgelist=edges_in_dfs_path, edge_color='red', width=2)

# Draw the labels for nodes
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)

plt.show()
