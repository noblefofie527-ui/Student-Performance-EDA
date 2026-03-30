# Import Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset 
data = pd.read_csv ("students.csv")

# Display first rows
print("First rows of dataset: ")
print(data.head())

data.columns = data.columns.str.strip()

# Summary Statistics 
print("\nSummary Statistics: ")
print(data.describe())

# Mean, Median, Mode 
print("\nMean")
print(data.mean(numeric_only=True))
print("\nMedian")
print(data.median(numeric_only=True))
print("\nMode")
print(data.mode())

# Histogram
plt.hist(data["Exam_Score"])
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

# Boxplot
sns.boxplot(x=data["Exam_Score"])
plt.title("Boxplot of Exam Scores")
plt.show()

# Scatter Plot
plt.scatter(data["Hours_Studied"], data["Exam_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Hours Studied vs Exam Score")
plt.show()

# Correlation 
correlation = data.corr(numeric_only=True)
print("\nCorrelation Matrix: ")
print(correlation)