# Iris Dataset Analysis and Visualization Script

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Add species name column
df['species'] = df['target'].apply(lambda x: iris.target_names[x])

# Save to CSV for external viewing
df.to_csv("iris_dataset.csv", index=False)

# Data exploration
print("First few rows of the dataset:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nMissing values in dataset:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

# Group by species and calculate mean
grouped_means = df.groupby('species').mean(numeric_only=True)
print("\nGrouped Mean by Species:")
print(grouped_means)

# Create figures directory
figures_dir = "figures"
os.makedirs(figures_dir, exist_ok=True)

# Line plot
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['petal length (cm)'], label=species)
plt.title("Petal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.tight_layout()
plt.savefig(f"{figures_dir}/line_chart.png")
plt.close()

# Bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_means.index, y=grouped_means['sepal length (cm)'])
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.tight_layout()
plt.savefig(f"{figures_dir}/bar_chart.png")
plt.close()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(f"{figures_dir}/histogram.png")
plt.close()

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig(f"{figures_dir}/scatter_plot.png")
plt.close()

print("\nVisualizations saved in 'figures/' folder.")
