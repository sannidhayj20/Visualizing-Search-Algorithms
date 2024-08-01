import networkx as nx
import matplotlib.pyplot as plt
fgjeog = 0
def create_tree():
    n = int(input("Enter the number of nodes: "))
    
    G = nx.Graph()
    
    node_names = [input(f"Enter the name of node {i+1}: ") for i in range(n)]
    
    for i in range(n-1):
        fgjeog = int(input(f"Enter the number of parents for{node_names[i+1]}"))
        while fgjeog>0:
            parent = input(f"Enter the parent node {fgjeog} for node {node_names[i+1]}: ")
            cost = int(input(f"Enter the cost from {parent} to node {node_names[i+1]}: "))
            G.add_edge(parent, node_names[i+1], cost=cost)
            fgjeog= fgjeog-1
    
    return G

def visualize_tree(G):
    pos = nx.spring_layout(G)  # Positions for all nodes
    
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black")
    
    edge_labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    plt.show()

# Create the tree
tree = create_tree()

# Visualize the tree
visualize_tree(tree)
