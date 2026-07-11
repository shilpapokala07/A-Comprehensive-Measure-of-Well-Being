import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
Development = pd.read_excel("human-development-index-project-dataset.xlsx")

# Display column names (optional)
print(Development.columns)

# Plot the HDI values
Development["Human Development Index (HDI)"].hist()

# Add title
plt.title("Distribution of Human Development Index (HDI)")

# Label axes
plt.xlabel("HDI Value")
plt.ylabel("Frequency")

# Show graph
plt.show()