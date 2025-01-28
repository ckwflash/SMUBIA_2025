import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Step 1: Load the cleaned dataset
df = pd.read_csv("cleaned_relationships.csv")

# Step 2: Combine Subject and Object columns into a single text corpus
text = " ".join(df["Subject"].tolist() + df["Object"].tolist())

# Step 3: Generate the word cloud
wordcloud = WordCloud(
    width=800,              # Width of the word cloud image
    height=400,             # Height of the word cloud image
    background_color="white",  # Background color
    max_words=100,          # Maximum number of words to display
    colormap="viridis",     # Color scheme
    stopwords=None,         # Add custom stopwords if needed
).generate(text)

# Step 4: Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Hide the axes
plt.title("Word Cloud from Cleaned Relationships")
plt.show()

# Step 5: Save the word cloud as an image (optional)
wordcloud.to_file("wordcloud.png")
print("Word cloud saved as 'wordcloud.png'.")