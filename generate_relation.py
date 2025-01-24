import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the extracted relationships dataset (ensure the file path is correct)
df = pd.read_csv('extracted_relationships.csv')

# Inspect the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# 1. Frequency of Entities (Subjects and Objects)
# Count the frequency of subjects and objects separately
subject_counts = df['Subject'].value_counts()
object_counts = df['Object'].value_counts()

# Display the most frequent subjects and objects
print("\nMost frequent subjects (entities):")
print(subject_counts.head(10))

print("\nMost frequent objects (entities):")
print(object_counts.head(10))

# 2. Frequency of Relationships
# Count the frequency of relationships
relationship_counts = df['Relationship'].value_counts()

# Display the most frequent relationships
print("\nMost frequent relationships:")
print(relationship_counts.head(10))

# 3. Create Network Graph for Visualizing Relationships
# Initialize a Graph object from NetworkX
G = nx.Graph()

# Add edges to the graph using Subject-Object pairs and relationship as edge attribute
for _, row in df.iterrows():
    G.add_edge(row['Subject'], row['Object'], relationship=row['Relationship'])

# 4. Visualize the Network Graph
plt.figure(figsize=(12, 12))

# Use a spring layout for better visualization of larger graphs
pos = nx.spring_layout(G, k=0.15, iterations=20)  # Adjust parameters as needed

# Draw the graph with labels
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray', alpha=0.7)

# Add titles and annotations
plt.title('Entity Relationship Network')
plt.show()

# 5. Highlight Key Relationships (Top 10 Frequent Relationships)
# Create a subgraph for the top 10 most frequent relationships
top_relationships = relationship_counts.head(10).index

# Filter the dataframe to include only the top relationships
top_df = df[df['Relationship'].isin(top_relationships)]

# Create a graph for the filtered relationships
G_top = nx.Graph()

# Add edges to the subgraph
for _, row in top_df.iterrows():
    G_top.add_edge(row['Subject'], row['Object'], relationship=row['Relationship'])

# Visualize the subgraph
plt.figure(figsize=(10, 10))
pos_top = nx.spring_layout(G_top, k=0.2, iterations=15)
nx.draw(G_top, pos_top, with_labels=True, node_size=3000, node_color='lightgreen', font_size=12, font_weight='bold', edge_color='red', alpha=0.7)
plt.title('Top 10 Frequent Relationships in Entity Network')
plt.show()


# Summary of insights
print("\nSummary of insights:")
print(f"- Total subjects (entities) found: {len(subject_counts)}")
print(f"- Total objects (entities) found: {len(object_counts)}")
print(f"- Total relationships found: {len(relationship_counts)}")
