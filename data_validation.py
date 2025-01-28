import pandas as pd

# Load the CSV file
df = pd.read_csv("extracted_relationships.csv")

# Display the first few rows of the dataset
print("Sample Data:")
print(df.head())

# 1. Check for Missing Values
print("\nChecking for Missing Values:")
print(df.isnull().sum())

# 2. Check for Duplicate Rows
print("\nChecking for Duplicate Rows:")
duplicates = df.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")
if duplicates.sum() > 0:
    print("\nDuplicate Rows:")
    print(df[duplicates])

# 3. Check for Inconsistent Relationships
# Example: Ensure that relationships like "nsubj" and "dobj" are valid
valid_relationships = ["nsubj", "dobj"]  # Add other valid relationships if needed
invalid_relationships = df[~df["Relationship"].isin(valid_relationships)]
print("\nChecking for Invalid Relationships:")
if not invalid_relationships.empty:
    print("Invalid Relationships Found:")
    print(invalid_relationships)
else:
    print("All relationships are valid.")

# 4. Check for Consistency in Subject-Object Pairs
# Example: Ensure that the same subject-object pair does not have multiple conflicting relationships
print("\nChecking for Inconsistent Subject-Object Pairs:")
inconsistent_pairs = df.groupby(["Subject", "Object"])["Relationship"].nunique().reset_index()
inconsistent_pairs = inconsistent_pairs[inconsistent_pairs["Relationship"] > 1]
if not inconsistent_pairs.empty:
    print("Inconsistent Subject-Object Pairs Found:")
    print(inconsistent_pairs)
else:
    print("All subject-object pairs are consistent.")

# 5. Check for Empty or Invalid Subjects/Objects
print("\nChecking for Empty or Invalid Subjects/Objects:")
empty_subjects = df[df["Subject"].str.strip() == ""]
empty_objects = df[df["Object"].str.strip() == ""]
if not empty_subjects.empty:
    print("Empty Subjects Found:")
    print(empty_subjects)
if not empty_objects.empty:
    print("Empty Objects Found:")
    print(empty_objects)

# 6. Summary of Data Quality
print("\nData Quality Summary:")
print(f"Total Rows: {len(df)}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {duplicates.sum()}")
print(f"Invalid Relationships: {len(invalid_relationships)}")
print(f"Inconsistent Subject-Object Pairs: {len(inconsistent_pairs)}")
print(f"Empty Subjects: {len(empty_subjects)}")
print(f"Empty Objects: {len(empty_objects)}")