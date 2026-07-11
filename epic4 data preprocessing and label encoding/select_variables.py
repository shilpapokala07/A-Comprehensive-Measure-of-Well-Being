import pandas as pd

# Load the dataset
Development = pd.read_excel("human-development-index-project-dataset.xlsx")

# Display all column names
print("Dataset Columns:")
print(Development.columns)

# Select Independent Variables (X)
X = Development[[
    "Life Expectancy",
    "Schooling",
    "GNI per Capita",
    "Internet Users (%)"
]]

# Select Dependent Variable (Y)
Y = Development["Human Development Index (HDI)"]

# Display the selected variables
print("\nIndependent Variables (X):")
print(X.head())

print("\nDependent Variable (Y):")
print(Y.head())