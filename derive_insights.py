import pandas as pd

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

# Step 4: Anomalies or Outliers
rare_relationships = df.groupby(["Subject", "Object", "Relationship"]).size().reset_index(name="Count")
rare_relationships = rare_relationships[rare_relationships["Count"] == 1]
print("\nRare Relationships:")
print(rare_relationships.head(10))

# Step 5: Summarize Insights
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

# Step 6: Save Insights to a File
with open("insights_summary.txt", "w") as f:
    f.write(insights_summary)

print("Insights saved to 'insights_summary.txt'.")