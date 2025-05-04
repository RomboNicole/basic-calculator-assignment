# === Task 1: Load and Explore the Dataset ===

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset with error handling
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)
    exit()

# Display first few rows
print("\n--- First 5 rows ---")
print(df.head())

# Data types and missing values
print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

# Clean dataset (no missing values in iris, but shown for practice)
df = df.dropna()

# === Task 2: Basic Data Analysis ===

# Basic statistics
print("\n--- Basic Statistics ---")
print(df.describe())

# Group by species and compute mean of numerical columns
print("\n--- Mean values by species ---")
grouped = df.groupby('species').mean()
print(grouped)

# Example insight
print("\nInsight: On average, Virginica flowers have the longest petals.")

# === Task 3: Data Visualization ===

sns.set(style="whitegrid")

# 1. Line chart – we'll simulate a "trend" by adding an index
df['index'] = df.index
plt.figure(figsize=(10, 5))
sns.lineplot(x='index', y='sepal length (cm)', data=df, label='Sepal Length')
sns.lineplot(x='index', y='petal length (cm)', data=df, label='Petal Length')
plt.title("Line Chart: Sepal and Petal Length Over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart – average petal length per species
plt.figure(figsize=(7, 5))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram – distribution of sepal width
plt.figure(figsize=(7, 5))
sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot – Sepal Length vs Petal Length
plt.figure(figsize=(7, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
