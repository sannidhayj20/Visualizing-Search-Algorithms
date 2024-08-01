import networkx as nx
import matplotlib.pyplot as plt

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

def visualize_tree(G):
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black")
    
    edge_labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.show()

visualize_tree(G)


paths = nx.all_simple_paths(G, source="P", target="S")
paths_final = []

for path in paths:
    cost = sum(G[path[i]][path[i+1]]["cost"] for i in range(len(path)-1))
    paths_final.append((path, cost))

paths_final.sort(key=lambda x: x[1])

for path, cost in paths_final:
    result_for_this_loop = " -> ".join(path)
    print(f"The Path Followed is {result_for_this_loop} and the cost of it is {cost}")
    path_graph = G.edge_subgraph([(path[i], path[i+1]) for i in range(len(path)-1)])
    
    pos = nx.shell_layout(path_graph)
    nx.draw_networkx_nodes(path_graph, pos)
    nx.draw_networkx_edges(path_graph, pos)
    nx.draw_networkx_edge_labels(path_graph, pos, edge_labels={(path[i], path[i+1]): G[path[i]][path[i+1]]["cost"] for i in range(len(path)-1)})
    nx.draw_networkx_labels(path_graph, pos)
    
    plt.title(f"Path: {' -> '.join(path)}\nCost: {cost}")
    
    # Show the plot
    plt.show()

final_result = " -> ".join(paths_final[0][0])
print(f"The oracle is {final_result} and the cost is {paths_final[0][1]}")
