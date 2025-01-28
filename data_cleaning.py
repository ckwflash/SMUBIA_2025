import pandas as pd

# Load the CSV file
df = pd.read_csv("extracted_relationships.csv")

# Display the initial data quality summary
print("Initial Data Quality Summary:")
print(f"Total Rows: {len(df)}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Inconsistent Subject-Object Pairs: {df.groupby(['Subject', 'Object'])['Relationship'].nunique().gt(1).sum()}")
print(f"Empty Subjects: {df[df['Subject'].str.strip() == ''].shape[0]}")
print(f"Empty Objects: {df[df['Object'].str.strip() == ''].shape[0]}")

# Step 1: Handle Missing Values
# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Step 2: Remove Duplicate Rows
# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Step 3: Handle Inconsistent Subject-Object Pairs
# For inconsistent pairs, keep the most frequent relationship
df = df.groupby(['Subject', 'Object', 'Relationship']).size().reset_index(name='Count')
df = df.sort_values(by='Count', ascending=False).drop_duplicates(subset=['Subject', 'Object'], keep='first')
df = df.drop(columns=['Count'])

# Step 4: Save the Cleaned Data to a New CSV File
df.to_csv("cleaned_relationships.csv", index=False)

# Display the cleaned data quality summary
print("\nCleaned Data Quality Summary:")
print(f"Total Rows: {len(df)}")
print(f"Missing Values: {df.isnull().sum().sum()}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Inconsistent Subject-Object Pairs: {df.groupby(['Subject', 'Object'])['Relationship'].nunique().gt(1).sum()}")
print(f"Empty Subjects: {df[df['Subject'].str.strip() == ''].shape[0]}")
print(f"Empty Objects: {df[df['Object'].str.strip() == ''].shape[0]}")

print("\nCleaned data saved to 'cleaned_relationships.csv'.")