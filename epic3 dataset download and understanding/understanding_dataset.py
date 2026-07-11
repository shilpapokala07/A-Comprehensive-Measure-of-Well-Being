import pandas as pd

# Read the Excel dataset
Development = pd.read_excel("dataset/human-development-index-project-dataset.xlsx")

# Show number of rows and columns
print("Shape of dataset:")
print(Development.shape)

# Show column names
print("\nColumn names:")
print(Development.columns)

# Show detailed information
print("\nDataset information:")
Development.info()

# Check for missing values
print("\nMissing values:")
print(Development.isnull().sum())

# Statistical summary
print("\nStatistics:")
print(Development.describe())