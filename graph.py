import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'entity_relationships.csv'  # Replace with the path to your file
data = pd.read_csv(file_path)

# Use a subset of the data for faster processing (e.g., first 100 rows)
data_sample = data.head(50)  # Adjust this number as needed

# Create the graph
G = nx.from_pandas_edgelist(data_sample, 'Entity_1', 'Entity_2', edge_attr='Source')

# Use a faster layout algorithm
pos = nx.circular_layout(G)  # Faster and simpler than spring_layout

# Configure plot size
plt.figure(figsize=(12, 8))

# Draw the graph with reduced complexity
nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_size=1000,  # Smaller node size
    node_color="skyblue", 
    edge_color="gray", 
    font_size=8,  # Smaller font size for labels
    font_weight="bold"
)

# Add edge labels (sources)
edge_labels = nx.get_edge_attributes(G, 'Source')
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_color='red', font_size=6  # Smaller edge label font size
)

# Add a title and display the graph
plt.title("Optimized Entity-Relationship Network Graph", fontsize=14)
plt.show()
