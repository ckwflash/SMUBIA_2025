import pandas as pd
import spacy

# Load SpaCy's English model
nlp = spacy.load('en_core_web_sm')

# Function to extract relationships from text
def extract_relationships(text):
    doc = nlp(text)
    relationships = []
    for token in doc:
        # Capture subject-object relationships (nsubj = subject, dobj = object)
        if token.dep_ in ('nsubj', 'dobj'):
            subj = token.head.text  # The head of the subject
            obj = token.text  # The dependent object
            rel = token.dep_  # Relationship type (e.g., nsubj, dobj)
            relationships.append((subj, rel, obj))
    return relationships

# Example function to process a DataFrame and extract relationships
def process_dataset_and_extract_relations(df, text_column):
    relations = []
    for text in df[text_column]:
        relations.extend(extract_relationships(text))  # Add all relations from this text
    return relations

# Load the CSV files (assuming 'wikileaks_parsed.csv' and 'news_excerpts_parsed.csv')
wikileaks_df = pd.read_csv('wikileaks_parsed.csv')
news_excerpts_df = pd.read_csv('news_excerpts_parsed.csv')

# Extract relationships from both datasets
wikileaks_relations = process_dataset_and_extract_relations(wikileaks_df, 'Text')
news_excerpts_relations = process_dataset_and_extract_relations(news_excerpts_df, 'Text')

# Combine both sets of relations into one DataFrame
all_relations = wikileaks_relations + news_excerpts_relations
relations_df = pd.DataFrame(all_relations, columns=['Subject', 'Relationship', 'Object'])

# Save the relationships to a CSV file
relations_df.to_csv('extracted_relationships.csv', index=False)

# Display the first few rows of the output DataFrame
print(relations_df.head())
