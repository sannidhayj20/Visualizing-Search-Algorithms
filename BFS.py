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


start_node = 'P'
bfs_edges = list(nx.bfs_edges(G, source=start_node))


pos = nx.spring_layout(G) 
node_colors = ['g' if node == start_node else 'b' for node in G.nodes()]
edge_colors = ['r' if edge in bfs_edges else 'k' for edge in G.edges()]

plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=800, font_size=12, font_color='white')
edge_labels = nx.get_edge_attributes(G, 'cost')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.4)

plt.title('Breadth-First Search (BFS) Visualization')
plt.show()
print("BFS Traversal Order:")
for edge in bfs_edges:
    print( '->'.join(map(str, edge)))

new_graph = nx.DiGraph(bfs_edges)

pos = nx.spring_layout(new_graph)  # Position nodes for a nicer layout

plt.figure(figsize=(8, 6))
nx.draw(new_graph, pos, with_labels=True, node_size=800, font_size=12, font_color='black')

plt.title('New Graph with Specified Edges')
plt.show()