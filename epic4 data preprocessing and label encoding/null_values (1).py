import pandas as pd

# Load the dataset
Development = pd.read_excel("human-development-index-project-dataset.xlsx")

# Select Independent Variables (X)
X = Development[[
    "Life Expectancy",
    "Schooling",
    "GNI per Capita",
    "Internet Users (%)"
]]

# Check null values
print("Null values before filling:")
print(X.isnull().sum())

# Fill null values with column mean
X = X.fillna(X.mean())

# Check again
print("\nNull values after filling:")
print(X.isnull().sum())

# Display first 5 rows
print("\nUpdated Dataset:")
print(X.head())