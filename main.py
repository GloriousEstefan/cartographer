import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Define the CDP neighbor information
cdp_neighbors = [("R1", "R2"), ("R5", "R2"), ("R2", "R3"), ("R3", "R4")]

# Add edges to the graph based on the CDP neighbor information
for src, dst in cdp_neighbors:
    G.add_edge(src, dst)

# Draw the graph using matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Display the graph
plt.show()