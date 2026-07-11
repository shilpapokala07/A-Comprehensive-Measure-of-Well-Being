import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_excel("human-development-index-project-dataset.xlsx")

# Display column names
print(df.columns)

# Select Independent Variables (X)
X = df[[
    "Life Expectancy",
    "Schooling",
    "GNI per Capita",
    "Internet Users (%)"
]]

# Select Dependent Variable (Y)
y = df["Human Development Index (HDI)"]

# Split the dataset into Training and Testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.1,
    random_state=42
)

# Display shapes
print("Training Features:", X_train.shape)
print("Testing Features:", X_test.shape)
print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)