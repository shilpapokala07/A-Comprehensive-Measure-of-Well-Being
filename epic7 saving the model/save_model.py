import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load Excel dataset
Development = pd.read_excel("human-development-index-project-dataset.xlsx")

# Independent variables
X = Development[[
    "Life Expectancy",
    "Schooling",
    "GNI per Capita",
    "Internet Users (%)"
]]

# Dependent variable
Y = Development["Human Development Index (HDI)"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=0
)

# Train model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Prediction
y_pred = reg.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))

# Save model
pickle.dump(reg, open("HDI.pkl", "wb"))

print("HDI.pkl created successfully!")