import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain 

# Step 1: Load the Cleaned Data
df = pd.read_csv("cleaned_relationships.csv")
print("Sample Data:")
print(df.head())

# Step 2: Network Analysis
G = nx.from_pandas_edgelist(df, source="Subject", target="Object", edge_attr="Relationship", create_using=nx.DiGraph())

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Network Graph of Relationships")
plt.show()

# Step 3: Entity Clusters
G_undirected = G.to_undirected()
partition = community_louvain.best_partition(G_undirected)
nx.set_node_attributes(G_undirected, partition, "community")

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G_undirected)
nx.draw(G_undirected, pos, with_labels=True, node_size=2000, node_color=list(partition.values()), cmap=plt.cm.tab20, font_size=10, font_weight="bold", edge_color="gray")
plt.title("Entity Clusters (Communities)")
plt.show()