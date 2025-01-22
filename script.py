import pandas as pd
import spacy
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Function to extract entities from text
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to identify relationships (co-occurring entities in the same text)
def extract_relationships(entities):
    # Generate all pair combinations of entities in the same text
    relationships = list(combinations([ent[0] for ent in entities], 2))
    return relationships

# Load datasets
wikileaks_data = pd.read_csv("wikileaks_parsed.csv")
news_data = pd.read_csv("news_excerpts_parsed.csv")

# Merge datasets into one for processing
wikileaks_data["Source"] = "Wikileaks"
news_data["Source"] = "News"
combined_data = pd.concat([wikileaks_data, news_data], ignore_index=True)

# Extract entities and relationships
entity_data = []
relationship_data = []

for index, row in combined_data.iterrows():
    text = row["Text"]  # Adjust column name if needed
    entities = extract_entities(text)
    
    # Save entities
    for ent_text, ent_type in entities:
        entity_data.append({"Text": text, "Entity": ent_text, "Entity_Type": ent_type, "Source": row["Source"]})
    
    # Save relationships
    relationships = extract_relationships(entities)
    for rel in relationships:
        relationship_data.append({"Entity_1": rel[0], "Entity_2": rel[1], "Source": row["Source"]})

# Save extracted entities and relationships to CSV files
entities_df = pd.DataFrame(entity_data)
relationships_df = pd.DataFrame(relationship_data)

entities_df.to_csv("extracted_entities.csv", index=False)
relationships_df.to_csv("entity_relationships.csv", index=False)

# Create a network graph from relationships
G = nx.Graph()

# Add nodes and edges to the graph
for _, row in relationships_df.iterrows():
    G.add_edge(row["Entity_1"], row["Entity_2"], source=row["Source"])

# Plot the network graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=3000, font_size=10)
plt.title("Entity Relationship Network")
plt.show()
