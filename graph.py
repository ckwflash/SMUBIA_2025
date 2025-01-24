import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('extracted_relationships.csv')

# Drop rows with missing values
df = df.dropna(subset=['Subject', 'Object', 'Relationship'])

# Check for duplicates
df = df.drop_duplicates(subset=['Subject', 'Object', 'Relationship'])

# Check the frequency of subjects and objects
subject_counts = df['Subject'].value_counts()
object_counts = df['Object'].value_counts()

# Get the top 10 most frequent subjects and objects
top_subjects = subject_counts.head(10).index
top_objects = object_counts.head(10).index

# Filter the data to include only top subjects and objects
filtered_df = df[df['Subject'].isin(top_subjects) | df['Object'].isin(top_objects)]

# Initialize the Graph
G = nx.Graph()

# Add edges for the filtered data
for _, row in filtered_df.iterrows():
    G.add_edge(row['Subject'], row['Object'], relationship=row['Relationship'])

# Check the number of nodes and edges after filtering
print(f"Number of nodes in the filtered graph: {len(G.nodes)}")
print(f"Number of edges in the filtered graph: {len(G.edges)}")

# Use a simpler layout for visualization
pos = nx.spring_layout(G, k=0.15, iterations=20)  # spring layout with adjustments

# Plot the filtered graph
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray', alpha=0.7)
plt.title('Top Entities and Relationships Network')
plt.show()
