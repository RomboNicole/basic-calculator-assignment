# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Error handling when loading data
try:
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})

    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 1: Explore the Dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Clean the dataset (no missing values in Iris, but for demo let's add fake NA and drop)
df_cleaned = df.copy()
df_cleaned.loc[0, 'sepal length (cm)'] = None
df_cleaned = df_cleaned.dropna()

# Task 2: Basic Data Analysis
print("\nDescriptive statistics:")
print(df_cleaned.describe())

print("\nMean values grouped by species:")
print(df_cleaned.groupby('species').mean())

# Task 3: Data Visualization
sns.set(style="whitegrid")

# 1. Line Chart: Not typical for Iris, so simulate index as time
plt.figure(figsize=(10, 5))
plt.plot(df_cleaned.index, df_cleaned['sepal length (cm)'], label='Sepal Length')
plt.title("Line Chart: Sepal Length over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(data=df_cleaned, x='species', y='petal length (cm)', ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned['sepal width (cm)'], bins=15, kde=True)
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()
