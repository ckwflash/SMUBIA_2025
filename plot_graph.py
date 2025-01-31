import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain 

# Step 1: Load the Cleaned Data
df = pd.read_csv("cleaned_relationships.csv")
print("Sample Data:")
print(df.head())

# Step 2: Create the Graph
G = nx.from_pandas_edgelist(df, source="Subject", target="Object", edge_attr="Relationship", create_using=nx.DiGraph())

# Step 3: Filter Nodes and Edges
# Filter nodes with degree >= 2
degrees = dict(G.degree())
filtered_nodes = [node for node in G.nodes if degrees[node] >= 2]
G_filtered = G.subgraph(filtered_nodes)

# Step 4: Optimize the Layout
pos = nx.spring_layout(G_filtered, k=0.5, iterations=50)  # Adjust k and iterations for better spacing

# Step 5: Customize Node and Edge Appearance
# Node size based on degree
node_sizes = [degrees[node] * 100 for node in G_filtered.nodes]

# Node color based on community detection
G_undirected = G_filtered.to_undirected()
partition = community_louvain.best_partition(G_undirected)
node_colors = [partition[node] for node in G_filtered.nodes]

# Edge width based on weight (if available)
edge_widths = [1 for edge in G_filtered.edges]  # Default width (customize if weights are available)

# Step 6: Visualize the Graph
plt.figure(figsize=(14, 10))
nx.draw(
    G_filtered,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    edge_color="gray",
    width=edge_widths,
    font_size=10,
    font_weight="bold",
    cmap=plt.cm.tab20,  # Color map for nodes
)

# Add edge labels (optional)
edge_labels = nx.get_edge_attributes(G_filtered, "Relationship")
nx.draw_networkx_edge_labels(
    G_filtered,
    pos,
    edge_labels=edge_labels,
    font_size=8,
)

plt.title("Fine-Tuned Network Graph of Relationships")
plt.show()

# Step 7: Save the Graph
plt.savefig("fine_tuned_network_graph.png", dpi=300, bbox_inches="tight")
print("Fine-tuned network graph saved as 'fine_tuned_network_graph.png'.")

# Step 8: Entity Clusters (Optional)
plt.figure(figsize=(14, 10))
nx.draw(
    G_undirected,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color=node_colors,
    edge_color="gray",
    width=edge_widths,
    font_size=10,
    font_weight="bold",
    cmap=plt.cm.tab20,  # Color map for nodes
)
plt.title("Entity Clusters (Communities)")
plt.show()