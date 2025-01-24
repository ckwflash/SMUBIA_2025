import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the extracted relationships dataset
df = pd.read_csv('extracted_relationships.csv')

# Inspect the first few rows to check the structure of the dataset
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

# 3. Visualize the Relationships using a Network Graph
# Create a graph for visualizing relationships
G = nx.Graph()

# Add relationships as edges between the Subject and Object entities
for _, row in df.iterrows():
    G.add_edge(row['Subject'], row['Object'], relationship=row['Relationship'])

# Draw the network graph
plt.figure(figsize=(12, 12))
nx.draw(G, with_labels=True, node_size=1000, font_size=10, font_weight='bold', edge_color='blue', alpha=0.5)
plt.title('Entity Relationship Network')
plt.show()

# Summarize the insights
print("\nSummary of insights:")
print(f"- Total subjects (entities) found: {len(subject_counts)}")
print(f"- Total objects (entities) found: {len(object_counts)}")
print(f"- Total relationships found: {len(relationship_counts)}")
