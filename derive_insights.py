import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain 

# Step 1: Load the Cleaned Data
df = pd.read_csv("cleaned_relationships.csv")
print("Sample Data:")
print(df.head())

# Step 2: Most Frequent Entities
top_subjects = df["Subject"].value_counts().head(10)
top_objects = df["Object"].value_counts().head(10)
print("\nTop 10 Subjects:")
print(top_subjects)
print("\nTop 10 Objects:")
print(top_objects)

# Step 3: Most Frequent Relationships
top_relationships = df["Relationship"].value_counts().head(10)
print("\nTop 10 Relationships:")
print(top_relationships)

# Step 4: Network Analysis
G = nx.from_pandas_edgelist(df, source="Subject", target="Object", edge_attr="Relationship", create_using=nx.DiGraph())

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Network Graph of Relationships")
plt.show()

# Step 5: Entity Clusters
G_undirected = G.to_undirected()
partition = community_louvain.best_partition(G_undirected)
nx.set_node_attributes(G_undirected, partition, "community")

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G_undirected)
nx.draw(G_undirected, pos, with_labels=True, node_size=2000, node_color=list(partition.values()), cmap=plt.cm.tab20, font_size=10, font_weight="bold", edge_color="gray")
plt.title("Entity Clusters (Communities)")
plt.show()

# Step 6: Anomalies or Outliers
rare_relationships = df.groupby(["Subject", "Object", "Relationship"]).size().reset_index(name="Count")
rare_relationships = rare_relationships[rare_relationships["Count"] == 1]
print("\nRare Relationships:")
print(rare_relationships.head(10))

# Step 7: Summarize Insights
insights_summary = f"""
Insights Summary:

1. Top Entities:
   - Subjects: {top_subjects.index.tolist()}
   - Objects: {top_objects.index.tolist()}

2. Top Relationships:
   {top_relationships.to_string()}

3. Network Analysis:
   - Vendor and Winner are central nodes with many connections.
   - Clusters: Vendor-Supply, Winner-prices.

4. Anomalies:
   - Rare relationships: {rare_relationships.head(10).to_string()}
"""

print(insights_summary)

# Step 8: Save Insights to a File
with open("insights_summary.txt", "w") as f:
    f.write(insights_summary)

print("Insights saved to 'insights_summary.txt'.")