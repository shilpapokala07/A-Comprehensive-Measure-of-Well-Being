import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the Excel dataset
Development = pd.read_excel("dataset/human-development-index-project-dataset.xlsx")

# Display column names
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

# Split the dataset into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=0
)

# Create the Linear Regression model
reg = LinearRegression()

# Train the model
reg.fit(X_train, y_train)

# Predict the test data
y_pred = reg.predict(X_test)

# Print Predicted Values
print("\nPredicted HDI Values:")
print(y_pred)

# Print Actual Values
print("\nActual HDI Values:")
print(y_test.values)

# Calculate R-Squared Score
score = r2_score(y_test, y_pred)

print("\nR-Squared Value:")
print(score)

# Predict for first 5 test samples
print("\nPrediction for First 5 Test Samples:")
print(reg.predict(X_test.head()))

# Print all predicted values
print("\nAll Predicted Values:")
print(y_pred)