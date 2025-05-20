import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

#To load the Iris Dataset as oanda dataframe
iris = load_iris(as_frame = True)
df = iris.frame

#Inspect First 5 rows
print("The first 5 rows of dataset: ")
print(df.head())

#Check datatyoes and missing values
print ("\nData Types: ")
print(df.dtypes)

print("\nMissing Values: ")
print(df.isnull().sum())

#Descriptive statistics Give mean meadian and mode for each column
print("\nDescriptive statistics")
print (df.describe())

#   Group data by category
grouped = df.groupby("target").mean()
print("\nMean values grouped by species: ")
print(grouped)

#Simulate Time series Data
df["date"] = pd.date_range(start="2025-01-01", periods=len(df))
time_series = df.groupby("date")["sepal length (cm)"].mean()

#Line Chart
time_series.plot(title="Avg. Sepal length over time")
plt.xlabel("Date")
plt.ylabel("Sepal Length (cm)")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.clf()

#Bar chart
sns.barplot(x=iris.target_names, y = grouped["petal length (cm)"])
plt.title("Avg. Petal length by species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.clf()
print("\nBarchat")

#Histogram
plt.hist(df["sepal width (cm)"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram.png")
plt.clf()

#Scatter Plot
sns.scatterplot(data=df, x="sepal length (cm)", y = "petal length (cm)",
                hue = "target", palette = "Set2")
plt.title("Sepal length vs Petal length")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Petal length (cm)")
plt.legend(title="Species", labels=iris.target_names)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.clf()

#Final Message
print("\nAll plots save successfullly")
